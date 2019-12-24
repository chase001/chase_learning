
from common.objects import BaseObj
from order_service.api import *
                

class HomeRecommendProductListObj(Baserder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeRecommendProductListObj, self).__init__()
        self.info = "分页查询推荐"
        self.uri = "/home/recommendProduct/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.productName = None
            self.recommendStatus = None
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(HomeRecommendProductListObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.CommonPage«SmsHomeRecommendProduct»()  # None
            self.message = None  # None
            
        class CommonPage«SmsHomeRecommendProduct»(object):
            """None"""
            def __init__(self):
                self.list = [self.SmsHomeRecommendProduct()]  # None
                self.pageNum = None  # None
                self.pageSize = None  # None
                self.total = None  # None
                self.totalPage = None  # None
                
            class SmsHomeRecommendProduct(object):
                """None"""
                def __init__(self):
    
