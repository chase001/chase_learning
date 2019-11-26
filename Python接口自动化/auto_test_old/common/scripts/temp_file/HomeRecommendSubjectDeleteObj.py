

class HomeRecommendSubjectDelete(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeRecommendSubjectDelete, self).__init__()
        self.info = "批量删除推荐"
        self.uri = "/home/recommendSubject/delete"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(HomeRecommendSubjectDelete.Resp, self).__init__()

