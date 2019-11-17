

class FlashList(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(FlashList, self).__init__()
        self.info = "根据活动名称分页查询"
        self.uri = "/flash/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.keyword = None
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(FlashList.Resp, self).__init__()
            pass

