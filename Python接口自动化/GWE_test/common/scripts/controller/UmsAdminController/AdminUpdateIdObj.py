
from common.objects import BaseObj
from order_service.api import *
                

class AdminUpdateIdObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(AdminUpdateIdObj, self).__init__()
        self.info = "修改指定用户信息"
        self.uri = "/admin/update/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            self.createTime = None  # 创建时间
            self.email = None  # 邮箱
            self.icon = None  # 头像
            self.id = None  # None
            self.loginTime = None  # 最后登录时间
            self.nickName = None  # 昵称
            self.note = None  # 备注信息
            self.password = None  # None
            self.status = None  # 帐号启用状态：0->禁用；1->启用
            self.username = None  # None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(AdminUpdateIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
