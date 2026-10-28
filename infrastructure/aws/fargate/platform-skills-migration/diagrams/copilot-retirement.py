"""
Retiring AWS Copilot: two pipelines coexist, on purpose, until three
specific collisions are resolved in order.

The point of this diagram: the platform's Terraform never touches what
Copilot built. Both stacks run side by side under different resource names
-- that's what makes it safe to migrate without downtime. Only three
GLOBAL namespaces force an order: a DNS record, an ACM validation CNAME,
and any globally-unique name (an S3 bucket). Everything else can simply
exist twice until the old one is deleted.

    ./venv/bin/python infrastructure/aws/fargate/platform-skills-migration/diagrams/copilot-retirement.py
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Fargate
from diagrams.aws.network import ALB, Route53
from diagrams.aws.database import Dynamodb, DynamodbGlobalSecondaryIndex
from diagrams.aws.security import Cognito, CertificateManager
from diagrams.aws.storage import SimpleStorageServiceS3
from diagrams.aws.management import Cloudformation
from diagrams.aws.devtools import CommandLineInterface
from diagrams.onprem.ci import GithubActions
from diagrams.onprem.iac import Terraform
from diagrams.aws.general import Marketplace

GRAPH_ATTR = {
    "fontsize": "15",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "spline",
    "nodesep": "0.5",
    "ranksep": "0.85",
}

C_COPILOT = "#B8860B"    # the old, imperative CLI path
C_PLATFORM = "#7B42BC"   # the new, declarative path
C_COLLIDE = "#d14b4b"    # the three things that genuinely collide

with Diagram(
    "Two stacks coexist safely -- except for three global names",
    filename="infrastructure/aws/fargate/platform-skills-migration/images/copilot-retirement",
    show=False,
    direction="LR",
    graph_attr=GRAPH_ATTR,
):

    with Cluster("Before  —  AWS Copilot CLI, run from a laptop"):
        copilot = CommandLineInterface("copilot init\nsvc init · env init\ndeploy")
        cfn = Cloudformation("Copilot-managed\nCloudFormation stack")
        addon = DynamodbGlobalSecondaryIndex("addon: DynamoDB\n+ 2 GSIs (hand-written)")
        copilot >> Edge(color=C_COPILOT, style="bold") >> cfn
        cfn >> Edge(color=C_COPILOT) >> addon

    with Cluster("After  —  GitHub Actions + Terraform, via OIDC"):
        gha = GithubActions("Platform: App CD\nOIDC, no static keys")
        broker = Marketplace("marketplace broker\nresolve → provision → bind")
        kv = Dynamodb("keyvalue offering\n(GSI support: planned)")
        gha >> Edge(color=C_PLATFORM, style="bold") >> broker
        broker >> Edge(color=C_PLATFORM) >> kv

    with Cluster("What genuinely collides, and the safe order"):
        dns = Route53("1. DNS A record\n(colour subdomain first)")
        acm = CertificateManager("2. ACM validation CNAME\n(issue platform cert first)")
        bucket = SimpleStorageServiceS3("3. S3 bucket name\n(terraform import, not create)")

    with Cluster("AWS  (same app, both pipelines reach it)"):
        alb = ALB("ALB")
        app = Fargate("ECS Fargate\nservice")
        auth = Cognito("Cognito\n(from the old\nCopilot + Cognito project)")
        alb >> Edge(color="gray40") >> app
        auth >> Edge(color="gray40") >> alb

    cfn >> Edge(color=C_COPILOT) >> app
    kv >> Edge(color=C_PLATFORM) >> app
    broker >> Edge(color=C_PLATFORM, label="user-registry offering") >> auth

    cfn >> Edge(color=C_COLLIDE, style="dashed") >> dns
    gha >> Edge(color=C_COLLIDE, style="dashed") >> dns
    cfn >> Edge(color=C_COLLIDE, style="dashed") >> acm
    gha >> Edge(color=C_COLLIDE, style="dashed") >> acm
    cfn >> Edge(color=C_COLLIDE, style="dashed") >> bucket
    gha >> Edge(color=C_COLLIDE, style="dashed") >> bucket
