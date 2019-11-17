
from common.objects import BaseObj
from ..__init__ import *


class AdminDeleteId(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(AdminDeleteId, self).__init__()
        self.info = "删除指定用户信息"
        self.uri = "/admin/delete/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(AdminDeleteId.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None

