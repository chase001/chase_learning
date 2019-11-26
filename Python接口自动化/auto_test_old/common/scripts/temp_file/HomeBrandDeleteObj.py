

class HomeBrandDelete(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeBrandDelete, self).__init__()
        self.info = "批量删除推荐品牌"
        self.uri = "/home/brand/delete"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(HomeBrandDelete.Resp, self).__init__()

