

class ProductAttributeCategoryId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductAttributeCategoryId, self).__init__()
        self.info = "获取单个商品属性分类信息"
        self.uri = "/productAttribute/category/{id}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductAttributeCategoryId.Resp, self).__init__()

