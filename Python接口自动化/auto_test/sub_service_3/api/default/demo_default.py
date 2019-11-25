from ..base.demo_base import MyServiceBaseMockDemoApi
from common.mock.BaseMock import BaseMock


class MyServiceMockDemoApi(MyServiceBaseMockDemoApi, BaseMock):
    def __init__(self):
        BaseMock.__init__(self)
        MyServiceBaseMockDemoApi.__init__(self)
        self.mock_name = 'service2mockapi'
        self.status = 0
        self.update_default_body()

    def update_default_body(self):
        self.body.args_1 = 3333
        self.body.args_2 = 44444



    def check(self):
        pass