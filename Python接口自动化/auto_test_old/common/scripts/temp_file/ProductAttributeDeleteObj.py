

class ProductAttributeDelete(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductAttributeDelete, self).__init__()
        self.info = "批量删除商品属性"
        self.uri = "/productAttribute/delete"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductAttributeDelete.Resp, self).__init__()

