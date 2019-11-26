

class ProductCategoryId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductCategoryId, self).__init__()
        self.info = "根据id获取商品分类"
        self.uri = "/productCategory/{id}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductCategoryId.Resp, self).__init__()

