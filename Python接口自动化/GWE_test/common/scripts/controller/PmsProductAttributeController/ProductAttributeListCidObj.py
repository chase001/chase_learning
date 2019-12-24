
from common.objects import BaseObj
from order_service.api import *
                

class ProductAttributeListCidObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductAttributeListCidObj, self).__init__()
        self.info = "根据分类查询属性列表或参数列表"
        self.uri = "/productAttribute/list/{cid}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.cid = None
            self.pageSize = None
            self.pageNum = None
            self.type = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ProductAttributeListCidObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.CommonPage«PmsProductAttribute»()  # None
            self.message = None  # None
            
        class CommonPage«PmsProductAttribute»(object):
            """None"""
            def __init__(self):
                self.list = [self.PmsProductAttribute()]  # None
                self.pageNum = None  # None
                self.pageSize = None  # None
                self.total = None  # None
                self.totalPage = None  # None
                
            class PmsProductAttribute(object):
                """None"""
                def __init__(self):
    
