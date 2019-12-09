from common.CompareModel import CompareModel
from .PwSubServiceUtil import PwSubServiceUtil
from .BusinessInfo import BusinessInfo


class SubServiceCompare(CompareModel):
    def __init__(self, order_id):
        super(SubServiceCompare, self).__init__()
        # 业务模型:拥有生成期望结果的功能
        self.business_info = BusinessInfo(order_id=order_id)
        self.pw = PwSubServiceUtil(order_id=order_id)