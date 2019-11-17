

class SubjectList(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(SubjectList, self).__init__()
        self.info = "根据专题名称分页获取专题"
        self.uri = "/subject/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.keyword = None
            self.pageNum = None
            self.pageSize = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(SubjectList.Resp, self).__init__()

