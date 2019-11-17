
from order_service.api.service.coupon_create_api import CouponCreateApi
from common.log.Logger import log


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


# # parameterized为第三方开源库，对源代码有做修改已支持py4.0框架以及args or kwargs两种模式
# @parameterized([
#     param('abc', args2='bcd', msg="用例1111描述....."),
#     # param('7777', args2='8888', msg="用例2222描述....."),
# ])  # 第三方库参数化风格
def test_coupon_create_strong():
    log.step("验证优惠券价格=100时候接口逻辑正确")
    my_demo_api = CouponCreateApi()
    my_demo_api.body.amount = 100
    my_demo_api.send_request()
    my_demo_api.check()

