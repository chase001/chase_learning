

class ProductCategoryCreate(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductCategoryCreate, self).__init__()
        self.info = "添加产品分类"
        self.uri = "/productCategory/create"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductCategoryCreate.Resp, self).__init__()

