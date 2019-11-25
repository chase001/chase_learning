import pytest


@pytest.fixture
def my_demo_api():
    from sub_service_1.api.default.demo_default import MyServiceDemoApi
    return MyServiceDemoApi(args1='yinyuting')


@pytest.fixture
def my_demo_api_2():
    from sub_service_1.api.default.demo_default import MyServiceDemoApi
    return MyServiceDemoApi(args1='yyt')


@pytest.fixture
def my_demo_mock_api():
    from sub_service_2.api.default.demo_default import MyServiceMockDemoApi
    # 这里可以给默认值或者其他需要mock的值
    return MyServiceMockDemoApi()


def coupon_type_ids(fixture_value):
    return "设置优惠券类型为{}".format(fixture_value)


def user_type_ids(fixture_value):
    return "设置用户类型为{}".format(fixture_value)


@pytest.fixture(params=[0, 1, 2], ids=coupon_type_ids)
def coupon_type_all(request):
    return request.param


@pytest.fixture(params=[0, 1, 2], ids=user_type_ids)
def user_type_all(request):
    return request.param

# todo 以下为直接返回没有teardown的做法
# @pytest.fixture
# def smtp_connection():
#     import smtplib
#     smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
#     return smtp_connection  # provide the fixture value


# todo 以下为包含teardown的做法，其中yield相当于return
# @pytest.fixture
# def smtp_connection():
#     import smtplib
#     smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
#     yield smtp_connection  # provide the fixture value
#     print("teardown smtp")
#     smtp_connection.close()
#
# # todo 以下为包含teardown的做法，和上线效果一样
# @pytest.fixture()
# def smtp_connection():
#     import smtplib
#     with smtplib.SMTP("smtp.gmail.com", 587, timeout=5) as smtp_connection:
#         yield smtp_connection  # provide the fixture value


# todo 参数化 params中每个元素都会是用例被执行一次
# @pytest.fixture(params=["smtp.gmail.com", "mail.python.org"])
# def smtp_connection(request):
#     import smtplib
#     smtp_connection = smtplib.SMTP(request.param, 587, timeout=5)
#     yield smtp_connection
#     print("finalizing %s" % smtp_connection)
#     smtp_connection.close()

