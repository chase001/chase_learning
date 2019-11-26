

class HomeNewProductUpdateSortId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeNewProductUpdateSortId, self).__init__()
        self.info = "修改推荐排序"
        self.uri = "/home/newProduct/update/sort/{id}"
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
            super(HomeNewProductUpdateSortId.Resp, self).__init__()

