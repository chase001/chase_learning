from peewee import *

database = MySQLDatabase('test', **{'charset': 'utf8', 'use_unicode': True, 'host': '10.40.6.26', 'user': 'gb_m_user', 'password': 'fEtWqVMzBC'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Q4Jira需求统计(BaseModel):
    时间上线时间 = DateTimeField(null=True)
    是否延期 = IntegerField(null=True)
    期望完成时间 = DateTimeField(null=True)
    状态 = CharField(null=True)
    需求名称 = CharField(null=True)
    需求类型 = CharField(null=True)

    class Meta:
        table_name = 'Q4-jira需求统计'

class DirectSkuGuidePrice201612301339(BaseModel):
    goods_id = IntegerField()
    id = IntegerField(constraints=[SQL("DEFAULT 0")])
    max_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    min_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    price = DecimalField(constraints=[SQL("DEFAULT 0.00")])

    class Meta:
        table_name = 'direct_sku_guide_price_201612301339'
        primary_key = False

class EloadCategory(BaseModel):
    brand_date_from = CharField(null=True)
    brand_date_to = CharField(null=True)
    brand_key_word = CharField(null=True)
    cat_banner = CharField(constraints=[SQL("DEFAULT ''")])
    cat_cont = TextField(null=True)
    cat_desc = CharField(constraints=[SQL("DEFAULT ''")])
    cat_id = AutoField()
    cat_name = CharField(constraints=[SQL("DEFAULT ''")])
    cat_pic = CharField(null=True)
    cat_pic_small = CharField(null=True)
    category_hot_search_keywords = TextField()
    category_template = IntegerField(constraints=[SQL("DEFAULT 0")])
    chuhuo_qujian = CharField(null=True)
    cnum = IntegerField(constraints=[SQL("DEFAULT 0")])
    custom_size = IntegerField(constraints=[SQL("DEFAULT 0")])
    custom_size_price = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    deals_order_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    default_order = CharField(constraints=[SQL("DEFAULT ''")])
    default_sort_by = CharField(constraints=[SQL("DEFAULT 'hot'")], null=True)
    grade = CharField(constraints=[SQL("DEFAULT ''")])
    hot_sort = CharField(null=True)
    is_deals_state = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_free_shipping_cate = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_home = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_home_under = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_linkshow = IntegerField()
    is_login = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_show = IntegerField(constraints=[SQL("DEFAULT 1")])
    is_suit = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_suit_type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_traking_number = IntegerField(constraints=[SQL("DEFAULT 0")])
    keywords = CharField(constraints=[SQL("DEFAULT ''")])
    level = IntegerField()
    like_sort = CharField(null=True)
    low_price_sort = CharField(null=True)
    measure_unit = CharField(constraints=[SQL("DEFAULT ''")])
    mobile_cat_pic = CharField(constraints=[SQL("DEFAULT ''")])
    new_sort = CharField(null=True)
    node = CharField()
    parent_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    points_percent = IntegerField(constraints=[SQL("DEFAULT 0")])
    points_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    price_sort = CharField(null=True)
    review_count = IntegerField()
    reviews_sort = CharField(null=True)
    seo_title = CharField()
    shipping_method = CharField(constraints=[SQL("DEFAULT '3,1,2,4'")])
    size_converter = IntegerField(constraints=[SQL("DEFAULT 1")])
    sort_order = IntegerField(constraints=[SQL("DEFAULT 0")])
    template_file = CharField(constraints=[SQL("DEFAULT ''")])
    template_id = IntegerField()
    up_price_sort = CharField(null=True)
    url_title = CharField()
    zhekou = CharField(constraints=[SQL("DEFAULT ''")])
    zhuijia_price = CharField(null=True)

    class Meta:
        table_name = 'eload_category'

class EloadCategoryBak1019(BaseModel):
    brand_date_from = CharField(null=True)
    brand_date_to = CharField(null=True)
    brand_key_word = CharField(null=True)
    cat_banner = CharField(constraints=[SQL("DEFAULT ''")])
    cat_cont = TextField(null=True)
    cat_desc = CharField(constraints=[SQL("DEFAULT ''")])
    cat_id = AutoField()
    cat_name = CharField(constraints=[SQL("DEFAULT ''")])
    cat_pic = CharField(null=True)
    cat_pic_small = CharField(null=True)
    category_hot_search_keywords = TextField()
    category_template = IntegerField(constraints=[SQL("DEFAULT 0")])
    chuhuo_qujian = CharField(null=True)
    cnum = IntegerField(constraints=[SQL("DEFAULT 0")])
    custom_size = IntegerField(constraints=[SQL("DEFAULT 0")])
    custom_size_price = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    deals_order_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    default_order = CharField(constraints=[SQL("DEFAULT ''")])
    default_sort_by = CharField(constraints=[SQL("DEFAULT 'hot'")], null=True)
    grade = CharField(constraints=[SQL("DEFAULT ''")])
    hot_sort = CharField(null=True)
    is_deals_state = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_free_shipping_cate = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_home = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_home_under = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_linkshow = IntegerField()
    is_login = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_show = IntegerField(constraints=[SQL("DEFAULT 1")])
    is_suit = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_suit_type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_traking_number = IntegerField(constraints=[SQL("DEFAULT 0")])
    keywords = CharField(constraints=[SQL("DEFAULT ''")])
    level = IntegerField()
    like_sort = CharField(null=True)
    low_price_sort = CharField(null=True)
    measure_unit = CharField(constraints=[SQL("DEFAULT ''")])
    mobile_cat_pic = CharField(constraints=[SQL("DEFAULT ''")])
    new_sort = CharField(null=True)
    node = CharField()
    parent_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    points_percent = IntegerField(constraints=[SQL("DEFAULT 0")])
    points_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    price_sort = CharField(null=True)
    review_count = IntegerField()
    reviews_sort = CharField(null=True)
    seo_title = CharField()
    shipping_method = CharField(constraints=[SQL("DEFAULT '3,1,2,4'")])
    size_converter = IntegerField(constraints=[SQL("DEFAULT 1")])
    sort_order = IntegerField(constraints=[SQL("DEFAULT 0")])
    template_file = CharField(constraints=[SQL("DEFAULT ''")])
    template_id = IntegerField()
    up_price_sort = CharField(null=True)
    url_title = CharField()
    zhekou = CharField(constraints=[SQL("DEFAULT ''")])
    zhuijia_price = CharField(null=True)

    class Meta:
        table_name = 'eload_category_bak1019'

class EloadCategoryCopy(BaseModel):
    brand_date_from = CharField(null=True)
    brand_date_to = CharField(null=True)
    brand_key_word = CharField(null=True)
    cat_banner = CharField(constraints=[SQL("DEFAULT ''")])
    cat_cont = TextField(null=True)
    cat_desc = CharField(constraints=[SQL("DEFAULT ''")])
    cat_id = AutoField()
    cat_name = CharField(constraints=[SQL("DEFAULT ''")])
    cat_pic = CharField(null=True)
    cat_pic_small = CharField(null=True)
    category_hot_search_keywords = TextField()
    category_template = IntegerField(constraints=[SQL("DEFAULT 0")])
    chuhuo_qujian = CharField(null=True)
    cnum = IntegerField(constraints=[SQL("DEFAULT 0")])
    custom_size = IntegerField(constraints=[SQL("DEFAULT 0")])
    custom_size_price = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    deals_order_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    default_order = CharField(constraints=[SQL("DEFAULT ''")])
    default_sort_by = CharField(constraints=[SQL("DEFAULT 'hot'")], null=True)
    grade = CharField(constraints=[SQL("DEFAULT ''")])
    hot_sort = CharField(null=True)
    is_deals_state = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_free_shipping_cate = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_home = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_home_under = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_linkshow = IntegerField()
    is_login = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_show = IntegerField(constraints=[SQL("DEFAULT 1")])
    is_suit = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_suit_type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_traking_number = IntegerField(constraints=[SQL("DEFAULT 0")])
    keywords = CharField(constraints=[SQL("DEFAULT ''")])
    level = IntegerField()
    like_sort = CharField(null=True)
    low_price_sort = CharField(null=True)
    measure_unit = CharField(constraints=[SQL("DEFAULT ''")])
    mobile_cat_pic = CharField(constraints=[SQL("DEFAULT ''")])
    new_sort = CharField(null=True)
    node = CharField()
    parent_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    points_percent = IntegerField(constraints=[SQL("DEFAULT 0")])
    points_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    price_sort = CharField(null=True)
    review_count = IntegerField()
    reviews_sort = CharField(null=True)
    seo_title = CharField()
    shipping_method = CharField(constraints=[SQL("DEFAULT '3,1,2,4'")])
    size_converter = IntegerField(constraints=[SQL("DEFAULT 1")])
    sort_order = IntegerField(constraints=[SQL("DEFAULT 0")])
    template_file = CharField(constraints=[SQL("DEFAULT ''")])
    template_id = IntegerField()
    up_price_sort = CharField(null=True)
    url_title = CharField()
    zhekou = CharField(constraints=[SQL("DEFAULT ''")])
    zhuijia_price = CharField(null=True)

    class Meta:
        table_name = 'eload_category_copy'

class EloadCategoryMutiLang(BaseModel):
    cat_cont = TextField(null=True)
    cat_desc = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    cat_id = IntegerField()
    cat_name = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    keywords = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    lang = CharField(constraints=[SQL("DEFAULT ''")])
    seo_title = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    url_title_lang = CharField(constraints=[SQL("DEFAULT ''")], null=True)

    class Meta:
        table_name = 'eload_category_muti_lang'
        indexes = (
            (('cat_id', 'lang'), True),
        )
        primary_key = CompositeKey('cat_id', 'lang')

class EloadCategoryMutiLang1028Bak(BaseModel):
    cat_cont = TextField(null=True)
    cat_desc = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    cat_id = IntegerField()
    cat_name = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    keywords = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    lang = CharField(constraints=[SQL("DEFAULT ''")])
    seo_title = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    url_title_lang = CharField(constraints=[SQL("DEFAULT ''")], null=True)

    class Meta:
        table_name = 'eload_category_muti_lang_1028bak'
        indexes = (
            (('cat_id', 'lang'), True),
        )
        primary_key = CompositeKey('cat_id', 'lang')

class EloadCategoryMutiLang27(BaseModel):
    cat_cont = TextField(null=True)
    cat_desc = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    cat_id = IntegerField()
    cat_name = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    keywords = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    lang = CharField(constraints=[SQL("DEFAULT ''")])
    seo_title = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    url_title_lang = CharField(constraints=[SQL("DEFAULT ''")], null=True)

    class Meta:
        table_name = 'eload_category_muti_lang_27'
        indexes = (
            (('cat_id', 'lang'), True),
        )
        primary_key = CompositeKey('cat_id', 'lang')

class EloadCategoryMutiLangBak1019(BaseModel):
    cat_cont = TextField(null=True)
    cat_desc = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    cat_id = IntegerField()
    cat_name = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    keywords = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    lang = CharField(constraints=[SQL("DEFAULT ''")])
    seo_title = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    url_title_lang = CharField(constraints=[SQL("DEFAULT ''")], null=True)

    class Meta:
        table_name = 'eload_category_muti_lang_bak1019'
        indexes = (
            (('cat_id', 'lang'), True),
        )
        primary_key = CompositeKey('cat_id', 'lang')

class EloadExchangeActive(BaseModel):
    activetype = IntegerField(constraints=[SQL("DEFAULT 1")])
    brand_name = CharField()
    cat_id = TextField()
    etime = IntegerField()
    links = CharField()
    main_goods_sn = TextField()
    max_number = IntegerField()
    name = CharField()
    seo_desc = CharField()
    seo_title = CharField()
    stime = IntegerField()
    wid = IntegerField()

    class Meta:
        table_name = 'eload_exchange_active'

class EloadExchangeGoods(BaseModel):
    active_id = IntegerField(index=True)
    exchange_price = DecimalField()
    goods_id = IntegerField()
    goods_name = CharField()
    goods_name_lang = TextField()
    goods_sn = CharField(index=True)
    goods_thumb = CharField()
    ladder_price = DecimalField()
    shop_price = DecimalField()
    sort_label = IntegerField(constraints=[SQL("DEFAULT 0")])
    stock = IntegerField()
    stock_use = IntegerField(constraints=[SQL("DEFAULT 0")])
    url = CharField()

    class Meta:
        table_name = 'eload_exchange_goods'

class EloadGoods1(BaseModel):
    link = CharField(null=True)
    sku = CharField(constraints=[SQL("DEFAULT ''")], primary_key=True)

    class Meta:
        table_name = 'eload_goods_1'

class EloadGoods2(BaseModel):
    link = CharField(null=True)
    sku = CharField(constraints=[SQL("DEFAULT ''")], primary_key=True)

    class Meta:
        table_name = 'eload_goods_2'

class EloadGoods3(BaseModel):
    gmv = CharField(column_name='GMV', null=True)
    sku = CharField(column_name='SKU', null=True)
    site = CharField(null=True)

    class Meta:
        table_name = 'eload_goods_3'
        primary_key = False

class EloadGoodsAttrBak1019(BaseModel):
    attr_goods_sn = CharField(index=True, null=True)
    attr_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    attr_price = CharField(constraints=[SQL("DEFAULT ''")])
    attr_value = TextField()
    goods_attr_id = AutoField()
    goods_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)

    class Meta:
        table_name = 'eload_goods_attr_bak1019'

class EloadGoodsBak1019(BaseModel):
    activity_list = CharField(constraints=[SQL("DEFAULT ''")])
    add_time = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    add_user = CharField(null=True)
    attention_num = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cat_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    chuhuo_price = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    click_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    color = CharField(null=True)
    daydeal_price = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    daydeal_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    daydeal_time_end = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    daydeal_time_start = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    details_keyword = TextField(null=True)
    goods_brief = TextField(null=True)
    goods_desc = TextField()
    goods_grid = CharField(null=True)
    goods_id = AutoField()
    goods_img = CharField(constraints=[SQL("DEFAULT ''")])
    goods_name = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    goods_name_style = CharField(constraints=[SQL("DEFAULT '+'")])
    goods_number = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    goods_search_attr = TextField(null=True)
    goods_sn = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    goods_sn_back = CharField(null=True)
    goods_sn_old = CharField(constraints=[SQL("DEFAULT ''")])
    goods_thumb = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    goods_thumb_220 = CharField(constraints=[SQL("DEFAULT ''")])
    goods_title = CharField(index=True, null=True)
    goods_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    goods_upc = CharField(index=True, null=True)
    goods_volume_weight = DecimalField(constraints=[SQL("DEFAULT 0.000")])
    goods_weight = DecimalField(constraints=[SQL("DEFAULT 0.000")], index=True)
    group_goods_id = IntegerField(index=True)
    img_type = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    is_alone_sale = IntegerField(constraints=[SQL("DEFAULT 1")], index=True)
    is_best = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    is_bighot = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_cool = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    is_daydeal = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_delete = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_dinghuo_goods = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_direct_sale_off = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_erhot = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_free_shipping = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    is_fun = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    is_hold_price = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_home = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_hot = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    is_login = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_new = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    is_new_sn = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_on_sale = IntegerField(constraints=[SQL("DEFAULT 1")], index=True)
    is_ping = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_promote = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    is_seo_new = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_show_alone = IntegerField(constraints=[SQL("DEFAULT 2")])
    keywords = TextField(null=True)
    last_update = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    m_status = IntegerField(constraints=[SQL("DEFAULT 1")], index=True)
    market_price = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    new_sign = IntegerField(constraints=[SQL("DEFAULT 0")])
    original_img = CharField(constraints=[SQL("DEFAULT ''")])
    peijian_price = DecimalField(null=True)
    point_rate = DecimalField(constraints=[SQL("DEFAULT 1.0")], index=True, null=True)
    presale_date_from = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    presale_date_to = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    promote_end_date = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    promote_lv = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    promote_price = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    promote_start_date = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    refresh_data = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sale_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    sale_number = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    seller_note = TextField()
    shop_price = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    shop_price_backup = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    size = CharField(null=True)
    sort_order = IntegerField(constraints=[SQL("DEFAULT 99")], index=True)
    sync_sku_to_gb = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    update_user = CharField(null=True)
    url_title = CharField(null=True)
    warehouse_code = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    warn_number = IntegerField(constraints=[SQL("DEFAULT 1")])
    week2sale = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)

    class Meta:
        table_name = 'eload_goods_bak1019'
        indexes = (
            (('is_delete', 'is_on_sale'), False),
            (('is_login', 'is_delete', 'is_alone_sale'), False),
        )

