
from common.objects import BaseObj
from ..__init__ import *


class DevBiOrderplandate(BaseFinance):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(DevBiOrderplandate, self).__init__()
        self.info = "添加BI提供的历史订单有效期"
        self.uri = "/dev/bi/orderplandate"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()

    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.orderId = None  # None
            self.classId = None  # None
            self.startDate = None  # None
            # self.endDate = None  # None
            self.add = None
            BaseObj.__init__(**kwargs)

    class Resp(object):
        def __init__(self):
            super(DevBiOrderplandate.Resp, self).__init__()
            self.resultCode = None  # None
            self.resultMessage = None  # None
            self.success = None  # None

