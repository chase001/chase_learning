

class AreaCode(object):
    def __init__(self):
        self.code = None
        self.level = None
        self.name = None
        self.parent_code = None


class BatchOrderCustomer(object):
    def __init__(self):
        self.company_id = None
        self.create_time = None
        self.hj_user_id = None
        self.id = None
        self.order_id = None
        self.receive_address = None
        self.receive_name = None
        self.receive_phone = None
        self.reference_order_id = None
        self.rerification_status = None
        self.ship_to_city = None
        self.ship_to_country = None
        self.ship_to_province = None
        self.ship_to_town = None
        self.task_id = None
        self.user_name = None

class BatchOrderProduct(object):
    def __init__(self):
        self.business_product_id = None
        self.combin_discount_amount = None
        self.create_time = None
        self.id = None
        self.is_master_product = None
        self.manual_discount = None
        self.master_product_id = None
        self.product_id = None
        self.product_name = None
        self.product_type = None
        self.promotion_discount_amount = None
        self.quantity = None
        self.shipping_fee = None
        self.task_id = None
        self.unit_price = None

class BatchOrderTask(object):
    def __init__(self):
        self.create_time = None
        self.end_date = None
        self.operator = None
        self.operator_user_id = None
        self.order_department_id = None
        self.order_memo = None
        self.order_project_code = None
        self.order_reason_id = None
        self.start_date = None
        self.status = None
        self.task_id = None
        self.task_name = None

class BiBusiness(object):
    def __init__(self):
        self.code = None
        self.description = None
        self.id = None

class BiCouponType(object):
    def __init__(self):
        self.code = None
        self.description = None
        self.id = None

class BiDeviceType(object):
    def __init__(self):
        self.code = None
        self.description = None
        self.id = None

class BiOrderReason(object):
    def __init__(self):
        self.code = None
        self.description = None
        self.id = None

class BiOrderSalesChannel(object):
    def __init__(self):
        self.code = None
        self.description = None
        self.id = None

class BiOrderSource(object):
    def __init__(self):
        self.code = None
        self.description = None
        self.id = None

class BiOrderType(object):
    def __init__(self):
        self.code = None
        self.description = None
        self.id = None

class BiPayMethod(object):
    def __init__(self):
        self.code = None
        self.description = None
        self.id = None
        self.is_active = None
        self.pay_method_foe = None

class BiPlatformType(object):
    def __init__(self):
        self.code = None
        self.description = None
        self.id = None

class BiProductStatus(object):
    def __init__(self):
        self.code = None
        self.description = None
        self.id = None

class BiProductType(object):
    def __init__(self):
        self.code = None
        self.description = None
        self.id = None

class BiSourceType(object):
    def __init__(self):
        self.code = None
        self.description = None
        self.id = None

class BiSupplierType(object):
    def __init__(self):
        self.code = None
        self.description = None
        self.id = None

class DepartmentCode(object):
    def __init__(self):
        self.department_id = None
        self.department_name = None
        self.id = None
        self.is_active = None

class EsIndexOrderLog(object):
    def __init__(self):
        self.create_date = None
        self.custom_data = None
        self.from_ = None
        self.id = None
        self.is_valid = None
        self.last_order_date = None
        self.last_order_id = None
        self.size = None
        self.total_records = None

class GroupBuyCategory(object):
    def __init__(self):
        self.added_date = None
        self.alias = None
        self.id = None
        self.is_valid = None
        self.name = None
        self.parent_id = None
        self.path = None

class GroupBuyCategoryAdmin(object):
    def __init__(self):
        self.added_date = None
        self.description = None
        self.id = None
        self.is_valid = None
        self.name = None

class GroupBuyCoupon(object):
    def __init__(self):
        self.added_date = None
        self.batch_id = None
        self.batch_size = None
        self.description = None
        self.id = None
        self.is_active = None
        self.mail_format = None
        self.title = None

class GroupBuyCouponDetail(object):
    def __init__(self):
        self.added_date = None
        self.batch_id = None
        self.batch_type = None
        self.coupon_code = None
        self.expired_date = None
        self.extended = None
        self.group_buy_id = None
        self.id = None
        self.is_active = None
        self.send_date = None
        self.user_id = None

class GroupBuyGlobalSettings(object):
    def __init__(self):
        self.display_a4_list_page = None

