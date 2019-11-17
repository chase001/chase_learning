

class ProductAttributeCategoryDeleteId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductAttributeCategoryDeleteId, self).__init__()
        self.info = "删除单个商品属性分类"
        self.uri = "/productAttribute/category/delete/{id}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductAttributeCategoryDeleteId.Resp, self).__init__()

