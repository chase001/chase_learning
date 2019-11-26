

class ProductUpdateNewStatus(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductUpdateNewStatus, self).__init__()
        self.info = "批量设为新品"
        self.uri = "/product/update/newStatus"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            self.newStatus = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductUpdateNewStatus.Resp, self).__init__()

