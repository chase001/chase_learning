

class OrderUpdateDelivery(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(OrderUpdateDelivery, self).__init__()
        self.info = "批量发货"
        self.uri = "/order/update/delivery"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(OrderUpdateDelivery.Resp, self).__init__()

