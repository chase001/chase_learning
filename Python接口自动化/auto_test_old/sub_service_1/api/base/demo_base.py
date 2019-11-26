# 以下代码从swagger拉取生成，可从swagger重新拉取更新

from common.objects import BaseObj
from ..__init__ import *


class MyServiceBaseDemoApi(BaseServiceDemo):
    """接口对象"""
    def __init__(self, **kwargs):
        super(MyServiceBaseDemoApi, self).__init__()
        self.info = "my demo接口例子"
        self.uri = "mock/origin"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.args_1 = None
            self.args_2 = None
            self.args_3 = None
            BaseObj.__init__(self, **kwargs)

    class Resp(object):
        def __init__(self):
            super(MyServiceBaseDemoApi.Resp, self).__init__()
            self.status = None  # None
            self.msg = None  # 公司ID
            self.data = self.Items()  # 公司ID

        class Items(object):
            def __init__(self):
                self.name = None
                self.age = None
