

class V1IncomeRmaid(BaseFinance):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(V1IncomeRmaid, self).__init__()
        self.info = "根据RMAID,逆向订单财务收入接口"
        self.uri = "/v1/income/rmaid"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.rmaId = None  # None
            self.rmaOperationType = None  # None
            self.companyId = None  # None
            self.orderId = None  # None
            self.tradeNumber = None  # None
            self.orderType = None  # None
            self.isRMAConfirmed = None  # None
            self.isRMARefundCompleted = None  # None
            self.rmaConfirmedDate = None  # None
            self.rmaRefundCompletedDate = None  # None
            self.billBatchCode = None  # None
            self.rmaItems = [self.RMAItem()]  # None

        class RMAItem(object):
            """None"""
            def __init__(self):
                self.productId = None  # None
                self.productType = None  # None
                self.quantity = None  # None
                self.batchId = None  # None
                self.categoryId = None  # None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(V1IncomeRmaid.Resp, self).__init__()
            self.resultCode = None  # None
            self.resultMessage = None  # None
            self.success = None  # None

