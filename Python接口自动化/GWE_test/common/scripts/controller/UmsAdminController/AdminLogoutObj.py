
from common.objects import BaseObj
from order_service.api import *
                

class AdminLogoutObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(AdminLogoutObj, self).__init__()
        self.info = "登出功能"
        self.uri = "/admin/logout"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(AdminLogoutObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
