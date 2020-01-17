from peewee import *
from datetime import date

# 连接数据库
database = MySQLDatabase('test', user='gb_m_user',password='fEtWqVMzBC', host='10.40.6.26', port=3306)

# 定义Person
class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = database

# 创建表
Person.create_table()

# # 已经存在过数据库，则直接通过python -m pwiz批量创建Model
# python -m pwiz -e mysql -u gb_m_user -H 10.40.6.26 --password  test > testModel.py


# 添加一条数据
p = Person(name = 'liuchungui',birthday=date(1990,12,20),is_relative=True)
p.save()

# p.id = 4
# p.delete_instance()

Person.delete().where(Person.name=='liuchungui').execute()

