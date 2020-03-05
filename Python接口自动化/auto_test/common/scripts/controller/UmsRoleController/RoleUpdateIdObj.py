
from common.objects import BaseObj
from Gwe_service.api import *
                

class RoleUpdateIdObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(RoleUpdateIdObj, self).__init__()
        self.info = "修改角色"
        self.uri = "/role/update/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
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
            super(RoleUpdateIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
