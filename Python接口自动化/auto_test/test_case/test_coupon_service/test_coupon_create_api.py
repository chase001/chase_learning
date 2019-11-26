

# import sys
# sys.path.append(r'/Users/yinyuting/Documents/auto_test')
from order_service.api.service.coupon_create_api import CouponCreateApi
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
# 健壮性用例
@parameterized([
    param(req_data=dict(amount=-1), msg="验证amount=-1返回错误码xxxx"),
    param(req_data=dict(amount=0), msg="xxxxx"),
    param(req_data=dict(amount=None), msg="xxxxx"),
    param(req_data=dict(amount='1'), msg="xxxxx"),
    param(req_data=dict(amount='abc'), msg="xxxxx"),
    param(req_data=dict(amount=10000000000), msg="xxxxx"),
])  # 第三方库参数化风格
@case_model()
def test_coupon_create_strong_amount_v2(req_data={}, msg=None):
    log.step(msg)
    api_obj = CouponCreateApi(**req_data)
    return api_obj


# 单参数业务覆盖
@parameterized([
    param(req_data=dict(amount=100.99), msg="验证amount=100.99时创建优惠券成功"),
    param(req_data=dict(amount=100), msg="xxxxx"),
    param(req_data=dict(amount=1), msg="xxxxx"),
    param(req_data=dict(amount=999.9), msg="xxxxx"),
])  # 第三方库参数化风格
@case_model()
def test_coupon_create_amount_v2(req_data={}, msg=None):
    log.step(msg)
    api_obj = CouponCreateApi(**req_data)
    return api_obj


f = "%Y-%m-%dT%H:%M:%S00Z"
# 多参数业务覆盖
@parameterized([
    param(input=dict(startTime=now(days=-1, format=f),
                     enableTime=now(days=1, format=f)),
          msg="验证xxxxxx情况下能成功创建优惠券"),
    param(input=dict(startTime=now(days=1, format=f), enableTime=now(days=31, format=f)),
          msg="跨月"),
    param(input=dict(startTime=now(days=1, format=f), enableTime=now(days=365, format=f)),
          msg="跨年"),
    param(input=dict(startTime=now(days=-5, format=f), enableTime=now(days=-1, format=f)),
          msg="报错1"),
    param(input=dict(startTime=now(days=6, format=f), enableTime=now(days=5, format=f)),
          msg="报错2"),
])  # 第三方库参数化风格
@case_model()
def test_coupon_create_time_v2(input={}, msg=None):
    log.step(msg)
    api_obj = CouponCreateApi(**input)
    return api_obj


# pytest原生 conftest风格
@case_model()
def test_combo_coupon_type_and_user_type(user_type_all, coupon_type_all):
    log.step("验证用户类型和优惠券类型组合情况创建优惠券成功")
    api_obj = CouponCreateApi(type=coupon_type_all, useType=user_type_all)
    return api_obj


# 外部check，主要用于接口对比的校验方式

def check(api_obj, compare_obj):
    fill_in_obj_from_obj(compare_obj.body, api_obj.body)
    compare_obj.host = "http://test-xxxxx/"  # 不用看这个调不通。。。只是一个例子
    compare_obj.send_request()
    from common.ObjAssert import ObjAssert
    assert_obj = ObjAssert()
    assert_obj.is_equal(exp_obj=compare_obj.resp, act_obj=api_obj.resp)


@parameterized([
    param(req_data=dict(amount=100.99), msg="验证amount=100.99时创建优惠券成功")
])  # 对服务对比检查
@case_model(compare_hook=check, compare_obj=CouponCreateApi())
def test_coupon_compare_other_api(input={}, msg=None):
    log.step(msg)
    api_obj = CouponCreateApi(**input)
    return api_obj


def test_coupon_create_strong():
    log.step("验证优惠券价格=100时候接口逻辑正确")
    my_demo_api = CouponCreateApi(amount=0, name="jfkdjfdo");
    # my_demo_api.body.amount = 100
    my_demo_api.send_request()
    my_demo_api.check()

