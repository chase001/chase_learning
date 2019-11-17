

class FlashId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(FlashId, self).__init__()
        self.info = "获取活动详情"
        self.uri = "/flash/{id}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(FlashId.Resp, self).__init__()
            pass

