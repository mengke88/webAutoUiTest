# 1.导包
import time
import unittest
from parameterized import parameterized
from page.home_page import HomeProxy
from page.login_page import LoginProxy
from utils import DriverUtils, build_data, get_msg


# 2.定义测试类
class TestLogin(unittest.TestCase):

    # 类级别的初始化的fixture
    # a.打开浏览器并且打开测试网址
    @classmethod
    def setUpClass(cls):
        # 创建的浏览器驱动对象
        cls.driver = DriverUtils.get_driver()
        # 创建首页业务层对象
        cls.home_proxy = HomeProxy()
        # 创建登陆业务层对象
        cls.login_proxy = LoginProxy()

    # 类级别的销毁的fixture
    # e.关闭浏览器
    @classmethod
    def tearDownClass(cls):
        DriverUtils.quit_driver()

    # 方法级别的初始化fixture
    # 每个方法在运行之前都会回到首页
    def setUp(self):
        time.sleep(2)
        self.driver.get("http://localhost/")

    # 3.定义测试方法
    @parameterized.expand(build_data("../data/test_login_data.json"))
    def test_login(self, username, password, code, expect, is_suc):
        print(
            "username={}, password={}, code={}, expect={}, is_suc={}".format(username, password, code, expect, is_suc))
        # b.在tpshop首页点击登陆的超链接
        self.home_proxy.to_login_page()
        # c.执行登陆操作
        self.login_proxy.test_login(username, password, code)
        # 如果是反向的测试用例，获取是弹出提示信息
        if is_suc:
            # 如果是正向的测试用，获取是的页面的标题
            time.sleep(3)
            msg = self.driver.title
            self.assertIn(expect, msg)
        else:
            msg = get_msg()
            self.assertIn(expect, msg)
