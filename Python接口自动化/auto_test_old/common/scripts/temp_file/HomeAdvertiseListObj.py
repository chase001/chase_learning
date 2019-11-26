

class HomeAdvertiseList(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeAdvertiseList, self).__init__()
        self.info = "分页查询广告"
        self.uri = "/home/advertise/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.name = None
            self.type = None
            self.endTime = None
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(HomeAdvertiseList.Resp, self).__init__()
            self.code = None  # None
            self.data = self.CommonPage«SmsHomeAdvertise»()  # None
            self.message = None  # None

        class CommonPage«SmsHomeAdvertise»(object):
            """None"""
            def __init__(self):
                self.list = [self.SmsHomeAdvertise()]  # None
                self.pageNum = None  # None
                self.pageSize = None  # None
                self.total = None  # None
                self.totalPage = None  # None

            class SmsHomeAdvertise(object):
                """None"""
                def __init__(self):
                    self.clickCount = None  # 点击数
                    self.endTime = None  # None
                    self.id = None  # None
                    self.name = None  # None
                    self.note = None  # 备注
                    self.orderCount = None  # 下单数
                    self.pic = None  # None
                    self.sort = None  # 排序
                    self.startTime = None  # None
                    self.status = None  # 上下线状态：0->下线；1->上线
                    self.type = None  # 轮播位置：0->PC首页轮播；1->app首页轮播
                    self.url = None  # 链接地址