class EloadGoodsCatBak1019(BaseModel):
    cat_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    goods_id = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'eload_goods_cat_bak1019'
        indexes = (
            (('goods_id', 'cat_id'), True),
        )
        primary_key = CompositeKey('cat_id', 'goods_id')

class EloadGoodsDeBak1019(BaseModel):
    goods_brief = TextField(null=True)
    goods_desc = TextField(null=True)
    goods_id = IntegerField(index=True)
    goods_name = CharField(null=True)
    goods_search_attr = TextField(null=True)
    goods_title = CharField(null=True)
    is_ping = IntegerField(constraints=[SQL("DEFAULT 0")])
    keywords = TextField(null=True)
    phone_attr_table = TextField(null=True)
    phone_size_table = TextField(null=True)
    relate_size_chart = TextField(null=True)
    seller_note = CharField(null=True)
    seo_cannonical = CharField(null=True)
    seo_description = CharField(null=True)
    seo_title = CharField(null=True)
    size_chart = TextField(null=True)
    sub_title = CharField(null=True)
    update_time = IntegerField()
    url_title_lang = CharField(constraints=[SQL("DEFAULT ''")], null=True)

    class Meta:
        table_name = 'eload_goods_de_bak1019'
        primary_key = False

class EloadGoodsEsBak1019(BaseModel):
    goods_brief = TextField(null=True)
    goods_desc = TextField(null=True)
    goods_id = IntegerField(index=True)
    goods_name = CharField(null=True)
    goods_search_attr = TextField(null=True)
    goods_title = CharField(null=True)
    is_ping = IntegerField(constraints=[SQL("DEFAULT 0")])
    keywords = TextField(null=True)
    phone_attr_table = TextField(null=True)
    phone_size_table = TextField(null=True)
    relate_size_chart = TextField(null=True)
    seller_note = CharField(null=True)
    seo_cannonical = CharField(null=True)
    seo_description = CharField(null=True)
    seo_title = CharField(null=True)
    size_chart = TextField(null=True)
    sub_title = CharField(null=True)
    update_time = IntegerField()
    url_title_lang = CharField(constraints=[SQL("DEFAULT ''")], null=True)

    class Meta:
        table_name = 'eload_goods_es_bak1019'
        primary_key = False

