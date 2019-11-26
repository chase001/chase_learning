

class RolePermissionUpdate(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(RolePermissionUpdate, self).__init__()
        self.info = "修改角色权限"
        self.uri = "/role/permission/update"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.roleId = None
            self.permissionIds = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(RolePermissionUpdate.Resp, self).__init__()

