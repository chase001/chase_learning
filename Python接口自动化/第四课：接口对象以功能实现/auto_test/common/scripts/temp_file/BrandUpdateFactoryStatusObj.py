

class BrandUpdateFactoryStatus(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(BrandUpdateFactoryStatus, self).__init__()
        self.info = "批量更新厂家制造商状态"
        self.uri = "/brand/update/factoryStatus"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.ids = None
            self.factoryStatus = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(BrandUpdateFactoryStatus.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None

