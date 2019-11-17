

class OrderSettingId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(OrderSettingId, self).__init__()
        self.info = "获取指定订单设置"
        self.uri = "/orderSetting/{id}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(OrderSettingId.Resp, self).__init__()

