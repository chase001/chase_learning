
from common.objects import BaseObj
from order_service.api import *
                

class HomeAdvertiseUpdateIdObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeAdvertiseUpdateIdObj, self).__init__()
        self.info = "修改广告"
        self.uri = "/home/advertise/update/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
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
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(HomeAdvertiseUpdateIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
