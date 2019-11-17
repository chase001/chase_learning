

class DevRoutingBillBatchCode(BaseFinance):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(DevRoutingBillBatchCode, self).__init__()
        self.info = "获取billBatchCode的路由规则"
        self.uri = "/dev/routing/{billBatchCode}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.billBatchCode = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(DevRoutingBillBatchCode.Resp, self).__init__()
            self.slot = None  # None
            self.dbSuffix = None  # None
            self.tbSuffix = None  # None

