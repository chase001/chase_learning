

class OrderSettingUpdateId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(OrderSettingUpdateId, self).__init__()
        self.info = "修改指定订单设置"
        self.uri = "/orderSetting/update/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(OrderSettingUpdateId.Resp, self).__init__()

