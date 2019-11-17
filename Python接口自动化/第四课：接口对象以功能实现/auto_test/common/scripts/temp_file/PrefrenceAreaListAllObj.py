

class PrefrenceAreaListAll(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(PrefrenceAreaListAll, self).__init__()
        self.info = "获取所有商品优选"
        self.uri = "/prefrenceArea/listAll"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(PrefrenceAreaListAll.Resp, self).__init__()

