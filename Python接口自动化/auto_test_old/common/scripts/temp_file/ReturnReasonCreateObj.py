

class ReturnReasonCreate(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ReturnReasonCreate, self).__init__()
        self.info = "添加退货原因"
        self.uri = "/returnReason/create"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ReturnReasonCreate.Resp, self).__init__()

