
from common.objects import BaseObj
from order_service.api import *
                

class RoleCreateObj(Baserder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(RoleCreateObj, self).__init__()
        self.info = "添加角色"
        self.uri = "/role/create"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.adminCount = None  # 后台用户数量
            self.createTime = None  # 创建时间
            self.description = None  # 描述
            self.id = None  # None
            self.name = None  # 名称
            self.sort = None  # None
            self.status = None  # 启用状态：0->禁用；1->启用
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(RoleCreateObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
