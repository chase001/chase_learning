# -*- coding:utf8 -*-
import re
from common.func import *
from common.log.Logger import log


class ObjAssert(object):
    def __init__(self):
        """
        所有pw结果带id的必需自行加上id
        :return:
        """

        self.error_list = []  # todo rename error_list

    def error_print(self, title=None):  # todo rename
        if self.error_list:
            log.error(title)
            for error in self.error_list:
                # print('\033[1;31;40m', error, '\033[0m')    # 改log
                print("\n")
                log.error(msg=error)
            self.print_order_id_diff()  # query 比较开关
            print("=====================END======================")

    def is_equal(self, exp_obj, map=None, is_update_api=False, is_toggle=True,
                 is_assert=True, ex=[], external_msg="", act_obj=None):
        """
        对比接口与peewee返回的结果
        :param exp_obj: 期望结果对象，结构要与实际结果一致
        :param map:
        :param is_update_api: 这个传True 会排除掉传入的request或者返回的response中为空,但数据库中有值的数据,
        主要用于更新的这类接口,需求:如果数据库有值而传入的值为空,则不更新数据库
        :param is_toggle: 是否要在对比过程中将act_obj中的驼峰字段名转换成下划线类型字段名，默认True转换
        :return:
        """
        if act_obj is None:
            act_obj = self
        if hasattr(act_obj, 'data'):
            self.for_obj(act_obj=act_obj.data, exp_obj=exp_obj, map=map, is_toggle=is_toggle, ex=ex)
        else:
            # 开始遍历实际response中的属性值
            self.for_obj(act_obj=act_obj, exp_obj=exp_obj, map=map, is_toggle=is_toggle, ex=ex)
        # log.formmat_error(title="Assert Error Msg", content=self.error_list)

        if is_update_api and self.error_list:
            error_list_tmp = self.error_list.copy()
            #  假如是更新类型的api 则数据库中有值,传入值为空,判断为正确,从错误列表中排除
            for item in error_list_tmp:
                if item.get('act_value') is None:
                    self.error_list.remove(item)
            # log.formmat_error(title="Update API Strip None", content=self.error_list)
            self.error_print("==============Update API Strip None============")

        if is_assert:
            self.error_print("=====================Assert Error Msg {}======================".format(external_msg))
            check_equal(act_v=self.error_list, exp_v=[], err_msg="API Test Fail!!!!!!!")
        else:
            return self.error_list

    def is_equal_pw(self, exp_obj, act_obj=None, do_not_compare=list(), is_normal_obj=False):
        """
        对比两个peewee返回的结果
        :param exp_obj: 期望值
        :param act_obj: 实际值
        :param do_not_compare: 不需要对比的字段列表
        :param is_normal_obj:这是啥？
        :return:
        """
        del_args = ["dirty_fields", "DoesNotExist"] + do_not_compare

        act_obj = act_obj if act_obj else self

        # 将act_obj中需要对比的字段setattr进去一个新类，以便for_obj方法可以正确对比
        # 不知道为什么vars(object)取不到peewee返回对象中的值，所以多此一步转换
        class Temp(object):
            pass

        new_act = Temp()
        if is_normal_obj:
            for k, value in vars(act_obj).items():
                v = getattr(act_obj, k)
                if str(k).startswith("_") is False and k not in del_args:
                    setattr(new_act, k, v)
        else:
            for k in dir(act_obj):
                v = getattr(act_obj, k)
                if str(k).startswith("_") is False and k not in del_args:
                    setattr(new_act, k, v)

        # 对比转换过的act_obj和原始exp_obj，is_toggle传递False，不进行大小写转换
        self.for_obj(act_obj=new_act, exp_obj=exp_obj, is_toggle=False, ex=del_args)
        self.error_print("=======Assert Error Msg==========")
        self.print_order_id_diff()
        # log.formmat_error(title="Assert Error Msg", content=self.error_list)
        check_equal(act_v=self.error_list,
                    exp_v=[],
                    err_msg="Peewee Compare Fail!!!!!!!")

    def print_order_id_diff(self):
        if self.error_list:
            log.error("=============仅仅打印orderId不一致的情况===============")
            for error in self.error_list:
                # print('\033[1;31;40m', error, '\033[0m')    # 改log

                if isinstance(error, dict):
                    if 'orderId' in error.get('key', ''):
                        print("\n")
                        log.error(msg=error)
            print("=====================END仅仅打印orderId不一致的情况======================")

    def for_obj(self, act_obj, exp_obj, map=None, is_delete_id=False, is_toggle=True, name=None, index=None, ex=[],
                need_to_compare=list()):
        # assert_list = []
        obj = act_obj
        path = ""
        if name is not None:
            path += "{name}".format(name=name)
        if index is not None:
            path += "/{index}".format(index=index)

        for name, value in list(vars(obj).items()):
            if name == 'error_list': continue
            if name in ex: continue  # 排除对比的字段
            if len(need_to_compare) > 0 and name not in need_to_compare: continue  # 如果指定了对比的属性，则属性名不在指定列表时就跳过
            is_object = is_custom_object(value)
            m = self.map_convert(name=name,
                                 map=map,
                                 is_delete_id=is_delete_id,
                                 is_toggle=is_toggle
                                 )
            new_name = m.get('new_name')
            sub_map = m.get('sub_map')

            #  region 在exp_obj中寻找对应的key
            try:
                exp_value = getattr(exp_obj, new_name)
            except AttributeError as e:
                exp_value = None
                msg = '{exp_obj}中不存在属性:{new_name}'.format(exp_obj=exp_obj, new_name=new_name)
                print(msg)
                self.error_list.append(msg)
            # endregion

            if exp_value:  # 在期望结果中存在对应的key
                if is_object:
                    # self.p=path
                    self.for_obj(act_obj=value, exp_obj=exp_value, map=sub_map, name=path + "/" + name,
                                 is_toggle=is_toggle, ex=ex, need_to_compare=need_to_compare)
                elif isinstance(value, (list, tuple)) and value:  # 此处之前忘记判断空列表的情况
                    # 先判断list长度是否一致
                    self.deal_equal_msg(
                        self.equal_msg(len(exp_value), len(value), key="{key}的长度".format(key=new_name)))
                    # 对象的值是list,开始遍历list中的值
                    for index, v in enumerate(value):
                        if is_custom_object(v):
                            try:
                                self.for_obj(act_obj=value[index], exp_obj=exp_value[index], map=sub_map,
                                             name=path + "/" + name,
                                             index=index, is_toggle=is_toggle, ex=ex, need_to_compare=need_to_compare)
                            except IndexError as e:
                                # msg = '{value}对应的期望结果{exp_value}中没有值'.format(value=value,exp_value=exp_value)
                                msg = '{value}对应的期望结果{exp_value}中没有值'
                                print(msg)
                                self.error_list.append(msg)
                        else:
                            try:
                                exp_value_ele = exp_value[index]
                            except Exception as e:
                                exp_value_ele = None
                            self.deal_equal_msg(
                                self.equal_msg(exp_value_ele, v, key=path + "/" + name))

                else:
                    self.deal_equal_msg(self.equal_msg(exp_value, value, path + "/" + name))
            else:
                self.deal_equal_msg(self.equal_msg(exp_value, value, path + "/" + name))

                # return assert_list

    def deal_equal_msg(self, msg):
        if msg:
            self.error_list.append(msg)

    def str_is_equal(self, exp_value, act_value):

        exp_value = self.deal_value(exp_value)
        act_value = self.deal_value(act_value)
        act_value = self.deal_time(act_value)
        exp_value = self.deal_time(exp_value)

        # print("期望值:", exp_value, "实际值:", act_value)
        log.check("比较期望值:" + str(exp_value) + "实际值:" + str(act_value))
        if act_value == exp_value:
            return True
        elif act_value in [None, []] and exp_value in [None, []]:
            return True
        elif act_value in [None, {}, '{}'] and exp_value in [None, {}, '{}']:
            return True
        elif act_value in [None, False] and exp_value in [None, False]:
            return True
        elif act_value in ['', None, 'null'] and exp_value in ['', None, 'null']:
            return True
        elif isinstance(exp_value, str) and isinstance(act_value, str):
            mat_exp = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", exp_value)
            mat_act = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", act_value)
            if mat_act and mat_exp:
                if mat_act.groups()[0] == mat_exp.groups()[0]:
                    return True
        else:
            try:
                if float(act_value) == float(exp_value):
                    return True
                else:
                    return False
            except Exception as e:
                # print e
                return False

    def deal_value(self, value):
        """
        统一处理空类
        :param value:
        :return:
        """
        if isinstance(value, (list, tuple)) and len(value) > 0:
            for index, item in enumerate(value):
                if is_custom_object(item):
                    for n, v in list(vars(item).items()):
                        if v is not None: return value
                    return None
                else:
                    return value
        else:
            return value

    def deal_time(self, value):
        """
        将时间统一处理成xxxxTxxxx+0800
        :param value:
        :return:
        """
        pattern = re.compile(r"^\d{4}(-\d\d){2} \d\d(:\d\d){2}")
        pattern1 = re.compile(r"^\d{4}(-\d\d){2}$")
        pattern2 = re.compile(r"^\d{4}(-\d\d){2}[T]\d\d(:\d\d){2}[+08:00]]")
        pattern3 = re.compile(r"\d{10}000$")  # 13位时间戳
        try:
            if pattern.match(str(value)):
                temp = value.split(' ')
                return temp[0] + 'T' + temp[1] + '+0800'
            elif pattern1.match(str(value)):
                return value + 'T00:00:00+0800'
            elif pattern2.match(str(value)):
                value = value.replace("08:00", "0800")
                return value
            elif pattern3.match(str(value)):
                import time
                new_time = time.localtime(value / 1000)
                return time.strftime("%Y-%m-%dT%H:%M:%S+0800", new_time)
            else:
                return value
        except Exception as e:
            return value

    # todo 先替换map 在转换大小写
    def map_convert(self, name, map, is_delete_id=True, is_toggle=True):
        # name = self.toggle_case(name)
        if map:
            for k, v in list(map.items()):
                if name == k:
                    if isinstance(v, dict):
                        new_name = list(v.keys())[0]
                        return dict(new_name=new_name,
                                    sub_map=v[new_name])
                    else:
                        # print(v+"haha")
                        return dict(new_name=v,
                                    sub_map=None)
            return dict(new_name=self.toggle_case(name, is_delete_id=is_delete_id, is_toggle=is_toggle),
                        sub_map=map)
        else:
            return dict(new_name=self.toggle_case(name, is_delete_id=is_delete_id, is_toggle=is_toggle),
                        sub_map=map)

    def toggle_case(self, name, is_delete_id=True, is_toggle=True):
        """
        将saleProductId转换成sale_product
        :param name:
        :return:
        """
        skip_upper = ["ID", "XB", "RMA"]
        new_name = ''
        case = ''
        if is_toggle is True:
            for u in skip_upper:
                target = u[0] + u[1:].lower()
                name = name.replace(u, target)
            name = name[0].lower() + name[1:]
            for s in name:
                if s.isupper():
                    new_name = new_name + case.lower() + "_"
                    case = ''  # 清空case
                    case = case + s.lower()
                else:
                    case = case + s
        else:
            # 处理不需要转换大小写的情况
            case = name
        if case and new_name:
            if case == 'id' and is_delete_id:
                new_name = new_name[:-1]
            else:
                new_name = new_name + case
        else:
            new_name = case
        return new_name

    def equal_msg(self, exp_value, act_value, key=None):
        # print("路径:", key)
        log.check("路径:" + key)
        if self.str_is_equal(exp_value, act_value):
            return None
        else:
            msg = dict(act_value=act_value,
                       exp_value=exp_value,
                       key=key)
            return msg

    def assert_two_pw_obj_having_modified(self, origin_obj=None, obj=None, modified_dict=None, ex=[],
                                          is_normal_obj=False):
        """
        对比两个无嵌套对象被改变的值和并修改原始数据返回两个obj
        :param origin_obj:
        :param obj:
        :param modified_dict:
        :param ex:
        :return:
        """

        def error_msg(key, value, act_value):
            return "新对象中属性值" + str(key) + "期望结果是:" + str(value) + ",实际结果是:" + str(act_value)

        ex.extend(["error_list"])
        modified_error = []
        if modified_dict:
            for key, value in modified_dict.items():
                if key in ex:
                    continue
                if hasattr(obj, key) is True:
                    if self.str_is_equal(getattr(obj, key), value) is False:
                        modified_error.append(error_msg(key,
                                                        value,
                                                        getattr(obj, key)
                                                        ))
                    elif origin_obj:
                        setattr(origin_obj, key, value)
                    else:
                        pass
            if origin_obj:
                self.is_equal_pw(origin_obj, obj, ex, is_normal_obj=is_normal_obj)

        else:
            self.is_equal_pw(origin_obj, obj, ex, is_normal_obj=is_normal_obj)
        check_equal(modified_error, [])

    def generate_modified_dict(self, update_obj, is_toggle=True):
        modified_dict = {}
        for k, v in vars(update_obj).items():
            if v is not None:
                if is_toggle is True:
                    k = self.toggle_case(k, is_delete_id=False)
                modified_dict.update({k: v})
        return modified_dict

    def assert_pw_query_having_modified(self, origin_pw_query, pw_query, modified_dict=None, ex=None):
        try:
            for index, pw_obj in enumerate(pw_query):
                self.assert_two_pw_obj_having_modified(origin_pw_query[index],
                                                       pw_obj,
                                                       modified_dict,
                                                       ex)
        except TypeError as e:
            self.assert_two_pw_obj_having_modified(origin_pw_query,
                                                   pw_query,
                                                   modified_dict,
                                                   ex)

    def is_obj_equal(self, act_obj, exp_obj, need_to_compare=list()):
        self.error_list = list()

        class Temp(object):
            pass

        new_act = Temp()
        for k in dir(act_obj):
            v = getattr(act_obj, k)
            if str(k).startswith("_") is False:
                setattr(new_act, k, v)

        self.for_obj(act_obj=new_act, exp_obj=exp_obj, need_to_compare=need_to_compare, is_toggle=False)
        if len(self.error_list) > 0:
            log.info("对象对比不通过，现在打印对比不通过内容")
            log.info(self.error_list)
            return False
        else:
            log.info("对比通过")
            return True


obj_util = ObjAssert()
