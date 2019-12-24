
from order_service.api.controller.CmsPrefrenceAreaController.PrefrenceAreaListAllObj import PrefrenceAreaListAllObj as TemplateController
from common.func import *

class PrefrenceAreaListAll(TemplateController):
    """获取所有商品优选"""
    def __init__(self, status=0, message='成功', **kwargs):
        super(PrefrenceAreaListAll, self).__init__()
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
        