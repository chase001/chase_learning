
from common.objects import BaseObj
from order_service.api import *
                

class FlashProductRelationListObj(Baserder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(FlashProductRelationListObj, self).__init__()
        self.info = "分页查询不同场次关联及商品信息"
        self.uri = "/flashProductRelation/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.flashPromotionId = None
            self.flashPromotionSessionId = None
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(FlashProductRelationListObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.CommonPage«SmsFlashPromotionProduct»()  # None
            self.message = None  # None
            
        class CommonPage«SmsFlashPromotionProduct»(object):
            """None"""
            def __init__(self):
                self.list = [self.SmsFlashPromotionProduct()]  # None
                self.pageNum = None  # None
                self.pageSize = None  # None
                self.total = None  # None
                self.totalPage = None  # None
                
            class SmsFlashPromotionProduct(object):
                """None"""
                def __init__(self):
    
