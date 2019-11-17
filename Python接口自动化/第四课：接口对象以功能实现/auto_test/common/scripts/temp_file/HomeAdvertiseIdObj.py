

class HomeAdvertiseId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeAdvertiseId, self).__init__()
        self.info = "获取广告详情"
        self.uri = "/home/advertise/{id}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(HomeAdvertiseId.Resp, self).__init__()
            self.code = None  # None
            self.data = self.SmsHomeAdvertise()  # None
            self.message = None  # None

        class SmsHomeAdvertise(object):
            """None"""
            def __init__(self):

