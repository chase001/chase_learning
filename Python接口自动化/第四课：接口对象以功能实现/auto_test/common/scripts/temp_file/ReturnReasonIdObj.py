

class ReturnReasonId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ReturnReasonId, self).__init__()
        self.info = "获取单个退货原因详情信息"
        self.uri = "/returnReason/{id}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ReturnReasonId.Resp, self).__init__()

