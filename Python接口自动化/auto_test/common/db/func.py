from peewee import MySQLDatabase, DoesNotExist
from conf.conf import *
from functools import wraps
import math
from common.func import *


def init_database(section):
    """
    :param path: 配置文件地址
    :param section: section name
    :return: peewee model database
    """
    conf = db_conf()
    db = MySQLDatabase(conf.get(section, 'db'),
                       **{'host': conf.get(section, 'host'),
                          'port': int(conf.get(section, 'port')),
                          'user': conf.get(section, 'user'),
                          'password': conf.get(section, 'pw')
                          }
                         )
    return db


def merge_where(wheres):
    """
    可以处理空where
    :param wheres: [where, where]
    :return:
    """
    new_where = None
    for where in wheres:
        if where is None:
            continue
        elif new_where:
            new_where = new_where & where
        else:
            new_where = where
    return new_where


def pagination(self, page_num_arg="pageNum", page_size_arg="pageSize"):
    """
    peewee对象分页计算(new:对象)
    :param page_num_arg: 接口请求参数中代表当前页数的字段，默认为pageNum
    :param page_size_arg: 接口请求参数中代表每页显示数量的字段，默认为pageSize
    :return:
    """

    def deco_resp(func, back=[]):
        @wraps(func)
        def wrapper(*args, **kwargs):
            query_array = []
            f = func(*args, **kwargs)
            query_total = len(f)  # 分页对象统计查询
            self.pagination_total = query_total
            page_num = getattr(args[1], page_num_arg) if getattr(args[1], page_num_arg) else 1
            page_size = getattr(args[1], page_size_arg) if getattr(args[1], page_size_arg) else 20
            page_query = f.paginate(page_num, page_size)  # 重新进行分页查询
            self.total_page = math.ceil(self.pagination_total / page_size)
            try:
                page_query.get()
                for q in page_query:
                    setattr(q, "total", query_total)  # todo 玉婷在代码里下毒！！！
                    query_array.append(q)
                self.query_result = query_array
                return self
            except DoesNotExist as e:
                self.query_result = back
                return self

        return wrapper

    return deco_resp


def cal_offset_limit(is_next=True, is_pre=False, total_num=20, start=0):
    """
    limit 5 offset 0 从 1 到5 条
    limit 5 offset 5 从 6 到10 条
    :param self:
    :param is_next: 是否向下查询
    :param is_pre: 是否向上查询
    :param total_num: 查询总条数
    :param start: 起点
    :return: [limit, offset]
    """
    if is_next == is_pre:
        assert False, 'is_next和is_pre不能相等'
    limit = int(total_num)
    offset = int(start)
    if is_pre:
        # 向上查询
        offset = 0 if offset < limit else offset - limit
    return limit, offset


def generate_where_single(kwargs, obj):
    where_list = list()
    if is_custom_object(kwargs) is True:
        kwargs = vars(kwargs)
    if len(kwargs) > 0:
        for k, v in dict(kwargs).items():
            # if k not in ["error_list", ""]:
            try:
                obj_v = getattr(obj, k)
                _append_if_valid(where_list, obj_v, v)
            except Exception as e:
                print(e)
                continue
    return where_list


def generate_update_dict_single(kwargs, obj, origin_dict=None):
    origin_dict = origin_dict if origin_dict else {}
    for k, v in dict(kwargs).items():
        _append_if_valid(origin_dict, key=getattr(obj, k), value=v)
    return origin_dict


def _append_if_valid(l, key=None, value=None, expr=None):
    # 内部方法，如value不为空，则往list中加入peewee where条件
    if isinstance(l, list):
        if expr is None:
            l.append(key == value) if value is not None else None
        else:
            l.append(expr) if value is not None else None
    elif isinstance(l, dict):
        l.update({key: value}) if value is not None else None


def strip_pw_attr(pw_obj_list):
    """
    don't use
    清洗pw对象中的pw相关的属性，返回新属性
    :param pw_obj: pw对象
    :return:
    """
    if isinstance(pw_obj_list, list):
        new_obj_list = []
        for pw_obj in pw_obj_list:

            class Temp(object):
                def __init__(self):
                    pass

            new_act = Temp()
            for k, value in pw_obj._meta.fields.items():
                v = getattr(pw_obj, k)
                setattr(new_act, k, v)
            new_obj_list.append(new_act)
        return new_obj_list
    else:
        class Temp(object):
            def __init__(self):
                pass

        new_act = Temp()
        for k, value in pw_obj_list._meta.fields.items():
            v = getattr(pw_obj_list, k)
            setattr(new_act, k, v)
        return new_act


if __name__ == "__main__":
    print(cal_offset_limit(is_next=False, is_pre=True, total_num=20, start=20))
