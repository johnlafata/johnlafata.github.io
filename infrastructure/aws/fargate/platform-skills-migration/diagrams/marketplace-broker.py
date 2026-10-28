"""
The marketplace broker: resolve, provision, bind.

An application requests backing services LOGICALLY in app.yaml -- an
offering and a plan, nothing more. No module name, no ARN, no pool id. The
broker (three Terraform stages: RESOLVE, PROVISION, BIND) turns that request
into real AWS resources and wires their credentials into the running task.

The point of this diagram: the application never names an implementation.
`postgres` could be RDS today and something else tomorrow; the manifest
would not change.

    ./venv/bin/python infrastructure/aws/fargate/platform-skills-migration/diagrams/marketplace-broker.py
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Fargate
from diagrams.aws.network import ALB
from diagrams.aws.database import RDSPostgresqlInstance, Dynamodb
from diagrams.aws.storage import SimpleStorageServiceS3
from diagrams.aws.analytics import ManagedStreamingForKafka
from diagrams.aws.security import Cognito, SecretsManager
from diagrams.aws.general import Marketplace
from diagrams.onprem.iac import Terraform
from diagrams.onprem.vcs import Github

GRAPH_ATTR = {
    "fontsize": "15",
    "bgcolor": "white",
    "pad": "0.5",
    "splines": "spline",
    "nodesep": "0.45",
    "ranksep": "0.95",
}

C_REQUEST = "#2F6FAB"   # the manifest's logical request
C_BROKER = "#7B42BC"    # resolve / provision
C_BIND = "#1f9c8f"       # bind -- credentials into the task

with Diagram(
    "The broker: an application requests logically, the platform resolves concretely",
    filename="infrastructure/aws/fargate/platform-skills-migration/images/marketplace-broker",
    show=False,
    direction="LR",
    graph_attr=GRAPH_ATTR,
):

    manifest = Github("app.yaml\nbacking_services:\n  main-db: {offering: postgres}\n  users: {offering: user-registry}")

    with Cluster("The broker  (broker.tf → provision.tf → bind.tf)"):
        resolve = Marketplace("RESOLVE\noffering + plan\nmerge & validate")
        provision = Terraform("PROVISION\none module per\nrequest, for_each")
        resolve >> Edge(color=C_BROKER, style="bold") >> provision

    with Cluster("marketplace.yaml offerings"):
        pg = RDSPostgresqlInstance("postgres")
        kv = Dynamodb("keyvalue")
        obj = SimpleStorageServiceS3("objectstore")
        stream = ManagedStreamingForKafka("eventstream")
        users = Cognito("user-registry")
        secret = SecretsManager("secrets / ai-model")

    with Cluster("AWS  (bound into the running task)"):
        alb = ALB("ALB\nauthenticate-cognito")
        task = Fargate("ECS Fargate\ntask")
        alb >> Edge(color="gray40") >> task

    manifest >> Edge(color=C_REQUEST, label="requests logically") >> resolve

    provision >> Edge(color=C_BROKER) >> pg
    provision >> Edge(color=C_BROKER) >> kv
    provision >> Edge(color=C_BROKER) >> obj
    provision >> Edge(color=C_BROKER) >> stream
    provision >> Edge(color=C_BROKER) >> users
    provision >> Edge(color=C_BROKER) >> secret

    pg >> Edge(color=C_BIND, label="secret-json") >> task
    kv >> Edge(color=C_BIND, label="config + IAM") >> task
    obj >> Edge(color=C_BIND, label="config + IAM") >> task
    stream >> Edge(color=C_BIND, label="secret-json") >> task
    users >> Edge(color=C_BIND, label="identity") >> alb
    secret >> Edge(color=C_BIND, label="secret-keys") >> task
