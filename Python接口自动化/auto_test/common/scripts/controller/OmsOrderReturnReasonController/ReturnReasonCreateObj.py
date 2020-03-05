
from common.objects import BaseObj
from Gwe_service.api import *
                

class ReturnReasonCreateObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ReturnReasonCreateObj, self).__init__()
        self.info = "添加退货原因"
        self.uri = "/returnReason/create"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.createTime = None  # 添加时间
            self.id = None  # None
            self.name = None  # 退货类型
            self.sort = None  # None
            self.status = None  # 状态：0->不启用；1->启用
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ReturnReasonCreateObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
