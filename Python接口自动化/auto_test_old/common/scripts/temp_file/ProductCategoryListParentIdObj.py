

class ProductCategoryListParentId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductCategoryListParentId, self).__init__()
        self.info = "分页查询商品分类"
        self.uri = "/productCategory/list/{parentId}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.parentId = None
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductCategoryListParentId.Resp, self).__init__()

