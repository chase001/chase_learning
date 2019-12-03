
from common.objects import BaseObj
from order_service.api import *
                

class RolePermissionUpdateObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(RolePermissionUpdateObj, self).__init__()
        self.info = "修改角色权限"
        self.uri = "/role/permission/update"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.roleId = None
            self.permissionIds = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(RolePermissionUpdateObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
