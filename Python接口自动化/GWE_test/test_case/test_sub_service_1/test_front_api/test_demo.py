from parameterized import parameterized, param  # 参数化
from sub_service_1.api.default.demo_default import MyServiceDemoApi
from common.log.Logger import log
import pytest


# pytest风格 也可以使用py自带的参数化库
# 运行这个用例需要提供redis地址修改common中的RedisUtil配置，否则会连不上redis卡住
def test_my_demo(my_demo_api, my_demo_mock_api):  # pytest fixture风格
    my_demo_mock_api.resp.data.age = 28
    my_demo_api.mock(my_demo_mock_api)
    my_demo_api.body.args_2 = 'test'
    my_demo_api.send_request()
    my_demo_api.check()



















# parameterized为第三方开源库，对源代码有做修改已支持py4.0框架以及args or kwargs两种模式
@parameterized([
    param('abc', args2='bcd', msg="用例1111描述....."),
    param('7777', args2='8888', msg="用例2222描述....."),
])  # 第三方库参数化风格
def test_my_demo_params(args1, args2=None, msg=None):
    log.step(msg)
    my_demo_api = MyServiceDemoApi()
    my_demo_api.body.args_1 = args1
    my_demo_api.body.args_2 = args2
    my_demo_api.send_request()
    my_demo_api.check()



# todo 修改生成代码脚本
# todo check部分
