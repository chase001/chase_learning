
from Gwe_service.api.controller.UmsPermissionController.PermissionDeleteObj import PermissionDeleteObj as TemplateController
from common.func import *

class PermissionDelete(TemplateController):
    """根据id批量删除权限"""
    def __init__(self, status=0, message='成功', **kwargs):
        super(PermissionDelete, self).__init__()
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
        