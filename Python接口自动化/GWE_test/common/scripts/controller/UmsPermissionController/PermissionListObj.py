
from common.objects import BaseObj
from order_service.api import *
                

class PermissionListObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(PermissionListObj, self).__init__()
        self.info = "获取所有权限列表"
        self.uri = "/permission/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(PermissionListObj.Resp, self).__init__()
            self.code = None  # None
            self.data = [self.UmsPermission()]  # None
            self.message = None  # None
            
        class UmsPermission(object):
            """None"""
            def __init__(self):
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
    
