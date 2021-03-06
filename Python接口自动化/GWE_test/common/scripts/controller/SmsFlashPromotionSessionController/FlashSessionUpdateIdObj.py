
from common.objects import BaseObj
from order_service.api import *
                

class FlashSessionUpdateIdObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(FlashSessionUpdateIdObj, self).__init__()
        self.info = "修改场次"
        self.uri = "/flashSession/update/{id}"
        self.method = "post"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            self.createTime = None  # 创建时间
            self.endTime = None  # 每日结束时间
            self.id = None  # 编号
            self.name = None  # 场次名称
            self.startTime = None  # 每日开始时间
            self.status = None  # 启用状态：0->不启用；1->启用
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(FlashSessionUpdateIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = None  # None
            self.message = None  # None
    
