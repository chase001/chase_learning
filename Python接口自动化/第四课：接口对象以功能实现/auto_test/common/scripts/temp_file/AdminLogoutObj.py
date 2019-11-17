

class AdminLogout(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(AdminLogout, self).__init__()
        self.info = "登出功能"
        self.uri = "/admin/logout"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(AdminLogout.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None

