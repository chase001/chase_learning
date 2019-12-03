
from common.objects import BaseObj
from order_service.api import *
                

class ReturnReasonListObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ReturnReasonListObj, self).__init__()
        self.info = "分页查询全部退货原因"
        self.uri = "/returnReason/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ReturnReasonListObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.CommonPage«OmsOrderReturnReason»()  # None
            self.message = None  # None
            
        class CommonPage«OmsOrderReturnReason»(object):
            """None"""
            def __init__(self):
                self.list = [self.OmsOrderReturnReason()]  # None
                self.pageNum = None  # None
                self.pageSize = None  # None
                self.total = None  # None
                self.totalPage = None  # None
                
            class OmsOrderReturnReason(object):
                """None"""
                def __init__(self):
    
