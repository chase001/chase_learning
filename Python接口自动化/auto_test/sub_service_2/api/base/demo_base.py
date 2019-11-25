from sub_service_2.api.Base2ServiceDemo import Base2ServiceDemo
from common.objects import BaseObj


class MyServiceBaseMockDemoApi(Base2ServiceDemo):
    """接口对象"""
    def __init__(self, **kwargs):
        super(MyServiceBaseMockDemoApi, self).__init__()
        self.info = "my demo mock 接口例子"
        self.uri = "mock/test"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.args_1 = None
            self.args_2 = None
            self.args_3 = None
            super(MyServiceBaseMockDemoApi.Body, self).__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(MyServiceBaseMockDemoApi.Resp, self).__init__()
            self.status = None  # None
            self.msg = None  # 公司ID
            self.data = self.Items()  # 公司ID

        class Items(object):
            def __init__(self):
                self.name = None
                self.age = None
