

class HomeNewProductList(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeNewProductList, self).__init__()
        self.info = "分页查询推荐"
        self.uri = "/home/newProduct/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.productName = None
            self.recommendStatus = None
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(HomeNewProductList.Resp, self).__init__()

