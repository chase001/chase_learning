
from common.objects import BaseObj
from Gwe_service.api import *
                

class FlashProductRelationIdObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(FlashProductRelationIdObj, self).__init__()
        self.info = "获取管理商品促销信息"
        self.uri = "/flashProductRelation/{id}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(FlashProductRelationIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.SmsFlashPromotionProductRelation()  # None
            self.message = None  # None
            
        class SmsFlashPromotionProductRelation(object):
            """None"""
            def __init__(self):
                self.flashPromotionCount = None  # 限时购数量
                self.flashPromotionId = None  # None
                self.flashPromotionLimit = None  # 每人限购数量
                self.flashPromotionPrice = None  # 限时购价格
                self.flashPromotionSessionId = None  # 编号
                self.id = None  # 编号
                self.productId = None  # None
                self.sort = None  # 排序
    
