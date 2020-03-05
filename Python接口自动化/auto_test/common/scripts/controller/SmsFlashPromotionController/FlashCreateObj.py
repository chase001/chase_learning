
from common.objects import BaseObj
from Gwe_service.api import *
                

class FlashCreateObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(FlashCreateObj, self).__init__()
        self.info = "添加活动"
        self.uri = "/flash/create"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.createTime = None  # 秒杀时间段名称
            self.endDate = None  # 结束日期
            self.id = None  # None
            self.startDate = None  # 开始日期
            self.status = None  # 上下线状态
            self.title = None  # None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(FlashCreateObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
