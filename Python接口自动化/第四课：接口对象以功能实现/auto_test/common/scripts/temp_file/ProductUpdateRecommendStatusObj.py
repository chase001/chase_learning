

class ProductUpdateRecommendStatus(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductUpdateRecommendStatus, self).__init__()
        self.info = "批量推荐商品"
        self.uri = "/product/update/recommendStatus"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            self.recommendStatus = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductUpdateRecommendStatus.Resp, self).__init__()

