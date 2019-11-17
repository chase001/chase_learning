

class OrderUpdateReceiverInfo(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(OrderUpdateReceiverInfo, self).__init__()
        self.info = "修改收货人信息"
        self.uri = "/order/update/receiverInfo"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(OrderUpdateReceiverInfo.Resp, self).__init__()

