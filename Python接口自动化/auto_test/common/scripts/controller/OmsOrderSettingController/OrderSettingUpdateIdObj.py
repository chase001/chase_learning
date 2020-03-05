
from common.objects import BaseObj
from Gwe_service.api import *
                

class OrderSettingUpdateIdObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(OrderSettingUpdateIdObj, self).__init__()
        self.info = "修改指定订单设置"
        self.uri = "/orderSetting/update/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            self.commentOvertime = None  # 订单完成后自动好评时间（天）
            self.confirmOvertime = None  # 发货后自动确认收货时间（天）
            self.finishOvertime = None  # 自动完成交易时间，不能申请售后（天）
            self.flashOrderOvertime = None  # 秒杀订单超时关闭时间(分)
            self.id = None  # None
            self.normalOrderOvertime = None  # 正常订单超时时间(分)
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(OrderSettingUpdateIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
