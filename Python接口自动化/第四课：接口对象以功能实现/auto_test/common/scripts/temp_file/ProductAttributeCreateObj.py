

class ProductAttributeCreate(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductAttributeCreate, self).__init__()
        self.info = "添加商品属性信息"
        self.uri = "/productAttribute/create"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductAttributeCreate.Resp, self).__init__()

