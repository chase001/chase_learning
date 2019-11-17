from peewee import *

database = MySQLDatabase('hj_cbz_orders', **{'charset': 'utf8', 'use_unicode': True, 'host': '192.168.36.101', 'port': 3306, 'user': 'user_hjcbz', 'password': '1hn2bvXuBrRDqhxt'})


class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class AreaCode(BaseModel):
    code = BigAutoField()
    level = IntegerField(null=True)
    name = CharField(null=True)
    parent_code = BigIntegerField(index=True, null=True)

    class Meta:
        table_name = 'area_code'

class BatchOrderCustomer(BaseModel):
    company_id = IntegerField(constraints=[SQL("DEFAULT 100")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    hj_user_id = BigIntegerField(null=True)
    id = BigAutoField()
    order_id = BigIntegerField(null=True)
    receive_address = CharField(null=True)
    receive_name = CharField(null=True)
    receive_phone = CharField(null=True)
    reference_order_id = BigIntegerField(null=True)
    rerification_status = IntegerField(null=True)
    ship_to_city = CharField(null=True)
    ship_to_country = CharField(null=True)
    ship_to_province = CharField(null=True)
    ship_to_town = CharField(null=True)
    task_id = BigIntegerField(index=True, null=True)
    user_name = CharField(null=True)

    class Meta:
        table_name = 'batch_order_customer'

class BatchOrderProduct(BaseModel):
    business_product_id = BigIntegerField(null=True)
    combin_discount_amount = DecimalField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    is_master_product = UnknownField(null=True)  # bit
    manual_discount = DecimalField(null=True)
    master_product_id = BigIntegerField(null=True)
    product_id = BigIntegerField(null=True)
    product_name = CharField(null=True)
    product_type = IntegerField(null=True)
    promotion_discount_amount = DecimalField(null=True)
    quantity = IntegerField(null=True)
    shipping_fee = DecimalField(null=True)
    task_id = BigIntegerField(null=True)
    unit_price = DecimalField(null=True)

    class Meta:
        table_name = 'batch_order_product'

class BatchOrderTask(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    end_date = DateTimeField(null=True)
    operator = CharField(null=True)
    operator_user_id = BigIntegerField(null=True)
    order_department_id = IntegerField(null=True)
    order_memo = CharField(null=True)
    order_project_code = CharField(null=True)
    order_reason_id = IntegerField(null=True)
    start_date = DateTimeField(null=True)
    status = IntegerField(null=True)
    task_id = BigAutoField()
    task_name = CharField(null=True)

    class Meta:
        table_name = 'batch_order_task'

class BiBusiness(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigAutoField()

    class Meta:
        table_name = 'bi_business'

class BiCouponType(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigAutoField()

    class Meta:
        table_name = 'bi_coupon_type'

class BiDeviceType(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigAutoField()

    class Meta:
        table_name = 'bi_device_type'

class BiOrderReason(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigAutoField()

    class Meta:
        table_name = 'bi_order_reason'

class BiOrderSalesChannel(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigAutoField()

    class Meta:
        table_name = 'bi_order_sales_channel'

class BiOrderSource(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigAutoField()

    class Meta:
        table_name = 'bi_order_source'

class BiOrderType(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigAutoField()

    class Meta:
        table_name = 'bi_order_type'

class BiPayMethod(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigAutoField()
    is_active = UnknownField(constraints=[SQL("DEFAULT b'1'")])  # bit
    pay_method_foe = CharField(null=True)

    class Meta:
        table_name = 'bi_pay_method'

class BiPlatformType(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigAutoField()

    class Meta:
        table_name = 'bi_platform_type'

class BiProductStatus(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigAutoField()

    class Meta:
        table_name = 'bi_product_status'

class BiProductType(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigAutoField()

    class Meta:
        table_name = 'bi_product_type'

class BiSourceType(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigAutoField()

    class Meta:
        table_name = 'bi_source_type'

class BiSupplierType(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigAutoField()

    class Meta:
        table_name = 'bi_supplier_type'

class DepartmentCode(BaseModel):
    department_id = BigIntegerField(unique=True)
    department_name = CharField()
    id = BigAutoField()
    is_active = UnknownField(constraints=[SQL("DEFAULT b'1'")])  # bit

    class Meta:
        table_name = 'department_code'

class EsIndexOrderLog(BaseModel):
    create_date = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    custom_data = CharField(null=True)
    from_ = BigIntegerField(column_name='from', null=True)
    id = BigAutoField()
    is_valid = UnknownField(constraints=[SQL("DEFAULT b'1'")], null=True)  # bit
    last_order_date = DateTimeField(null=True)
    last_order_id = BigIntegerField(null=True)
    size = IntegerField(null=True)
    total_records = IntegerField(null=True)

    class Meta:
        table_name = 'es_index_order_log'
        indexes = (
            (('last_order_id', 'from_', 'create_date'), False),
        )

class GroupBuyCategory(BaseModel):
    added_date = DateField(null=True)
    alias = CharField(null=True)
    id = BigAutoField()
    is_valid = UnknownField(null=True)  # bit
    name = CharField(null=True)
    parent_id = BigIntegerField(null=True)
    path = CharField(null=True)

    class Meta:
        table_name = 'group_buy_category'

class GroupBuyCategoryAdmin(BaseModel):
    added_date = DateField(null=True)
    description = CharField(null=True)
    id = BigAutoField()
    is_valid = UnknownField(null=True)  # bit
    name = CharField(null=True)

    class Meta:
        table_name = 'group_buy_category_admin'

class GroupBuyCoupon(BaseModel):
    added_date = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    batch_id = BigIntegerField(index=True)
    batch_size = BigIntegerField(null=True)
    description = CharField(null=True)
    id = BigAutoField()
    is_active = UnknownField(null=True)  # bit
    mail_format = CharField(null=True)
    title = CharField(null=True)

    class Meta:
        table_name = 'group_buy_coupon'

class GroupBuyCouponDetail(BaseModel):
    added_date = DateTimeField(null=True)
    batch_id = BigIntegerField(null=True)
    batch_type = IntegerField(null=True)
    coupon_code = CharField(null=True)
    expired_date = DateField(null=True)
    extended = CharField(null=True)
    group_buy_id = BigIntegerField(null=True)
    id = BigAutoField()
    is_active = UnknownField(null=True)  # bit
    send_date = DateTimeField(null=True)
    user_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'group_buy_coupon_detail'

class GroupBuyGlobalSettings(BaseModel):
    display_a4_list_page = UnknownField(null=True)  # bit

    class Meta:
        table_name = 'group_buy_global_settings'
        primary_key = False

class GroupBuyLuckOrders(BaseModel):
    email = CharField(null=True)
    group_buy_id = BigIntegerField(null=True)
    invitor_user_id = BigIntegerField(null=True)
    join_date = DateTimeField(null=True)
    join_reason = CharField(null=True)
    lucky_number = BigIntegerField(null=True)
    user_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'group_buy_luck_orders'
        primary_key = False

class GroupBuyProduct(BaseModel):
    _360_cate = CharField(column_name='360_cate', null=True)
    _360_display = UnknownField(column_name='360_display', null=True)  # bit
    _360_hot_bus_spot_name = CharField(column_name='360_hot_bus_spot_name', null=True)
    _360_img = CharField(column_name='360_img', null=True)
    _360_latitude = CharField(column_name='360_latitude', null=True)
    _360_longitude = CharField(column_name='360_longitude', null=True)
    _360_merchant_addr = CharField(column_name='360_merchant_addr', null=True)
    _360_merchant_name = CharField(column_name='360_merchant_name', null=True)
    _360_merchant_phone = CharField(column_name='360_merchant_phone', null=True)
    _360_spent_end_time = DateTimeField(column_name='360_spent_end_time', null=True)
    _360_spent_start_time = DateTimeField(column_name='360_spent_start_time', null=True)
    _360_title = CharField(column_name='360_title', null=True)
    admin_memo = TextField(null=True)
    big_img_name = CharField(null=True)
    bulo_display_img_url = CharField(null=True)
    buy_only_once = UnknownField(null=True)  # bit
    cate_id = BigIntegerField(null=True)
    cate_id_admin = BigIntegerField(null=True)
    class_id = BigIntegerField(null=True)
    ct_product_code = CharField(null=True)
    display_by_bulo = UnknownField(null=True)  # bit
    end_time = DateTimeField(null=True)
    free_buy_type = BigIntegerField(null=True)
    full_num = BigIntegerField(null=True)
    group_buy_price = DecimalField(null=True)
    group_buy_type = BigIntegerField(null=True)
    has_notice_by_mail = UnknownField(null=True)  # bit
    has_notice_by_sms = UnknownField(null=True)  # bit
    id = BigAutoField()
    is_active = UnknownField(null=True)  # bit
    is_free_by_count = UnknownField(null=True)  # bit
    is_free_delivery = UnknownField(null=True)  # bit
    is_hide = UnknownField(null=True)  # bit
    is_new_version = UnknownField(null=True)  # bit
    is_take_by_customer = UnknownField(null=True)  # bit
    is_valid = UnknownField(null=True)  # bit
    is_view = UnknownField(null=True)  # bit
    key_words = CharField(null=True)
    last_notice_time_mail = DateTimeField(null=True)
    last_notice_time_sms = DateTimeField(null=True)
    last_update_time = DateTimeField(null=True)
    list_price = DecimalField(null=True)
    low_cate_id = BigIntegerField(null=True)
    mark = BigIntegerField(null=True)
    max_buy_amount = BigIntegerField(null=True)
    mention = TextField(null=True)
    mini_product_name = CharField(null=True)
    prevision_img_name = CharField(null=True)
    product_desc = TextField(null=True)
    product_id = BigIntegerField(null=True)
    product_name = CharField(null=True)
    quantity = BigIntegerField(null=True)
    related_coupon_batch = BigIntegerField(null=True)
    related_coupon_batch_type = IntegerField(null=True)
    related_income = DecimalField(null=True)
    related_staff = CharField(null=True)
    room_id = BigIntegerField(null=True)
    short_product_name = CharField(null=True)
    small_img_name = CharField(null=True)
    sort_index = BigIntegerField(null=True)
    start_time = DateTimeField(null=True)
    supplier_id = BigIntegerField(null=True)
    supplier_type = BigIntegerField(null=True)
    system_remark = TextField(null=True)
    tags = CharField(null=True)
    time_up_warning = UnknownField(null=True)  # bit
    total_buy_amount = BigIntegerField(null=True)
    touch_product_desc = TextField(null=True)
    unit_cost = DecimalField(null=True)
    unit_delivery_cost = DecimalField(null=True)
    user_ce_hua = CharField(null=True)
    user_ce_hua_id = BigIntegerField(null=True)
    user_comment = TextField(null=True)
    user_design_id = BigIntegerField(null=True)
    user_tui_guang = CharField(null=True)
    user_tui_guang_id = BigIntegerField(null=True)
    user_wen_an = CharField(null=True)
    user_wen_an_id = BigIntegerField(null=True)
    virtual_buyer_amount = BigIntegerField(null=True)

    class Meta:
        table_name = 'group_buy_product'

class GroupBuyProductDetail(BaseModel):
    class_unit_cost = DecimalField(null=True)
    group_buy_id = BigIntegerField(null=True)
    id = BigAutoField()
    is_active = UnknownField(null=True)  # bit
    product_id = BigIntegerField(null=True)
    quantity = BigIntegerField(null=True)
    unit_cost = DecimalField(null=True)

    class Meta:
        table_name = 'group_buy_product_detail'

class GroupBuyProductWarehouse(BaseModel):
    group_buy_product_id = BigIntegerField(null=True)
    id = BigAutoField()
    warehouse_id = CharField(null=True)
    warehouse_product_id = CharField(null=True)

    class Meta:
        table_name = 'group_buy_product_warehouse'

class InvoiceManage(BaseModel):
    account_bank = CharField(null=True)
    account_number = CharField(null=True)
    apply_user_name = CharField(null=True)
    company_address = CharField(null=True)
    company_id = IntegerField(null=True)
    company_name = CharField(null=True)
    company_phone = CharField(null=True)
    courier_number = BigIntegerField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    create_user_id = BigIntegerField(null=True)
    express_name = CharField(null=True)
    express_pay_method = IntegerField(null=True)
    ext_param = CharField(null=True)
    id = BigAutoField()
    ident_number = CharField(null=True)
    invoice_content = IntegerField(null=True)
    invoice_fee = DecimalField(null=True)
    invoice_header = CharField(null=True)
    invoice_header_type = IntegerField(null=True)
    invoice_status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    invoice_type = IntegerField(null=True)
    is_print = UnknownField(constraints=[SQL("DEFAULT b'0'")], null=True)  # bit
    is_send = UnknownField(null=True)  # bit
    order_id = BigIntegerField(null=True)
    recipient = CharField(null=True)
    recipient_address = CharField(null=True)
    recipient_city = CharField(null=True)
    recipient_phone = CharField(null=True)
    recipient_province = CharField(null=True)
    recipient_town = CharField(null=True)
    remark = CharField(null=True)
    update_time = DateTimeField(null=True)
    update_user_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'invoice_manage'

class JdHjOrders(BaseModel):
    create_date = DateTimeField(null=True)
    customer_address = CharField(null=True)
    customer_phone = CharField(null=True)
    hj_deal_fee = DecimalField(null=True)
    hj_order_date = DateTimeField(null=True)
    hj_order_id = BigIntegerField(null=True)
    id = BigAutoField()
    is_processed = UnknownField(null=True)  # bit
    is_same = UnknownField(null=True)  # bit
    jd_order_date = DateTimeField(null=True)
    jd_order_id = CharField(unique=True)
    jd_seller_price = DecimalField(null=True)
    memo = CharField(null=True)

    class Meta:
        table_name = 'jd_hj_orders'

class OrderArchiveDetailLog(BaseModel):
    archive_batch_code = CharField(index=True)
    archive_time = DateTimeField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    delete_time = DateTimeField(null=True)
    id = BigAutoField()
    is_archive = UnknownField(null=True)  # bit
    is_delete = UnknownField(null=True)  # bit
    is_to_es = UnknownField(null=True)  # bit
    order_id = BigIntegerField(index=True)
    to_es_time = DateTimeField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'order_archive_detail_log'

class OrderArchiveMasterLog(BaseModel):
    archive_batch_code = CharField(index=True)
    archive_order_quantity = BigIntegerField(null=True)
    archive_status = UnknownField(null=True)  # bit
    begin_order_id = BigIntegerField(index=True, null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    delete_status = UnknownField(null=True)  # bit
    end_order_id = BigIntegerField(null=True)
    id = BigAutoField()
    to_es_status = UnknownField(null=True)  # bit
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'order_archive_master_log'

class OrderAssessment(BaseModel):
    business_product_id = BigIntegerField(null=True)
    deposit_discount_amount = DecimalField(null=True)
    id = BigAutoField()
    manual_discount_amount = DecimalField(null=True)
    multi_product_id = BigIntegerField(null=True)
    new_product_id = BigIntegerField(null=True)
    order_id = BigIntegerField(index=True, null=True)
    product_id = BigIntegerField(null=True)
    quantity = IntegerField(null=True)
    share_card_fee = DecimalField(null=True)
    share_card_income = DecimalField(null=True)
    share_combine_fee = DecimalField(null=True)
    share_cost = DecimalField(null=True)
    share_coupon_fee = DecimalField(null=True)
    share_coupon_income = DecimalField(null=True)
    share_course_code_fee = DecimalField(null=True)
    share_course_code_income = DecimalField(null=True)
    share_discount_fee = DecimalField(null=True)
    share_handling_fee = DecimalField(null=True)
    share_income = DecimalField(null=True)
    share_preincome = DecimalField(null=True)
    share_purchase_xb = DecimalField(null=True)
    share_recharge_xb = DecimalField(null=True)
    share_reward_xb = DecimalField(null=True)
    share_shipping_fee = DecimalField(null=True)
    share_user_handling_fee = DecimalField(null=True)
    share_vipcard_fee = DecimalField(null=True)
    share_vipcard_income = DecimalField(null=True)
    unit_price = DecimalField(null=True)

    class Meta:
        table_name = 'order_assessment'
        indexes = (
            (('order_id', 'product_id', 'multi_product_id'), False),
        )

class OrderBaseUser(BaseModel):
    address = CharField(null=True)
    answer = CharField(null=True)
    bbs_user_id = BigIntegerField(index=True, null=True)
    buy_times = IntegerField(null=True)
    cellphone = CharField(null=True)
    charge = DecimalField(null=True)
    display_pwd = CharField(null=True)
    email = CharField(null=True)
    expired_date = DateTimeField(null=True)
    fee_mark = IntegerField(null=True)
    froze_late_fee = DecimalField(null=True)
    gender = IntegerField(null=True)
    gold = IntegerField(null=True)
    has_validate_cellphone = UnknownField(null=True)  # bit
    icon_name = CharField(null=True)
    id_card_num = CharField(null=True)
    last_login_ip = CharField(null=True)
    last_login_time = DateTimeField(null=True)
    late_fee = DecimalField(null=True)
    lock_flag = IntegerField(null=True)
    login_times = IntegerField(null=True)
    phone = CharField(null=True)
    question = CharField(null=True)
    rank = IntegerField(null=True)
    rank_mark = IntegerField(null=True)
    reg_date = DateTimeField(null=True)
    reg_ip = CharField(null=True)
    sina_weibo_account = BigIntegerField(null=True)
    timestamp = DateTimeField(null=True)
    true_name = CharField(null=True)
    user_custom_cata_list = CharField(null=True)
    user_fav_cata_list = CharField(null=True)
    user_id = BigAutoField()
    user_name = CharField(null=True)
    user_pwd = CharField(null=True)
    user_top_custom_cata_list = CharField(null=True)
    veri_code = CharField(null=True)
    vip_level = IntegerField(null=True)
    vip_total_days = IntegerField(null=True)
    zipcode = CharField(null=True)

    class Meta:
        table_name = 'order_base_user'

class OrderBusinessExtend(BaseModel):
    business_org_code = CharField(null=True)
    company_id = IntegerField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    key = CharField(null=True)
    order_id = BigIntegerField(index=True, null=True)
    values = CharField(null=True)

    class Meta:
        table_name = 'order_business_extend'
        indexes = (
            (('key', 'order_id', 'business_org_code'), False),
            (('key', 'values'), False),
        )

class OrderCancelLog(BaseModel):
    cancel_type = IntegerField(null=True)
    create_date = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    ip = CharField(null=True)
    operator_user_id = BigIntegerField(null=True)
    operator_user_name = CharField(null=True)
    order_id = BigIntegerField(null=True)
    remark = CharField(null=True)
    source_id = IntegerField(null=True)
    status = IntegerField(null=True)

    class Meta:
        table_name = 'order_cancel_log'

class OrderCarriedForward(BaseModel):
    company_id = IntegerField(index=True, null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    create_user_id = BigIntegerField(null=True)
    id = BigAutoField()
    income = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    order_id = BigIntegerField(index=True, null=True)
    preincome = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    purchase_xb = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    recharge_xb = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    reward_xb = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    xb_fee = DecimalField(constraints=[SQL("DEFAULT 0.0000")])

    class Meta:
        table_name = 'order_carried_forward'

class OrderCarriedForwardMulti(BaseModel):
    business_id = IntegerField(null=True)
    category_id = IntegerField(null=True)
    company_id = IntegerField(index=True, null=True)
    id = BigAutoField()
    income = DecimalField()
    multi_product_id = BigIntegerField(null=True)
    order_id = BigIntegerField(index=True)
    preincome = DecimalField()
    product_id = BigIntegerField()
    product_type = IntegerField(null=True)
    purchase_xb = DecimalField()
    quantity = IntegerField()
    recharge_xb = DecimalField()
    reward_xb = DecimalField()
    seller_id = BigIntegerField(null=True)
    unit_price = DecimalField()
    xb_fee = DecimalField()

    class Meta:
        table_name = 'order_carried_forward_multi'
        indexes = (
            (('business_id', 'company_id', 'seller_id'), False),
            (('multi_product_id', 'product_id'), False),
        )

class OrderChangeLog(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    create_user_company_id = IntegerField(null=True)
    create_user_id = BigIntegerField(null=True)
    create_user_name = CharField(null=True)
    id = BigAutoField()
    old_ship_to_name = CharField(null=True)
    old_ship_to_zip = CharField(null=True)
    order_id = BigIntegerField(null=True)
    ship_to_name = CharField(null=True)
    ship_to_zip = CharField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    update_user_company_id = IntegerField(null=True)
    update_user_id = BigIntegerField(null=True)
    update_user_name = CharField(null=True)
    user_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'order_change_log'

class OrderConfig(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    create_user_id = BigIntegerField(null=True)
    create_user_name = CharField(null=True)
    id = BigAutoField()
    is_active = UnknownField(null=True)  # bit
    is_delete = UnknownField(null=True)  # bit
    key = CharField(index=True)
    remark = CharField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    update_user_id = BigIntegerField(null=True)
    update_user_name = CharField(null=True)
    value = CharField(null=True)

    class Meta:
        table_name = 'order_config'

class OrderCouponConsum(BaseModel):
    company_id = IntegerField(null=True)
    cost = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    coupon_code = CharField(index=True, null=True)
    coupon_discount = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    coupon_fee = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    coupon_income = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    coupon_name = CharField(null=True)
    coupon_type = IntegerField(null=True)
    id = BigAutoField()
    order_id = BigIntegerField(index=True)

    class Meta:
        table_name = 'order_coupon_consum'

class OrderDealMemo(BaseModel):
    deal_date = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    deal_memo = CharField(null=True)
    deal_user = CharField(null=True)
    deal_user_company_id = IntegerField(null=True)
    id = BigAutoField()
    order_id = BigIntegerField(index=True)

    class Meta:
        table_name = 'order_deal_memo'
        indexes = (
            (('order_id', 'deal_user'), False),
        )

class OrderDeliver(BaseModel):
    batch_id = IntegerField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    delivery_failed_qty = IntegerField(null=True)
    delivery_qty = IntegerField(null=True)
    delivery_status = IntegerField(null=True)
    id = BigAutoField()
    master_product_id = BigIntegerField(null=True)
    order_id = BigIntegerField()
    product_id = BigIntegerField()
    product_type = IntegerField(null=True)
    quantity = IntegerField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'order_deliver'
        indexes = (
            (('order_id', 'product_id'), False),
        )

class OrderDetail(BaseModel):
    account_date = DateTimeField(null=True)
    batch_id = IntegerField(null=True)
    business_id = IntegerField(null=True)
    business_product_id = BigIntegerField(index=True, null=True)
    category_id = IntegerField(null=True)
    combine_discount_amount = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    company_id = IntegerField(null=True)
    coupon_code = CharField(null=True)
    deposit_discount_amount = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    discount_amount = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    id = BigAutoField()
    is_master_product = UnknownField()  # bit
    is_refunded = UnknownField(null=True)  # bit
    manual_discount_amount = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    nsource = CharField(null=True)
    order_id = BigIntegerField(null=True)
    point_discount = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    product_cate = IntegerField(null=True)
    product_cost = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    product_id = BigIntegerField()
    product_name = CharField(null=True)
    product_type = IntegerField(null=True)
    promotion_info = CharField(null=True)
    quantity = IntegerField()
    seller_id = BigIntegerField(null=True)
    timestamp = DateTimeField(null=True)
    unit_price = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    warehouse_id = IntegerField(null=True)

    class Meta:
        table_name = 'order_detail'
        indexes = (
            (('order_id', 'product_id'), False),
            (('order_id', 'product_type'), False),
            (('order_id', 'quantity'), False),
        )

class OrderDetailAttached(BaseModel):
    company_id = IntegerField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    create_user_company_id = IntegerField(null=True)
    create_user_id = BigIntegerField(null=True)
    id = BigAutoField()
    master_product_id = BigIntegerField(index=True)
    order_id = BigIntegerField(index=True)
    product_id = BigIntegerField(index=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    update_user_company_id = IntegerField(null=True)
    update_user_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'order_detail_attached'

class OrderDetailCoupon(BaseModel):
    batch_id = IntegerField(null=True)
    coupon_code = CharField(index=True, null=True)
    coupon_type = IntegerField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    is_verificationed = UnknownField(null=True)  # bit
    multi_product_id = BigIntegerField(null=True)
    order_id = BigIntegerField()
    product_id = BigIntegerField(null=True)
    reference_verify_id = BigIntegerField(index=True, null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    verify_time = DateTimeField(null=True)

    class Meta:
        table_name = 'order_detail_coupon'
        indexes = (
            (('order_id', 'multi_product_id', 'product_id'), False),
        )

class OrderDetailDiscount(BaseModel):
    business_product_id = BigIntegerField(null=True)
    company_id = IntegerField(null=True)
    discount_amount = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    discount_dec = CharField(null=True)
    discount_xb = DecimalField(null=True)
    end_time = DateTimeField(null=True)
    id = BigAutoField()
    order_id = BigIntegerField(index=True, null=True)
    product_business_id = IntegerField(null=True)
    product_id = BigIntegerField(index=True, null=True)
    product_seller_id = BigIntegerField(null=True)
    source_code = CharField(index=True, null=True)
    source_id = BigIntegerField(null=True)
    source_type = IntegerField(null=True)
    start_time = DateTimeField(null=True)

    class Meta:
        table_name = 'order_detail_discount'

class OrderDetailMulti(BaseModel):
    add_to_cart_url = CharField(null=True)
    batch_id = IntegerField(null=True)
    business_id = IntegerField(null=True)
    business_product_id = BigIntegerField(index=True, null=True)
    category_id = IntegerField(null=True)
    combine_discount_amount = DecimalField(null=True)
    company_id = IntegerField(null=True)
    coupon_code = CharField(null=True)
    coupon_type = IntegerField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    deposit_discount_amount = DecimalField(null=True)
    discount_amount = DecimalField(null=True)
    has_subtotal_value = UnknownField(null=True)  # bit
    id = BigAutoField()
    manual_discount_amount = DecimalField(null=True)
    multi_product_id = BigIntegerField(null=True)
    order_id = BigIntegerField(null=True)
    point_discount = DecimalField(null=True)
    product_cost = DecimalField(null=True)
    product_id = BigIntegerField(index=True, null=True)
    product_name = CharField(null=True)
    product_type = IntegerField(null=True)
    quantity = IntegerField(null=True)
    seller_id = BigIntegerField(null=True)
    share_card_fee = DecimalField(null=True)
    share_card_income = DecimalField(null=True)
    share_coupon_fee = DecimalField(null=True)
    share_coupon_income = DecimalField(null=True)
    share_course_code_fee = DecimalField(null=True)
    share_course_code_income = DecimalField(null=True)
    share_discount_fee = DecimalField(null=True)
    share_handling_fee = DecimalField(null=True)
    share_income = DecimalField(null=True)
    share_invite_code_fee = DecimalField(null=True)
    share_preincome = DecimalField(null=True)
    share_purchase_xb = DecimalField(null=True)
    share_recharge_xb = DecimalField(null=True)
    share_reward_xb = DecimalField(null=True)
    share_shipping_fee = DecimalField(null=True)
    share_user_handling_fee = DecimalField(null=True)
    share_vipcard_fee = DecimalField(null=True)
    share_vipcard_income = DecimalField(null=True)
    sid = CharField(null=True)
    ssid = CharField(null=True)
    subtotal_card_fee = DecimalField(null=True)
    subtotal_card_income = DecimalField(null=True)
    subtotal_coupon_fee = DecimalField(null=True)
    subtotal_coupon_income = DecimalField(null=True)
    subtotal_course_code_fee = DecimalField(null=True)
    subtotal_course_code_income = DecimalField(null=True)
    subtotal_discount_amount = DecimalField(null=True)
    subtotal_handling_fee = DecimalField(null=True)
    subtotal_income = DecimalField(null=True)
    subtotal_invite_code_fee = DecimalField(null=True)
    subtotal_pre_income = DecimalField(null=True)
    subtotal_purchase_xb = DecimalField(null=True)
    subtotal_recharge_xb = DecimalField(null=True)
    subtotal_reward_xb = DecimalField(null=True)
    subtotal_shipping_fee = DecimalField(null=True)
    subtotal_user_handling_fee = DecimalField(null=True)
    subtotal_vipcard_fee = DecimalField(null=True)
    subtotal_vipcard_income = DecimalField(null=True)
    uid = CharField(null=True)
    unit_price = DecimalField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    warehouse_id = IntegerField(null=True)

    class Meta:
        table_name = 'order_detail_multi'
        indexes = (
            (('order_id', 'multi_product_id'), False),
            (('order_id', 'product_type'), False),
        )

class OrderFromTop(BaseModel):
    added_date = DateTimeField(null=True)
    ali_trade_no = BigIntegerField(null=True)
    id = BigAutoField()
    import_order = TextField(null=True)
    operator = CharField(null=True)
    order_id = BigIntegerField(null=True)
    platform_id = IntegerField(null=True)
    taobao_token = CharField(null=True)

    class Meta:
        table_name = 'order_from_top'

class OrderHjUser(BaseModel):
    bbs_user_id = BigIntegerField(index=True, null=True)
    company_id = IntegerField(null=True)
    department_id = IntegerField(null=True)
    email = CharField(null=True)
    id = BigAutoField()
    nick_name = CharField(null=True)
    true_name = CharField(null=True)
    user_name = CharField(null=True)

    class Meta:
        table_name = 'order_hj_user'

class OrderIncome(BaseModel):
    batch_id = BigIntegerField(null=True)
    coupon_code = CharField(index=True, null=True)
    income_date = DateTimeField(index=True, null=True)
    income_id = BigAutoField()
    income_type = IntegerField(null=True)
    last_update_date = DateTimeField(null=True)
    master_product_id = BigIntegerField(null=True)
    old_refund_id = BigIntegerField(null=True)
    operater_type = IntegerField(null=True)
    order_type = IntegerField(null=True)
    product_name = CharField(null=True)
    product_type = IntegerField(null=True)
    quantity = IntegerField(null=True)
    reference_income_id = BigIntegerField(null=True)
    share_income_fee = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    share_purchase_xb = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    share_recharege_xb = DecimalField()
    share_reward_xb = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    source_order_id = BigIntegerField(null=True)
    source_rma_id = BigIntegerField(index=True, null=True)
    status = IntegerField(null=True)
    sub_product_id = BigIntegerField(null=True)
    user_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'order_income'
        indexes = (
            (('source_order_id', 'sub_product_id'), False),
        )

class OrderIncomeStaging(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    id = BigAutoField()
    rma_id = BigIntegerField(index=True, null=True)
    source_order_id = BigIntegerField(index=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_time = DateTimeField(null=True)

    class Meta:
        table_name = 'order_income_staging'

class OrderMaster(BaseModel):
    ali_trade_no = CharField(null=True)
    bank_code = CharField(null=True)
    bill_date = DateTimeField(null=True)
    bill_no = CharField(null=True)
    cancel_date = DateTimeField(null=True)
    cell_phone = CharField(null=True)
    chest_fee = DecimalField(null=True)
    city_id = IntegerField(null=True)
    combine_fee = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    company_id = IntegerField(null=True)
    coupon_fee = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    coupon_income = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    create_user_company_id = IntegerField(null=True)
    create_user_id = BigIntegerField(null=True)
    deal_fee = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    deal_memo = CharField(null=True)
    deal_user = CharField(null=True)
    deliver_id = CharField(null=True)
    delivery_result = IntegerField(null=True)
    delivery_status = IntegerField(null=True)
    deposit_discount_fee = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    discount_fee = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    email = CharField(index=True, null=True)
    express = IntegerField(null=True)
    express_id = IntegerField(null=True)
    extend_bill_status = IntegerField(null=True)
    fee_memo = CharField(null=True)
    from_ip = CharField(null=True)
    handling_fee = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    hj_user_id = BigIntegerField(index=True, null=True)
    income = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    installment_number = IntegerField(null=True)
    invite_code_fee = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    is_active = UnknownField()  # bit
    is_audit = UnknownField(null=True)  # bit
    is_bill = UnknownField()  # bit
    is_cancel = UnknownField()  # bit
    is_child = UnknownField(constraints=[SQL("DEFAULT b'0'")], null=True)  # bit
    is_inside = UnknownField(null=True)  # bit
    is_notify = UnknownField(null=True)  # bit
    is_phone = UnknownField(null=True)  # bit
    is_print = UnknownField(null=True)  # bit
    is_test = UnknownField(null=True)  # bit
    is_trace = UnknownField(null=True)  # bit
    is_unusual = UnknownField(constraints=[SQL("DEFAULT b'0'")], null=True)  # bit
    is_valid = UnknownField()  # bit
    manual_discount_fee = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    mark = IntegerField(null=True)
    msn = CharField(null=True)
    notify_mark = CharField(null=True)
    nsource = CharField(null=True)
    operator_company_id = IntegerField(null=True)
    operator_user_id = BigIntegerField(null=True)
    order_date = DateTimeField(null=True)
    order_device_id = IntegerField(null=True)
    order_id = BigAutoField()
    order_number = CharField(index=True, null=True)
    order_type = IntegerField()
    outer_trade_no = CharField(index=True, null=True)
    parent_order_id = BigIntegerField(null=True)
    pay_card_type = IntegerField(null=True)
    pay_device_id = IntegerField(null=True)
    pay_method = CharField(null=True)
    payment_bank_discount = DecimalField(null=True)
    phone_date = DateTimeField(null=True)
    platform_id = IntegerField(null=True)
    point_fee = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    pre_income = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    province_id = IntegerField(null=True)
    purchase_xb = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    qq = CharField(null=True)
    recharge_xb = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    refer_source_id = IntegerField(null=True)
    refer_url = CharField(null=True)
    refund_type = CharField(null=True)
    related_order_id = BigIntegerField(index=True, null=True)
    reward_xb = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    seller_id = BigIntegerField(index=True, null=True)
    ship_date = DateTimeField(null=True)
    ship_flag = IntegerField(null=True)
    ship_method = CharField(null=True)
    ship_to_addr = CharField(null=True)
    ship_to_city = CharField(null=True)
    ship_to_country = CharField(constraints=[SQL("DEFAULT '中国'")], null=True)
    ship_to_name = CharField(index=True, null=True)
    ship_to_phone = CharField(index=True, null=True)
    ship_to_province = CharField(null=True)
    ship_to_time = CharField(null=True)
    ship_to_town = CharField(null=True)
    ship_to_zip = CharField(null=True)
    shipping_fee = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    temp_order_version = IntegerField(null=True)
    timestamp = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    total_cost = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    total_fee = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    total_order_today = IntegerField(null=True)
    town_id = IntegerField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    update_user_company_id = IntegerField(null=True)
    update_user_id = BigIntegerField(null=True)
    user_coupon_id = IntegerField(null=True)
    user_handling_fee = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    user_id = BigIntegerField(null=True)
    user_memo = CharField(null=True)
    user_reg_date = DateTimeField(null=True)
    user_source = CharField(null=True)
    user_title = CharField(null=True)
    xb_fee = DecimalField(constraints=[SQL("DEFAULT 0.0000")])

    class Meta:
        table_name = 'order_master'
        indexes = (
            (('bill_date', 'company_id', 'deal_fee', 'order_type', 'is_bill', 'is_cancel'), False),
            (('order_date', 'order_type', 'is_bill', 'ship_flag', 'is_cancel'), False),
            (('platform_id', 'temp_order_version'), False),
        )

class OrderMessageLog(BaseModel):
    id = BigAutoField()
    message_content = TextField(null=True)
    message_id = CharField(null=True)
    produce_id = CharField(null=True)
    send_date_time = DateTimeField(null=True)
    send_machine_ip = CharField(null=True)

    class Meta:
        table_name = 'order_message_log'

class OrderPayInfo(BaseModel):
    bank_code = CharField(null=True)
    begin_time = DateTimeField(null=True)
    bill_amount = DecimalField()
    child_order_id = BigIntegerField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    create_user_id = BigIntegerField(null=True)
    end_time = DateTimeField(null=True)
    ext_param = CharField(null=True)
    id = BigAutoField()
    order_id = BigIntegerField()
    order_type = IntegerField(null=True)
    origin_order_id = BigIntegerField(null=True)
    pay_channel = CharField(null=True)
    pay_device_id = IntegerField(null=True)
    pay_method = IntegerField(null=True)
    pay_num = CharField(null=True)
    pay_status = IntegerField(null=True)
    pay_time = DateTimeField(null=True)
    pay_type = IntegerField(null=True)
    purchase_xb = DecimalField()
    recharge_xb = DecimalField()
    remark = CharField(null=True)
    reward_xb = DecimalField()
    trans_seq_no = CharField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    update_user_id = BigIntegerField(null=True)
    xb_fee = DecimalField()

    class Meta:
        table_name = 'order_pay_info'
        indexes = (
            (('end_time', 'begin_time'), False),
            (('order_id', 'child_order_id'), False),
            (('order_id', 'order_type'), False),
            (('pay_time', 'pay_type'), False),
        )

class OrderProductGroupbuy(BaseModel):
    a_360_cate = CharField()
    a_360_display = UnknownField(constraints=[SQL("DEFAULT b'0'")])  # bit
    a_360_hot_bus_spot_name = CharField()
    a_360_img = CharField()
    a_360_latitude = CharField()
    a_360_longitude = CharField()
    a_360_merchant_addr = CharField()
    a_360_merchant_name = CharField()
    a_360_merchant_phone = CharField()
    a_360_spent_end_time = DateTimeField(null=True)
    a_360_spent_start_time = DateTimeField(null=True)
    a_360_title = CharField()
    admin_memo = CharField()
    big_img_name = CharField()
    bulo_display_img_url = CharField(null=True)
    buy_only_once = UnknownField(constraints=[SQL("DEFAULT b'0'")])  # bit
    cate_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    cate_idadmin = IntegerField(constraints=[SQL("DEFAULT 0")])
    class_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    ctproduct_code = CharField(null=True)
    display_by_bulo = UnknownField(constraints=[SQL("DEFAULT b'0'")])  # bit
    end_time = DateTimeField()
    free_buy_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    full_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    group_buy_price = DecimalField()
    groupbuy_type = IntegerField()
    has_notice_by_mail = UnknownField(constraints=[SQL("DEFAULT b'0'")])  # bit
    has_notice_by_sms = UnknownField(constraints=[SQL("DEFAULT b'0'")])  # bit
    id = BigAutoField()
    is_active = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_free_by_count = UnknownField(constraints=[SQL("DEFAULT b'0'")])  # bit
    is_free_delivery = UnknownField(constraints=[SQL("DEFAULT b'0'")])  # bit
    is_hide = UnknownField()  # bit
    is_new_version = UnknownField(null=True)  # bit
    is_takeby_customer = UnknownField(constraints=[SQL("DEFAULT b'0'")])  # bit
    is_valid = UnknownField(constraints=[SQL("DEFAULT b'1'")])  # bit
    is_view = UnknownField(constraints=[SQL("DEFAULT b'0'")])  # bit
    keywords = CharField(null=True)
    last_notice_time_mail = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    last_notice_time_sms = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    last_update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    list_price = DecimalField()
    low_cate_id = IntegerField(null=True)
    mark = IntegerField()
    max_buy_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    mention = CharField()
    mini_product_name = CharField(null=True)
    prevision_img_name = CharField()
    product_desc = TextField()
    product_id = BigIntegerField(index=True)
    product_name = CharField(null=True)
    quantity = IntegerField()
    related_coupon_batch = IntegerField(constraints=[SQL("DEFAULT 0")])
    related_coupon_batch_type = IntegerField(null=True)
    related_income = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    related_staff = CharField(null=True)
    room_id = IntegerField(null=True)
    short_product_name = CharField(null=True)
    small_img_name = CharField()
    sort_index = IntegerField(constraints=[SQL("DEFAULT 0")])
    start_time = DateTimeField()
    supplier_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    supplier_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    system_remark = TextField(null=True)
    tags = CharField(null=True)
    timeup_warning = UnknownField(constraints=[SQL("DEFAULT b'1'")])  # bit
    total_buy_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    touch_product_desc = TextField(null=True)
    unit_cost = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    unit_delivery_cost = DecimalField(constraints=[SQL("DEFAULT 0.0000")])
    user_ce_hua = CharField()
    user_ce_hua_id = IntegerField(null=True)
    user_comment = TextField()
    user_design_id = IntegerField(null=True)
    user_tui_guang = CharField()
    user_tui_guang_id = IntegerField(null=True)
    user_wen_an = CharField()
    user_wen_an_id = IntegerField(null=True)
    virtual_buyer_amount = IntegerField()

    class Meta:
        table_name = 'order_product_groupbuy'

class OrderSplitIndex(BaseModel):
    begin_order_id = BigIntegerField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    database_index = CharField(null=True)
    end_order_id = BigIntegerField(null=True)
    id = BigAutoField()
    last_order_id = BigIntegerField(null=True)
    table_index = CharField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'order_split_index'
        indexes = (
            (('begin_order_id', 'end_order_id'), False),
        )

class OrderStageRetry(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    order_id = BigIntegerField()
    retry_times = IntegerField(constraints=[SQL("DEFAULT 1")])
    stage = IntegerField()
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_time = DateTimeField(null=True)

    class Meta:
        table_name = 'order_stage_retry'
        indexes = (
            (('order_id', 'stage'), True),
        )
        primary_key = CompositeKey('order_id', 'stage')

class OrderTester(BaseModel):
    company_id = IntegerField(null=True)
    hj_user_id = BigIntegerField(index=True, null=True)
    id = BigAutoField()
    status = UnknownField(null=True)  # bit
    user_id = BigIntegerField(null=True)
    user_name = CharField(null=True)

    class Meta:
        table_name = 'order_tester'

class OrderTracking(BaseModel):
    add_to_cart_url = CharField(null=True)
    app_id = CharField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    device_id = CharField(null=True)
    ext_param = CharField(null=True)
    from_ip = CharField(null=True)
    id = BigAutoField()
    order_department_id = IntegerField(null=True)
    order_device_id = IntegerField(null=True)
    order_id = BigIntegerField()
    order_reason_id = IntegerField(null=True)
    order_source_id = IntegerField(null=True)
    pay_device_id = IntegerField(null=True)
    refer_url = CharField(null=True)
    reference_order_id = BigIntegerField(index=True, null=True)
    rma_flag = IntegerField(null=True)
    sales_channel_id = IntegerField(null=True)
    sales_platform_id = IntegerField(null=True)
    sid = CharField(null=True)
    solution_code = CharField(null=True)
    ssid = CharField(null=True)
    swap_solution_code = CharField(null=True)
    uid = CharField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True, null=True)

    class Meta:
        table_name = 'order_tracking'
        indexes = (
            (('order_id', 'order_source_id', 'solution_code', 'sales_platform_id'), False),
        )

class OrderUserAddressLog(BaseModel):
    address = CharField(null=True)
    change_date = DateTimeField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    create_user_company_id = IntegerField(null=True)
    create_user_id = BigIntegerField(null=True)
    id = BigAutoField()
    old_address = CharField(null=True)
    operator = CharField(null=True)
    order_id = BigIntegerField(null=True)
    shop_user_id = BigIntegerField(null=True)
    user_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'order_user_address_log'

class OrderUserPhoneLog(BaseModel):
    change_date = DateTimeField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    create_user_company_id = IntegerField(null=True)
    create_user_id = BigIntegerField(null=True)
    id = BigAutoField()
    old_phone = CharField(null=True)
    operator = CharField(null=True)
    order_id = BigIntegerField(null=True)
    phone = CharField(null=True)
    shop_user_id = BigIntegerField(null=True)
    type = IntegerField(null=True)
    user_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'order_user_phone_log'

class OrderVirtualDeliver(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    order_deliver_id = BigIntegerField(index=True, null=True)
    order_id = BigIntegerField(index=True, null=True)
    send_code = CharField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'order_virtual_deliver'

class TempOrderMetaData(BaseModel):
    hj_user_id = BigIntegerField(null=True)
    id = BigAutoField()
    product_id = BigIntegerField(null=True)
    user_domain = CharField(null=True)

    class Meta:
        table_name = 'temp_order_meta_data'

class TempOrderSellerCc(BaseModel):
    id = BigAutoField()
    seller_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'temp_order_seller_cc'

class TempOrderUserCc(BaseModel):
    hj_user_id = BigIntegerField(null=True)
    id = BigAutoField()

    class Meta:
        table_name = 'temp_order_user_cc'

class TradeControl(BaseModel):
    compensate_action = CharField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    create_user_id = BigIntegerField(null=True)
    has_cancel = IntegerField(null=True)
    has_commit = IntegerField(null=True)
    has_compensate = IntegerField(index=True, null=True)
    has_freeze = IntegerField(null=True)
    id = BigAutoField()
    order_id = BigIntegerField(index=True, null=True)
    trade_number = CharField(unique=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    update_user_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'trade_control'

class TradeResourceStatus(BaseModel):
    cancel_time = DateTimeField(null=True)
    commit_time = DateTimeField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    create_user_id = BigIntegerField(null=True)
    freeze_time = DateTimeField(null=True)
    has_cancel = IntegerField(null=True)
    has_commit = IntegerField(null=True)
    has_freeze = IntegerField(null=True)
    id = BigAutoField()
    order_id = BigIntegerField(null=True)
    resource_code = CharField(null=True, unique=True)
    resource_type = IntegerField(null=True)
    retry_count = IntegerField(null=True)
    retry_time = DateTimeField(null=True)
    trade_number = CharField(index=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    update_user_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'trade_resource_status'

class UserAddress(BaseModel):
    city_id = IntegerField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    create_user_company_id = IntegerField(null=True)
    create_user_id = BigIntegerField(null=True)
    id = BigAutoField()
    is_default = UnknownField(null=True)  # bit
    msn = CharField(null=True)
    province_id = IntegerField(null=True)
    qq = CharField(null=True)
    ship_to_address = CharField(null=True)
    ship_to_cellphone = CharField(null=True)
    ship_to_email = CharField(null=True)
    ship_to_name = CharField(null=True)
    ship_to_phone = CharField(null=True)
    ship_to_zip = CharField(null=True)
    shop_user_id = BigIntegerField(null=True)
    town_id = IntegerField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    update_user_company_id = IntegerField(null=True)
    update_user_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'user_address'

