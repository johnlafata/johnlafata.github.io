"""
From one application pipeline to a three-repo platform.

Before: a single repo (the "original application deployment pipeline") welded one 
application to the generic parts of a Fargate deploy -- Vault,
Kafka, hand-rolled Terraform, its own CD. Generic and specific were not
separable.

After: three repos, each owning exactly one thing. platform_skills is the
skills/CLI front end; it reads the platform repo's catalog and marketplace
and writes each application's own app.yaml. The platform repo owns the
Terraform and the CD workflows that actually touch AWS. The original application
whose app started this was split back out into its own
frozen repo once its specific pieces were no longer welded to the generic
ones.

    ./venv/bin/python infrastructure/aws/fargate/platform-skills-migration/diagrams/repo-split.py
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Fargate
from diagrams.aws.network import ALB
from diagrams.onprem.vcs import Github
from diagrams.onprem.ci import GithubActions
from diagrams.onprem.iac import Terraform
from diagrams.generic.storage import Storage
from diagrams.onprem.queue import Kafka

GRAPH_ATTR = {
    "fontsize": "15",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "spline",
    "nodesep": "0.55",
    "ranksep": "0.85",
}

C_BEFORE = "#B8860B"   # the welded-together original
C_PLATFORM = "#7B42BC"  # the generic platform repo
C_SKILLS = "#2F6FAB"    # platform_skills, the front end
C_SPLIT = "gray50"      # what moved where

with Diagram(
    "One welded repo becomes three, each owning one thing",
    filename="infrastructure/aws/fargate/platform-skills-migration/images/repo-split",
    show=False,
    direction="LR",
    graph_attr=GRAPH_ATTR,
):

    with Cluster("Before  —  the original application CD pipeline_githubActions\n(one application, everything welded in)"):
        b_vault = Storage("Vault\n(secrets)")
        b_kafka = Kafka("Kafka")
        b_tf = Terraform("hand-rolled\nTerraform")
        b_app = Fargate("The Original Application\n(the oroginal applciation only)")
        b_vault >> Edge(color=C_BEFORE) >> b_app
        b_kafka >> Edge(color=C_BEFORE) >> b_app
        b_tf >> Edge(color=C_BEFORE, style="bold") >> b_app

    with Cluster("After  —  platform_skills\n(the front end, owns no state)"):
        skills = GithubActions("skills + CLI\n(thin wrapper)")

    with Cluster("After  —  aws-fargate-githubactions\n(the platform: catalog + marketplace + CD)"):
        catalog = Terraform("catalog.yaml\n+ marketplace.yaml")
        cd = GithubActions("Platform: App CD\n(OIDC, no static keys)")
        catalog >> Edge(color=C_PLATFORM) >> cd

    with Cluster("After  —  each application repo"):
        manifest = Github("app.yaml\n+ code")

    with Cluster("After  —  The Original Application-infrastructure\n(frozen, still live)"):
        frozen = Fargate("The Original Application\n(unchanged, split out)")

    with Cluster("AWS"):
        alb = ALB("shared ALB")
        fargate = Fargate("ECS Fargate\nservice")
        alb >> Edge(color="gray40") >> fargate

    skills >> Edge(color=C_SKILLS, label="reads") >> catalog
    skills >> Edge(color=C_SKILLS, label="writes") >> manifest
    manifest >> Edge(color=C_PLATFORM) >> cd
    cd >> Edge(color=C_PLATFORM, style="bold") >> fargate

    b_tf >> Edge(color=C_SPLIT, style="dashed", label="generalized, Sep 2026") >> catalog
    b_app >> Edge(color=C_SPLIT, style="dashed", label="split back out") >> frozen
