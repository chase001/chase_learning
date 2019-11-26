

class ReturnReasonUpdateId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ReturnReasonUpdateId, self).__init__()
        self.info = "修改退货原因"
        self.uri = "/returnReason/update/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ReturnReasonUpdateId.Resp, self).__init__()

