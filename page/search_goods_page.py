"""
搜索结果页
"""
from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandle


# 对象库层
class SearchGoodsPage(BasePage):

    def __init__(self):
        super().__init__()
        # 加入购物车连接
        self.to_goods_info = (By.XPATH, "//*[text()='加入购物车']")

    # 找到加入购物车连接方法
    def find_to_goods_info(self):
        return self.find_ele(self.to_goods_info)


# 操作层
class SearchGoodsHandle(BaseHandle):

    def __init__(self):
        # 创建对象库的对象
        self.sg_page = SearchGoodsPage()

    # 点击第一个商品的加入购物车
    def click_to_goods_info(self):
        self.sg_page.find_to_goods_info().click()


# 业务层
class SearchGoodsProxy:

    def __init__(self):
        # 创建操作层的对象
        self.sg_handle = SearchGoodsHandle()

    # 去详情页面
    def to_goods_info_page(self):
        # 点击第一个商品结果
        self.sg_handle.click_to_goods_info()
