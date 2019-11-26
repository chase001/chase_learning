

class AdminRoleAdminId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(AdminRoleAdminId, self).__init__()
        self.info = "获取指定用户的角色"
        self.uri = "/admin/role/{adminId}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.adminId = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(AdminRoleAdminId.Resp, self).__init__()
            self.code = None  # None
            self.data = [self.UmsRole()]  # None
            self.message = None  # None

        class UmsRole(object):
            """None"""
            def __init__(self):
                self.adminCount = None  # 后台用户数量
                self.createTime = None  # 创建时间
                self.description = None  # 描述
                self.id = None  # None
                self.name = None  # 名称
                self.sort = None  # None
                self.status = None  # 启用状态：0->禁用；1->启用

