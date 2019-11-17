

class ProductAttributeListCid(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductAttributeListCid, self).__init__()
        self.info = "根据分类查询属性列表或参数列表"
        self.uri = "/productAttribute/list/{cid}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.cid = None
            self.pageSize = None
            self.pageNum = None
            self.type = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductAttributeListCid.Resp, self).__init__()

