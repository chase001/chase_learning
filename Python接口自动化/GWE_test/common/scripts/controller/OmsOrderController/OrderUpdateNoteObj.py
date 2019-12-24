
from common.objects import BaseObj
from order_service.api import *
                

class OrderUpdateNoteObj(Baserder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(OrderUpdateNoteObj, self).__init__()
        self.info = "备注订单"
        self.uri = "/order/update/note"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            self.note = None
            self.status = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(OrderUpdateNoteObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
