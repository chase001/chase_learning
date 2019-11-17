

class HomeRecommendProductList(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeRecommendProductList, self).__init__()
        self.info = "分页查询推荐"
        self.uri = "/home/recommendProduct/list"
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
            super(HomeRecommendProductList.Resp, self).__init__()

