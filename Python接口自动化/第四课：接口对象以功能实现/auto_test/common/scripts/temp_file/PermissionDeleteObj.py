

class PermissionDelete(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(PermissionDelete, self).__init__()
        self.info = "根据id批量删除权限"
        self.uri = "/permission/delete"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(PermissionDelete.Resp, self).__init__()

