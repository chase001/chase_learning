from peewee import *
import datetime, json


class MyBitField(Field):
    """
    自定义的bit类型 ,对应mysql库中的bit类型
    """
    field_type = 'mybit'

    # def db_value(self, value):  # 实际未调用改方法,注释掉
    #     if value is None:
    #         return None
    #     if value == b'\x00':
    #         return False
    #     elif value == b'\x01':
    #         return True
    #     elif value is True:
    #         return 1
    #     elif value is False or value == 0:
    #         return 0
    #     elif value is None:
    #         return None
    #     else:
    #         return True

    def python_value(self, value):  # 替换原来的coerce()方法
        if value is None:
            return None
        if value == b'\x00':
            return False
        elif value == b'\x01':
            return True
        elif value is True:
            return 1
        elif value is False or value == 0:
            return 0
        elif value is None:
            return None
        else:
            return True


#MyBitField = MyBitField()


class MySmallIntegerFields(SmallIntegerField):
    db_field = 'mysmallint'

    def python_value(self, value):
        if value is None or value == 0:
            return False
        elif value == 1:
            return True
        else:
            raise NameError('mysql中字段{0}取出的值不在[None(False),0(False),1(True)]中'.format(self.name))


class MyDateTimeField(DateTimeField):
    db_field = "mydatetime"

    def python_value(self, value):
        if value and isinstance(value, datetime.datetime):
            return self.__format_date_time(value)
        return value

    def __format_date_time(self, value):
        return datetime.datetime.strftime(value, "%Y-%m-%dT%H:%M:%S+0800")


class UnknownField(object):
    def __init__(self, *_, **__): pass


class MyJsonField(Field):
    """
    自定义json field，将db中类型为json的字段转为json格式直接输出
    """
    db_field = 'json'

    def python_value(self, value):
        try:
            return json.loads(str(value))
        except:
            return json.dumps(value)


class MyDateField(Field):
    db_field = 'datetime'

    def python_value(self, value):
        if value and isinstance(value, datetime.datetime):
            return datetime.datetime.strftime(value, "%Y-%m-%d %H:%M:%S")
        return value