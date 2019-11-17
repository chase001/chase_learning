

class OrderUpdateClose(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(OrderUpdateClose, self).__init__()
        self.info = "批量关闭订单"
        self.uri = "/order/update/close"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            self.note = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(OrderUpdateClose.Resp, self).__init__()

