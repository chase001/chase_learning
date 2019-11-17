

class ProductCategoryUpdateShowStatus(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductCategoryUpdateShowStatus, self).__init__()
        self.info = "修改显示状态"
        self.uri = "/productCategory/update/showStatus"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            self.showStatus = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductCategoryUpdateShowStatus.Resp, self).__init__()

