# -*- coding:utf8 -*-


"""方法"""


def common(name, value):
    print("这是{}".format(name))
    print(value)


def study_data_type_v2():
    common("字符", "欢迎光临1213abc")
    common("列表", [1, "字符串", dict(name='tt', age=123), [1, 3, 4, 5, ], ])
    print("还有其他有序数据类型：元祖、集合等")
    common("字典", {"name": 'yyt', 'age': 12})


"""1. 简单数据结构"""


def study_data_type_v1():
    print("我就是字符串")
    print("下面是列表")
    print([1,
           "字符串",
           dict(name='tt', age=123),
           [1, 3, 4, 5, ],

           ])  # 这里在加一个对象
    print("还有其他有序数据类型：元祖、集合等")
    print("下面是字典")
    print({"name": 'yyt',
           'age': 12}
          )


study_data_type_v1()


"""2. 简单数据类型的操作"""
# region 字符串
str_a = "我喜欢"
str_b = "吃饭"
str_c = "睡觉"
test_1 = "这是一个组合" + "的字符串"  # 字符串拼接 1
test_2 = "_".join([str_a, str_b, str_c])  # 字符串拼接 2
test_3 = test_2.split("-")  # 字符串分割
test_4 = test_2.replace("_", "&&")  # 字符串的替换

str_d = "字符串的判断"
bool_result = bool("判断" in str_d)
str_e = "字符串的遍历"
for i in str_e:
    print(i)
for index, i in enumerate(str_e):
    print("字符串中序号为{}的汉字是{}".format(index, i))
# endregion

# region 列表
list_a = [1, 3, 5, 4]
list_b = ["a", "b", "c"]
list_c = [1, 1, 1, 1]
list_d = ['d']
list_b.extend(list_d)  # 两个列表合并
list_b[-1] = 'e'  # 赋值
list_b.append('f')  # 追加
split_list_1 = list_b[1:2]
split_list_2 = list_b[:2]
split_list_3 = list_b[1:]
# 判断
bool_result = bool("a" in list_b)
# 排序
list_a.sort(reverse=True)  # 从大到小
# 遍历
for i in list_a:
    print(i)
# endregion

# region字典
dict_a = dict(name='中国', age=19)
dict_b = {"name": "中国",
          "age": 19
          }
dict_a['age'] = 20  # 赋值
dict_a.update(sex='女')  # 更新
# 判断
bool_result = bool("name" in dict_b)
keys = dict_a.keys()
# 遍历
for k, v in dict_a.items():
    print("key:{key} value:{value}".format(key=k, value=v))
# endregion


list_e = [i*10 for i in range(0, 5)]  # 推到式

""" 对象 """


class BaseObj:
    class_host = 'http://www.class_dev.com'

    def __init__(self, **kwargs):
        """origin doc"""
        print("调用__init__构造函数")
        self.host = "http://www.dev.com"
        self.db = "test"
        self.update_value(**kwargs)

    def __str__(self):
        """调用print（）方法时候会执行此处"""
        return str(self.__dict__)

    def __repr__(self):
        """我就是str的备胎"""
        return "使用备胎打印" + str(self.__dict__)

    def __enter__(self):
        """使用with语法时候会调用此处"""
        print("我正在连接{}的DB".format(self.db))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """使用with语法时会调用此处"""
        print("我需要关闭掉当前的{}连接".format(self.db))

    def update_value(self, **kwargs):
        if kwargs:
            for attribute_name in kwargs.keys():
                setattr(self, attribute_name, kwargs.get(attribute_name))

    def get_value(self, name, default=None):
        """
        获取对象的属性值
        :param name: 属性名
        :param default: 如果没有返回的默认值
        :return:
        """
        value = getattr(self, name, default)
        if value is None:
            return default
        else:
            return value

    def __getattr__(self, attr):
        """实现.符号取值"""
        try:
            return self.__getattribute__(attr)
        except AttributeError:
            # raise AttributeError(attr)
            return None

    @staticmethod
    def static_func():
        return "静态方法"
    #
    # def clear_value(self):
    #     for k, v in vars(self).items():
    #         setattr(self, k, None)



# region 修改属性-例子: 统一修改接口访问host
print(BaseObj.class_host)
c = BaseObj()
# 修改类属性
BaseObj.class_host = 'http://www.class_test.com'
a = BaseObj()
b = BaseObj()
print(a.class_host)
print(b.class_host)
print(c.class_host)  # 这个地址会变改变吗？

# 修改对象a的属性
a.host = 'http://www.test.com'
print(a.host)
print(b.host)

# 修改对象b的属性
b.host = 'http://www.test.com'
print(a.host)
print(b.host)
# endregion

# region 放开上面对象中各种方法之后的效果你知道吗？
a = BaseObj()
b = BaseObj(url='/test/productInfo', db='dev')  # 调用了update_value方法, 看看对象的属性
print(b)  # 调用了__repr__方法
with BaseObj(file='test.txt', encode='utf-8') as file_obj:
    print(file_obj.file)
# 调用了__enter__ 和 __exit__ 方法
print(b.unknown)  # 如果没有重新定义__getattr__的会报错
print(b.get_value('unknown', '自定义返回的默认数据'))
BaseObj.static_func()
# endregion


# region 继承
class UserInfo(BaseObj):
    def __init__(self, **kwargs):
        self.name = "狗子"
        self.age = 1
        super(UserInfo, self).__init__(**kwargs)

    def set_name(self, name):
        self.name = name


user_info = UserInfo(name="哈斯奇", db="dev")  # 看看里面的属性

user_info.name = "泰迪"

user_info.set_name("吉娃娃")

name = user_info.get_value("name")
default_value = user_info.get_value("dddd", "默认值")

# endregion


# region  python 所有数据类型都是对象包括type()本身
class AttrDict(dict):
    """
    usa这个对象继承了dict的所有方法
    同时有自定义了部分方法，可以实现dict本身没有的功能，比如：

    """

    def __getattr__(self, attr):
        """实现.符号取值"""
        try:
            return self[attr]
        except KeyError:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):
        """实现.符号赋值"""
        self[attr] = value

    def __add__(self, d):
        """实现+计算符"""
        for k, v in d.items():
            if k in self:
                self.score += d.score
                break
        return self


dict_obj = AttrDict(name='二哈', score=18)
print("dict_obj的id:{}".format(id(dict_obj)))
"""dict_a = dict(name='二哈', age=18)"""
print(dict_obj.name)
"""print(dict_a['name'])"""
dict_obj.name = '泰迪'
"""dict_a['name'] = '泰迪'"""
other_dict_obj = AttrDict(name='二哈', score=2)
print("other_dict_obj的id:{}".format(id(other_dict_obj)))
new_dict_obj = dict_obj + other_dict_obj
new_other_dict_obj = other_dict_obj + dict_obj
# endregion


# region装饰器
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        print('args = {}'.format(*args))
        return func(*args, **kwargs)

    return wrapper


@log
def test(p):
    print(test.__name__ + " param: " + p)


test("I'm a param")
# endregion











