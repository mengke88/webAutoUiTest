"""
提交订单的页面
"""
import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


# 对象库层
class SubmitOrderPage(BasePage):
    def __init__(self):
        # 和父类的方法重名，需要重写，调用super()进行重写
        super().__init__()
        # 定位元素
        self.sumbit_order_btn = (By.CSS_SELECTOR, ".Sub-orders")
        # 返回点击提交订单后的文本信息
        self.sumbit_order_result=(By.CSS_SELECTOR,".erhuh h3")

    # 找到结算按钮
    def find_sumbit(self):
        return self.find_ele(self.sumbit_order_btn)

    def find_sumbit_result(self):
        return self.find_ele(self.sumbit_order_result)


# 操作层
class SubmitHandle(BaseHandle):
    # 实例化对象库层，用于对象库层类的方法使用
    def __init__(self):
        self.cart_page = SubmitOrderPage()

    # 实现点击操作
    def click_submit_btn(self):
        time.sleep(5)
        return self.cart_page.find_sumbit().click()
    # 获取订单结果
    def get_sbo_result(self):
        return self.cart_page.find_sumbit_result().text


# 业务层
class SubmitProxy:
    # 调用操作层类方法
    def __init__(self):
        self.cart_handle = SubmitHandle()

    # 调用方法实现业务操作
    def test_submit_order(self):
        self.cart_handle.click_submit_btn()
        return self.cart_handle.get_sbo_result()