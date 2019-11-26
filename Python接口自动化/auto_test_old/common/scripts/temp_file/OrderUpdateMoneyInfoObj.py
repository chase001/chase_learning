

class OrderUpdateMoneyInfo(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(OrderUpdateMoneyInfo, self).__init__()
        self.info = "修改订单费用信息"
        self.uri = "/order/update/moneyInfo"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(OrderUpdateMoneyInfo.Resp, self).__init__()

