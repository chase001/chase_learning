
from common.objects import BaseObj
from order_service.api import *
                

class ProductUpdateInfoIdObj(BaseOrder):
    """api controller obj"""
    def __init__(self, **kwargs):
        super(ProductUpdateInfoIdObj, self).__init__()
        self.info = "根据商品id获取商品编辑信息"
        self.uri = "/product/updateInfo/{id}"
        self.method = "get"
        self.body = self.Body(**kwargs)
        self.resp = self.Resp()
            
    class Body(BaseObj):
        def __init__(self, **kwargs):
            self.id = None
            BaseObj.__init__(self, **kwargs)
    
    class Resp(object):
        def __init__(self):
            super(ProductUpdateInfoIdObj.Resp, self).__init__()
            self.code = None  # None
            self.data = self.PmsProductResult()  # None
            self.message = None  # None
            
        class PmsProductResult(object):
            """None"""
            def __init__(self):
                self.albumPics = None  # 画册图片，连产品图片限制为5张，以逗号分割
                self.brandId = None  # None
                self.brandName = None  # 品牌名称
                self.cateParentId = None  # None
                self.deleteStatus = None  # 删除状态：0->未删除；1->已删除
                self.description = None  # 商品描述
                self.detailDesc = None  # None
                self.detailHtml = None  # 产品详情网页内容
                self.detailMobileHtml = None  # 移动端网页详情
                self.detailTitle = None  # None
                self.feightTemplateId = None  # None
                self.giftGrowth = None  # 赠送的成长值
                self.giftPoint = None  # 赠送的积分
                self.id = None  # None
                self.keywords = None  # None
                self.lowStock = None  # 库存预警值
                self.memberPriceList = [self.PmsMemberPrice()]  # 商品会员价格设置
                self.name = None  # None
                self.newStatus = None  # 新品状态:0->不是新品；1->新品
                self.note = None  # None
                self.originalPrice = None  # 市场价
                self.pic = None  # None
                self.prefrenceAreaProductRelationList = [self.CmsPrefrenceAreaProductRelation()]  # 优选专区和商品的关系
                self.previewStatus = None  # 是否为预告商品：0->不是；1->是
                self.price = None  # None
                self.productAttributeCategoryId = None  # None
                self.productAttributeValueList = [self.PmsProductAttributeValue()]  # 商品参数及自定义规格属性
                self.productCategoryId = None  # None
                self.productCategoryName = None  # 商品分类名称
                self.productFullReductionList = [self.PmsProductFullReduction()]  # 商品满减价格设置
                self.productLadderList = [self.PmsProductLadder()]  # 商品阶梯价格设置
                self.productSn = None  # 货号
                self.promotionEndTime = None  # 促销结束时间
                self.promotionPerLimit = None  # 活动限购数量
                self.promotionPrice = None  # 促销价格
                self.promotionStartTime = None  # 促销开始时间
                self.promotionType = None  # 促销类型：0->没有促销使用原价;1->使用促销价；2->使用会员价；3->使用阶梯价格；4->使用满减价格；5->限时购
                self.publishStatus = None  # 上架状态：0->下架；1->上架
                self.recommandStatus = None  # 推荐状态；0->不推荐；1->推荐
                self.sale = None  # 销量
                self.serviceIds = None  # 以逗号分割的产品服务：1->无忧退货；2->快速退款；3->免费包邮
                self.skuStockList = [self.PmsSkuStock()]  # 商品的sku库存信息
                self.sort = None  # 排序
                self.stock = None  # 库存
                self.subTitle = None  # 副标题
                self.subjectProductRelationList = [self.CmsSubjectProductRelation()]  # 专题和商品关系
                self.unit = None  # 单位
                self.usePointLimit = None  # 限制使用的积分数
                self.verifyStatus = None  # 审核状态：0->未审核；1->审核通过
                self.weight = None  # 商品重量，默认为克
                
            class PmsMemberPrice(object):
                """None"""
                def __init__(self):
                
            class CmsPrefrenceAreaProductRelation(object):
                """None"""
                def __init__(self):
                
            class PmsProductAttributeValue(object):
                """None"""
                def __init__(self):
                
            class PmsProductFullReduction(object):
                """None"""
                def __init__(self):
                
            class PmsProductLadder(object):
                """None"""
                def __init__(self):
                
            class PmsSkuStock(object):
                """None"""
                def __init__(self):
                
            class CmsSubjectProductRelation(object):
                """None"""
                def __init__(self):
    