class GroupBuyLuckOrders(object):
    def __init__(self):
        self.email = None
        self.group_buy_id = None
        self.invitor_user_id = None
        self.join_date = None
        self.join_reason = None
        self.lucky_number = None
        self.user_id = None

class GroupBuyProduct(object):
    def __init__(self):
        self._360_cate = None
        self._360_display = None
        self._360_hot_bus_spot_name = None
        self._360_img = None
        self._360_latitude = None
        self._360_longitude = None
        self._360_merchant_addr = None
        self._360_merchant_name = None
        self._360_merchant_phone = None
        self._360_spent_end_time = None
        self._360_spent_start_time = None
        self._360_title = None
        self.admin_memo = None
        self.big_img_name = None
        self.bulo_display_img_url = None
        self.buy_only_once = None
        self.cate_id = None
        self.cate_id_admin = None
        self.class_id = None
        self.ct_product_code = None
        self.display_by_bulo = None
        self.end_time = None
        self.free_buy_type = None
        self.full_num = None
        self.group_buy_price = None
        self.group_buy_type = None
        self.has_notice_by_mail = None
        self.has_notice_by_sms = None
        self.id = None
        self.is_active = None
        self.is_free_by_count = None
        self.is_free_delivery = None
        self.is_hide = None
        self.is_new_version = None
        self.is_take_by_customer = None
        self.is_valid = None
        self.is_view = None
        self.key_words = None
        self.last_notice_time_mail = None
        self.last_notice_time_sms = None
        self.last_update_time = None
        self.list_price = None
        self.low_cate_id = None
        self.mark = None
        self.max_buy_amount = None
        self.mention = None
        self.mini_product_name = None
        self.prevision_img_name = None
        self.product_desc = None
        self.product_id = None
        self.product_name = None
        self.quantity = None
        self.related_coupon_batch = None
        self.related_coupon_batch_type = None
        self.related_income = None
        self.related_staff = None
        self.room_id = None
        self.short_product_name = None
        self.small_img_name = None
        self.sort_index = None
        self.start_time = None
        self.supplier_id = None
        self.supplier_type = None
        self.system_remark = None
        self.tags = None
        self.time_up_warning = None
        self.total_buy_amount = None
        self.touch_product_desc = None
        self.unit_cost = None
        self.unit_delivery_cost = None
        self.user_ce_hua = None
        self.user_ce_hua_id = None
        self.user_comment = None
        self.user_design_id = None
        self.user_tui_guang = None
        self.user_tui_guang_id = None
        self.user_wen_an = None
        self.user_wen_an_id = None
        self.virtual_buyer_amount = None

class GroupBuyProductDetail(object):
    def __init__(self):
        self.class_unit_cost = None
        self.group_buy_id = None
        self.id = None
        self.is_active = None
        self.product_id = None
        self.quantity = None
        self.unit_cost = None

class GroupBuyProductWarehouse(object):
    def __init__(self):
        self.group_buy_product_id = None
        self.id = None
        self.warehouse_id = None
        self.warehouse_product_id = None

class InvoiceManage(object):
    def __init__(self):
        self.account_bank = None
        self.account_number = None
        self.apply_user_name = None
        self.company_address = None
        self.company_id = None
        self.company_name = None
        self.company_phone = None
        self.courier_number = None
        self.create_time = None
        self.create_user_id = None
        self.express_name = None
        self.express_pay_method = None
        self.ext_param = None
        self.id = None
        self.ident_number = None
        self.invoice_content = None
        self.invoice_fee = None
        self.invoice_header = None
        self.invoice_header_type = None
        self.invoice_status = None
        self.invoice_type = None
        self.is_print = None
        self.is_send = None
        self.order_id = None
        self.recipient = None
        self.recipient_address = None
        self.recipient_city = None
        self.recipient_phone = None
        self.recipient_province = None
        self.recipient_town = None
        self.remark = None
        self.update_time = None
        self.update_user_id = None

class JdHjOrders(object):
    def __init__(self):
        self.create_date = None
        self.customer_address = None
        self.customer_phone = None
        self.hj_deal_fee = None
        self.hj_order_date = None
        self.hj_order_id = None
        self.id = None
        self.is_processed = None
        self.is_same = None
        self.jd_order_date = None
        self.jd_order_id = None
        self.jd_seller_price = None
        self.memo = None

