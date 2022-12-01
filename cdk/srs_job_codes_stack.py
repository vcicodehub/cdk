from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

class SRSJobCodesStack(Stack):

    '''
    STACK
    - get vpc & subnets
    - get ecs security groups
    - create ecs policies
    - create ecs execution role (using policies & AmazonECSTaskExecutionRolePolicy)  
    - create ecs task role (using policies & AmazonECSTaskExecutionRolePolicy)
    '''
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
