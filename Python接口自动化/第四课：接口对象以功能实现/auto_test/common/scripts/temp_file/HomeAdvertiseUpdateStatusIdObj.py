

class HomeAdvertiseUpdateStatusId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeAdvertiseUpdateStatusId, self).__init__()
        self.info = "修改上下线状态"
        self.uri = "/home/advertise/update/status/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            self.status = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(HomeAdvertiseUpdateStatusId.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None

