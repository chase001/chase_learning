

class SkuUpdatePid(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(SkuUpdatePid, self).__init__()
        self.info = "批量更新库存信息"
        self.uri = "/sku/update/{pid}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.pid = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(SkuUpdatePid.Resp, self).__init__()

