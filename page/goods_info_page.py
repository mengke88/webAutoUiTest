"""
商品详情页(尝试编写详情页面的PO)
用于添加购物车详情页并返回添加成功的字样，需要切换到iframe
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle
from utils import DriverUtils


class GoodsIofoPage(BasePage):
    """
    对象库层，BasePage继承基类文件，V5封装
    """

    def __init__(self):
        super().__init__()
        # 加入购物车
        self.add_card = (By.ID, 'join_cart')
        # iframe页面
        self.iframe = (By.ID, "layui-layer-iframe1")
        # 结果信息
        self.result = (By.CSS_SELECTOR, '.conect-title>span')

    def find_add_card(self):
        return self.find_ele(self.add_card)

    def find_iframe(self):
        return self.find_ele(self.iframe)

    def find_result(self):
        return self.find_ele(self.result)


class GoodsInfoHandle(BaseHandle):
    """
    操作层,BaseHandle基类方法，用于对输入框输入的优化封装
    """

    def __init__(self):
        self.gi_page = GoodsIofoPage()

    def click_add_card(self):
        return self.gi_page.find_add_card().click()

    def get_result(self):
        # 切换到iframe窗口
        DriverUtils.get_driver().switch_to.frame(self.gi_page.find_iframe())
        return self.gi_page.find_result().text


class GoodsUnfoProxy:
    """
    业务层
    """

    def __init__(self):
        self.gi_handle = GoodsInfoHandle()

    def test_add_cart(self):
        self.gi_handle.click_add_card()
        # 返回添加结果
        return self.gi_handle.get_result()
