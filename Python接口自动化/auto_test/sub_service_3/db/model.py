from common.db.MyFields import *
from common.db.func import init_database
import os


class BaseModel(Model):
    class Meta:
        database = init_database(section='db_hot')  # 活库


class OrderMaster(BaseModel):
    ali_trade_no = CharField(null=True)
    bank_code = CharField(null=True)
    bill_date = MyDateTimeField(null=True)
    bill_no = CharField(null=True)
    cancel_date = MyDateTimeField(null=True)
    cell_phone = CharField(null=True)
    chest_fee = DecimalField(null=True)
    city_id = IntegerField(column_name='city_id', null=True)
    combine_fee = DecimalField()
    company_id = IntegerField(column_name='company_id', null=True)
    coupon_fee = DecimalField()
    coupon_income = DecimalField()
    create_time = MyDateTimeField()
    create_user_company_id = IntegerField(column_name='create_user_company_id', null=True)
    create_user_id = BigIntegerField(column_name='create_user_id', null=True)
    deal_fee = DecimalField()
    deal_memo = CharField(null=True)
    deal_user = CharField(null=True)
    deliver_id = CharField(column_name='deliver_id', null=True)
    delivery_result = IntegerField(null=True)
    delivery_status = IntegerField(null=True)
    deposit_discount_fee = DecimalField()
    discount_fee = DecimalField()
    email = CharField(index=True, null=True)
    express = IntegerField(null=True)
    express_id = IntegerField(null=True)
    extend_bill_status = IntegerField(null=True)
    fee_memo = CharField(null=True)
    from_ip = CharField(null=True)
    handling_fee = DecimalField()
    hj_user_id = BigIntegerField(column_name='hj_user_id', index=True, null=True)
    income = DecimalField()
    installment_number = IntegerField(null=True)
    invite_code_fee = DecimalField()
    is_active = MyBitField(null=True)  # bit
    is_audit = MyBitField(null=True)  # bit
    is_bill = MyBitField(null=True)  # bit
    is_cancel = MyBitField(null=True)  # bit
    is_child = MyBitField(null=True)  # bit
    is_inside = MyBitField(null=True)  # bit
    is_notify = MyBitField(null=True)  # bit
    is_phone = MyBitField(null=True)  # bit
    is_print = MyBitField(null=True)  # bit
    is_test = MyBitField(null=True)  # bit
    is_trace = MyBitField(null=True)  # bit
    is_unusual = MyBitField(null=True)  # bit
    is_valid = MyBitField(null=True)  # bit
    manual_discount_fee = DecimalField()
    mark = IntegerField(null=True)
    msn = CharField(null=True)
    notify_mark = CharField(null=True)
    nsource = CharField(null=True)
    operator_company_id = IntegerField(column_name='operator_company_id', null=True)
    operator_user_id = BigIntegerField(column_name='operator_user_id', null=True)
    order_date = MyDateTimeField(null=True)
    order_device_id = IntegerField(column_name='order_device_id', null=True)
    order_id = BigIntegerField(column_name='order_id', primary_key=True)
    order_number = CharField(null=True)
    order_type = IntegerField()
    outer_trade_no = CharField(null=True)
    parent_order_id = BigIntegerField(column_name='parent_order_id', null=True)
    pay_card_type = IntegerField(null=True)
    pay_device_id = IntegerField(column_name='pay_device_id', null=True)
    pay_method = CharField(null=True)
    payment_bank_discount = DecimalField(null=True)
    phone_date = MyDateTimeField(null=True)
    platform_id = IntegerField(column_name='platform_id', null=True)
    point_fee = DecimalField()
    pre_income = DecimalField()
    province_id = IntegerField(column_name='province_id', null=True)
    purchase_xb = DecimalField()
    qq = CharField(null=True)
    recharge_xb = DecimalField()
    refer_source_id = IntegerField(column_name='refer_source_id', null=True)
    refer_url = CharField(null=True)
    refund_type = CharField(null=True)
    related_order_id = BigIntegerField(column_name='related_order_id', index=True, null=True)
    reward_xb = DecimalField()
    seller_id = BigIntegerField(column_name='seller_id', index=True, null=True)
    ship_date = MyDateTimeField(null=True)
    ship_flag = IntegerField(null=True)
    ship_method = CharField(null=True)
    ship_to_addr = CharField(null=True)
    ship_to_city = CharField(null=True)
    ship_to_country = CharField(null=True)
    ship_to_name = CharField(index=True, null=True)
    ship_to_phone = CharField(index=True, null=True)
    ship_to_province = CharField(null=True)
    ship_to_time = CharField(null=True)
    ship_to_town = CharField(null=True)
    ship_to_zip = CharField(null=True)
    shipping_fee = DecimalField()
    temp_order_version = IntegerField(null=True)
    timestamp = MyDateTimeField()
    total_cost = DecimalField()
    total_fee = DecimalField()
    total_order_today = IntegerField(null=True)
    town_id = IntegerField(column_name='town_id', null=True)
    update_time = MyDateTimeField()
    update_user_company_id = IntegerField(column_name='update_user_company_id', null=True)
    update_user_id = BigIntegerField(column_name='update_user_id', null=True)
    user_coupon_id = IntegerField(column_name='user_coupon_id', null=True)
    user_handling_fee = DecimalField()
    user_id = BigIntegerField(column_name='user_id', null=True)
    user_memo = CharField(null=True)
    user_reg_date = MyDateTimeField(null=True)
    user_source = CharField(null=True)
    user_title = CharField(null=True)
    xb_fee = DecimalField()

    class Meta:
        db_table = 'order_master'
        indexes = (
            (('bill_date', 'company', 'deal_fee', 'order_type', 'is_bill', 'is_cancel'), False),
            (('order_date', 'order_type', 'is_bill', 'ship_flag', 'is_cancel'), False),
            (('platform', 'temp_order_version'), False),
        )


class AreaCode(BaseModel):
    code = BigIntegerField(primary_key=True)
    level = IntegerField(null=True)
    name = CharField(null=True)
    parent_code = BigIntegerField(index=True, null=True)

    class Meta:
        db_table = 'area_code'


class BatchOrderCustomer(BaseModel):
    company = IntegerField(column_name='company_id')
    create_time = MyDateTimeField()
    hj_user = BigIntegerField(column_name='hj_user_id', null=True)
    id = BigIntegerField(primary_key=True)
    order = BigIntegerField(column_name='order_id', null=True)
    receive_address = CharField(null=True)
    receive_name = CharField(null=True)
    receive_phone = CharField(null=True)
    reference_order = BigIntegerField(column_name='reference_order_id', null=True)
    rerification_status = IntegerField(null=True)
    ship_to_city = CharField(null=True)
    ship_to_country = CharField(null=True)
    ship_to_province = CharField(null=True)
    ship_to_town = CharField(null=True)
    task = BigIntegerField(column_name='task_id', index=True, null=True)
    user_name = CharField(null=True)

    class Meta:
        db_table = 'batch_order_customer'


class BatchOrderProduct(BaseModel):
    business_product = BigIntegerField(column_name='business_product_id', null=True)
    combin_discount_amount = DecimalField(null=True)
    create_time = MyDateTimeField()
    id = BigIntegerField(primary_key=True)
    is_master_product = MyBitField(null=True)  # bit
    manual_discount = DecimalField(null=True)
    master_product = BigIntegerField(column_name='master_product_id', null=True)
    product = BigIntegerField(column_name='product_id', null=True)
    product_name = CharField(null=True)
    product_type = IntegerField(null=True)
    promotion_discount_amount = DecimalField(null=True)
    quantity = IntegerField(null=True)
    shipping_fee = DecimalField(null=True)
    task = BigIntegerField(column_name='task_id', null=True)
    unit_price = DecimalField(null=True)

    class Meta:
        db_table = 'batch_order_product'


