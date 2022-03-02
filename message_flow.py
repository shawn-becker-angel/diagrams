# from https://medium.com/@arnab.sen44/create-neat-technical-diagrams-using-python-4e5296b78c02

# requires running:
# brew install graphviz
# pip install diagrams  

from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.integration import SQS
from  diagrams.aws.storage import S3
from diagrams.saas.chat import Slack
attributes = {"pad": "1.0", "fontsize": "25"}
with Diagram("message flow", show=True, direction="LR",
             outformat="png",
             graph_attr=attributes):
    elb =  ELB("load balancer")
    service1 = EC2('Service1')
    service2 = EC2('Service2')
    service3 = EC2('service3')
    db = RDS("primary DB")
    
    elb >> service1 >> db
    elb >> service2 >> db
    service1 >> SQS('sqs') >> service3 >> S3('s3')