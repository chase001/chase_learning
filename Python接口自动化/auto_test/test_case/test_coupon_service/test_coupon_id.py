
from order_service.api.service.CouponId import CouponId
from common.log.Logger import log
from parameterized import parameterized, param
from common.TestHome import case_model
from common.func import now, fill_in_obj_from_obj



# pytest风格 也可以使用py自带的参数化库
# 运行这个用例需要提供redis地址修改common中的RedisUtil配置，否则会连不上redis卡住
# def test_my_demo(my_demo_api, my_demo_mock_api):  # pytest fixture风格
#     my_demo_mock_api.resp.data.age = 28
#     my_demo_api.mock(my_demo_mock_api)
#     my_demo_api.body.args_2 = 'cuirong'
#     my_demo_api.send_request()
#     my_demo_api.check()

# 1. 执行用例
# 2. 文件分布管理
# 2. debug看实现，重点：继承和send_requests
# 3. 其他相关知识点：python导入（__init__）,


# parameterized为第三方开源库，对源代码有做修改已支持py4.0框架以及args or kwargs两种模式
@parameterized([
    param(2, msg="查询普通优惠券详情结果正确"),
])  # 第三方库参数化风格

#hw
@case_model()
def test_coupon_id_success(coupon_id, msg=None, code=200):
    log.step(msg)
    api_obj = CouponId(coupon_id=coupon_id, status=code)
    return api_obj



