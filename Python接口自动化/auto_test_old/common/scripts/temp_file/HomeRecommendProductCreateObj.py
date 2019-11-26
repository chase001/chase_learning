

class HomeRecommendProductCreate(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeRecommendProductCreate, self).__init__()
        self.info = "添加首页推荐"
        self.uri = "/home/recommendProduct/create"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(HomeRecommendProductCreate.Resp, self).__init__()

