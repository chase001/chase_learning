

class HomeBrandList(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeBrandList, self).__init__()
        self.info = "分页查询推荐品牌"
        self.uri = "/home/brand/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.brandName = None
            self.recommendStatus = None
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(HomeBrandList.Resp, self).__init__()

