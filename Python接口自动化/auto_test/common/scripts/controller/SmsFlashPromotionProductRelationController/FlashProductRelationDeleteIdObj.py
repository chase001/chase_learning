
from common.objects import BaseObj
from Gwe_service.api import *
                

class FlashProductRelationDeleteIdObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(FlashProductRelationDeleteIdObj, self).__init__()
        self.info = "删除关联"
        self.uri = "/flashProductRelation/delete/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(FlashProductRelationDeleteIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
