
from common.objects import BaseObj
from order_service.api import *
                

class OrderListObj(Baserder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(OrderListObj, self).__init__()
        self.info = "查询订单"
        self.uri = "/order/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.orderSn = None
            self.receiverKeyword = None
            self.status = None
            self.orderType = None
            self.sourceType = None
            self.createTime = None
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(OrderListObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.CommonPage«OmsOrder»()  # None
            self.message = None  # None
            
        class CommonPage«OmsOrder»(object):
            """None"""
            def __init__(self):
                self.list = [self.OmsOrder()]  # None
                self.pageNum = None  # None
                self.pageSize = None  # None
                self.total = None  # None
                self.totalPage = None  # None
                
            class OmsOrder(object):
                """None"""
                def __init__(self):
    
