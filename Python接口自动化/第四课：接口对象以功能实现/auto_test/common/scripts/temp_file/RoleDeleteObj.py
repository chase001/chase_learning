

class RoleDelete(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(RoleDelete, self).__init__()
        self.info = "批量删除角色"
        self.uri = "/role/delete"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(RoleDelete.Resp, self).__init__()

