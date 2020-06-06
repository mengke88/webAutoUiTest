"""
购物车的页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


# 对象库层
class CartPage(BasePage):
    def __init__(self):
        # 和父类的方法重名，需要重写，调用super()进行重写
        super().__init__()
        # 定位元素
        self.go_settle_bnt = (By.CSS_SELECTOR, ".gwc-qjs")

    # 找到结算按钮
    def find_settle(self):
        return self.find_ele(self.go_settle_bnt)


# 操作层
class CartHandle(BaseHandle):
    # 实例化对象库层，用于对象库层类的方法使用
    def __init__(self):
        self.cart_page = CartPage()

    # 实现点击操作
    def click_settle_btn(self):
        return self.cart_page.find_settle().click()


# 业务层
class CartProxy:
    # 调用操作层类方法
    def __init__(self):
        self.cart_handle = CartHandle()

    # 调用方法实现业务操作
    def to_submit_order_page(self):
        self.cart_handle.click_settle_btn()
