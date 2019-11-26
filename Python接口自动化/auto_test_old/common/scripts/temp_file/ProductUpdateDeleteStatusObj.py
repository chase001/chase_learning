

class ProductUpdateDeleteStatus(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductUpdateDeleteStatus, self).__init__()
        self.info = "批量修改删除状态"
        self.uri = "/product/update/deleteStatus"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            self.deleteStatus = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductUpdateDeleteStatus.Resp, self).__init__()

