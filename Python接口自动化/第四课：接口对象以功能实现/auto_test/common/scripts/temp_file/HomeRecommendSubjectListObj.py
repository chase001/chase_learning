

class HomeRecommendSubjectList(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeRecommendSubjectList, self).__init__()
        self.info = "分页查询推荐"
        self.uri = "/home/recommendSubject/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.subjectName = None
            self.recommendStatus = None
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(HomeRecommendSubjectList.Resp, self).__init__()

