
from common.objects import BaseObj
from order_service.api import *
                

class FlashUpdateIdObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(FlashUpdateIdObj, self).__init__()
        self.info = "编辑活动信息"
        self.uri = "/flash/update/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            self.createTime = None  # 秒杀时间段名称
            self.endDate = None  # 结束日期
            self.id = None  # None
            self.startDate = None  # 开始日期
            self.status = None  # 上下线状态
            self.title = None  # None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(FlashUpdateIdObj.Resp, self).__init__()
            pass
    
