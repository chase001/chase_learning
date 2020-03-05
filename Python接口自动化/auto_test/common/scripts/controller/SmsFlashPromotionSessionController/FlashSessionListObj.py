
from common.objects import BaseObj
from Gwe_service.api import *
                

class FlashSessionListObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(FlashSessionListObj, self).__init__()
        self.info = "获取全部场次"
        self.uri = "/flashSession/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(FlashSessionListObj.Resp, self).__init__()
            self.code = None  # None
            self.data = [self.SmsFlashPromotionSession()]  # None
            self.message = None  # None
            
        class SmsFlashPromotionSession(object):
            """None"""
            def __init__(self):
                self.createTime = None  # 创建时间
                self.endTime = None  # 每日结束时间
                self.id = None  # 编号
                self.name = None  # 场次名称
                self.startTime = None  # 每日开始时间
                self.status = None  # 启用状态：0->不启用；1->启用
    
