

class OrderId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(OrderId, self).__init__()
        self.info = "获取订单详情:订单信息、商品信息、操作记录"
        self.uri = "/order/{id}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(OrderId.Resp, self).__init__()

