
from common.objects import BaseObj
from order_service.api import *
                

class ReturnApplyUpdateStatusIdObj(Baserder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ReturnApplyUpdateStatusIdObj, self).__init__()
        self.info = "修改申请状态"
        self.uri = "/returnApply/update/status/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            self.companyAddressId = None  # 收货地址关联id
            self.handleMan = None  # 处理人
            self.handleNote = None  # 处理备注
            self.id = None  # 服务单号
            self.receiveMan = None  # 收货人
            self.receiveNote = None  # 收货备注
            self.returnAmount = None  # 确认退款金额
            self.status = None  # 申请状态：1->退货中；2->已完成；3->已拒绝
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ReturnApplyUpdateStatusIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
