

class RoleCreate(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(RoleCreate, self).__init__()
        self.info = "添加角色"
        self.uri = "/role/create"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(RoleCreate.Resp, self).__init__()

