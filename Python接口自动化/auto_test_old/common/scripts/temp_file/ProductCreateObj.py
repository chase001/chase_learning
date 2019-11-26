

class ProductCreate(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductCreate, self).__init__()
        self.info = "创建商品"
        self.uri = "/product/create"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductCreate.Resp, self).__init__()

