
from common.objects import BaseObj
from order_service.api import *
                

class BrandListObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(BrandListObj, self).__init__()
        self.info = "根据品牌名称分页获取品牌列表"
        self.uri = "/brand/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.keyword = None
            self.pageNum = None
            self.pageSize = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(BrandListObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.CommonPage«PmsBrand»()  # None
            self.message = None  # None
            
        class CommonPage«PmsBrand»(object):
            """None"""
            def __init__(self):
                self.list = [self.PmsBrand()]  # None
                self.pageNum = None  # None
                self.pageSize = None  # None
                self.total = None  # None
                self.totalPage = None  # None
                
            class PmsBrand(object):
                """None"""
                def __init__(self):
    
