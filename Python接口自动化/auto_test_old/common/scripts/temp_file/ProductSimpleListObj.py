

class ProductSimpleList(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductSimpleList, self).__init__()
        self.info = "根据商品名称或货号模糊查询"
        self.uri = "/product/simpleList"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.keyword = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductSimpleList.Resp, self).__init__()

