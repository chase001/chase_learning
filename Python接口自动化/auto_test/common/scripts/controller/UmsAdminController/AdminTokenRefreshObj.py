
from common.objects import BaseObj
from Gwe_service.api import *
                

class AdminTokenRefreshObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(AdminTokenRefreshObj, self).__init__()
        self.info = "刷新token"
        self.uri = "/admin/token/refresh"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(AdminTokenRefreshObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
