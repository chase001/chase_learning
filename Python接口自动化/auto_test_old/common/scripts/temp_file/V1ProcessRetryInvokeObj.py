

class V1ProcessRetryInvoke(BaseFinance):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(V1ProcessRetryInvoke, self).__init__()
        self.info = "补偿订单财务收入接口"
        self.uri = "/v1/processRetryInvoke"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.bizId = None  # None
            self.bizIdentifier = None  # None
            self.bizType = None  # None
            self.bizOperationType = None  # None
            self.orderId = None  # None
            self.tradeNumber = None  # None
            self.orderType = None  # None
            self.companyId = None  # None
            self.isCreate = None  # None
            self.isCompleted = None  # None
            self.createDate = None  # None
            self.completeDate = None  # None
            self.extendBillStatus = None  # None
            self.products = [self.ProductInfo()]  # None

        class ProductInfo(object):
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
            super(V1ProcessRetryInvoke.Resp, self).__init__()
            self.resultCode = None  # None
            self.resultMessage = None  # None
            self.success = None  # None

