

class ReturnReasonList(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ReturnReasonList, self).__init__()
        self.info = "分页查询全部退货原因"
        self.uri = "/returnReason/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ReturnReasonList.Resp, self).__init__()