class EloadGoodsFrBak1019(BaseModel):
    goods_brief = TextField(null=True)
    goods_desc = TextField(null=True)
    goods_id = IntegerField(index=True)
    goods_name = CharField(null=True)
    goods_search_attr = TextField(null=True)
    goods_title = CharField(null=True)
    is_ping = IntegerField(constraints=[SQL("DEFAULT 0")])
    keywords = TextField(null=True)
    phone_attr_table = TextField(null=True)
    phone_size_table = TextField(null=True)
    relate_size_chart = TextField(null=True)
    seller_note = CharField(null=True)
    seo_cannonical = CharField(null=True)
    seo_description = CharField(null=True)
    seo_title = CharField(null=True)
    size_chart = TextField(null=True)
    sub_title = CharField(null=True)
    update_time = IntegerField()
    url_title_lang = CharField(constraints=[SQL("DEFAULT ''")], null=True)

    class Meta:
        table_name = 'eload_goods_fr_bak1019'
        primary_key = False

class EloadGoodsItBak1019(BaseModel):
    goods_brief = TextField(null=True)
    goods_desc = TextField(null=True)
    goods_id = IntegerField(index=True)
    goods_name = CharField(null=True)
    goods_search_attr = TextField(null=True)
    goods_title = CharField(null=True)
    is_ping = IntegerField(constraints=[SQL("DEFAULT 0")])
    keywords = TextField(null=True)
    phone_attr_table = TextField(null=True)
    phone_size_table = TextField(null=True)
    relate_size_chart = TextField(null=True)
    seller_note = CharField(null=True)
    seo_cannonical = CharField(null=True)
    seo_description = CharField(null=True)
    seo_title = CharField(null=True)
    size_chart = TextField(null=True)
    sub_title = CharField(null=True)
    update_time = IntegerField()
    url_title_lang = CharField(constraints=[SQL("DEFAULT ''")], null=True)

    class Meta:
        table_name = 'eload_goods_it_bak1019'
        primary_key = False

