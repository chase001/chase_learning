

class ProductCategoryUpdateId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductCategoryUpdateId, self).__init__()
        self.info = "修改商品分类"
        self.uri = "/productCategory/update/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductCategoryUpdateId.Resp, self).__init__()

