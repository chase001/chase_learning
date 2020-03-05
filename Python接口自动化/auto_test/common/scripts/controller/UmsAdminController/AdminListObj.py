
from common.objects import BaseObj
from Gwe_service.api import *
                

class AdminListObj(BaseGwe):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(AdminListObj, self).__init__()
        self.info = "根据用户名或姓名分页获取用户列表"
        self.uri = "/admin/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.name = None
            self.pageSize = None
            self.pageNum = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(AdminListObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.CommonPage«UmsAdmin»()  # None
            self.message = None  # None
            
        class CommonPage«UmsAdmin»(object):
            """None"""
            def __init__(self):
                self.list = [self.UmsAdmin()]  # None
                self.pageNum = None  # None
                self.pageSize = None  # None
                self.total = None  # None
                self.totalPage = None  # None
                
            class UmsAdmin(object):
                """None"""
                def __init__(self):
    
