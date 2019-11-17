

class HomeRecommendProductUpdateRecommendStatus(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeRecommendProductUpdateRecommendStatus, self).__init__()
        self.info = "批量修改推荐状态"
        self.uri = "/home/recommendProduct/update/recommendStatus"
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
            super(HomeRecommendProductUpdateRecommendStatus.Resp, self).__init__()

