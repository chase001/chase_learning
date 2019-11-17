

class FlashSessionCreate(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(FlashSessionCreate, self).__init__()
        self.info = "添加场次"
        self.uri = "/flashSession/create"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.createTime = None  # 创建时间
            self.endTime = None  # 每日结束时间
            self.id = None  # 编号
            self.name = None  # 场次名称
            self.startTime = None  # 每日开始时间
            self.status = None  # 启用状态：0->不启用；1->启用
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(FlashSessionCreate.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None

