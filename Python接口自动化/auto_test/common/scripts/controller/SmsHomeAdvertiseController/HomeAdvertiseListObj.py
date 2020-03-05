
from common.objects import BaseObj
from Gwe_service.api import *
                

class HomeAdvertiseListObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(HomeAdvertiseListObj, self).__init__()
        self.info = "分页查询广告"
        self.uri = "/home/advertise/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.name = None
            self.type = None
            self.endTime = None
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(HomeAdvertiseListObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.CommonPage«SmsHomeAdvertise»()  # None
            self.message = None  # None
            
        class CommonPage«SmsHomeAdvertise»(object):
            """None"""
            def __init__(self):
                self.list = [self.SmsHomeAdvertise()]  # None
                self.pageNum = None  # None
                self.pageSize = None  # None
                self.total = None  # None
                self.totalPage = None  # None
                
            class SmsHomeAdvertise(object):
                """None"""
                def __init__(self):
    
