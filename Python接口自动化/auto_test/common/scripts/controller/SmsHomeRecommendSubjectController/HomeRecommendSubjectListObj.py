
from common.objects import BaseObj
from Gwe_service.api import *
                

class HomeRecommendSubjectListObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeRecommendSubjectListObj, self).__init__()
        self.info = "分页查询推荐"
        self.uri = "/home/recommendSubject/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.subjectName = None
            self.recommendStatus = None
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(HomeRecommendSubjectListObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.CommonPage«SmsHomeRecommendSubject»()  # None
            self.message = None  # None
            
        class CommonPage«SmsHomeRecommendSubject»(object):
            """None"""
            def __init__(self):
                self.list = [self.SmsHomeRecommendSubject()]  # None
                self.pageNum = None  # None
                self.pageSize = None  # None
                self.total = None  # None
                self.totalPage = None  # None
                
            class SmsHomeRecommendSubject(object):
                """None"""
                def __init__(self):
    
