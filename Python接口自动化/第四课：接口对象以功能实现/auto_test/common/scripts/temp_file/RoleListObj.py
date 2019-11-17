

class RoleList(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(RoleList, self).__init__()
        self.info = "获取所有角色"
        self.uri = "/role/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(RoleList.Resp, self).__init__()
            pass

