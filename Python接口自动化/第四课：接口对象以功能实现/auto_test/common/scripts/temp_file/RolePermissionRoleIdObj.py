

class RolePermissionRoleId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(RolePermissionRoleId, self).__init__()
        self.info = "获取相应角色权限"
        self.uri = "/role/permission/{roleId}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.roleId = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(RolePermissionRoleId.Resp, self).__init__()

