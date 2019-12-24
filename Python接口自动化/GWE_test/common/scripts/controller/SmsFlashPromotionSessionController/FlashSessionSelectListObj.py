
from common.objects import BaseObj
from order_service.api import *
                

class FlashSessionSelectListObj(Baserder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(FlashSessionSelectListObj, self).__init__()
        self.info = "获取全部可选场次及其数量"
        self.uri = "/flashSession/selectList"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.flashPromotionId = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(FlashSessionSelectListObj.Resp, self).__init__()
            self.code = None  # None
            self.data = [self.SmsFlashPromotionSessionDetail()]  # None
            self.message = None  # None
            
        class SmsFlashPromotionSessionDetail(object):
            """None"""
            def __init__(self):
                self.createTime = None  # 创建时间
                self.endTime = None  # 每日结束时间
                self.id = None  # 编号
                self.name = None  # 场次名称
                self.productCount = None  # None
                self.startTime = None  # 每日开始时间
                self.status = None  # 启用状态：0->不启用；1->启用
    
