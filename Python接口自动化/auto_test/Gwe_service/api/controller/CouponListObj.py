
from common.objects import BaseObj

from Gwe_service.api import *
                

class CouponListObj(BaseGweManageService):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(CouponListObj, self).__init__()
        self.info = "根据优惠券名称和类型分页获取优惠券列表"
        self.uri = "/coupon/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.name = None
            self.type = None
            self.pageSize = None
            self.pageNum = None
            self.id = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(CouponListObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.CommonPageSmsCoupon()  # None
            self.message = None  # None
            
        class CommonPageSmsCoupon(object):
            """None"""
            def __init__(self):
                self.list = [self.SmsCoupon()]  # None
                self.pageNum = None  # None
                self.pageSize = None  # None
                self.total = None  # None
                self.totalPage = None  # None
                
            class SmsCoupon(object):
                """None"""
                def __init__(self):
                    pass
