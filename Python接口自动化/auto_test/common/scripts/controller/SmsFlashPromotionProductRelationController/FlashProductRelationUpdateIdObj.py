
from common.objects import BaseObj
from order_service.api import *
                

class FlashProductRelationUpdateIdObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(FlashProductRelationUpdateIdObj, self).__init__()
        self.info = "修改关联相关信息"
        self.uri = "/flashProductRelation/update/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            self.flashPromotionCount = None  # 限时购数量
            self.flashPromotionId = None  # None
            self.flashPromotionLimit = None  # 每人限购数量
            self.flashPromotionPrice = None  # 限时购价格
            self.flashPromotionSessionId = None  # 编号
            self.id = None  # 编号
            self.productId = None  # None
            self.sort = None  # 排序
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(FlashProductRelationUpdateIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
