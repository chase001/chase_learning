
from common.objects import BaseObj
from Gwe_service.api import *
                

class ProductListObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductListObj, self).__init__()
        self.info = "查询商品"
        self.uri = "/product/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.publishStatus = None
            self.verifyStatus = None
            self.keyword = None
            self.productSn = None
            self.productCategoryId = None
            self.brandId = None
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ProductListObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.CommonPage«PmsProduct»()  # None
            self.message = None  # None
            
        class CommonPage«PmsProduct»(object):
            """None"""
            def __init__(self):
                self.list = [self.PmsProduct()]  # None
                self.pageNum = None  # None
                self.pageSize = None  # None
                self.total = None  # None
                self.totalPage = None  # None
                
            class PmsProduct(object):
                """None"""
                def __init__(self):
    
