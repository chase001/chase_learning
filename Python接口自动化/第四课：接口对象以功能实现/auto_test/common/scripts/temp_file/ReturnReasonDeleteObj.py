

class ReturnReasonDelete(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ReturnReasonDelete, self).__init__()
        self.info = "批量删除退货原因"
        self.uri = "/returnReason/delete"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ReturnReasonDelete.Resp, self).__init__()