class OrderArchiveDetailLog(object):
    def __init__(self):
        self.archive_batch_code = None
        self.archive_time = None
        self.create_time = None
        self.delete_time = None
        self.id = None
        self.is_archive = None
        self.is_delete = None
        self.is_to_es = None
        self.order_id = None
        self.to_es_time = None
        self.update_time = None

class OrderArchiveMasterLog(object):
    def __init__(self):
        self.archive_batch_code = None
        self.archive_order_quantity = None
        self.archive_status = None
        self.begin_order_id = None
        self.create_time = None
        self.delete_status = None
        self.end_order_id = None
        self.id = None
        self.to_es_status = None
        self.update_time = None

class OrderAssessment(object):
    def __init__(self):
        self.business_product_id = None
        self.deposit_discount_amount = None
        self.id = None
        self.manual_discount_amount = None
        self.multi_product_id = None
        self.new_product_id = None
        self.order_id = None
        self.product_id = None
        self.quantity = None
        self.share_card_fee = None
        self.share_card_income = None
        self.share_combine_fee = None
        self.share_cost = None
        self.share_coupon_fee = None
        self.share_coupon_income = None
        self.share_course_code_fee = None
        self.share_course_code_income = None
        self.share_discount_fee = None
        self.share_handling_fee = None
        self.share_income = None
        self.share_preincome = None
        self.share_purchase_xb = None
        self.share_recharge_xb = None
        self.share_reward_xb = None
        self.share_shipping_fee = None
        self.share_user_handling_fee = None
        self.share_vipcard_fee = None
        self.share_vipcard_income = None
        self.unit_price = None

class OrderBaseUser(object):
    def __init__(self):
        self.address = None
        self.answer = None
        self.bbs_user_id = None
        self.buy_times = None
        self.cellphone = None
        self.charge = None
        self.display_pwd = None
        self.email = None
        self.expired_date = None
        self.fee_mark = None
        self.froze_late_fee = None
        self.gender = None
        self.gold = None
        self.has_validate_cellphone = None
        self.icon_name = None
        self.id_card_num = None
        self.last_login_ip = None
        self.last_login_time = None
        self.late_fee = None
        self.lock_flag = None
        self.login_times = None
        self.phone = None
        self.question = None
        self.rank = None
        self.rank_mark = None
        self.reg_date = None
        self.reg_ip = None
        self.sina_weibo_account = None
        self.timestamp = None
        self.true_name = None
        self.user_custom_cata_list = None
        self.user_fav_cata_list = None
        self.user_id = None
        self.user_name = None
        self.user_pwd = None
        self.user_top_custom_cata_list = None
        self.veri_code = None
        self.vip_level = None
        self.vip_total_days = None
        self.zipcode = None

class OrderBusinessExtend(object):
    def __init__(self):
        self.business_org_code = None
        self.company_id = None
        self.create_time = None
        self.id = None
        self.key = None
        self.order_id = None
        self.values = None

class OrderCancelLog(object):
    def __init__(self):
        self.cancel_type = None
        self.create_date = None
        self.id = None
        self.ip = None
        self.operator_user_id = None
        self.operator_user_name = None
        self.order_id = None
        self.remark = None
        self.source_id = None
        self.status = None

class OrderCarriedForward(object):
    def __init__(self):
        self.company_id = None
        self.create_time = None
        self.create_user_id = None
        self.id = None
        self.income = None
        self.order_id = None
        self.preincome = None
        self.purchase_xb = None
        self.recharge_xb = None
        self.reward_xb = None
        self.xb_fee = None

class OrderCarriedForwardMulti(object):
    def __init__(self):
        self.business_id = None
        self.category_id = None
        self.company_id = None
        self.id = None
        self.income = None
        self.multi_product_id = None
        self.order_id = None
        self.preincome = None
        self.product_id = None
        self.product_type = None
        self.purchase_xb = None
        self.quantity = None
        self.recharge_xb = None
        self.reward_xb = None
        self.seller_id = None
        self.unit_price = None
        self.xb_fee = None

