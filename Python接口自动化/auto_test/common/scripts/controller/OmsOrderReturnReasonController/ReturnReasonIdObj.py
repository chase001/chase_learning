
from common.objects import BaseObj
from Gwe_service.api import *
                

class ReturnReasonIdObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ReturnReasonIdObj, self).__init__()
        self.info = "获取单个退货原因详情信息"
        self.uri = "/returnReason/{id}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ReturnReasonIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.OmsOrderReturnReason()  # None
            self.message = None  # None
            
        class OmsOrderReturnReason(object):
            """None"""
            def __init__(self):
                self.createTime = None  # 添加时间
                self.id = None  # None
                self.name = None  # 退货类型
                self.sort = None  # None
                self.status = None  # 状态：0->不启用；1->启用
    
