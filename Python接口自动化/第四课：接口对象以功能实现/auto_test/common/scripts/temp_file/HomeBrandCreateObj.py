

class HomeBrandCreate(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeBrandCreate, self).__init__()
        self.info = "添加首页推荐品牌"
        self.uri = "/home/brand/create"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(HomeBrandCreate.Resp, self).__init__()

