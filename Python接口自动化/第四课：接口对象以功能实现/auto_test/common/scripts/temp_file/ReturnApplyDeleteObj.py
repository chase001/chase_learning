

class ReturnApplyDelete(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ReturnApplyDelete, self).__init__()
        self.info = "批量删除申请"
        self.uri = "/returnApply/delete"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ReturnApplyDelete.Resp, self).__init__()

