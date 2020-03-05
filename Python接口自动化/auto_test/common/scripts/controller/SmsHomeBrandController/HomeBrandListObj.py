
from common.objects import BaseObj
from Gwe_service.api import *
                

class HomeBrandListObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeBrandListObj, self).__init__()
        self.info = "分页查询推荐品牌"
        self.uri = "/home/brand/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.brandName = None
            self.recommendStatus = None
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(HomeBrandListObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.CommonPage«SmsHomeBrand»()  # None
            self.message = None  # None
            
        class CommonPage«SmsHomeBrand»(object):
            """None"""
            def __init__(self):
                self.list = [self.SmsHomeBrand()]  # None
                self.pageNum = None  # None
                self.pageSize = None  # None
                self.total = None  # None
                self.totalPage = None  # None
                
            class SmsHomeBrand(object):
                """None"""
                def __init__(self):
    
