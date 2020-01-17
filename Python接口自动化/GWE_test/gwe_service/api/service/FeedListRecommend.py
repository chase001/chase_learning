
from gwe_service.api.controller.FeedListRecommendObj import FeedListRecommendObj as TemplateController
from common.func import *

class FeedListRecommend(TemplateController):
    """获取单个优惠券的详细信息"""
    def __init__(self, coupon_id, status=0, message='操作成功', **kwargs):
        super(FeedListRecommend, self).__init__(coupon_id)
        self.status = status  # 期望返回结果
        self.message = message
        self.update_default_body(**kwargs)

    def update_default_body(self, **kwargs):
        self.body.update_value(**kwargs)

    def check(self):
        """
        查询类
        1. 检查状态self.status
        2. 检查resp
        3. 检查数据落库
        2. 检查其他内容：redis, mq ,
        :return:
        """
        assert str(self.status) == str(self.resp.code), "该接口实际返回结果中的code{act_code}码不符合期望结果{exp_code}".format(act_code=self.resp.code,
                                                                                                   exp_code=self.status)
        assert str(self.message) == str(self.resp.message)

        # 检查数据库
        exp_obj = TemplateController.Resp.SmsCouponParam()
        from gwe_service.check.OrderPWUtil import db
        coupon_detail = db.sms_coupon(id=self.body.id)
        if coupon_detail:
            fill_in_obj_from_obj(exp_obj, coupon_detail[0])
            # f = "%Y-%m-%dT%H:%M:%S.000+0000"
            # exp_obj.startTime = exp_obj.startTime.strftime(format=f)
            # exp_obj.endTime = exp_obj.endTime.strftime(format=f)
            # exp_obj.enableTime = exp_obj.enableTime.strftime(format=f)

            from common.ObjAssert import ObjAssert
            ObjAssert().is_equal(exp_obj=exp_obj, act_obj=self.resp.data, is_toggle=False, ex=[])
        else:
            assert self.resp.data is None




