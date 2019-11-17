

class ReturnApplyId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ReturnApplyId, self).__init__()
        self.info = "获取退货申请详情"
        self.uri = "/returnApply/{id}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ReturnApplyId.Resp, self).__init__()

