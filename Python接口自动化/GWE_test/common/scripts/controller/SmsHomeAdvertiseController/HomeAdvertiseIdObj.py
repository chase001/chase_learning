
from common.objects import BaseObj
from order_service.api import *
                

class HomeAdvertiseIdObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeAdvertiseIdObj, self).__init__()
        self.info = "获取广告详情"
        self.uri = "/home/advertise/{id}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(HomeAdvertiseIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.SmsHomeAdvertise()  # None
            self.message = None  # None
            
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
    