class EloadGoodsPtBak1019(BaseModel):
    goods_brief = TextField(null=True)
    goods_desc = TextField(null=True)
    goods_id = IntegerField(index=True)
    goods_name = CharField(null=True)
    goods_search_attr = TextField(null=True)
    goods_title = CharField(null=True)
    is_ping = IntegerField(constraints=[SQL("DEFAULT 0")])
    keywords = TextField(null=True)
    phone_attr_table = TextField(null=True)
    phone_size_table = TextField(null=True)
    relate_size_chart = TextField(null=True)
    seller_note = CharField(null=True)
    seo_cannonical = CharField(null=True)
    seo_description = CharField(null=True)
    seo_title = CharField(null=True)
    size_chart = TextField(null=True)
    sub_title = CharField(null=True)
    update_time = IntegerField()
    url_title_lang = CharField(constraints=[SQL("DEFAULT ''")], null=True)

    class Meta:
        table_name = 'eload_goods_pt_bak1019'
        primary_key = False

class EloadGoodsRuBak1019(BaseModel):
    goods_brief = TextField(null=True)
    goods_desc = TextField(null=True)
    goods_id = IntegerField(index=True)
    goods_name = CharField(null=True)
    goods_search_attr = TextField(null=True)
    goods_title = CharField(null=True)
    is_ping = IntegerField(constraints=[SQL("DEFAULT 0")])
    keywords = TextField(null=True)
    phone_attr_table = TextField(null=True)
    phone_size_table = TextField(null=True)
    relate_size_chart = TextField(null=True)
    seller_note = CharField(null=True)
    seo_cannonical = CharField(null=True)
    seo_description = CharField(null=True)
    seo_title = CharField(null=True)
    size_chart = TextField(null=True)
    sub_title = CharField(null=True)
    update_time = IntegerField()
    url_title_lang = CharField(constraints=[SQL("DEFAULT ''")], null=True)

    class Meta:
        table_name = 'eload_goods_ru_bak1019'
        primary_key = False

class EloadMailTemplatesBr(BaseModel):
    template_content = TextField()
    template_id = IntegerField()
    template_subject = CharField()

    class Meta:
        table_name = 'eload_mail_templates_br'
        primary_key = False

