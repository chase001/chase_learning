

class OrderUpdateNote(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(OrderUpdateNote, self).__init__()
        self.info = "备注订单"
        self.uri = "/order/update/note"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            self.note = None
            self.status = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(OrderUpdateNote.Resp, self).__init__()

