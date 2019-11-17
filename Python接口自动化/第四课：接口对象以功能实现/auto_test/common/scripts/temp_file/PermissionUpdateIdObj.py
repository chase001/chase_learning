

class PermissionUpdateId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(PermissionUpdateId, self).__init__()
        self.info = "修改权限"
        self.uri = "/permission/update/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(PermissionUpdateId.Resp, self).__init__()