class EloadOsGoodsBak1019(BaseModel):
    add_time = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    app_comment = CharField(constraints=[SQL("DEFAULT ''")])
    app_last_updater = IntegerField(constraints=[SQL("DEFAULT 0")])
    app_order_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    app_update_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    cart_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_hold_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    delivery_price = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    first_on_sale = IntegerField(constraints=[SQL("DEFAULT 0")])
    first_trip_price = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)
    free_division_id = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    free_division_id_copy = CharField(null=True)
    freeshipping_division_id = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    freeshipping_division_id_copy = CharField(null=True)
    freeshipping_fee = DecimalField(null=True)
    from_wid = IntegerField(constraints=[SQL("DEFAULT 0")])
    goods_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    goods_number = IntegerField(constraints=[SQL("DEFAULT 0")])
    handle_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    has_limit_country = IntegerField(constraints=[SQL("DEFAULT 0")])
    hold_end_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    hold_start_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_on_sale = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    is_promote = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_third_clearance = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_warehouse_price = IntegerField(constraints=[SQL("DEFAULT 1")])
    last_update = IntegerField(constraints=[SQL("DEFAULT 0")])
    limit_coutry = TextField(null=True)
    m_status = IntegerField(constraints=[SQL("DEFAULT 1")])
    market_price = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    mobile_date_from = IntegerField(constraints=[SQL("DEFAULT 0")])
    mobile_date_to = IntegerField(constraints=[SQL("DEFAULT 0")])
    mobile_price = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    pre_hour = IntegerField(constraints=[SQL("DEFAULT 0")])
    pre_notice = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    pre_order_number = IntegerField(constraints=[SQL("DEFAULT 0")])
    pre_price = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    pre_time_price = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    presale_date_from = IntegerField(constraints=[SQL("DEFAULT 0")])
    presale_date_to = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    presale_type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    promote_bz = CharField(constraints=[SQL("DEFAULT ''")])
    promote_end_date = IntegerField(constraints=[SQL("DEFAULT 0")])
    promote_lv = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    promote_price = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    promote_start_date = IntegerField(constraints=[SQL("DEFAULT 0")])
    refresh_data = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sale_mark = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    shop_price = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    shot_comment = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    stock_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    sync_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    update_user = CharField(constraints=[SQL("DEFAULT ''")])
    user_limit = IntegerField(constraints=[SQL("DEFAULT 0")])
    wid = IntegerField(constraints=[SQL("DEFAULT 0")])
    zhuijia_price = DecimalField(constraints=[SQL("DEFAULT 0.00")], null=True)

    class Meta:
        table_name = 'eload_os_goods_bak1019'
        indexes = (
            (('goods_id', 'wid'), True),
            (('presale_date_from', 'wid', 'is_on_sale', 'presale_type'), False),
            (('wid', 'has_limit_country'), False),
            (('wid', 'is_promote'), False),
            (('wid', 'limit_coutry'), False),
            (('wid', 'promote_start_date', 'promote_end_date'), False),
        )

class EloadSearchAttrAllLangBak1019(BaseModel):
    attr_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    attr_type = CharField(null=True)
    attr_update_time = CharField(null=True)
    en_attr_value = CharField()
    lang = CharField()
    lang_attr_value = CharField()

    class Meta:
        table_name = 'eload_search_attr_all_lang_bak1019'

class EloadSearchAttrBak1019(BaseModel):
    odr = IntegerField()
    search_attr_brief = CharField(constraints=[SQL("DEFAULT ''")])
    search_attr_id = AutoField()
    search_attr_name = CharField(constraints=[SQL("DEFAULT ''")])
    search_value = TextField()
    template_id = IntegerField()

    class Meta:
        table_name = 'eload_search_attr_bak1019'

