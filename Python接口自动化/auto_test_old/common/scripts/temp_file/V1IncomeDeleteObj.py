

class V1IncomeDelete(BaseFinance):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(V1IncomeDelete, self).__init__()
        self.info = "根据批次号删除财务记录"
        self.uri = "/v1/income/delete"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.batchCode = None  # None
            self.hjUserId = None  # None
            self.comments = None  # None
            self.operationType = None  # None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(V1IncomeDelete.Resp, self).__init__()
            self.resultCode = None  # None
            self.resultMessage = None  # None
            self.success = None  # None

