

class RoleUpdateId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(RoleUpdateId, self).__init__()
        self.info = "修改角色"
        self.uri = "/role/update/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(RoleUpdateId.Resp, self).__init__()

