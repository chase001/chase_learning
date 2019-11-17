

class ReturnApplyList(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ReturnApplyList, self).__init__()
        self.info = "分页查询退货申请"
        self.uri = "/returnApply/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            self.receiverKeyword = None
            self.status = None
            self.createTime = None
            self.handleMan = None
            self.handleTime = None
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ReturnApplyList.Resp, self).__init__()

