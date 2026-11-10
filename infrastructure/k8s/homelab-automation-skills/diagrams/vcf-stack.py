"""
VCF 9.1.1 / VKS homelab -- the target stack.

Two physical hosts in one vSphere cluster: a Ryzen Minisforum MS-A2 and an
older Supermicro Xeon D. Different CPU vendors, which is why cluster EVC is
off and vMotion between them is impossible -- a constraint that matters later.

What has to exist, bottom to top, before a single Kubernetes pod can run.
Each layer depends on everything beneath it, which is the whole reason the
build has to be staged.

    ./venv/bin/python infrastructure/k8s/homelab-automation-skills/diagrams/vcf-stack.py
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.generic.virtualization import Vmware
from diagrams.generic.compute import Rack
from diagrams.generic.network import Switch, Router
from diagrams.k8s.infra import Master, Node

GRAPH_ATTR = {
    "fontsize": "15",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "spline",
    "nodesep": "1.1",
    "ranksep": "0.9",
}

with Diagram(
    "VCF 9.1.1 homelab: what has to exist before a pod can run",
    filename="infrastructure/k8s/homelab-automation-skills/images/vcf-stack",
    show=False,
    direction="TB",
    graph_attr=GRAPH_ATTR,
):

    with Cluster("Physical  (2 hosts, one vSphere cluster)"):
        esxi_mini = Rack("esxi-mini\nMinisforum MS-A2\nRyzen 9 9955HX\n16 cores / 96 GB")
        esxi_sm = Rack("esxi-sm\nSupermicro\nXeon D-1541\n8 cores / 128 GB")
        hosts = [esxi_mini, esxi_sm]

    with Cluster("Management plane"):
        vcenter = Vmware("vCenter Server\n(vCenter Appliance)")
        nsx_mgr = Vmware("NSX Manager\n6 vCPU / 24 GB")

    with Cluster("Network data plane"):
        edge = Router("NSX Edge\ntransport node")
        t0 = Switch("Tier-0 gateway\n+ uplink to LAN")
        prep = Switch("Host transport node\n(DVS + overlay)")

    with Cluster("Supervisor  (Workload Control Plane)"):
        sup = [
            Master("Supervisor CP 1"),
            Master("Supervisor CP 2"),
            Master("Supervisor CP 3"),
        ]

    with Cluster("VKS guest cluster"):
        guest_cp = Master("control plane")
        guest_w = Node("worker")

    hosts >> Edge(color="darkgreen") >> vcenter
    vcenter >> Edge(color="darkgreen") >> nsx_mgr
    nsx_mgr >> Edge(color="darkgreen") >> edge
    edge >> Edge(color="darkgreen") >> t0
    nsx_mgr >> Edge(color="darkgreen", style="dashed") >> prep
    t0 >> Edge(color="darkgreen") >> sup[1]
    prep >> Edge(color="darkgreen", style="dashed") >> sup[1]
    sup[1] >> Edge(color="darkgreen") >> guest_cp
    guest_cp >> Edge(color="darkgreen") >> guest_w
