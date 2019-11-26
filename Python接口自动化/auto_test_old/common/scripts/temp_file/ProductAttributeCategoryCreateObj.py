

class ProductAttributeCategoryCreate(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductAttributeCategoryCreate, self).__init__()
        self.info = "添加商品属性分类"
        self.uri = "/productAttribute/category/create"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.name = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductAttributeCategoryCreate.Resp, self).__init__()

