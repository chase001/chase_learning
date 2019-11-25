
from common.objects import BaseObj
from order_service.api import *
                

class FlashProductRelationCreateObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(FlashProductRelationCreateObj, self).__init__()
        self.info = "批量选择商品添加关联"
        self.uri = "/flashProductRelation/create"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(FlashProductRelationCreateObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
