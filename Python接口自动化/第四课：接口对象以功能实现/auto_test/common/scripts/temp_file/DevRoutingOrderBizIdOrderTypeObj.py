

class DevRoutingOrderBizIdOrderType(BaseFinance):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(DevRoutingOrderBizIdOrderType, self).__init__()
        self.info = "获取billBatchCode的路由规则"
        self.uri = "/dev/routing/order/{bizId}/{orderType}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.bizId = None
            self.orderType = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(DevRoutingOrderBizIdOrderType.Resp, self).__init__()
            self.slot = None  # None
            self.dbSuffix = None  # None
            self.tbSuffix = None  # None

