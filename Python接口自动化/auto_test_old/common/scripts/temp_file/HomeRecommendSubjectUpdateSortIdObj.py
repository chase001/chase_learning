

class HomeRecommendSubjectUpdateSortId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeRecommendSubjectUpdateSortId, self).__init__()
        self.info = "修改推荐排序"
        self.uri = "/home/recommendSubject/update/sort/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            self.sort = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(HomeRecommendSubjectUpdateSortId.Resp, self).__init__()

