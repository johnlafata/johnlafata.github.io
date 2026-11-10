"""
VCF 9.1.1 / VKS homelab -- which tool provisions which layer.

The point of this diagram: no single tool covers the stack. Terraform does
the broad middle, but the bottom (vCenter bootstrap) and one stage near the
top (Supervisor enablement) are deliberately NOT Terraform, and the very top
is Kubernetes' own API. Four tools, and the seams between them are where the
interesting failures live.

Laid out one stage per row, tool on the left of the thing it builds, so the
edges stay short and every tool sits next to its own stage.

    ./venv/bin/python infrastructure/k8s/homelab-automation-skills/diagrams/provisioning-toolchain.py
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.generic.virtualization import Vmware
from diagrams.generic.compute import Rack
from diagrams.generic.network import Switch, Router
from diagrams.k8s.infra import Master, Node
from diagrams.onprem.iac import Terraform
from diagrams.programming.language import Bash

GRAPH_ATTR = {
    "fontsize": "15",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "ortho",
    "nodesep": "0.5",
    "ranksep": "0.7",
}

# One colour per tool, used consistently on the edges.
C_CLI = "#B8860B"   # vcsa-deploy  (imperative CLI)
C_TF = "#7B42BC"    # Terraform
C_PS = "#2F6FAB"    # PowerCLI
C_K8S = "#326CE5"   # kubectl

with Diagram(
    "Provisioning the stack: four tools, because one will not reach",
    filename="infrastructure/k8s/homelab-automation-skills/images/provisioning-toolchain",
    show=False,
    direction="LR",
    graph_attr=GRAPH_ATTR,
):

    with Cluster("Stage 0  —  vcsa-deploy  (no Terraform resource exists)"):
        s0_tool = Bash("vcsa-deploy")
        s0 = Vmware("vCenter Server")
        s0_tool >> Edge(color=C_CLI, style="bold") >> s0

    with Cluster("Stages 1 – 2.5  —  Terraform  (vsphere + nsxt providers)"):
        s1_tool = Terraform("terraform apply")
        s1a = Rack("ESXi hosts\n+ cluster inventory")
        s1b = Vmware("NSX Manager")
        s1c = Router("NSX Edge\n+ Tier-0 gateway")
        s1d = Switch("host transport node\n(DVS + overlay)")
        s1_tool >> Edge(color=C_TF) >> s1a
        s1_tool >> Edge(color=C_TF) >> s1b
        s1_tool >> Edge(color=C_TF) >> s1c
        s1_tool >> Edge(color=C_TF) >> s1d

    with Cluster("Stage 4a  —  PowerCLI  (the Terraform resource is a dead end)"):
        s4_tool = Bash("Enable-WMCluster")
        s4 = Master("Supervisor\n(Workload Management)")
        s4_tool >> Edge(color=C_PS, style="bold") >> s4

    with Cluster("Stage 4b  —  Terraform"):
        s4b_tool = Terraform("terraform apply")
        s4b = Vmware("namespace +\nTKr content library")
        s4b_tool >> Edge(color=C_TF) >> s4b

    with Cluster("Stage 5  —  kubectl  (Cluster API CRD)"):
        s5_tool = Bash("kubectl apply")
        s5 = Node("VKS guest cluster")
        s5_tool >> Edge(color=C_K8S, style="bold") >> s5

    # Stage ordering: each stage can only start once the one below it exists.
    s0 >> Edge(color="gray55", style="dashed") >> s1_tool
    s1d >> Edge(color="gray55", style="dashed") >> s4_tool
    s4 >> Edge(color="gray55", style="dashed") >> s4b_tool
    s4b >> Edge(color="gray55", style="dashed") >> s5_tool
