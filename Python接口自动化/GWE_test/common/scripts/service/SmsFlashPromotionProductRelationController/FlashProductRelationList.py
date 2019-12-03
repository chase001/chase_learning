
from order_service.api.controller.SmsFlashPromotionProductRelationController.FlashProductRelationListObj import FlashProductRelationListObj as TemplateController
from common.func import *

class FlashProductRelationList(TemplateController):
    """分页查询不同场次关联及商品信息"""
    def __init__(self, status=0, message='成功', **kwargs):
        super(FlashProductRelationList, self).__init__()
        self.status = status  # 期望返回结果
        self.message = message
        self.update_default_body(**kwargs)

    def update_default_body(self, **kwargs):
        self.body.update_value(**kwargs)

    def check(self):
        """
        1. 检查状态self.status
        2. 检查resp
        3. 检查数据落库
        2. 检查其他内容：redis, mq ,
        :return:
        """
        pass       
        