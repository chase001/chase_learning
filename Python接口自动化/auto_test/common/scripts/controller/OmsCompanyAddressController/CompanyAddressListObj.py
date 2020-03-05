
from common.objects import BaseObj
from Gwe_service.api import *
                

class CompanyAddressListObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(CompanyAddressListObj, self).__init__()
        self.info = "获取所有收货地址"
        self.uri = "/companyAddress/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(CompanyAddressListObj.Resp, self).__init__()
            self.code = None  # None
            self.data = [self.OmsCompanyAddress()]  # None
            self.message = None  # None
            
        class OmsCompanyAddress(object):
            """None"""
            def __init__(self):
                self.addressName = None  # 地址名称
                self.city = None  # 市
                self.detailAddress = None  # 详细地址
                self.id = None  # None
                self.name = None  # 收发货人姓名
                self.phone = None  # 收货人电话
                self.province = None  # 省/直辖市
                self.receiveStatus = None  # 是否默认收货地址：0->否；1->是
                self.region = None  # 区
                self.sendStatus = None  # 默认发货地址：0->否；1->是
    
