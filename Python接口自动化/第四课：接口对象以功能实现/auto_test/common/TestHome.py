# -*- coding: UTF-8 -*-

from hujiang.testcasev1.apiQueryOrderV2.BackendQueryOrderObj import BaseBackendQuery
from hujiang.testcasev1.apiQueryOrderV2.queryOrderObj import BaseQueryOrder
from hujiang.testcasev1.apiPlaceOrderV2.BasePlaceOrder import BasePlaceOrder
from hujiang.business.apiCommonTools.ObjUtil import ObjUtil
from functools import wraps
from hujiang.conf.ecm_config import ecm_host


class TestHome(object):
    def __init__(self):
        pass

    def test_case_home(self, is_double=False, is_check=True, is_compare=False, do_not_compare=[],
                       is_pay=False, check_ecm=True, init_order_info=True):
        """

        @param is_double:
        @param is_check:
        @param is_compare:
        @param do_not_compare:
        @param is_pay:
        @param check_type: 0 全部检查，1 仅仅检查普通表，2 仅检查财务域表
        @:param init_order_info: 是否要初始化订单数据
        @return:
        """
        def deco_resp(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                print(('执行用例 %s():' % func.__name__))
                # TODO 如需要切换环境不要直接修改如下代码，请到conf/service/api_host.ini中修改
                BaseBackendQuery.class_host = ecm_host['ecm_backend']  # 切换环境A
                BaseQueryOrder.class_host = ecm_host['query_order']   # 切换环境A
                BasePlaceOrder.class_host = ecm_host['placeorder']   # 切换环境A

                api_obj_a = func(*args, **kwargs)
                if isinstance(api_obj_a, list):
                    api_objs = api_obj_a
                else:
                    api_objs = [api_obj_a]
                for api_obj in api_objs:
                    status = self.get_expect_status(args, api_obj)
                    if status is not None:
                        if status > 4999:
                            api_obj.status_map = dict()
                    api_obj.send_request(status_exp=status)

                    # setattr(api_obj, 'pay_method', kwargs.get("pay_method", None))
                    if is_check and status == api_obj.success_status:
                        if init_order_info:
                            if getattr(api_obj, "init_default_model", None):
                                api_obj.init_default_model()
                                api_obj.init_order_info()
                        # pass
                        api_obj.check(is_pay=is_pay, check_ecm=check_ecm)
                        # api_obj.only_check_finance(is_pay=is_pay, check_ecm=check_ecm)

                if is_double:  # 如果要跑两套环境

                    BaseBackendQuery.class_host = "http://192.168.36.27:9030/"   # 切换环境B
                    BaseQueryOrder.class_host = "http://192.168.38.86:9032/"
                    api_obj_b = func(*args, **kwargs)
                    status = self.get_expect_status(args, api_obj_b)
                    api_obj_b.send_request(status_exp=status)
                    if is_check and status == 0:
                        api_obj_b.check()

                    if is_compare and status == 0:  # 接口返回状态如果不等于0不需要比较内容
                        util_tools = ObjUtil()
                        if api_obj_a.resp is None:
                            assert getattr(api_obj_b.resp, "totalCount", None) is None, "如有totalCount，验证为None"
                            assert len(getattr(api_obj_b.resp, "list", [])) == 0, "如有list，验证为空列表"
                        else:
                            util_tools.is_equal_pw(exp_obj=api_obj_a.resp,
                                                   act_obj=api_obj_b.resp,
                                                   is_normal_obj=True,
                                                   do_not_compare=do_not_compare)
                # if is_cancel:
                #     cancel_order(api_obj_a.resp.orderID)
            return wrapper
        return deco_resp

    def get_expect_status(self, args, api_obj=None):
        if api_obj:
            return api_obj.status
        elif isinstance(args[-2], int):
            return args[-2]
        elif isinstance(args[-1], int):
            return args[-1]
        else:
            return 0



compare_tools = TestHome()





