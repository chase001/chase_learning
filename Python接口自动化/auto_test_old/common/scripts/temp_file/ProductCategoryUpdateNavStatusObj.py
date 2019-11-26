

class ProductCategoryUpdateNavStatus(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductCategoryUpdateNavStatus, self).__init__()
        self.info = "修改导航栏显示状态"
        self.uri = "/productCategory/update/navStatus"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            self.navStatus = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(ProductCategoryUpdateNavStatus.Resp, self).__init__()

