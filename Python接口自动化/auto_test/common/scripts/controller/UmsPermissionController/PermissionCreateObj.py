
from common.objects import BaseObj
from Gwe_service.api import *
                

class PermissionCreateObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(PermissionCreateObj, self).__init__()
        self.info = "添加权限"
        self.uri = "/permission/create"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.createTime = None  # 创建时间
            self.icon = None  # 图标
            self.id = None  # None
            self.name = None  # 名称
            self.pid = None  # 父级权限id
            self.sort = None  # 排序
            self.status = None  # 启用状态；0->禁用；1->启用
            self.type = None  # 权限类型：0->目录；1->菜单；2->按钮（接口绑定权限）
            self.uri = None  # 前端资源路径
            self.value = None  # 权限值
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(PermissionCreateObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
