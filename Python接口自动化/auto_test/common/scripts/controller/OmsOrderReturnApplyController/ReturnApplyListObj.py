
from common.objects import BaseObj
from order_service.api import *
                

class ReturnApplyListObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ReturnApplyListObj, self).__init__()
        self.info = "分页查询退货申请"
        self.uri = "/returnApply/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            self.receiverKeyword = None
            self.status = None
            self.createTime = None
            self.handleMan = None
            self.handleTime = None
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ReturnApplyListObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.CommonPage«OmsOrderReturnApply»()  # None
            self.message = None  # None
            
        class CommonPage«OmsOrderReturnApply»(object):
            """None"""
            def __init__(self):
                self.list = [self.OmsOrderReturnApply()]  # None
                self.pageNum = None  # None
                self.pageSize = None  # None
                self.total = None  # None
                self.totalPage = None  # None
                
            class OmsOrderReturnApply(object):
                """None"""
                def __init__(self):
    
