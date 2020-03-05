
from Gwe_service.api.controller.SmsHomeBrandController.HomeBrandUpdateSortIdObj import HomeBrandUpdateSortIdObj as TemplateController
from common.func import *

class HomeBrandUpdateSortId(TemplateController):
    """修改品牌排序"""
    def __init__(self, status=0, message='成功', **kwargs):
        super(HomeBrandUpdateSortId, self).__init__()
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
        