
from common.objects import BaseObj
from Gwe_service.api import *
                

class AdminInfoObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(AdminInfoObj, self).__init__()
        self.info = "获取当前登录用户信息"
        self.uri = "/admin/info"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(AdminInfoObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
