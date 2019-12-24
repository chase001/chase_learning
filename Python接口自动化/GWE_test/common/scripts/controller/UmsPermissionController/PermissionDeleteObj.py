
from common.objects import BaseObj
from order_service.api import *
                

class PermissionDeleteObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(PermissionDeleteObj, self).__init__()
        self.info = "根据id批量删除权限"
        self.uri = "/permission/delete"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(PermissionDeleteObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
