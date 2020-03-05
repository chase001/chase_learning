
from common.objects import BaseObj
from Gwe_service.api import *
                

class SubjectListObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(SubjectListObj, self).__init__()
        self.info = "根据专题名称分页获取专题"
        self.uri = "/subject/list"
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
            super(SubjectListObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.CommonPage«CmsSubject»()  # None
            self.message = None  # None
            
        class CommonPage«CmsSubject»(object):
            """None"""
            def __init__(self):
                self.list = [self.CmsSubject()]  # None
                self.pageNum = None  # None
                self.pageSize = None  # None
                self.total = None  # None
                self.totalPage = None  # None
                
            class CmsSubject(object):
                """None"""
                def __init__(self):
    
