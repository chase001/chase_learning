

class V1IncomeQuery(BaseFinance):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(V1IncomeQuery, self).__init__()
        self.info = "根据订单号查询正向财务收入"
        self.uri = "/v1/income/query"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.bizId = None  # None
            self.bizType = None  # None
            self.bizIdentity = None  # None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(V1IncomeQuery.Resp, self).__init__()
            self.resultCode = None  # None
            self.resultMessage = None  # None
            self.success = None  # None

