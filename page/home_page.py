"""
tpshop首页
"""
from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandle


# 对象库层
class HomePage(BasePage):

    def __init__(self):
        # 重写父类的初始化方法
        super().__init__()
        # 登陆超链接
        self.login_link = (By.CSS_SELECTOR, ".red")
        # 搜索输入框
        self.search_input_box = (By.ID, "q")
        # 搜索按钮
        self.search_btn = (By.CSS_SELECTOR, ".search_usercenter_btn")
        # 点击购物车页面
        self.click_cart = (By.CSS_SELECTOR, ".share-shopcar-index")

    # 定义找到登陆超链接的方法
    def find_login_link(self):
        return self.find_ele(self.login_link)

    # 找到搜索输入框
    def find_search_input_box(self):
        return self.find_ele(self.search_input_box)

    # 找到搜索按钮
    def find_search_btn(self):
        return self.find_ele(self.search_btn)

    # 找到购物车按钮
    def find_click_cart(self):
        return self.find_ele(self.click_cart)


# 操作层
class HomeHandle(BaseHandle):

    # 实例化对象库层
    def __init__(self):
        self.home_page = HomePage()

    # 点击登陆超链接的方法
    def click_login_link(self):
        self.home_page.find_login_link().click()

    # 搜索输入框输入
    def input_search_box(self, key):
        self.input_text(self.home_page.find_search_input_box(), key)

    # 搜索按钮点击
    def click_search_btn(self):
        self.home_page.find_search_btn().click()

    # 点击我的购物车
    def click_my_cart(self):
        self.home_page.find_click_cart().click()


# 业务层
class HomeProxy:

    # 实例化操作层
    def __init__(self):
        self.home_handle = HomeHandle()

    # 跳转登录页面业务
    def to_login_page(self):
        # 在首页点击登陆超链接
        self.home_handle.click_login_link()

    # 商品搜索的业务操作
    def test_search_goods(self, key):
        # 输入商品的信息
        self.home_handle.input_search_box(key)
        # 点击搜索按钮
        self.home_handle.click_search_btn()

    # 点击我的购物车
    def test_my_card(self):
        self.home_handle.click_my_cart()
