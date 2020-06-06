import time
import unittest

from page.car_page import CartProxy
from page.home_page import HomeProxy
from page.submit_order_page import SubmitProxy
from utils import DriverUtils


class TestOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 获取浏览器驱动对象
        cls.driver = DriverUtils.get_driver()
        # 实例化首页业务层对象
        cls.home_proxy = HomeProxy()
        # 实例化购物车业务层对象
        cls.cart_proxy = CartProxy()
        # 实例化提交订单业务层对象
        cls.so_proxy = SubmitProxy()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        DriverUtils.quit_driver()

    def setUp(self):
        self.driver.get("http://localhost/")

    def test_submit_order(self):
        # 在首页点击购物车
        self.home_proxy.test_my_card()
        # 在购物车页面点击去结算
        self.cart_proxy.to_submit_order_page()
        # 在提交订单页面点击提交订单并且获取提交结果
        msg = self.so_proxy.test_submit_order()
        print("{}".format(msg))
        # 断言
        self.assertIn("订单提交成功", msg)
