

class ProductUpdateId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductUpdateId, self).__init__()
        self.info = "更新商品"
        self.uri = "/product/update/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductUpdateId.Resp, self).__init__()

