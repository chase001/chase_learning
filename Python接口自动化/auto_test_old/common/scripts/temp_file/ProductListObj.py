

class ProductList(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductList, self).__init__()
        self.info = "查询商品"
        self.uri = "/product/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.publishStatus = None
            self.verifyStatus = None
            self.keyword = None
            self.productSn = None
            self.productCategoryId = None
            self.brandId = None
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductList.Resp, self).__init__()

