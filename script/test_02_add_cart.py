"""
商品添加购物车用例
"""
import time
import unittest

from page.goods_info_page import GoodsUnfoProxy
from page.home_page import HomeProxy
from page.search_goods_page import SearchGoodsProxy
from utils import DriverUtils


class TestAddCart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 实例化浏览器对象
        cls.driver = DriverUtils.get_driver()
        # 实例化首页对象，用于搜索商品
        cls.home_proxy = HomeProxy()
        # 实例化搜索结果页业务对象，对搜索的结果点击加入购物车跳转到商品详情页
        cls.sg_proxy = SearchGoodsProxy()
        # 实例化添加到购物车的方法，用于返回购物添加是否成功
        cls.gi_proxy = GoodsUnfoProxy()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        DriverUtils.quit_driver()

    def test_add_cart(self):
        # 进入首页调用商品搜索框
        self.home_proxy.test_search_goods("小米")
        # 在搜索结果后点击添加到购物
        self.sg_proxy.to_goods_info_page()
        # 设置断言，看看添加是否成功
        msg = self.gi_proxy.test_add_cart()
        print("信息提示：",msg)
        # 断言
        self.assertIn("添加成功", msg)
