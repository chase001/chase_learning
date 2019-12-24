
from common.objects import BaseObj
from order_service.api import *
                

class AdminRoleUpdateObj(Baserder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(AdminRoleUpdateObj, self).__init__()
        self.info = "给用户分配角色"
        self.uri = "/admin/role/update"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.adminId = None
            self.roleIds = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(AdminRoleUpdateObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
