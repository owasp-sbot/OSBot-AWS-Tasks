from unittest import TestCase

from osbot_aws.apis.Cloud_Watch_Logs import Cloud_Watch_Logs
from osbot_aws.apis.ECS import ECS
from osbot_aws.apis.STS import STS

from osbot_aws_tasks.ecs.ECS_Actions import ECS_Actions


class test_ECS_Actions(TestCase):

    def setUp(self) -> None:
        self.ecs_actions = ECS_Actions()

    def test__init__(self):
        assert type(self.ecs_actions.ecs) is ECS

    def test_ecs_setup(self):
        #STS().check_current_session_credentials()
        return
        self.ecs          = ECS()
        self.logs         = Cloud_Watch_Logs()
        self.account_id   = self.ecs.account_id
        self.region       = self.ecs.region
        self.cluster_name = 'test_ecs_cluster_2'
        self.task_family  = 'test_task_create'
        self.cluster_arn  = self.ecs.cluster_arn(self.cluster_name)