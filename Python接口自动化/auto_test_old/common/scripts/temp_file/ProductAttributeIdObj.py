

class ProductAttributeId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductAttributeId, self).__init__()
        self.info = "查询单个商品属性"
        self.uri = "/productAttribute/{id}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductAttributeId.Resp, self).__init__()

