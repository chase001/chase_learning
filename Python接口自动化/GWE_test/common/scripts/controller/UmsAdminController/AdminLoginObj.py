
from common.objects import BaseObj
from order_service.api import *
                

class AdminLoginObj(Baserder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(AdminLoginObj, self).__init__()
        self.info = "登录以后返回token"
        self.uri = "/admin/login"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.password = None  # 密码
            self.username = None  # 用户名
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(AdminLoginObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
