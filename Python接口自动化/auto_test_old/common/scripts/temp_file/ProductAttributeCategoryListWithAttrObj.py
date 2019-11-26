

class ProductAttributeCategoryListWithAttr(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductAttributeCategoryListWithAttr, self).__init__()
        self.info = "获取所有商品属性分类及其下属性"
        self.uri = "/productAttribute/category/list/withAttr"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductAttributeCategoryListWithAttr.Resp, self).__init__()

