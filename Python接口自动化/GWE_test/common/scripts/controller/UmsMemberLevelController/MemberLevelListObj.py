
from common.objects import BaseObj
from order_service.api import *
                

class MemberLevelListObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(MemberLevelListObj, self).__init__()
        self.info = "查询所有会员等级"
        self.uri = "/memberLevel/list"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.defaultStatus = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(MemberLevelListObj.Resp, self).__init__()
            self.code = None  # None
            self.data = [self.UmsMemberLevel()]  # None
            self.message = None  # None
            
        class UmsMemberLevel(object):
            """None"""
            def __init__(self):
                self.commentGrowthPoint = None  # 每次评价获取的成长值
                self.defaultStatus = None  # 是否为默认等级：0->不是；1->是
                self.freeFreightPoint = None  # 免运费标准
                self.growthPoint = None  # None
                self.id = None  # None
                self.name = None  # None
                self.note = None  # None
                self.priviledgeBirthday = None  # 是否有生日特权
                self.priviledgeComment = None  # 是否有评论获奖励特权
                self.priviledgeFreeFreight = None  # 是否有免邮特权
                self.priviledgeMemberPrice = None  # 是否有会员价格特权
                self.priviledgePromotion = None  # 是否有专享活动特权
                self.priviledgeSignIn = None  # 是否有签到特权
    
