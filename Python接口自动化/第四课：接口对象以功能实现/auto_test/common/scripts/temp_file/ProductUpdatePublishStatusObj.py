

class ProductUpdatePublishStatus(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductUpdatePublishStatus, self).__init__()
        self.info = "批量上下架"
        self.uri = "/product/update/publishStatus"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            self.publishStatus = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductUpdatePublishStatus.Resp, self).__init__()

