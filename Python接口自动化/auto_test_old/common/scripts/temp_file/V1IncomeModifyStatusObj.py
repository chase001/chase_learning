

class V1IncomeModifyStatus(BaseFinance):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(V1IncomeModifyStatus, self).__init__()
        self.info = "None"
        self.uri = "/v1/income/modify/status"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.bizId = None  # None
            self.bizType = None  # None
            self.bizIdentity = None  # None
            self.isActive = None  # None
            self.operator = None  # None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(V1IncomeModifyStatus.Resp, self).__init__()
            self.resultCode = None  # None
            self.resultMessage = None  # None
            self.success = None  # None

