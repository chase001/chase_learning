

class ProductCategoryListWithChildren(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductCategoryListWithChildren, self).__init__()
        self.info = "查询所有一级分类及子分类"
        self.uri = "/productCategory/list/withChildren"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductCategoryListWithChildren.Resp, self).__init__()

