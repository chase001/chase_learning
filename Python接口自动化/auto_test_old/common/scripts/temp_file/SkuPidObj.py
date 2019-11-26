

class SkuPid(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(SkuPid, self).__init__()
        self.info = "根据商品编号及编号模糊搜索sku库存"
        self.uri = "/sku/{pid}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.pid = None
            self.keyword = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(SkuPid.Resp, self).__init__()

