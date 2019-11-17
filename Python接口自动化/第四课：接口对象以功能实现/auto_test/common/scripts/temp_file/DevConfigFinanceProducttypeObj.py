

class DevConfigFinanceProducttype(BaseFinance):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(DevConfigFinanceProducttype, self).__init__()
        self.info = "添加商品类型"
        self.uri = "/dev/config/finance/producttype"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.productType = None  # None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(DevConfigFinanceProducttype.Resp, self).__init__()
            self.resultCode = None  # None
            self.resultMessage = None  # None
            self.success = None  # None

