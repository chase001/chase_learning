

class HomeRecommendSubjectCreate(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeRecommendSubjectCreate, self).__init__()
        self.info = "添加首页推荐专题"
        self.uri = "/home/recommendSubject/create"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(HomeRecommendSubjectCreate.Resp, self).__init__()

