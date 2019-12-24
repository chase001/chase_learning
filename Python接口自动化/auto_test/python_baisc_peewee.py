"""ORM:
对象关系映射（Object Relational Mapping，简称ORM）
是通过使用描述对象和数据库之间映射的元数据

"""

from peewee import *

db = MySQLDatabase('mall',
                   **{'charset': 'utf8',
                      'use_unicode': True,
                      'host': '144.34.200.237',
                      'port': 3306,
                      'user': 'root',
                      'password': 'root'
                      })


class Person(Model):  # table_name = "person"
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db  # This model uses the "people.db" database.
        # table_name = 'person_a'


class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db  # this model uses the "people.db" database


db.connect()  # 连接数据库
db.create_tables([Person, Pet])  # 创建数据表
print(db.get_tables("mall"))


"""新建数据"""
from datetime import date
uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
uncle_bob.save()  # bob is now stored in the database


grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1))
herb = Person.create(name='Herb', birthday=date(1950, 5, 5))

"""Tip class.create() == class().save()"""

"""更新数据库数据"""
grandma.name = 'Grandma L.'
grandma.save()

"""新建宠物"""
bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

"""修改主人"""
herb_fido.owner = uncle_bob
herb_fido.save()

"""各种查询"""
grandma = Person.select().where(Person.name == 'Grandma L.').get()
# grandma = Person.get(Person.name == 'Grandma L.')  # 更简单的写法
# uncle_bob.pets[0].name == uncle_bob.pets.get().name

for person in Person.select():
    print(person.name)


query = Pet.select().where(Pet.animal_type == 'cat')
for pet in query:
    print(pet.name, pet.owner.name)

"""pet.owner.name 造成的额外查询，如何避免额外查询"""

query = (Pet
         .select(Pet, Person)
         .join(Person)
         .where(Pet.animal_type == 'cat'))

query.get()

for pet in query:
    print(pet.name, pet.owner.name)

"""排序"""
for person in Person.select().paginate().order_by(Person.birthday.desc()):
    print(person.name, person.birthday)

""""""

"""
改变：
1. 目前最终的表达方式较长，例如 Person.name == 'Grandma L.', 希望能直接简单的变成name="Grandma L."
2. 希望添加通用的获取到查询结果的方式
3. 支持分库分表查询以及一些可以调节的自定义功能
4. 希望打印出每次查询的sql语句，方便排查问题
5. 希望返回的结构中是干净的数据对象，方便和期望结果做对比


from order_service.check.OrderPWUtil import db
r = db.sms_coupon(name="测试优惠券")
"""


