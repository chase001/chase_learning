

class ReturnApplyUpdateStatusId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ReturnApplyUpdateStatusId, self).__init__()
        self.info = "修改申请状态"
        self.uri = "/returnApply/update/status/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ReturnApplyUpdateStatusId.Resp, self).__init__()

