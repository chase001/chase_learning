from peewee import *
from common.db.func import init_database
from common.db.MyFields import MyDateTimeField

# database = MySQLDatabase('mall', **{'charset': 'utf8', 'use_unicode': True, 'host': '144.34.200.237', 'port': 3306, 'user': 'root', 'password': 'root'})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = init_database(section='Gwe_db')  # 活库
        # database = database  # 活库


class SmsCoupon(BaseModel):
    amount = DecimalField(null=True)
    code = CharField(null=True)
    count = IntegerField(null=True)
    # enable_time = DateTimeField(null=True)
    enable_time = MyDateTimeField(null=True)
    # end_time = DateTimeField(null=True)
    end_time = MyDateTimeField(null=True)
    id = BigAutoField()
    member_level = IntegerField(null=True)
    min_point = DecimalField(null=True)
    name = CharField(null=True)
    note = CharField(null=True)
    per_limit = IntegerField(null=True)
    platform = IntegerField(null=True)
    publish_count = IntegerField(null=True)
    receive_count = IntegerField(null=True)
    # start_time = DateTimeField(null=True)
    start_time = MyDateTimeField(null=True)
    type = IntegerField(null=True)
    use_count = IntegerField(null=True)
    use_type = IntegerField(null=True)

    class Meta:
        table_name = 'sms_coupon'

class SmsCouponProductCategoryRelation(BaseModel):
    coupon_id = BigIntegerField(null=True)
    id = BigAutoField()
    parent_category_name = CharField(null=True)
    product_category_id = BigIntegerField(null=True)
    product_category_name = CharField(null=True)

    class Meta:
        table_name = 'sms_coupon_product_category_relation'

class SmsCouponProductRelation(BaseModel):
    coupon_id = BigIntegerField(null=True)
    id = BigAutoField()
    product_id = BigIntegerField(null=True)
    product_name = CharField(null=True)
    product_sn = CharField(null=True)

    class Meta:
        table_name = 'sms_coupon_product_relation'

