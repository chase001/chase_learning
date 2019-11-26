

class FlashSessionUpdateStatusId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(FlashSessionUpdateStatusId, self).__init__()
        self.info = "修改启用状态"
        self.uri = "/flashSession/update/status/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            self.status = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(FlashSessionUpdateStatusId.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None