class EloadSpecial(BaseModel):
    banner = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    banner_desc = TextField()
    bg_color = CharField(constraints=[SQL("DEFAULT ''")])
    bg_pic = CharField(constraints=[SQL("DEFAULT ''")])
    coupon = CharField(constraints=[SQL("DEFAULT ''")])
    coupon_point = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_switch = IntegerField(constraints=[SQL("DEFAULT 0")])
    css_path = CharField(constraints=[SQL("DEFAULT ''")])
    description = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    keyword = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    lang_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    m_banner = CharField(constraints=[SQL("DEFAULT ''")])
    memo = CharField(constraints=[SQL("DEFAULT ''")])
    module = CharField(constraints=[SQL("DEFAULT ''")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    new_template = IntegerField(constraints=[SQL("DEFAULT 0")])
    point_end_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    point_start_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    remark = CharField(null=True)
    share_img = CharField(null=True)
    special_id = AutoField()
    temp = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    title = CharField(constraints=[SQL("DEFAULT ''")], null=True)

    class Meta:
        table_name = 'eload_special'

class EloadSpecialBr(BaseModel):
    banner_br = CharField(constraints=[SQL("DEFAULT ''")])
    banner_desc_br = TextField()
    bg_color_br = CharField(constraints=[SQL("DEFAULT ''")])
    bg_pic_br = CharField(constraints=[SQL("DEFAULT ''")])
    br_id = AutoField()
    css_path_br = CharField()
    description_br = CharField(constraints=[SQL("DEFAULT ''")])
    keyword_br = CharField(constraints=[SQL("DEFAULT ''")])
    m_banner_br = CharField(constraints=[SQL("DEFAULT ''")])
    remark_br = CharField(constraints=[SQL("DEFAULT ''")])
    share_img_br = CharField(constraints=[SQL("DEFAULT ''")])
    special_id = IntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    title_br = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'eload_special_br'

class EloadSpecialDe(BaseModel):
    banner_de = CharField(null=True)
    banner_desc_de = TextField()
    bg_color_de = CharField(constraints=[SQL("DEFAULT ''")])
    bg_pic_de = CharField(constraints=[SQL("DEFAULT ''")])
    css_path_de = CharField()
    de_id = AutoField()
    description_de = CharField(null=True)
    keyword_de = CharField(null=True)
    m_banner_de = CharField()
    remark_de = CharField(null=True)
    share_img_de = CharField(null=True)
    special_id = IntegerField(unique=True)
    title_de = CharField(null=True)

    class Meta:
        table_name = 'eload_special_de'

class EloadSpecialEs(BaseModel):
    banner_desc_es = TextField()
    banner_es = CharField(null=True)
    bg_color_es = CharField(constraints=[SQL("DEFAULT ''")])
    bg_pic_es = CharField(constraints=[SQL("DEFAULT ''")])
    css_path_es = CharField()
    description_es = CharField(null=True)
    es_id = AutoField()
    keyword_es = CharField(null=True)
    m_banner_es = CharField()
    remark_es = CharField(null=True)
    share_img_es = CharField(null=True)
    special_id = IntegerField(unique=True)
    title_es = CharField(null=True)

    class Meta:
        table_name = 'eload_special_es'

class EloadSpecialFr(BaseModel):
    banner_desc_fr = TextField()
    banner_fr = CharField(constraints=[SQL("DEFAULT ''")])
    bg_color_fr = CharField(constraints=[SQL("DEFAULT ''")])
    bg_pic_fr = CharField(constraints=[SQL("DEFAULT ''")])
    css_path_fr = CharField()
    description_fr = CharField(constraints=[SQL("DEFAULT ''")])
    fr_id = AutoField()
    keyword_fr = CharField(constraints=[SQL("DEFAULT ''")])
    m_banner_fr = CharField(constraints=[SQL("DEFAULT ''")])
    remark_fr = CharField(constraints=[SQL("DEFAULT ''")])
    share_img_fr = CharField(constraints=[SQL("DEFAULT ''")])
    special_id = IntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    title_fr = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'eload_special_fr'

class EloadSpecialIt(BaseModel):
    banner_desc_it = TextField()
    banner_it = CharField(null=True)
    bg_color_it = CharField(constraints=[SQL("DEFAULT ''")])
    bg_pic_it = CharField(constraints=[SQL("DEFAULT ''")])
    css_path_it = CharField()
    description_it = CharField(null=True)
    it_id = AutoField()
    keyword_it = CharField(null=True)
    m_banner_it = CharField()
    remark_it = CharField(null=True)
    share_img_it = CharField(null=True)
    special_id = IntegerField(unique=True)
    title_it = CharField(null=True)

    class Meta:
        table_name = 'eload_special_it'

class EloadSpecialPositionBr(BaseModel):
    bottom_code_br = TextField(null=True)
    but_nav_code_br = TextField(null=True)
    count_down_br = IntegerField(constraints=[SQL("DEFAULT 0")])
    discount_mark_br = IntegerField(constraints=[SQL("DEFAULT 1")])
    left_brif_br = IntegerField(constraints=[SQL("DEFAULT 0")])
    m_name_br = CharField(constraints=[SQL("DEFAULT ''")])
    memo_br = CharField(constraints=[SQL("DEFAULT ''")])
    muti_name_br = CharField(constraints=[SQL("DEFAULT ''")])
    name_br = CharField(constraints=[SQL("DEFAULT ''")])
    nav_name_br = CharField()
    position_id = AutoField()
    show_market_br = IntegerField(constraints=[SQL("DEFAULT 1")])
    special_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    special_position_id_br = IntegerField()
    top_code_br = TextField(null=True)
    top_nav_code_br = TextField(null=True)
    url_br = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'eload_special_position_br'

class EloadSpecialPositionDe(BaseModel):
    bottom_code_de = TextField()
    but_nav_code_de = TextField()
    count_down_de = IntegerField(constraints=[SQL("DEFAULT 0")])
    discount_mark_de = IntegerField(constraints=[SQL("DEFAULT 1")])
    left_brif_de = IntegerField(constraints=[SQL("DEFAULT 0")])
    m_name_de = CharField(constraints=[SQL("DEFAULT ''")])
    memo_de = CharField()
    muti_name_de = CharField(constraints=[SQL("DEFAULT ''")])
    name_de = CharField(constraints=[SQL("DEFAULT ''")])
    nav_name_de = CharField()
    position_id = AutoField()
    show_market_de = IntegerField(constraints=[SQL("DEFAULT 1")])
    special_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    special_position_id_de = IntegerField()
    top_code_de = TextField()
    top_nav_code_de = TextField()
    url_de = CharField()

    class Meta:
        table_name = 'eload_special_position_de'

class EloadSpecialPositionEs(BaseModel):
    bottom_code_es = TextField(null=True)
    but_nav_code_es = TextField(null=True)
    count_down_es = IntegerField(constraints=[SQL("DEFAULT 0")])
    discount_mark_es = IntegerField(constraints=[SQL("DEFAULT 1")])
    left_brif_es = IntegerField(constraints=[SQL("DEFAULT 0")])
    m_name_es = CharField(constraints=[SQL("DEFAULT ''")])
    memo_es = CharField(constraints=[SQL("DEFAULT ''")])
    muti_name_es = CharField(constraints=[SQL("DEFAULT ''")])
    name_es = CharField(constraints=[SQL("DEFAULT ''")])
    nav_name_es = CharField()
    position_id = AutoField()
    show_market_es = IntegerField(constraints=[SQL("DEFAULT 1")])
    special_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    special_position_id_es = IntegerField()
    top_code_es = TextField(null=True)
    top_nav_code_es = TextField(null=True)
    url_es = CharField(null=True)

    class Meta:
        table_name = 'eload_special_position_es'

class EloadSpecialPositionFr(BaseModel):
    bottom_code_fr = TextField(null=True)
    but_nav_code_fr = TextField(null=True)
    count_down_fr = IntegerField(constraints=[SQL("DEFAULT 0")])
    discount_mark_fr = IntegerField(constraints=[SQL("DEFAULT 1")])
    left_brif_fr = IntegerField(constraints=[SQL("DEFAULT 0")])
    m_name_fr = CharField(constraints=[SQL("DEFAULT ''")])
    memo_fr = CharField(constraints=[SQL("DEFAULT ''")])
    muti_name_fr = CharField(constraints=[SQL("DEFAULT ''")])
    name_fr = CharField(constraints=[SQL("DEFAULT ''")])
    nav_name_fr = CharField()
    position_id = AutoField()
    show_market_fr = IntegerField(constraints=[SQL("DEFAULT 1")])
    special_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    special_position_id_fr = IntegerField()
    top_code_fr = TextField(null=True)
    top_nav_code_fr = TextField(null=True)
    url_fr = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'eload_special_position_fr'

class EloadSpecialPositionIt(BaseModel):
    bottom_code_it = TextField(null=True)
    but_nav_code_it = TextField(null=True)
    count_down_it = IntegerField(constraints=[SQL("DEFAULT 0")])
    discount_mark_it = IntegerField(constraints=[SQL("DEFAULT 1")])
    left_brif_it = IntegerField(constraints=[SQL("DEFAULT 0")])
    m_name_it = CharField(constraints=[SQL("DEFAULT ''")])
    memo_it = CharField(constraints=[SQL("DEFAULT ''")])
    muti_name_it = CharField(constraints=[SQL("DEFAULT ''")])
    name_it = CharField(constraints=[SQL("DEFAULT ''")])
    nav_name_it = CharField()
    position_id = AutoField()
    show_market_it = IntegerField(constraints=[SQL("DEFAULT 1")])
    special_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    special_position_id_it = IntegerField()
    top_code_it = TextField(null=True)
    top_nav_code_it = TextField(null=True)
    url_it = CharField(null=True)

    class Meta:
        table_name = 'eload_special_position_it'

class EloadSpecialPositionRu(BaseModel):
    bottom_code_ru = TextField(null=True)
    but_nav_code_ru = TextField(null=True)
    count_down_ru = IntegerField(constraints=[SQL("DEFAULT 0")])
    discount_mark_ru = IntegerField(constraints=[SQL("DEFAULT 1")])
    left_brif_ru = IntegerField(constraints=[SQL("DEFAULT 0")])
    m_name_ru = CharField(constraints=[SQL("DEFAULT ''")])
    memo_ru = CharField(constraints=[SQL("DEFAULT ''")])
    muti_name_ru = CharField(constraints=[SQL("DEFAULT ''")])
    name_ru = CharField(constraints=[SQL("DEFAULT ''")])
    nav_name_ru = CharField()
    position_id = AutoField()
    show_market_ru = IntegerField(constraints=[SQL("DEFAULT 1")])
    special_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    special_position_id_ru = IntegerField()
    top_code_ru = TextField(null=True)
    top_nav_code_ru = TextField(null=True)
    url_ru = CharField(null=True)

    class Meta:
        table_name = 'eload_special_position_ru'

class EloadSpecialRu(BaseModel):
    banner_desc_ru = TextField()
    banner_ru = CharField(null=True)
    bg_color_ru = CharField(constraints=[SQL("DEFAULT ''")])
    bg_pic_ru = CharField(constraints=[SQL("DEFAULT ''")])
    css_path_ru = CharField()
    description_ru = CharField(null=True)
    keyword_ru = CharField(null=True)
    m_banner_ru = CharField()
    remark_ru = CharField(null=True)
    ru_id = AutoField()
    share_img_ru = CharField(null=True)
    special_id = IntegerField(unique=True)
    title_ru = CharField(null=True)

    class Meta:
        table_name = 'eload_special_ru'

class EloadSpuSpecBr(BaseModel):
    attr_goods_sn = CharField()
    attr_id = IntegerField()
    attr_name = CharField()
    attr_price = CharField()
    attr_value = CharField()
    goods_id = IntegerField()
    spu = CharField()

    class Meta:
        table_name = 'eload_spu_spec_br'
        indexes = (
            (('goods_id', 'attr_id'), False),
            (('spu', 'attr_id'), False),
        )

class Label(BaseModel):
    background_color = CharField(constraints=[SQL("DEFAULT ''")])
    border_color = CharField(constraints=[SQL("DEFAULT ''")])
    create_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    end_time = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    filter_order = IntegerField(constraints=[SQL("DEFAULT 0")])
    filter_title = CharField(constraints=[SQL("DEFAULT ''")])
    is_delete = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_effective = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_filter = IntegerField(constraints=[SQL("DEFAULT 1")])
    is_show = IntegerField(constraints=[SQL("DEFAULT 1")])
    label_desc = CharField(constraints=[SQL("DEFAULT ''")])
    label_name = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    logo = CharField(constraints=[SQL("DEFAULT ''")])
    service_order = IntegerField(constraints=[SQL("DEFAULT 0")])
    service_text = CharField(constraints=[SQL("DEFAULT ''")])
    start_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    text_color = CharField(constraints=[SQL("DEFAULT ''")])
    type = IntegerField(constraints=[SQL("DEFAULT 1")], index=True)
    update_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    updater = CharField(constraints=[SQL("DEFAULT ''")])
    url = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'label'

class LabelGoods(BaseModel):
    create_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    goods_sn = CharField(constraints=[SQL("DEFAULT ''")])
    is_delete = IntegerField(constraints=[SQL("DEFAULT 0")])
    label_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    pipeline_code = CharField(constraints=[SQL("DEFAULT 'GB'")], index=True)
    platform = CharField(constraints=[SQL("DEFAULT ''")])
    update_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    updater = CharField(constraints=[SQL("DEFAULT ''")])
    warehouse_code = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'label_goods'
        indexes = (
            (('goods_sn', 'warehouse_code'), False),
            (('label_id', 'is_delete'), False),
        )

class MaxIntValues(BaseModel):
    extra = CharField(constraints=[SQL("DEFAULT ''")])
    int_type = CharField(index=True)
    max_value = BigIntegerField(index=True)

    class Meta:
        table_name = 'max_int_values'
        indexes = (
            (('int_type', 'max_value'), True),
        )
        primary_key = CompositeKey('int_type', 'max_value')

class Person(BaseModel):
    birthday = DateField()
    is_relative = IntegerField()
    name = CharField()

    class Meta:
        table_name = 'person'

class PmsContractPaymethod201612301339(BaseModel):
    create_time = DateTimeField()
    create_user = CharField()
    depart_id = IntegerField()
    paymethod = CharField(constraints=[SQL("DEFAULT ''")])
    paymethod_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    paymethod_type = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_time = DateTimeField()
    update_user = CharField()

    class Meta:
        table_name = 'pms_contract_paymethod_201612301339'
        primary_key = False

class PmsDeclarationSuccessInfo201612301339(BaseModel):
    amount = IntegerField()
    declarationnu = CharField()
    declarationnu_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    purchase_sn = CharField()
    sku = CharField()
    status = CharField()
    status_mark = IntegerField()
    stock_code = CharField()

    class Meta:
        table_name = 'pms_declaration_success_info_201612301339'
        primary_key = False

class PmsOemInfoBak(BaseModel):
    active_num = IntegerField(null=True)
    audit_date = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    back_quantity = IntegerField(constraints=[SQL("DEFAULT 0")])
    caigou_desc = TextField()
    create_date = DateTimeField(index=True)
    currency_code = CharField(constraints=[SQL("DEFAULT 'CNY'")])
    data_source = IntegerField(constraints=[SQL("DEFAULT 1")])
    depart_type = IntegerField(constraints=[SQL("DEFAULT 1")])
    is_default_purchaser = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_net = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    is_sync_erp = IntegerField(constraints=[SQL("DEFAULT 1")])
    last_lowest_price = DecimalField(constraints=[SQL("DEFAULT 0.00000")])
    makeup_stock_sn = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    nee_delivery_date = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    need_produce_time = DateTimeField(null=True)
    need_stock_date = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    order_create_date = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    order_price = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    order_quantity = IntegerField(constraints=[SQL("DEFAULT 0")])
    owner_user = CharField()
    plan_sales_period = IntegerField(constraints=[SQL("DEFAULT 0")])
    pm = CharField(constraints=[SQL("DEFAULT ''")])
    pms_sku = CharField()
    provider_name = CharField(constraints=[SQL("DEFAULT ''")])
    provider_sku = CharField()
    provider_sn = CharField()
    purchase_id = AutoField()
    purchase_price = DecimalField(constraints=[SQL("DEFAULT 0.00000")])
    purchase_type = IntegerField(constraints=[SQL("DEFAULT 1")])
    purchaser = CharField(index=True)
    recmd_level = CharField(constraints=[SQL("DEFAULT ''")])
    reference_price = DecimalField(constraints=[SQL("DEFAULT 0.00000")])
    remarks = CharField()
    require_info = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    require_type = IntegerField(constraints=[SQL("DEFAULT 1")])
    requirement_b = IntegerField(constraints=[SQL("DEFAULT 0")])
    requirement_quantity = IntegerField(constraints=[SQL("DEFAULT 0")])
    sales_seven = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sales_time_end = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    sales_time_start = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    show_create_date = DateTimeField()
    sku = CharField(index=True)
    sku_img_thumb = CharField()
    sku_name = CharField(constraints=[SQL("DEFAULT '产品名称'")])
    sku_source_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    sku_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    special_stock_reason = CharField()
    statistics_quantity = IntegerField(constraints=[SQL("DEFAULT 0")])
    stock_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    stock_num = IntegerField(null=True)
    stock_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    stockout_period = IntegerField(constraints=[SQL("DEFAULT 0")])
    transport = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'pms_oem_info_bak'

class PmsPayProvider201612301339(BaseModel):
    advantage = TextField()
    broker = CharField(constraints=[SQL("DEFAULT ''")])
    capacity = CharField(constraints=[SQL("DEFAULT ''")])
    car_num = CharField(constraints=[SQL("DEFAULT ''")])
    client_address = CharField(constraints=[SQL("DEFAULT ''")])
    factory_area = CharField(constraints=[SQL("DEFAULT ''")])
    id = IntegerField(constraints=[SQL("DEFAULT 0")])
    other = TextField()
    produce_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    provider_address = CharField(constraints=[SQL("DEFAULT ''")])
    provider_contact = CharField(constraints=[SQL("DEFAULT ''")])
    provider_name = CharField(constraints=[SQL("DEFAULT ''")])
    provider_sn = CharField()
    service_state = CharField(constraints=[SQL("DEFAULT ''")])
    staff_num = CharField(constraints=[SQL("DEFAULT ''")])
    work_wish = TextField()

    class Meta:
        table_name = 'pms_pay_provider_201612301339'
        primary_key = False

class PmsPayRecords201612301339(BaseModel):
    add_time = DateTimeField()
    contact_job = CharField()
    contact_people = CharField()
    contact_phone = CharField()
    contact_type = IntegerField()
    desc_provider = TextField()
    end_time = DateTimeField()
    id = IntegerField(constraints=[SQL("DEFAULT 0")])
    interview_address = CharField(constraints=[SQL("DEFAULT ''")])
    interview_record_user = CharField(constraints=[SQL("DEFAULT ''")])
    interview_topic = CharField(constraints=[SQL("DEFAULT ''")])
    interview_user = CharField(constraints=[SQL("DEFAULT ''")])
    is_submit = IntegerField(constraints=[SQL("DEFAULT 1")])
    last_butt = CharField()
    last_job = CharField()
    last_phone = CharField()
    lastmonth_order = CharField(constraints=[SQL("DEFAULT ''")])
    lastmonth_rate = CharField(constraints=[SQL("DEFAULT ''")])
    offline_scores = IntegerField()
    provider_sn = CharField()
    purchaser = CharField()
    visit_time = DateTimeField()
    wait_order = CharField()
    words = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'pms_pay_records_201612301339'
        primary_key = False

class PmsProviderEnter201612301339(BaseModel):
    address = CharField(null=True)
    alipay_account = CharField(null=True)
    alipay_username = CharField(null=True)
    area = CharField(null=True)
    brand_name = CharField(constraints=[SQL("DEFAULT '无'")])
    business_license = CharField(null=True)
    business_model = CharField(null=True)
    company_name = CharField()
    company_profile = TextField(null=True)
    corporate = CharField(null=True)
    create_time = DateTimeField()
    email = CharField()
    found_time = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    id = IntegerField(constraints=[SQL("DEFAULT 0")])
    linkman = CharField()
    phone_number = CharField()
    product = CharField(null=True)
    qq = CharField()
    registered_capital = CharField(null=True)
    registered_currency = CharField(constraints=[SQL("DEFAULT 'CNY'")])
    website = CharField()

    class Meta:
        table_name = 'pms_provider_enter_201612301339'
        primary_key = False

class ProductBrandFrompdm201612301339(BaseModel):
    brand_code = CharField()
    brand_en_name = CharField()
    brand_name = CharField()
    brand_remark = CharField()
    catalog_type = CharField()
    id = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_enable = IntegerField()
    pdm_brand_id = IntegerField()
    update_time = DateTimeField()
    update_user = CharField()

    class Meta:
        table_name = 'product_brand_frompdm_201612301339'
        primary_key = False

class ProductCharacter201612301339(BaseModel):
    characters = CharField()
    create_time = DateTimeField()
    id = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_enable = IntegerField()
    pdm_id = IntegerField()
    update_time = DateTimeField()

    class Meta:
        table_name = 'product_character_201612301339'
        primary_key = False

class ProductColorFrompdm201612301339(BaseModel):
    attr_extend = CharField()
    attr_id = IntegerField()
    attr_name = CharField()
    attr_value = CharField()
    attr_value_en = CharField()
    attr_value_group_id = IntegerField()
    attr_value_group_name = CharField()
    attr_value_group_name_en = CharField()
    attr_value_id = IntegerField()
    id = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'product_color_frompdm_201612301339'
        primary_key = False

class SoaTest(BaseModel):
    goods_id = BigAutoField()
    name = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'soa_test'

class Tt(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    num = FloatField(null=True)

    class Meta:
        table_name = 'tt'
        primary_key = False

class Tt1(BaseModel):
    num = FloatField(null=True)

    class Meta:
        table_name = 'tt1'
        primary_key = False

