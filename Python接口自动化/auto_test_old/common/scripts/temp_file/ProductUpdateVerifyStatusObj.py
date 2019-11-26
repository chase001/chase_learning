

class ProductUpdateVerifyStatus(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductUpdateVerifyStatus, self).__init__()
        self.info = "批量修改审核状态"
        self.uri = "/product/update/verifyStatus"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            self.verifyStatus = None
            self.detail = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductUpdateVerifyStatus.Resp, self).__init__()

