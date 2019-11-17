

class V1IncomeOrder(BaseFinance):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(V1IncomeOrder, self).__init__()
        self.info = "正向订单财务收入接口"
        self.uri = "/v1/income/order"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.orderId = None  # None
            self.tradeNumber = None  # None
            self.orderType = None  # None
            self.companyId = None  # None
            self.billDate = None  # None
            self.shipDate = None  # None
            self.isPay = None  # None
            self.isDelivered = None  # None
            self.extendBillStatus = None  # None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(V1IncomeOrder.Resp, self).__init__()
            self.resultCode = None  # None
            self.resultMessage = None  # None
            self.success = None  # None

