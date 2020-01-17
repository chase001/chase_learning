
# def bubbleSort(arr):
#     n = len(arr)
#
#     # 遍历所有数组元素
#     for i in range(n):
#
#         # Last i elements are already in place
#         for j in range(0, n - i - 1):
#
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#
# arr = [64, 34, -20,25, 12, 22, 90,11]
#
# bubbleSort(arr)
#
# print("排序后的数组:")
# for i in range(len(arr)):
#     print("%d" % arr[i])




# # 入门，这是装饰器函数，参数 func 是被装饰的函数
# def logger(func):
#     def wrapper(*args, **kw):
#         print('主人，我准备开始执行：{} 函数了:'.format(func.__name__))
#
#         # 真正执行的是这行。
#         func(*args, **kw)
#
#         print('主人，我执行完啦。')
#     return wrapper
#
# @logger
# def add(x, y):
#     print('{} + {} = {}'.format(x, y, x+y))
#
#
# add(12142,1245151)



#
# #带参数的函数装饰器
# def say_hello(contry):
#     def wrappe(func):
#         def deco(*args,**kwargs):
#             if contry =="china":
#                 print("您好，北京.")
#             if contry == "english":
#                 print("hello paris.")
#             else:
#                 return print('hello world.')
#             #真正执行函数的地方
#             func(*args,**kwargs)
#
#         return deco
#     return wrappe
#
# # 小明，中国人
# @say_hello("china")
# def xiaoming():
#     pass
#
# # jack，美国人
# @say_hello("america")
# def jack():
#     pass
#
# xiaoming()



# #不带参数的类装饰器
# class logger(object):
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print("[INFO]: the function {func}() is running..."
#             .format(func=self.func.__name__))
#         return self.func(*args, **kwargs)
#
# @logger
# def say(something):
#     print("say {}!".format(something))
#
# say("hello")

#当前时间
import datetime


def now(days= 0, minutes = 0, seconds = 0, format = "%Y-%m-%d %H:%M:%S"):
  """
  根据传参以当前时间为基准计算前后时间
  例如 今天是2019-11-2 00:00:00
   delay_time = now(days=1, format="%Y-%m-%d")  此时得到2019-11-3
  :return:
  """
  time_result = (datetime.datetime.now()+datetime.timedelta(days=days,minutes=minutes,seconds=seconds)).strftime(format)
  return time_result


#高阶：带参数的类装饰器
class logger(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("[INFO]{now}: the function {func}() is running..."
            .format(now=now(),func=self.func.__name__))
        return self.func(*args, **kwargs)


# @logger
# def paomao(list):
#     ll = len(list)
#     for i in  range(0,ll):
#         for m in  range(0,ll-i-1):
#             if list[m] > list[m+1]:
#                 list[m],list[m+1] = list[m+1],list[m]
#     return list
#
# a=paomao(list=[1026,99,-22,37,66,102,896,-300])
# print(a)