class OrderChangeLog(object):
    def __init__(self):
        self.create_time = None
        self.create_user_company_id = None
        self.create_user_id = None
        self.create_user_name = None
        self.id = None
        self.old_ship_to_name = None
        self.old_ship_to_zip = None
        self.order_id = None
        self.ship_to_name = None
        self.ship_to_zip = None
        self.update_time = None
        self.update_user_company_id = None
        self.update_user_id = None
        self.update_user_name = None
        self.user_id = None

class OrderConfig(object):
    def __init__(self):
        self.create_time = None
        self.create_user_id = None
        self.create_user_name = None
        self.id = None
        self.is_active = None
        self.is_delete = None
        self.key = None
        self.remark = None
        self.update_time = None
        self.update_user_id = None
        self.update_user_name = None
        self.value = None

class OrderCouponConsum(object):
    def __init__(self):
        self.company_id = None
        self.cost = None
        self.coupon_code = None
        self.coupon_discount = None
        self.coupon_fee = None
        self.coupon_income = None
        self.coupon_name = None
        self.coupon_type = None
        self.id = None
        self.order_id = None

class OrderDealMemo(object):
    def __init__(self):
        self.deal_date = None
        self.deal_memo = None
        self.deal_user = None
        self.deal_user_company_id = None
        self.id = None
        self.order_id = None

class OrderDeliver(object):
    def __init__(self):
        self.batch_id = None
        self.create_time = None
        self.delivery_failed_qty = None
        self.delivery_qty = None
        self.delivery_status = None
        self.id = None
        self.master_product_id = None
        self.order_id = None
        self.product_id = None
        self.product_type = None
        self.quantity = None
        self.update_time = None

class OrderDetail(object):
    def __init__(self):
        self.account_date = None
        self.batch_id = None
        self.business_id = None
        self.business_product_id = None
        self.category_id = None
        self.combine_discount_amount = None
        self.company_id = None
        self.coupon_code = None
        self.deposit_discount_amount = None
        self.discount_amount = None
        self.id = None
        self.is_master_product = None
        self.is_refunded = None
        self.manual_discount_amount = None
        self.nsource = None
        self.order_id = None
        self.point_discount = None
        self.product_cate = None
        self.product_cost = None
        self.product_id = None
        self.product_name = None
        self.product_type = None
        self.promotion_info = None
        self.quantity = None
        self.seller_id = None
        self.timestamp = None
        self.unit_price = None
        self.warehouse_id = None

class OrderDetailAttached(object):
    def __init__(self):
        self.company_id = None
        self.create_time = None
        self.create_user_company_id = None
        self.create_user_id = None
        self.id = None
        self.master_product_id = None
        self.order_id = None
        self.product_id = None
        self.update_time = None
        self.update_user_company_id = None
        self.update_user_id = None

class OrderDetailCoupon(object):
    def __init__(self):
        self.batch_id = None
        self.coupon_code = None
        self.coupon_type = None
        self.create_time = None
        self.id = None
        self.is_verificationed = None
        self.multi_product_id = None
        self.order_id = None
        self.product_id = None
        self.reference_verify_id = None
        self.update_time = None
        self.verify_time = None

class OrderDetailDiscount(object):
    def __init__(self):
        self.business_product_id = None
        self.company_id = None
        self.discount_amount = None
        self.discount_dec = None
        self.discount_xb = None
        self.end_time = None
        self.id = None
        self.order_id = None
        self.product_business_id = None
        self.product_id = None
        self.product_seller_id = None
        self.source_code = None
        self.source_id = None
        self.source_type = None
        self.start_time = None

