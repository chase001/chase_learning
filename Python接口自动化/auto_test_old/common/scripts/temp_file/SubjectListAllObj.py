

class SubjectListAll(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(SubjectListAll, self).__init__()
        self.info = "获取全部商品专题"
        self.uri = "/subject/listAll"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(SubjectListAll.Resp, self).__init__()

