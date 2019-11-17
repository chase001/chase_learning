

class ReturnReasonUpdateStatus(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ReturnReasonUpdateStatus, self).__init__()
        self.info = "修改退货原因启用状态"
        self.uri = "/returnReason/update/status"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.status = None
            self.ids = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ReturnReasonUpdateStatus.Resp, self).__init__()