class OrderDetailMulti(object):
    def __init__(self):
        self.add_to_cart_url = None
        self.batch_id = None
        self.business_id = None
        self.business_product_id = None
        self.category_id = None
        self.combine_discount_amount = None
        self.company_id = None
        self.coupon_code = None
        self.coupon_type = None
        self.create_time = None
        self.deposit_discount_amount = None
        self.discount_amount = None
        self.has_subtotal_value = None
        self.id = None
        self.manual_discount_amount = None
        self.multi_product_id = None
        self.order_id = None
        self.point_discount = None
        self.product_cost = None
        self.product_id = None
        self.product_name = None
        self.product_type = None
        self.quantity = None
        self.seller_id = None
        self.share_card_fee = None
        self.share_card_income = None
        self.share_coupon_fee = None
        self.share_coupon_income = None
        self.share_course_code_fee = None
        self.share_course_code_income = None
        self.share_discount_fee = None
        self.share_handling_fee = None
        self.share_income = None
        self.share_invite_code_fee = None
        self.share_preincome = None
        self.share_purchase_xb = None
        self.share_recharge_xb = None
        self.share_reward_xb = None
        self.share_shipping_fee = None
        self.share_user_handling_fee = None
        self.share_vipcard_fee = None
        self.share_vipcard_income = None
        self.sid = None
        self.ssid = None
        self.subtotal_card_fee = None
        self.subtotal_card_income = None
        self.subtotal_coupon_fee = None
        self.subtotal_coupon_income = None
        self.subtotal_course_code_fee = None
        self.subtotal_course_code_income = None
        self.subtotal_discount_amount = None
        self.subtotal_handling_fee = None
        self.subtotal_income = None
        self.subtotal_invite_code_fee = None
        self.subtotal_pre_income = None
        self.subtotal_purchase_xb = None
        self.subtotal_recharge_xb = None
        self.subtotal_reward_xb = None
        self.subtotal_shipping_fee = None
        self.subtotal_user_handling_fee = None
        self.subtotal_vipcard_fee = None
        self.subtotal_vipcard_income = None
        self.uid = None
        self.unit_price = None
        self.update_time = None
        self.warehouse_id = None

class OrderFromTop(object):
    def __init__(self):
        self.added_date = None
        self.ali_trade_no = None
        self.id = None
        self.import_order = None
        self.operator = None
        self.order_id = None
        self.platform_id = None
        self.taobao_token = None

class OrderHjUser(object):
    def __init__(self):
        self.bbs_user_id = None
        self.company_id = None
        self.department_id = None
        self.email = None
        self.id = None
        self.nick_name = None
        self.true_name = None
        self.user_name = None

class OrderIncome(object):
    def __init__(self):
        self.batch_id = None
        self.coupon_code = None
        self.income_date = None
        self.income_id = None
        self.income_type = None
        self.last_update_date = None
        self.master_product_id = None
        self.old_refund_id = None
        self.operater_type = None
        self.order_type = None
        self.product_name = None
        self.product_type = None
        self.quantity = None
        self.reference_income_id = None
        self.share_income_fee = None
        self.share_purchase_xb = None
        self.share_recharege_xb = None
        self.share_reward_xb = None
        self.source_order_id = None
        self.source_rma_id = None
        self.status = None
        self.sub_product_id = None
        self.user_id = None

class OrderIncomeStaging(object):
    def __init__(self):
        self.create_time = None
        self.id = None
        self.rma_id = None
        self.source_order_id = None
        self.status = None
        self.update_time = None

class OrderMaster(object):
    def __init__(self):
        self.ali_trade_no = None
        self.bank_code = None
        self.bill_date = None
        self.bill_no = None
        self.cancel_date = None
        self.cell_phone = None
        self.chest_fee = None
        self.city_id = None
        self.combine_fee = None
        self.company_id = None
        self.coupon_fee = None
        self.coupon_income = None
        self.create_time = None
        self.create_user_company_id = None
        self.create_user_id = None
        self.deal_fee = None
        self.deal_memo = None
        self.deal_user = None
        self.deliver_id = None
        self.delivery_result = None
        self.delivery_status = None
        self.deposit_discount_fee = None
        self.discount_fee = None
        self.email = None
        self.express = None
        self.express_id = None
        self.extend_bill_status = None
        self.fee_memo = None
        self.from_ip = None
        self.handling_fee = None
        self.hj_user_id = None
        self.income = None
        self.installment_number = None
        self.invite_code_fee = None
        self.is_active = None
        self.is_audit = None
        self.is_bill = None
        self.is_cancel = None
        self.is_child = None
        self.is_inside = None
        self.is_notify = None
        self.is_phone = None
        self.is_print = None
        self.is_test = None
        self.is_trace = None
        self.is_unusual = None
        self.is_valid = None
        self.manual_discount_fee = None
        self.mark = None
        self.msn = None
        self.notify_mark = None
        self.nsource = None
        self.operator_company_id = None
        self.operator_user_id = None
        self.order_date = None
        self.order_device_id = None
        self.order_id = None
        self.order_number = None
        self.order_type = None
        self.outer_trade_no = None
        self.parent_order_id = None
        self.pay_card_type = None
        self.pay_device_id = None
        self.pay_method = None
        self.payment_bank_discount = None
        self.phone_date = None
        self.platform_id = None
        self.point_fee = None
        self.pre_income = None
        self.province_id = None
        self.purchase_xb = None
        self.qq = None
        self.recharge_xb = None
        self.refer_source_id = None
        self.refer_url = None
        self.refund_type = None
        self.related_order_id = None
        self.reward_xb = None
        self.seller_id = None
        self.ship_date = None
        self.ship_flag = None
        self.ship_method = None
        self.ship_to_addr = None
        self.ship_to_city = None
        self.ship_to_country = None
        self.ship_to_name = None
        self.ship_to_phone = None
        self.ship_to_province = None
        self.ship_to_time = None
        self.ship_to_town = None
        self.ship_to_zip = None
        self.shipping_fee = None
        self.temp_order_version = None
        self.timestamp = None
        self.total_cost = None
        self.total_fee = None
        self.total_order_today = None
        self.town_id = None
        self.update_time = None
        self.update_user_company_id = None
        self.update_user_id = None
        self.user_coupon_id = None
        self.user_handling_fee = None
        self.user_id = None
        self.user_memo = None
        self.user_reg_date = None
        self.user_source = None
        self.user_title = None
        self.xb_fee = None

