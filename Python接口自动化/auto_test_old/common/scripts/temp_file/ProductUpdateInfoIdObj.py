

class ProductUpdateInfoId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductUpdateInfoId, self).__init__()
        self.info = "根据商品id获取商品编辑信息"
        self.uri = "/product/updateInfo/{id}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductUpdateInfoId.Resp, self).__init__()

