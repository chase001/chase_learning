

class AdminTokenRefresh(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(AdminTokenRefresh, self).__init__()
        self.info = "刷新token"
        self.uri = "/admin/token/refresh"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(AdminTokenRefresh.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None

