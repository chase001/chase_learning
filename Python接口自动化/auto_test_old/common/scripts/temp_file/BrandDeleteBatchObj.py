

class BrandDeleteBatch(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(BrandDeleteBatch, self).__init__()
        self.info = "批量删除品牌"
        self.uri = "/brand/delete/batch"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(BrandDeleteBatch.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None

