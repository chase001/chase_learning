

class ProductAttributeCategoryUpdateId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductAttributeCategoryUpdateId, self).__init__()
        self.info = "修改商品属性分类"
        self.uri = "/productAttribute/category/update/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            self.name = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductAttributeCategoryUpdateId.Resp, self).__init__()

