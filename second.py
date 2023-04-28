from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.azure.network import ApplicationGateway
from diagrams.azure.network import LoadBalancers
from diagrams.azure.compute import VM
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53

with Diagram("Clustered Web Services2", show=False):
    gateway = ApplicationGateway("Azure Application Gateway")
    lb = LoadBalancers("internal lb")

    with Cluster("Backend"):
        svc_group = [
                     VM("web1"),
                     VM("web2")
                    ]

    # with Cluster("DB Cluster"):
    #     db_primary = RDS("userdb")
    #     db_primary - [RDS("userdb ro")]

    # memcached = ElastiCache("memcached")

    gateway >> lb >> svc_group
    # svc_group >> db_primary
    # svc_group >> memcached