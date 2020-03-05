
from common.objects import BaseObj
from Gwe_service.api import *
                

class AdminPermissionUpdateObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(AdminPermissionUpdateObj, self).__init__()
        self.info = "给用户分配+-权限"
        self.uri = "/admin/permission/update"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.adminId = None
            self.permissionIds = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(AdminPermissionUpdateObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