class BatchOrderTask(BaseModel):
    create_time = MyDateTimeField()
    end_date = MyDateTimeField(null=True)
    operator = CharField(null=True)
    operator_user = BigIntegerField(column_name='operator_user_id', null=True)
    order_memo = CharField(null=True)
    order_reason = IntegerField(column_name='order_reason_id', null=True)
    start_date = MyDateTimeField(null=True)
    status = IntegerField(null=True)
    task = BigIntegerField(column_name='task_id', primary_key=True)
    task_name = CharField(null=True)

    class Meta:
        db_table = 'batch_order_task'


class BiBusiness(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigIntegerField(primary_key=True)

    class Meta:
        db_table = 'bi_business'


class BiCouponType(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigIntegerField(primary_key=True)

    class Meta:
        db_table = 'bi_coupon_type'


class BiDeviceType(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigIntegerField(primary_key=True)

    class Meta:
        db_table = 'bi_device_type'


class BiOrderReason(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigIntegerField(primary_key=True)

    class Meta:
        db_table = 'bi_order_reason'


class BiOrderSource(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigIntegerField(primary_key=True)

    class Meta:
        db_table = 'bi_order_source'


class BiOrderType(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigIntegerField(primary_key=True)

    class Meta:
        db_table = 'bi_order_type'


class BiPayMethod(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigIntegerField(primary_key=True)

    class Meta:
        db_table = 'bi_pay_method'


class BiPlatformType(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigIntegerField(primary_key=True)

    class Meta:
        db_table = 'bi_platform_type'


class BiProductStatus(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigIntegerField(primary_key=True)

    class Meta:
        db_table = 'bi_product_status'


class BiProductType(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigIntegerField(primary_key=True)

    class Meta:
        db_table = 'bi_product_type'


class BiSourceType(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigIntegerField(primary_key=True)

    class Meta:
        db_table = 'bi_source_type'


class BiSupplierType(BaseModel):
    code = CharField(null=True)
    description = CharField(null=True)
    id = BigIntegerField(primary_key=True)

    class Meta:
        db_table = 'bi_supplier_type'


class GroupBuyCategory(BaseModel):
    added_date = DateField(null=True)
    alias = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    is_valid = MyBitField(null=True)  # bit
    name = CharField(null=True)
    parent = BigIntegerField(column_name='parent_id', null=True)
    path = CharField(null=True)

    class Meta:
        db_table = 'group_buy_category'


class GroupBuyCategoryAdmin(BaseModel):
    added_date = DateField(null=True)
    description = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    is_valid = MyBitField(null=True)  # bit
    name = CharField(null=True)

    class Meta:
        db_table = 'group_buy_category_admin'


class GroupBuyCoupon(BaseModel):
    added_date = MyDateTimeField()
    batch = BigIntegerField(column_name='batch_id', index=True)
    batch_size = BigIntegerField(null=True)
    description = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    is_active = MyBitField(null=True)  # bit
    mail_format = CharField(null=True)
    title = CharField(null=True)

    class Meta:
        db_table = 'group_buy_coupon'


class GroupBuyCouponDetail(BaseModel):
    added_date = MyDateTimeField(null=True)
    batch = BigIntegerField(column_name='batch_id', null=True)
    batch_type = IntegerField(null=True)
    coupon_code = CharField(null=True)
    expired_date = DateField(null=True)
    extended = CharField(null=True)
    group_buy = BigIntegerField(column_name='group_buy_id', null=True)
    id = BigIntegerField(primary_key=True)
    is_active = MyBitField(null=True)  # bit
    send_date = MyDateTimeField(null=True)
    user = BigIntegerField(column_name='user_id', null=True)

    class Meta:
        db_table = 'group_buy_coupon_detail'


class GroupBuyGlobalSettings(BaseModel):
    display_a4_list_page = MyBitField(null=True)  # bit

    class Meta:
        db_table = 'group_buy_global_settings'
        primary_key = False


class GroupBuyLuckOrders(BaseModel):
    email = CharField(null=True)
    group_buy = BigIntegerField(column_name='group_buy_id', null=True)
    invitor_user = BigIntegerField(column_name='invitor_user_id', null=True)
    join_date = MyDateTimeField(null=True)
    join_reason = CharField(null=True)
    lucky_number = BigIntegerField(null=True)
    user = BigIntegerField(column_name='user_id', null=True)

    class Meta:
        db_table = 'group_buy_luck_orders'
        primary_key = False


class GroupBuyProduct(BaseModel):
    _360_cate = CharField(column_name='360_cate', null=True)
    _360_display = MyBitField(column_name='360_display', null=True)  # bit
    _360_hot_bus_spot_name = CharField(column_name='360_hot_bus_spot_name', null=True)
    _360_img = CharField(column_name='360_img', null=True)
    _360_latitude = CharField(column_name='360_latitude', null=True)
    _360_longitude = CharField(column_name='360_longitude', null=True)
    _360_merchant_addr = CharField(column_name='360_merchant_addr', null=True)
    _360_merchant_name = CharField(column_name='360_merchant_name', null=True)
    _360_merchant_phone = CharField(column_name='360_merchant_phone', null=True)
    _360_spent_end_time = MyDateTimeField(column_name='360_spent_end_time', null=True)
    _360_spent_start_time = MyDateTimeField(column_name='360_spent_start_time', null=True)
    _360_title = CharField(column_name='360_title', null=True)
    admin_memo = TextField(null=True)
    big_img_name = CharField(null=True)
    bulo_display_img_url = CharField(null=True)
    buy_only_once = MyBitField(null=True)  # bit
    cate = BigIntegerField(column_name='cate_id', null=True)
    cate_id_admin = BigIntegerField(null=True)
    class_ = BigIntegerField(column_name='class_id', null=True)
    ct_product_code = CharField(null=True)
    display_by_bulo = MyBitField(null=True)  # bit
    end_time = MyDateTimeField(null=True)
    free_buy_type = BigIntegerField(null=True)
    full_num = BigIntegerField(null=True)
    group_buy_price = DecimalField(null=True)
    group_buy_type = BigIntegerField(null=True)
    has_notice_by_mail = MyBitField(null=True)  # bit
    has_notice_by_sms = MyBitField(null=True)  # bit
    id = BigIntegerField(primary_key=True)
    is_active = MyBitField(null=True)  # bit
    is_free_by_count = MyBitField(null=True)  # bit
    is_free_delivery = MyBitField(null=True)  # bit
    is_hide = MyBitField(null=True)  # bit
    is_new_version = MyBitField(null=True)  # bit
    is_take_by_customer = MyBitField(null=True)  # bit
    is_valid = MyBitField(null=True)  # bit
    is_view = MyBitField(null=True)  # bit
    key_words = CharField(null=True)
    last_notice_time_mail = MyDateTimeField(null=True)
    last_notice_time_sms = MyDateTimeField(null=True)
    last_update_time = MyDateTimeField(null=True)
    list_price = DecimalField(null=True)
    low_cate = BigIntegerField(column_name='low_cate_id', null=True)
    mark = BigIntegerField(null=True)
    max_buy_amount = BigIntegerField(null=True)
    mention = TextField(null=True)
    mini_product_name = CharField(null=True)
    prevision_img_name = CharField(null=True)
    product_desc = TextField(null=True)
    product = BigIntegerField(column_name='product_id', null=True)
    product_name = CharField(null=True)
    quantity = BigIntegerField(null=True)
    related_coupon_batch = BigIntegerField(null=True)
    related_coupon_batch_type = IntegerField(null=True)
    related_income = DecimalField(null=True)
    related_staff = CharField(null=True)
    room = BigIntegerField(column_name='room_id', null=True)
    short_product_name = CharField(null=True)
    small_img_name = CharField(null=True)
    sort_index = BigIntegerField(null=True)
    start_time = MyDateTimeField(null=True)
    supplier = BigIntegerField(column_name='supplier_id', null=True)
    supplier_type = BigIntegerField(null=True)
    system_remark = TextField(null=True)
    tags = CharField(null=True)
    time_up_warning = MyBitField(null=True)  # bit
    total_buy_amount = BigIntegerField(null=True)
    touch_product_desc = TextField(null=True)
    unit_cost = DecimalField(null=True)
    unit_delivery_cost = DecimalField(null=True)
    user_ce_hua = CharField(null=True)
    user_ce_hua_id = BigIntegerField(null=True)
    user_comment = TextField(null=True)
    user_design = BigIntegerField(column_name='user_design_id', null=True)
    user_tui_guang = CharField(null=True)
    user_tui_guang_id = BigIntegerField(null=True)
    user_wen_an = CharField(null=True)
    user_wen_an_id = BigIntegerField(null=True)
    virtual_buyer_amount = BigIntegerField(null=True)

    class Meta:
        db_table = 'group_buy_product'


class GroupBuyProductDetail(BaseModel):
    class_unit_cost = DecimalField(null=True)
    group_buy = BigIntegerField(column_name='group_buy_id', null=True)
    id = BigIntegerField(primary_key=True)
    is_active = MyBitField(null=True)  # bit
    product = BigIntegerField(column_name='product_id', null=True)
    quantity = BigIntegerField(null=True)
    unit_cost = DecimalField(null=True)

    class Meta:
        db_table = 'group_buy_product_detail'


class GroupBuyProductWarehouse(BaseModel):
    group_buy_product = BigIntegerField(column_name='group_buy_product_id', null=True)
    id = BigIntegerField(primary_key=True)
    warehouse = CharField(column_name='warehouse_id', null=True)
    warehouse_product = CharField(column_name='warehouse_product_id', null=True)

    class Meta:
        db_table = 'group_buy_product_warehouse'


class InvoiceManage(BaseModel):
    account_bank = CharField(null=True)
    account_number = CharField(null=True)
    apply_user_name = CharField(null=True)
    company_address = CharField(null=True)
    company_name = CharField(null=True)
    company_phone = CharField(null=True)
    courier_number = BigIntegerField(null=True)
    create_time = MyDateTimeField(null=True)
    create_user = BigIntegerField(column_name='create_user_id', null=True)
    express_name = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    ident_number = CharField(null=True)
    invoice_content = IntegerField(null=True)
    invoice_fee = DecimalField(null=True)
    invoice_header = CharField(null=True)
    invoice_header_type = IntegerField(null=True)
    invoice_status = IntegerField(null=True)
    invoice_type = IntegerField(null=True)
    is_print = MyBitField(null=True)  # bit
    order = BigIntegerField(column_name='order_id', null=True)
    recipient = CharField(null=True)
    recipient_address = CharField(null=True)
    recipient_city = CharField(null=True)
    recipient_phone = CharField(null=True)
    recipient_province = CharField(null=True)
    recipient_town = CharField(null=True)
    remark = CharField(null=True)
    update_time = MyDateTimeField(null=True)
    update_user = BigIntegerField(column_name='update_user_id', null=True)

    class Meta:
        db_table = 'invoice_manage'


class OrderAssessment(BaseModel):
    business_product = BigIntegerField(column_name='business_product_id', null=True)
    deposit_discount_amount = DecimalField(null=True)
    id = BigIntegerField(primary_key=True)
    manual_discount_amount = DecimalField(null=True)
    multi_product_id = BigIntegerField(column_name='multi_product_id', null=True)
    new_product_id = BigIntegerField(column_name='new_product_id', null=True)
    order_id = BigIntegerField(column_name='order_id', index=True, null=True)
    product_id = BigIntegerField(column_name='product_id', null=True)
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
        db_table = 'order_assessment'
        indexes = (
            (('order', 'product', 'multi_product'), False),
        )


class OrderBaseUser(BaseModel):
    address = CharField(null=True)
    answer = CharField(null=True)
    bbs_user = BigIntegerField(column_name='bbs_user_id', index=True, null=True)
    buy_times = IntegerField(null=True)
    cellphone = CharField(null=True)
    charge = DecimalField(null=True)
    display_pwd = CharField(null=True)
    email = CharField(null=True)
    expired_date = MyDateTimeField(null=True)
    fee_mark = IntegerField(null=True)
    froze_late_fee = DecimalField(null=True)
    gender = IntegerField(null=True)
    gold = IntegerField(null=True)
    has_validate_cellphone = MyBitField(null=True)  # bit
    icon_name = CharField(null=True)
    id_card_num = CharField(null=True)
    last_login_ip = CharField(null=True)
    last_login_time = MyDateTimeField(null=True)
    late_fee = DecimalField(null=True)
    lock_flag = IntegerField(null=True)
    login_times = IntegerField(null=True)
    phone = CharField(null=True)
    question = CharField(null=True)
    rank = IntegerField(null=True)
    rank_mark = IntegerField(null=True)
    reg_date = MyDateTimeField(null=True)
    reg_ip = CharField(null=True)
    sina_weibo_account = BigIntegerField(null=True)
    timestamp = MyDateTimeField(null=True)
    true_name = CharField(null=True)
    user_custom_cata_list = CharField(null=True)
    user_fav_cata_list = CharField(null=True)
    user = BigIntegerField(column_name='user_id', primary_key=True)
    user_name = CharField(null=True)
    user_pwd = CharField(null=True)
    user_top_custom_cata_list = CharField(null=True)
    veri_code = CharField(null=True)
    vip_level = IntegerField(null=True)
    vip_total_days = IntegerField(null=True)
    zipcode = CharField(null=True)

    class Meta:
        db_table = 'order_base_user'


class OrderBiConfig(BaseModel):
    code = CharField(null=True)
    create_time = MyDateTimeField(null=True)
    create_user = BigIntegerField(column_name='create_user_id', null=True)
    id = BigIntegerField(null=True)
    ip = CharField(null=True)
    remarks = CharField(null=True)
    status = IntegerField(null=True)
    type = IntegerField(null=True)
    update_time = MyDateTimeField(null=True)
    update_user = IntegerField(column_name='update_user_id', null=True)

    class Meta:
        db_table = 'order_bi_config'
        indexes = (
            (('id', 'type'), True),
        )
        primary_key = False


class OrderCancelLog(BaseModel):
    cancel_type = IntegerField(null=True)
    create_date = MyDateTimeField()
    id = BigIntegerField(primary_key=True)
    ip = CharField(null=True)
    operator_user = BigIntegerField(column_name='operator_user_id', null=True)
    operator_user_name = CharField(null=True)
    order = BigIntegerField(column_name='order_id', null=True)
    remark = CharField(null=True)
    source = IntegerField(column_name='source_id', null=True)
    status = IntegerField(null=True)

    class Meta:
        db_table = 'order_cancel_log'


class OrderCarriedForward(BaseModel):
    company_id = IntegerField(column_name='company_id', index=True, null=True)
    create_time = MyDateTimeField()
    create_user_id = BigIntegerField(column_name='create_user_id', null=True)
    id = BigIntegerField(primary_key=True)
    income = DecimalField()
    order_id = BigIntegerField(column_name='order_id', index=True, null=True)
    preincome = DecimalField()
    purchase_xb = DecimalField()
    recharge_xb = DecimalField()
    reward_xb = DecimalField()
    xb_fee = DecimalField()

    class Meta:
        db_table = 'order_carried_forward'


class OrderCarriedForwardMulti(BaseModel):
    business_id = IntegerField(column_name='business_id', null=True)
    category_id = IntegerField(column_name='category_id', null=True)
    company_id = IntegerField(column_name='company_id', index=True, null=True)
    id = BigIntegerField(primary_key=True)
    income = DecimalField()
    multi_product_id = BigIntegerField(column_name='multi_product_id', null=True)
    order_id = BigIntegerField(column_name='order_id', index=True)
    preincome = DecimalField()
    product_id = BigIntegerField(column_name='product_id')
    product_type = IntegerField(null=True)
    purchase_xb = DecimalField()
    quantity = IntegerField()
    recharge_xb = DecimalField()
    reward_xb = DecimalField()
    seller_id = BigIntegerField(column_name='seller_id', null=True)
    unit_price = DecimalField()
    xb_fee = DecimalField()

    class Meta:
        db_table = 'order_carried_forward_multi'
        indexes = (
            (('business', 'company', 'seller'), False),
            (('multi_product', 'product'), False),
        )


class OrderChangeLog(BaseModel):
    create_time = MyDateTimeField()
    create_user_company = IntegerField(column_name='create_user_company_id', null=True)
    create_user = BigIntegerField(column_name='create_user_id', null=True)
    create_user_name = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    old_ship_to_name = CharField(null=True)
    old_ship_to_zip = CharField(null=True)
    order = BigIntegerField(column_name='order_id', null=True)
    ship_to_name = CharField(null=True)
    ship_to_zip = CharField(null=True)
    update_time = MyDateTimeField()
    update_user_company = IntegerField(column_name='update_user_company_id', null=True)
    update_user = BigIntegerField(column_name='update_user_id', null=True)
    update_user_name = CharField(null=True)
    user = BigIntegerField(column_name='user_id', null=True)

    class Meta:
        db_table = 'order_change_log'


class OrderConfig(BaseModel):
    create_time = MyDateTimeField()
    create_user = BigIntegerField(column_name='create_user_id', null=True)
    create_user_name = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    is_active = MyBitField(null=True)  # bit
    is_delete = MyBitField(null=True)  # bit
    key = CharField(index=True)
    remark = CharField(null=True)
    update_time = MyDateTimeField()
    update_user = BigIntegerField(column_name='update_user_id', null=True)
    update_user_name = CharField(null=True)
    value = CharField(null=True)

    class Meta:
        db_table = 'order_config'


class OrderCouponConsum(BaseModel):
    company_id = IntegerField(column_name='company_id', null=True)
    cost = DecimalField()
    coupon_code = CharField(index=True, null=True)
    coupon_discount = DecimalField()
    coupon_fee = DecimalField()
    coupon_income = DecimalField()
    coupon_name = CharField(null=True)
    coupon_type = IntegerField(null=True)
    id = BigIntegerField(primary_key=True)
    order_id = BigIntegerField(column_name='order_id', index=True)

    class Meta:
        db_table = 'order_coupon_consum'


class OrderCouponConsumHistory(BaseModel):
    company = IntegerField(column_name='company_id', null=True)
    cost = DecimalField()
    coupon_code = CharField(index=True, null=True)
    coupon_discount = DecimalField()
    coupon_fee = DecimalField()
    coupon_income = DecimalField()
    coupon_name = CharField(null=True)
    coupon_type = IntegerField(null=True)
    id = BigIntegerField(primary_key=True)
    order = BigIntegerField(column_name='order_id', index=True)

    class Meta:
        db_table = 'order_coupon_consum_history'


class OrderDealMemo(BaseModel):
    deal_date = MyDateTimeField(index=True)
    deal_memo = CharField(null=True)
    deal_user = CharField(null=True)
    deal_user_company_id = IntegerField(column_name='deal_user_company_id', null=True)
    id = BigIntegerField(primary_key=True)
    order_id = BigIntegerField(column_name='order_id', index=True)

    class Meta:
        db_table = 'order_deal_memo'
        indexes = (
            (('order', 'deal_user'), False),
        )


class OrderDealMemoHistory(BaseModel):
    deal_date = MyDateTimeField(index=True)
    deal_memo = CharField(null=True)
    deal_user = CharField(null=True)
    deal_user_company_id = IntegerField(column_name='deal_user_company_id', null=True)
    id = BigIntegerField(primary_key=True)
    order_id = BigIntegerField(column_name='order_id', index=True)

    class Meta:
        db_table = 'order_deal_memo_history'
        indexes = (
            (('order', 'deal_user'), False),
        )


class OrderDeliver(BaseModel):
    batch_id = IntegerField(column_name='batch_id', null=True)
    create_time = MyDateTimeField()
    delivery_failed_qty = IntegerField(null=True)
    delivery_qty = IntegerField(null=True)
    delivery_status = IntegerField(null=True)
    id = BigIntegerField(primary_key=True)
    master_product_id = BigIntegerField(column_name='master_product_id', null=True)
    order_id = BigIntegerField(column_name='order_id')
    product_id = BigIntegerField(column_name='product_id')
    product_type = IntegerField(null=True)
    quantity = IntegerField(null=True)
    update_time = MyDateTimeField()

    class Meta:
        db_table = 'order_deliver'
        indexes = (
            (('order', 'product'), False),
        )


class OrderDeliverHistory(BaseModel):
    batch = IntegerField(column_name='batch_id', null=True)
    create_time = MyDateTimeField()
    delivery_failed_qty = IntegerField(null=True)
    delivery_qty = IntegerField(null=True)
    delivery_status = IntegerField(null=True)
    id = BigIntegerField(primary_key=True)
    master_product = BigIntegerField(column_name='master_product_id', null=True)
    order = BigIntegerField(column_name='order_id')
    product = BigIntegerField(column_name='product_id')
    product_type = IntegerField(null=True)
    quantity = IntegerField(null=True)
    update_time = MyDateTimeField()

    class Meta:
        db_table = 'order_deliver_history'
        indexes = (
            (('order', 'product'), False),
        )


class OrderDetail(BaseModel):
    account_date = MyDateTimeField(null=True)
    batch_id = IntegerField(column_name='batch_id', null=True)
    business_id = IntegerField(column_name='business_id', null=True)
    business_product_id = BigIntegerField(column_name='business_product_id', index=True, null=True)
    category_id = IntegerField(column_name='category_id', null=True)
    combine_discount_amount = DecimalField()
    company_id = IntegerField(column_name='company_id', null=True)
    coupon_code = CharField(null=True)
    deposit_discount_amount = DecimalField()
    discount_amount = DecimalField()
    id = BigIntegerField(primary_key=True)
    is_master_product = MyBitField(null=True)  # bit
    is_refunded = MyBitField(null=True)  # bit
    manual_discount_amount = DecimalField()
    nsource = CharField(null=True)
    order = ForeignKeyField(OrderMaster, column_name='order_id', index=True, backref="order_detail")
    # order_id = BigIntegerField(column_name='order_id', null=True)
    point_discount = DecimalField()
    product_cate = IntegerField(null=True)
    product_cost = DecimalField()
    product_id = BigIntegerField(column_name='product_id')
    product_name = CharField(null=True)
    product_type = IntegerField(null=True)
    promotion_info = CharField(null=True)
    quantity = IntegerField()
    seller_id = BigIntegerField(column_name='seller_id', null=True)
    timestamp = MyDateTimeField(null=True)
    unit_price = DecimalField(column_name="unit_price")
    warehouse_id = IntegerField(column_name='warehouse_id', null=True)

    class Meta:
        db_table = 'order_detail'
        indexes = (
            (('order', 'product'), False),
            (('order', 'product_type'), False),
            (('order', 'quantity'), False),
        )


class OrderDetailAttached(BaseModel):
    company_id = IntegerField(column_name='company_id', null=True)
    create_time = MyDateTimeField()
    create_user_company_id = IntegerField(column_name='create_user_company_id', null=True)
    create_user_id = BigIntegerField(column_name='create_user_id', null=True)
    id = BigIntegerField(primary_key=True)
    master_product_id = BigIntegerField(column_name='master_product_id', index=True)
    order_id = BigIntegerField(column_name='order_id', index=True)
    product_id = BigIntegerField(column_name='product_id', index=True)
    update_time = MyDateTimeField()
    update_user_company_id = IntegerField(column_name='update_user_company_id', null=True)
    update_user_id = BigIntegerField(column_name='update_user_id', null=True)

    class Meta:
        db_table = 'order_detail_attached'


class OrderDetailAttachedHistory(BaseModel):
    company = IntegerField(column_name='company_id', null=True)
    create_time = MyDateTimeField()
    create_user_company = IntegerField(column_name='create_user_company_id', null=True)
    create_user = BigIntegerField(column_name='create_user_id', null=True)
    id = BigIntegerField(primary_key=True)
    master_product = BigIntegerField(column_name='master_product_id', index=True)
    order = BigIntegerField(column_name='order_id', index=True)
    product = BigIntegerField(column_name='product_id', index=True)
    update_time = MyDateTimeField()
    update_user_company = IntegerField(column_name='update_user_company_id', null=True)
    update_user = BigIntegerField(column_name='update_user_id', null=True)

    class Meta:
        db_table = 'order_detail_attached_history'


class OrderDetailCoupon(BaseModel):
    batch_id = IntegerField(column_name='batch_id', null=True)
    coupon_code = CharField(index=True, null=True)
    coupon_type = IntegerField(null=True)
    create_time = MyDateTimeField()
    id = BigIntegerField(primary_key=True)
    is_verificationed = MyBitField(null=True)  # bit
    multi_product_id = BigIntegerField(column_name='multi_product_id', null=True)
    order_id = BigIntegerField(column_name='order_id')
    product_id = BigIntegerField(column_name='product_id', null=True)
    reference_verify_id = BigIntegerField(column_name='reference_verify_id', index=True, null=True)
    update_time = MyDateTimeField()
    verify_time = MyDateTimeField(null=True)

    class Meta:
        db_table = 'order_detail_coupon'
        indexes = (
            (('order', 'multi_product', 'product'), False),
        )


class OrderDetailCouponHistory(BaseModel):
    batch = IntegerField(column_name='batch_id', null=True)
    coupon_code = CharField(index=True, null=True)
    coupon_type = IntegerField(null=True)
    create_time = MyDateTimeField()
    id = BigIntegerField(primary_key=True)
    is_verificationed = MyBitField(null=True)  # bit
    multi_product = IntegerField(column_name='multi_product_id', null=True)
    order = BigIntegerField(column_name='order_id')
    product = BigIntegerField(column_name='product_id', null=True)
    reference_verify = BigIntegerField(column_name='reference_verify_id', index=True, null=True)
    update_time = MyDateTimeField()
    verify_time = MyDateTimeField(null=True)

    class Meta:
        db_table = 'order_detail_coupon_history'
        indexes = (
            (('order', 'multi_product', 'product'), False),
        )


class OrderDetailDiscount(BaseModel):
    business_product_id = BigIntegerField(column_name='business_product_id', null=True)
    company_id = IntegerField(column_name='company_id', null=True)
    discount_amount = DecimalField()
    discount_dec = CharField(null=True)
    discount_xb = DecimalField(null=True)
    id = BigIntegerField(primary_key=True)
    order_id = BigIntegerField(column_name='order_id', index=True, null=True)
    product_business_id = IntegerField(column_name='product_business_id', null=True)
    product_id = BigIntegerField(column_name='product_id', index=True, null=True)
    product_seller_id = BigIntegerField(column_name='product_seller_id', null=True)
    source_code = CharField(index=True, null=True)
    source_id = BigIntegerField(column_name='source_id', null=True)
    source_type = IntegerField(null=True)
    start_time = MyDateTimeField(column_name="start_time")
    end_time = MyDateTimeField(column_name="end_time")

    class Meta:
        db_table = 'order_detail_discount'


class OrderDetailDiscountHistory(BaseModel):
    business_product = BigIntegerField(column_name='business_product_id', null=True)
    company = IntegerField(column_name='company_id', null=True)
    discount_amount = DecimalField()
    discount_dec = CharField(null=True)
    discount_xb = DecimalField(null=True)
    id = BigIntegerField(primary_key=True)
    order = BigIntegerField(column_name='order_id', index=True, null=True)
    product_business = IntegerField(column_name='product_business_id', null=True)
    product = BigIntegerField(column_name='product_id', index=True, null=True)
    product_seller = BigIntegerField(column_name='product_seller_id', null=True)
    source_code = CharField(null=True)
    source = BigIntegerField(column_name='source_id', null=True)
    source_type = IntegerField(null=True)

    class Meta:
        db_table = 'order_detail_discount_history'


class OrderDetailHistory(BaseModel):
    account_date = MyDateTimeField(null=True)
    batch = IntegerField(column_name='batch_id', null=True)
    business = IntegerField(column_name='business_id', null=True)
    business_product = BigIntegerField(column_name='business_product_id', index=True, null=True)
    category_id = IntegerField(column_name='category_id', null=True)
    combine_discount_amount = DecimalField()
    company = IntegerField(column_name='company_id', null=True)
    coupon_code = CharField(null=True)
    deposit_discount_amount = DecimalField()
    discount_amount = DecimalField()
    id = BigIntegerField(primary_key=True)
    is_master_product = MyBitField(null=True)  # bit
    is_refunded = MyBitField(null=True)  # bit
    manual_discount_amount = DecimalField()
    nsource = CharField(null=True)
    order = BigIntegerField(column_name='order_id', null=True)
    point_discount = DecimalField()
    product_cate = IntegerField(null=True)
    product_cost = DecimalField()
    product = BigIntegerField(column_name='product_id')
    product_name = CharField(null=True)
    product_type = IntegerField(null=True)
    promotion_info = CharField(null=True)
    quantity = IntegerField()
    seller = BigIntegerField(column_name='seller_id', null=True)
    timestamp = MyDateTimeField(index=True, null=True)
    unit_price = DecimalField()
    warehouse = IntegerField(column_name='warehouse_id', null=True)

    class Meta:
        db_table = 'order_detail_history'
        indexes = (
            (('order', 'product'), False),
            (('order', 'product_type'), False),
            (('order', 'quantity'), False),
        )


class OrderDetailMulti(BaseModel):
    add_to_cart_url = CharField(null=True)
    batch_id = IntegerField(column_name='batch_id', null=True)
    business_id = IntegerField(column_name='business_id', null=True)
    business_product_id = BigIntegerField(column_name='business_product_id', index=True, null=True)
    category_id = IntegerField(column_name='category_id', null=True)
    combine_discount_amount = DecimalField(null=True)
    company_id = IntegerField(column_name='company_id', null=True)
    coupon_code = CharField(null=True)
    coupon_type = IntegerField(null=True)
    create_time = MyDateTimeField()
    deposit_discount_amount = DecimalField(null=True)
    discount_amount = DecimalField(null=True)
    has_subtotal_value = MyBitField(null=True)  # bit
    id = BigIntegerField(primary_key=True)
    manual_discount_amount = DecimalField(null=True)
    multi_product_id = BigIntegerField(column_name='multi_product_id', null=True)
    order_id = BigIntegerField(column_name='order_id', null=True)
    point_discount = DecimalField(null=True)
    product_cost = DecimalField(null=True)
    product_id = BigIntegerField(column_name='product_id', index=True, null=True)
    product_name = CharField(null=True)
    product_type = IntegerField(null=True)
    quantity = IntegerField(null=True)
    seller_id = BigIntegerField(column_name='seller_id', null=True)
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
    update_time = MyDateTimeField()
    warehouse_id = IntegerField(column_name='warehouse_id', null=True)

    class Meta:
        db_table = 'order_detail_multi'
        indexes = (
            (('order', 'multi_product'), False),
            (('order', 'product_type'), False),
        )


class OrderDetailMultiHistory(BaseModel):
    add_to_cart_url = CharField(null=True)
    batch = IntegerField(column_name='batch_id', null=True)
    business = IntegerField(column_name='business_id', null=True)
    business_product = BigIntegerField(column_name='business_product_id', index=True, null=True)
    category = IntegerField(column_name='category_id', null=True)
    combine_discount_amount = DecimalField(null=True)
    company = IntegerField(column_name='company_id', null=True)
    coupon_code = CharField(null=True)
    coupon_type = IntegerField(null=True)
    create_time = MyDateTimeField()
    deposit_discount_amount = DecimalField(null=True)
    discount_amount = DecimalField(null=True)
    has_subtotal_value = DecimalField(null=True)
    id = BigIntegerField(primary_key=True)
    manual_discount_amount = DecimalField(null=True)
    multi_product = BigIntegerField(column_name='multi_product_id', null=True)
    order = BigIntegerField(column_name='order_id', null=True)
    point_discount = DecimalField(null=True)
    product_cost = DecimalField(null=True)
    product = BigIntegerField(column_name='product_id', index=True, null=True)
    product_name = CharField(null=True)
    product_type = IntegerField(null=True)
    quantity = IntegerField(null=True)
    seller = BigIntegerField(column_name='seller_id', null=True)
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
    update_time = MyDateTimeField()
    warehouse = IntegerField(column_name='warehouse_id', null=True)

    class Meta:
        db_table = 'order_detail_multi_history'
        indexes = (
            (('order', 'multi_product'), False),
            (('order', 'product_type'), False),
        )


class OrderFromTop(BaseModel):
    added_date = MyDateTimeField(null=True)
    ali_trade_no = BigIntegerField(null=True)
    id = BigIntegerField(primary_key=True)
    import_order = TextField(null=True)
    operator = CharField(null=True)
    order = BigIntegerField(column_name='order_id', null=True)
    platform = IntegerField(column_name='platform_id', null=True)
    taobao_token = CharField(null=True)

    class Meta:
        db_table = 'order_from_top'


class OrderHjUser(BaseModel):
    bbs_user = BigIntegerField(column_name='bbs_user_id', index=True, null=True)
    company = IntegerField(column_name='company_id', null=True)
    department = IntegerField(column_name='department_id', null=True)
    email = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    nick_name = CharField(null=True)
    true_name = CharField(null=True)
    user_name = CharField(null=True)

    class Meta:
        db_table = 'order_hj_user'


class OrderIncome(BaseModel):
    batch = BigIntegerField(column_name='batch_id', null=True)
    coupon_code = CharField(index=True, null=True)
    income_date = MyDateTimeField(null=True)
    income_id = BigIntegerField(column_name='income_id', primary_key=True)
    income_type = IntegerField(null=True)
    last_update_date = MyDateTimeField(null=True)
    master_product = BigIntegerField(column_name='master_product_id', null=True)
    old_refund = BigIntegerField(column_name='old_refund_id', null=True)
    operater_type = IntegerField(null=True)
    order_type = IntegerField(null=True)
    product_name = CharField(null=True)
    product_type = IntegerField(null=True)
    quantity = IntegerField(null=True)
    reference_income = BigIntegerField(column_name='reference_income_id', null=True)
    share_income_fee = DecimalField()
    share_purchase_xb = DecimalField()
    share_recharege_xb = DecimalField()
    share_reward_xb = DecimalField()
    source_order = BigIntegerField(column_name='source_order_id', null=True)
    source_rma = BigIntegerField(column_name='source_rma_id', index=True, null=True)
    status = IntegerField(null=True)
    sub_product = BigIntegerField(column_name='sub_product_id', null=True)
    user = BigIntegerField(column_name='user_id', null=True)

    class Meta:
        db_table = 'order_income'
        indexes = (
            (('source_order', 'sub_product'), False),
        )


class OrderMasterHistory(BaseModel):
    ali_trade_no = CharField(null=True)
    bank_code = CharField(null=True)
    bill_date = MyDateTimeField(null=True)
    bill_no = CharField(null=True)
    cancel_date = MyDateTimeField(null=True)
    cell_phone = CharField(null=True)
    chest_fee = DecimalField(null=True)
    city = IntegerField(column_name='city_id', null=True)
    combine_fee = DecimalField()
    company = IntegerField(column_name='company_id', null=True)
    coupon_fee = DecimalField()
    coupon_income = DecimalField()
    create_time = MyDateTimeField()
    create_user_company = IntegerField(column_name='create_user_company_id', null=True)
    create_user = BigIntegerField(column_name='create_user_id', null=True)
    deal_fee = DecimalField()
    deal_memo = CharField(null=True)
    deal_user = CharField(null=True)
    deliver = CharField(column_name='deliver_id', index=True, null=True)
    delivery_result = IntegerField(null=True)
    delivery_status = IntegerField(null=True)
    deposit_discount_fee = DecimalField()
    discount_fee = DecimalField()
    email = CharField(index=True, null=True)
    express = IntegerField(null=True)
    express_id = IntegerField(null=True)
    extend_bill_status = IntegerField(null=True)
    fee_memo = CharField(null=True)
    from_ip = CharField(null=True)
    handling_fee = DecimalField()
    hj_user = BigIntegerField(column_name='hj_user_id', null=True)
    income = DecimalField()
    installment_number = IntegerField(null=True)
    invite_code_fee = DecimalField()
    is_active = MyBitField(null=True)  # bit
    is_audit = MyBitField(null=True)  # bit
    is_bill = MyBitField(null=True)  # bit
    is_cancel = MyBitField(null=True)  # bit
    is_child = MyBitField(null=True)  # bit
    is_inside = MyBitField(null=True)  # bit
    is_notify = MyBitField(null=True)  # bit
    is_phone = MyBitField(null=True)  # bit
    is_print = MyBitField(null=True)  # bit
    is_test = MyBitField(null=True)  # bit
    is_trace = MyBitField(null=True)  # bit
    is_unusual = MyBitField(null=True)  # bit
    is_valid = MyBitField(null=True)  # bit
    manual_discount_fee = DecimalField()
    mark = IntegerField(null=True)
    msn = CharField(null=True)
    notify_mark = CharField(null=True)
    nsource = CharField(null=True)
    operator_company = IntegerField(column_name='operator_company_id', null=True)
    operator_user = BigIntegerField(column_name='operator_user_id', null=True)
    order_date = MyDateTimeField(null=True)
    order_device = IntegerField(column_name='order_device_id', null=True)
    order = BigIntegerField(column_name='order_id', primary_key=True)
    order_number = CharField(null=True)
    order_type = IntegerField()
    outer_trade_no = CharField(null=True)
    parent_order = BigIntegerField(column_name='parent_order_id', null=True)
    pay_card_type = IntegerField(null=True)
    pay_device = IntegerField(column_name='pay_device_id', null=True)
    pay_method = CharField(null=True)
    payment_bank_discount = DecimalField(null=True)
    phone_date = MyDateTimeField(null=True)
    platform = IntegerField(column_name='platform_id', null=True)
    point_fee = DecimalField()
    pre_income = DecimalField()
    province = IntegerField(column_name='province_id', null=True)
    purchase_xb = DecimalField()
    qq = CharField(null=True)
    recharge_xb = DecimalField()
    refer_source = IntegerField(column_name='refer_source_id', null=True)
    refer_url = CharField(null=True)
    refund_type = CharField(null=True)
    related_order = BigIntegerField(column_name='related_order_id', index=True, null=True)
    reward_xb = DecimalField()
    seller = BigIntegerField(column_name='seller_id', index=True, null=True)
    ship_date = MyDateTimeField(null=True)
    ship_flag = IntegerField(null=True)
    ship_method = CharField(null=True)
    ship_to_addr = CharField(null=True)
    ship_to_city = CharField(null=True)
    ship_to_name = CharField(index=True, null=True)
    ship_to_phone = CharField(index=True, null=True)
    ship_to_province = CharField(null=True)
    ship_to_time = CharField(null=True)
    ship_to_zip = CharField(null=True)
    shipping_fee = DecimalField()
    temp_order_version = IntegerField(null=True)
    timestamp = MyDateTimeField(index=True)
    total_cost = DecimalField()
    total_fee = DecimalField()
    total_order_today = IntegerField(null=True)
    town = IntegerField(column_name='town_id', null=True)
    update_time = MyDateTimeField()
    update_user_company = IntegerField(column_name='update_user_company_id', null=True)
    update_user = BigIntegerField(column_name='update_user_id', null=True)
    user_coupon = IntegerField(column_name='user_coupon_id', null=True)
    user_handling_fee = DecimalField()
    user = BigIntegerField(column_name='user_id', null=True)
    user_memo = CharField(null=True)
    user_reg_date = MyDateTimeField(null=True)
    user_source = CharField(null=True)
    user_title = CharField(null=True)
    xb_fee = DecimalField()

    class Meta:
        db_table = 'order_master_history'
        indexes = (
            (('is_active', 'hj_user', 'order_type', 'is_cancel'), False),
            (('is_active', 'order_date', 'hj_user', 'order_type'), False),
            (('is_bill', 'bill_date', 'hj_user', 'order_type', 'is_active', 'is_cancel'), False),
            (('pay_method', 'order_date'), False),
            (('platform', 'temp_order_version'), False),
        )


class OrderMessageLog(BaseModel):
    id = BigIntegerField(primary_key=True)
    message_content = TextField(null=True)
    message = CharField(column_name='message_id', null=True)
    produce = CharField(column_name='produce_id', null=True)
    send_date_time = MyDateTimeField(null=True)
    send_machine_ip = CharField(null=True)

    class Meta:
        db_table = 'order_message_log'


class OrderPayInfo(BaseModel):
    bank_code = CharField(null=True)
    begin_time = MyDateTimeField(null=True)
    bill_amount = DecimalField()
    child_order_id = BigIntegerField(column_name='child_order_id', null=True)
    create_time = MyDateTimeField()
    create_user_id = BigIntegerField(column_name='create_user_id', null=True)
    end_time = MyDateTimeField(null=True)
    ext_param = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    order_id = BigIntegerField(column_name='order_id')
    order_type = IntegerField(null=True)
    origin_order_id = BigIntegerField(column_name='origin_order_id', null=True)
    pay_channel = CharField(null=True)
    pay_device_id = IntegerField(column_name='pay_device_id', null=True)
    pay_method = IntegerField(null=True)
    pay_num = CharField(null=True)
    pay_status = IntegerField(null=True)
    pay_time = MyDateTimeField(null=True)
    pay_type = IntegerField(null=True)
    purchase_xb = DecimalField()
    recharge_xb = DecimalField()
    remark = CharField(null=True)
    reward_xb = DecimalField()
    trans_seq_no = CharField(null=True)
    update_time = MyDateTimeField()
    update_user_id = BigIntegerField(column_name='update_user_id', null=True)
    xb_fee = DecimalField()

    class Meta:
        db_table = 'order_pay_info'
        indexes = (
            (('order', 'child_order'), False),
            (('order', 'order_type'), False),
        )


class OrderProductGroupbuy(BaseModel):
    a_360_cate = CharField()
    a_360_display = MyBitField(null=True)  # bit
    a_360_hot_bus_spot_name = CharField()
    a_360_img = CharField()
    a_360_latitude = CharField()
    a_360_longitude = CharField()
    a_360_merchant_addr = CharField()
    a_360_merchant_name = CharField()
    a_360_merchant_phone = CharField()
    a_360_spent_end_time = MyDateTimeField(null=True)
    a_360_spent_start_time = MyDateTimeField(null=True)
    a_360_title = CharField()
    admin_memo = CharField()
    big_img_name = CharField()
    bulo_display_img_url = CharField(null=True)
    buy_only_once = MyBitField(null=True)  # bit
    cate = IntegerField(column_name='cate_id')
    cate_idadmin = IntegerField()
    class_ = IntegerField(column_name='class_id')
    ctproduct_code = CharField(null=True)
    display_by_bulo = MyBitField(null=True)  # bit
    end_time = MyDateTimeField()
    free_buy_type = IntegerField()
    full_num = IntegerField()
    group_buy_price = DecimalField()
    groupbuy_type = IntegerField()
    has_notice_by_mail = MyBitField(null=True)  # bit
    has_notice_by_sms = MyBitField(null=True)  # bit
    id = BigIntegerField(primary_key=True)
    is_active = IntegerField()
    is_free_by_count = MyBitField(null=True)  # bit
    is_free_delivery = MyBitField(null=True)  # bit
    is_hide = MyBitField(null=True)  # bit
    is_new_version = MyBitField(null=True)  # bit
    is_takeby_customer = MyBitField(null=True)  # bit
    is_valid = MyBitField(null=True)  # bit
    is_view = MyBitField(null=True)  # bit
    keywords = CharField(null=True)
    last_notice_time_mail = MyDateTimeField()
    last_notice_time_sms = MyDateTimeField()
    last_update_time = MyDateTimeField()
    list_price = DecimalField()
    low_cate = IntegerField(column_name='low_cate_id', null=True)
    mark = IntegerField()
    max_buy_amount = IntegerField()
    mention = CharField()
    mini_product_name = CharField(null=True)
    prevision_img_name = CharField()
    product_desc = TextField()
    product = BigIntegerField(column_name='product_id', index=True)
    product_name = CharField(null=True)
    quantity = IntegerField()
    related_coupon_batch = IntegerField()
    related_coupon_batch_type = IntegerField(null=True)
    related_income = DecimalField()
    related_staff = CharField(null=True)
    room = IntegerField(column_name='room_id', null=True)
    short_product_name = CharField(null=True)
    small_img_name = CharField()
    sort_index = IntegerField()
    start_time = MyDateTimeField()
    supplier = IntegerField(column_name='supplier_id')
    supplier_type = IntegerField()
    system_remark = TextField(null=True)
    tags = CharField(null=True)
    timeup_warning = MyBitField(null=True)  # bit
    total_buy_amount = IntegerField()
    touch_product_desc = TextField(null=True)
    unit_cost = DecimalField()
    unit_delivery_cost = DecimalField()
    user_ce_hua = CharField()
    user_ce_hua_id = IntegerField(null=True)
    user_comment = TextField()
    user_design = IntegerField(column_name='user_design_id', null=True)
    user_tui_guang = CharField()
    user_tui_guang_id = IntegerField(null=True)
    user_wen_an = CharField()
    user_wen_an_id = IntegerField(null=True)
    virtual_buyer_amount = IntegerField()

    class Meta:
        db_table = 'order_product_groupbuy'


class OrderTester(BaseModel):
    company = IntegerField(column_name='company_id', null=True)
    hj_user = BigIntegerField(column_name='hj_user_id', index=True, null=True)
    id = BigIntegerField(primary_key=True)
    status = MyBitField(null=True)  # bit
    user = BigIntegerField(column_name='user_id', null=True)
    user_name = CharField(null=True)

    class Meta:
        db_table = 'order_tester'


class OrderTracking(BaseModel):
    add_to_cart_url = CharField(null=True)
    create_time = MyDateTimeField()
    device_id = CharField(column_name='device_id', null=True)
    ext_param = CharField(null=True)
    from_ip = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    order_department_id = IntegerField(column_name='order_department_id', null=True)
    order_device_id = IntegerField(column_name='order_device_id', null=True)
    # order_id = BigIntegerField(column_name='order_id')
    order = ForeignKeyField(OrderMaster, column_name='order_id', index=True, backref="order_tracking")
    order_reason_id = IntegerField(column_name='order_reason_id', null=True)
    order_source_id = IntegerField(column_name='order_source_id', null=True)
    pay_device_id = IntegerField(column_name='pay_device_id', null=True)
    refer_url = CharField(null=True)
    reference_order_id = BigIntegerField(column_name='reference_order_id', index=True, null=True)
    rma_flag = IntegerField(null=True)
    sales_channel_id = IntegerField(column_name='sales_channel_id', null=True)
    sales_platform_id = IntegerField(column_name='sales_platform_id', null=True)
    sid = CharField(null=True)
    solution_code = CharField(null=True)
    ssid = CharField(null=True)
    swap_solution_code = CharField(null=True)
    uid = CharField(null=True)
    update_time = MyDateTimeField(null=True)
    app_id = CharField(null=True)

    class Meta:
        db_table = 'order_tracking'
        indexes = (
            (('order', 'order_source', 'solution_code', 'sales_platform'), False),
        )


class OrderTrackingHistory(BaseModel):
    add_to_cart_url = CharField(null=True)
    create_time = MyDateTimeField()
    device = CharField(column_name='device_id', null=True)
    ext_param = CharField(null=True)
    from_ip = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    order_department = IntegerField(column_name='order_department_id', null=True)
    order_device = IntegerField(column_name='order_device_id', null=True)
    order = BigIntegerField(column_name='order_id')
    order_reason = IntegerField(column_name='order_reason_id', null=True)
    order_source = IntegerField(column_name='order_source_id', null=True)
    pay_device = IntegerField(column_name='pay_device_id', null=True)
    refer_url = CharField(null=True)
    reference_order = BigIntegerField(column_name='reference_order_id', index=True, null=True)
    rma_flag = IntegerField(null=True)
    sales_channel = IntegerField(column_name='sales_channel_id', null=True)
    sales_platform = IntegerField(column_name='sales_platform_id', null=True)
    sid = CharField(null=True)
    solution_code = CharField(null=True)
    ssid = CharField(null=True)
    swap_solution_code = CharField(null=True)
    uid = CharField(null=True)
    update_time = MyDateTimeField()

    class Meta:
        db_table = 'order_tracking_history'
        indexes = (
            (('order', 'order_reason'), False),
            (('order', 'order_source'), False),
            (('order', 'sales_platform'), False),
        )


class OrderUserAddressLog(BaseModel):
    address = CharField(null=True)
    change_date = MyDateTimeField(null=True)
    create_time = MyDateTimeField()
    create_user_company = IntegerField(column_name='create_user_company_id', null=True)
    create_user = BigIntegerField(column_name='create_user_id', null=True)
    id = BigIntegerField(primary_key=True)
    old_address = CharField(null=True)
    operator = CharField(null=True)
    order = BigIntegerField(column_name='order_id', null=True)
    shop_user = BigIntegerField(column_name='shop_user_id', null=True)
    user = BigIntegerField(column_name='user_id', null=True)

    class Meta:
        db_table = 'order_user_address_log'


class OrderUserPhoneLog(BaseModel):
    change_date = MyDateTimeField(null=True)
    create_time = MyDateTimeField()
    create_user_company = IntegerField(column_name='create_user_company_id', null=True)
    create_user = BigIntegerField(column_name='create_user_id', null=True)
    id = BigIntegerField(primary_key=True)
    old_phone = CharField(null=True)
    operator = CharField(null=True)
    order = BigIntegerField(column_name='order_id', null=True)
    phone = CharField(null=True)
    shop_user = BigIntegerField(column_name='shop_user_id', null=True)
    type = IntegerField(null=True)
    user = BigIntegerField(column_name='user_id', null=True)

    class Meta:
        db_table = 'order_user_phone_log'


class OrderVirtualDeliver(BaseModel):
    create_time = MyDateTimeField()
    id = BigIntegerField(primary_key=True)
    order_id = BigIntegerField()
    order_deliver_id = BigIntegerField(column_name='order_deliver_id', index=True, null=True)
    send_code = CharField(null=True)
    update_time = MyDateTimeField()

    class Meta:
        db_table = 'order_virtual_deliver'


class OrderVirtualDeliverHistory(BaseModel):
    create_time = MyDateTimeField()
    id = BigIntegerField(primary_key=True)
    order_deliver = BigIntegerField(column_name='order_deliver_id', index=True, null=True)
    send_code = CharField(null=True)
    update_time = MyDateTimeField()

    class Meta:
        db_table = 'order_virtual_deliver_history'


class UserAddress(BaseModel):
    city = IntegerField(column_name='city_id', null=True)
    create_time = MyDateTimeField()
    create_user_company = IntegerField(column_name='create_user_company_id', null=True)
    create_user = BigIntegerField(column_name='create_user_id', null=True)
    id = BigIntegerField(primary_key=True)
    is_default = MyBitField(null=True)  # bit
    msn = CharField(null=True)
    province = IntegerField(column_name='province_id', null=True)
    qq = CharField(null=True)
    ship_to_address = CharField(null=True)
    ship_to_cellphone = CharField(null=True)
    ship_to_email = CharField(null=True)
    ship_to_name = CharField(null=True)
    ship_to_phone = CharField(null=True)
    ship_to_zip = CharField(null=True)
    shop_user = BigIntegerField(column_name='shop_user_id', null=True)
    town = IntegerField(column_name='town_id', null=True)
    update_time = MyDateTimeField()
    update_user_company = IntegerField(column_name='update_user_company_id', null=True)
    update_user = BigIntegerField(column_name='update_user_id', null=True)

    class Meta:
        db_table = 'user_address'


class EsIndexOrderLog(BaseModel):
    create_date = DateTimeField(index=True)
    custom_data = CharField(null=True)
    from_ = BigIntegerField(column_name='from', null=True)
    id = BigIntegerField(primary_key=True)
    is_valid = MyBitField(null=True)  # bit
    last_order_date = DateTimeField(null=True)
    last_order_id = BigIntegerField(column_name='last_order_id', null=True)
    size = IntegerField(null=True)
    total_records = IntegerField(null=True)

    class Meta:
        db_table = 'es_index_order_log'
        indexes = (
            (('last_order', 'from_', 'create_date'), False),
        )


class OrderArchiveDetailLog(BaseModel):
    archive_batch_code = CharField(index=True)
    archive_time = DateTimeField(null=True)
    create_time = DateTimeField()
    delete_time = DateTimeField(null=True)
    id = BigIntegerField(primary_key=True)
    is_archive = MyBitField(null=True)  # bit
    is_delete = MyBitField(null=True)  # bit
    is_to_es = MyBitField(null=True)  # bit
    order_id = BigIntegerField(column_name='order_id', index=True)
    to_es_time = DateTimeField(null=True)
    update_time = DateTimeField()

    class Meta:
        db_table = 'order_archive_detail_log'


class OrderArchiveMasterLog(BaseModel):
    archive_batch_code = CharField(index=True)
    archive_order_quantity = BigIntegerField(null=True)
    archive_status = MyBitField(null=True)  # bit
    begin_order_id = BigIntegerField(column_name='begin_order_id', null=True)
    create_time = DateTimeField(index=True)
    delete_status = MyBitField(null=True)  # bit
    end_order_id = BigIntegerField(column_name='end_order_id', null=True)
    id = BigIntegerField(primary_key=True)
    to_es_status = MyBitField(null=True)  # bit
    update_time = DateTimeField()

    class Meta:
        db_table = 'order_archive_master_log'


class TradeControl(BaseModel):
    compensate_action = CharField(null=True)
    create_time = MyDateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    create_user_id = BigIntegerField(column_name='create_user_id', null=True)
    has_cancel = IntegerField(null=True)
    has_commit = IntegerField(null=True)
    has_compensate = IntegerField(index=True, null=True)
    has_freeze = IntegerField(null=True)
    id = BigAutoField()
    order_id = BigIntegerField(column_name='order_id', index=True, null=True)
    trade_number = CharField(unique=True)
    update_time = MyDateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    update_user_id = BigIntegerField(column_name='update_user_id', null=True)

    class Meta:
        table_name = 'trade_control'


class TradeResourceStatus(BaseModel):
    cancel_time = MyDateTimeField(null=True)
    commit_time = MyDateTimeField(null=True)
    create_time = MyDateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    create_user_id = BigIntegerField(column_name='create_user_id', null=True)
    freeze_time = MyDateTimeField(null=True)
    has_cancel = IntegerField(null=True)
    has_commit = IntegerField(null=True)
    has_freeze = IntegerField(null=True)
    id = BigAutoField()
    order_id = BigIntegerField(column_name='order_id', null=True)
    resource_code = CharField(null=True, unique=True)
    resource_type = IntegerField(null=True)
    retry_count = IntegerField(null=True)
    retry_time = MyDateTimeField(null=True)
    trade_number = CharField(index=True)
    update_time = MyDateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    update_user_id = BigIntegerField(column_name='update_user_id', null=True)

    class Meta:
        table_name = 'trade_resource_status'