class OrderMessageLog(object):
    def __init__(self):
        self.id = None
        self.message_content = None
        self.message_id = None
        self.produce_id = None
        self.send_date_time = None
        self.send_machine_ip = None

class OrderPayInfo(object):
    def __init__(self):
        self.bank_code = None
        self.begin_time = None
        self.bill_amount = None
        self.child_order_id = None
        self.create_time = None
        self.create_user_id = None
        self.end_time = None
        self.ext_param = None
        self.id = None
        self.order_id = None
        self.order_type = None
        self.origin_order_id = None
        self.pay_channel = None
        self.pay_device_id = None
        self.pay_method = None
        self.pay_num = None
        self.pay_status = None
        self.pay_time = None
        self.pay_type = None
        self.purchase_xb = None
        self.recharge_xb = None
        self.remark = None
        self.reward_xb = None
        self.trans_seq_no = None
        self.update_time = None
        self.update_user_id = None
        self.xb_fee = None

class OrderProductGroupbuy(object):
    def __init__(self):
        self.a_360_cate = None
        self.a_360_display = None
        self.a_360_hot_bus_spot_name = None
        self.a_360_img = None
        self.a_360_latitude = None
        self.a_360_longitude = None
        self.a_360_merchant_addr = None
        self.a_360_merchant_name = None
        self.a_360_merchant_phone = None
        self.a_360_spent_end_time = None
        self.a_360_spent_start_time = None
        self.a_360_title = None
        self.admin_memo = None
        self.big_img_name = None
        self.bulo_display_img_url = None
        self.buy_only_once = None
        self.cate_id = None
        self.cate_idadmin = None
        self.class_id = None
        self.ctproduct_code = None
        self.display_by_bulo = None
        self.end_time = None
        self.free_buy_type = None
        self.full_num = None
        self.group_buy_price = None
        self.groupbuy_type = None
        self.has_notice_by_mail = None
        self.has_notice_by_sms = None
        self.id = None
        self.is_active = None
        self.is_free_by_count = None
        self.is_free_delivery = None
        self.is_hide = None
        self.is_new_version = None
        self.is_takeby_customer = None
        self.is_valid = None
        self.is_view = None
        self.keywords = None
        self.last_notice_time_mail = None
        self.last_notice_time_sms = None
        self.last_update_time = None
        self.list_price = None
        self.low_cate_id = None
        self.mark = None
        self.max_buy_amount = None
        self.mention = None
        self.mini_product_name = None
        self.prevision_img_name = None
        self.product_desc = None
        self.product_id = None
        self.product_name = None
        self.quantity = None
        self.related_coupon_batch = None
        self.related_coupon_batch_type = None
        self.related_income = None
        self.related_staff = None
        self.room_id = None
        self.short_product_name = None
        self.small_img_name = None
        self.sort_index = None
        self.start_time = None
        self.supplier_id = None
        self.supplier_type = None
        self.system_remark = None
        self.tags = None
        self.timeup_warning = None
        self.total_buy_amount = None
        self.touch_product_desc = None
        self.unit_cost = None
        self.unit_delivery_cost = None
        self.user_ce_hua = None
        self.user_ce_hua_id = None
        self.user_comment = None
        self.user_design_id = None
        self.user_tui_guang = None
        self.user_tui_guang_id = None
        self.user_wen_an = None
        self.user_wen_an_id = None
        self.virtual_buyer_amount = None

