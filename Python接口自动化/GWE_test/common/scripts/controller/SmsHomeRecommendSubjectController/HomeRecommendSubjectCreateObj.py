
from common.objects import BaseObj
from order_service.api import *
                

class HomeRecommendSubjectCreateObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeRecommendSubjectCreateObj, self).__init__()
        self.info = "添加首页推荐专题"
        self.uri = "/home/recommendSubject/create"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(HomeRecommendSubjectCreateObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
