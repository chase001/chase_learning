""" 1. 补充下面方法的实现  （该题需要自己查资料完成）
def now(days=0, minutes=0, seconds=0, format="%Y-%m-%d %H:%M:%S"):

   根据传参以当前时间为基准计算前后时间
   例如 今天是2019-11-2 00:00:00
    delay_time = now(days=1, format="%Y-%m-%d")  此时得到2019-11-3
   :return:
"""

# 1. 补充下面方法的实现  （该题需要自己查资料完成）
def now(days=0, minutes=0, seconds=0, format="%Y-%m-%d %H:%M:%S"):
   """
   根据传参以当前时间为基准计算前后时间
   例如 今天是2019-11-2 00:00:00
    delay_time = now(days=1, format="%Y-%m-%d")  此时得到2019-11-3
   :return:
   """

# def get_attribute(obj, attr, default):
#     """实现.符号取值"""
#     result = getattr(obj, attr, default)
#     return default if result is None else result


def now(days=0, minutes=0, seconds=0, format="%Y-%m-%d %H:%M:%S"):
    """
      根据传参以当前时间为基准计算前后时间
      例如 今天是2019-11-2 00:00:00
       delay_time = now(days=1, format="%Y-%m-%d")  此时得到2019-11-3
      :return:
    """
    import datetime
    time_result = (datetime.datetime.now()+datetime.timedelta(days=days,
                                                              minutes=minutes,
                                                              seconds=seconds)).strftime(format)
    return time_result

    now = datetime.now()
    delay_time = now + timedelta(days, minutes, seconds)
    print(delay_time())


#
# list_1 = [1, 34, 45]
# list_new = [i for i in list_1 if i is not None]
# print(list_new)
#
# bool(0)  # False
#
#
# dict_a = {'a': 1, 'b': 2, 'c': 3, 'd': 'test1', 'e': [1, 2, 3, 4, 5], "f": None, 'g': None}
# dict_new = {key: value for key, value in dict_a.items() if value is not None}
# print(dict_new)
#
#
# a = (1, 3, 5, 7, None)
# ff = filter(lambda x: x is not None, a)
# print(list(ff))


