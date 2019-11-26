

class PermissionCreate(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(PermissionCreate, self).__init__()
        self.info = "添加权限"
        self.uri = "/permission/create"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(PermissionCreate.Resp, self).__init__()

