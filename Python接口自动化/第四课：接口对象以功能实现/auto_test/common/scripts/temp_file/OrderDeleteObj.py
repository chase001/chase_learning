

class OrderDelete(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(OrderDelete, self).__init__()
        self.info = "批量删除订单"
        self.uri = "/order/delete"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(OrderDelete.Resp, self).__init__()