class OrderSplitIndex(object):
    def __init__(self):
        self.begin_order_id = None
        self.create_time = None
        self.database_index = None
        self.end_order_id = None
        self.id = None
        self.last_order_id = None
        self.table_index = None
        self.update_time = None

class OrderStageRetry(object):
    def __init__(self):
        self.create_time = None
        self.order_id = None
        self.retry_times = None
        self.stage = None
        self.status = None
        self.update_time = None

class OrderTester(object):
    def __init__(self):
        self.company_id = None
        self.hj_user_id = None
        self.id = None
        self.status = None
        self.user_id = None
        self.user_name = None

class OrderTracking(object):
    def __init__(self):
        self.add_to_cart_url = None
        self.app_id = None
        self.create_time = None
        self.device_id = None
        self.ext_param = None
        self.from_ip = None
        self.id = None
        self.order_department_id = None
        self.order_device_id = None
        self.order_id = None
        self.order_reason_id = None
        self.order_source_id = None
        self.pay_device_id = None
        self.refer_url = None
        self.reference_order_id = None
        self.rma_flag = None
        self.sales_channel_id = None
        self.sales_platform_id = None
        self.sid = None
        self.solution_code = None
        self.ssid = None
        self.swap_solution_code = None
        self.uid = None
        self.update_time = None

class OrderUserAddressLog(object):
    def __init__(self):
        self.address = None
        self.change_date = None
        self.create_time = None
        self.create_user_company_id = None
        self.create_user_id = None
        self.id = None
        self.old_address = None
        self.operator = None
        self.order_id = None
        self.shop_user_id = None
        self.user_id = None

class OrderUserPhoneLog(object):
    def __init__(self):
        self.change_date = None
        self.create_time = None
        self.create_user_company_id = None
        self.create_user_id = None
        self.id = None
        self.old_phone = None
        self.operator = None
        self.order_id = None
        self.phone = None
        self.shop_user_id = None
        self.type = None
        self.user_id = None

class OrderVirtualDeliver(object):
    def __init__(self):
        self.create_time = None
        self.id = None
        self.order_deliver_id = None
        self.order_id = None
        self.send_code = None
        self.update_time = None

class TempOrderMetaData(object):
    def __init__(self):
        self.hj_user_id = None
        self.id = None
        self.product_id = None
        self.user_domain = None

class TempOrderSellerCc(object):
    def __init__(self):
        self.id = None
        self.seller_id = None

class TempOrderUserCc(object):
    def __init__(self):
        self.hj_user_id = None
        self.id = None

class TradeControl(object):
    def __init__(self):
        self.compensate_action = None
        self.create_time = None
        self.create_user_id = None
        self.has_cancel = None
        self.has_commit = None
        self.has_compensate = None
        self.has_freeze = None
        self.id = None
        self.order_id = None
        self.trade_number = None
        self.update_time = None
        self.update_user_id = None

class TradeResourceStatus(object):
    def __init__(self):
        self.cancel_time = None
        self.commit_time = None
        self.create_time = None
        self.create_user_id = None
        self.freeze_time = None
        self.has_cancel = None
        self.has_commit = None
        self.has_freeze = None
        self.id = None
        self.order_id = None
        self.resource_code = None
        self.resource_type = None
        self.retry_count = None
        self.retry_time = None
        self.trade_number = None
        self.update_time = None
        self.update_user_id = None

class UserAddress(object):
    def __init__(self):
        self.city_id = None
        self.create_time = None
        self.create_user_company_id = None
        self.create_user_id = None
        self.id = None
        self.is_default = None
        self.msn = None
        self.province_id = None
        self.qq = None
        self.ship_to_address = None
        self.ship_to_cellphone = None
        self.ship_to_email = None
        self.ship_to_name = None
        self.ship_to_phone = None
        self.ship_to_zip = None
        self.shop_user_id = None
        self.town_id = None
        self.update_time = None
        self.update_user_company_id = None
        self.update_user_id = None
