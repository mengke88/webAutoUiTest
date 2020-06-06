"""
tpshop登陆页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


# 对象库层
# 第一件事：将文案的测试用例所有在本页面中操作的元素对象的定位方式以及对应的值定义到实例属性中进行管理
# 第二件事：将文案的测试用例所有在本页面中操作的元素对象定位回来
class LoginPage(BasePage):
    # 定义实例属性
    def __init__(self):
        super().__init__()
        # 用户名输入框
        self.username = (By.ID, "username")
        # 密码输入框
        self.password = (By.ID, "password")
        # 验证码输入框
        self.code = (By.ID, "verify_code")
        # 登陆按钮
        self.login_btn = (By.NAME, "sbtbutton")

    # 找用户名输入框
    def find_username(self):
        return self.find_ele(self.username)

    # 找密码输入框
    def find_password(self):
        return self.find_ele(self.password)

    # 找验证码输入框
    def find_code(self):
        return self.find_ele(self.code)

    # 找登陆按钮
    def find_login_btn(self):
        return self.find_ele(self.login_btn)


# 操作层
class LoginHandle(BaseHandle):

    def __init__(self):
        self.login_page = LoginPage()

    # 用户名输入框输入
    def input_username(self, username):
        # 模拟输入
        self.input_text(self.login_page.find_username(), username)

    # 密码输入框输入
    def input_password(self, password):
        self.input_text(self.login_page.find_password(), password)

    # 验证码的输入
    def input_code(self, code):
        self.input_text(self.login_page.find_code(), code)

    # 登陆按钮的点击
    def click_login_btn(self):
        self.login_page.find_login_btn().click()


# 业务层
class LoginProxy:

    def __init__(self):
        self.login_handle = LoginHandle()

    # 登陆的业务方法
    def test_login(self, username, password, code):
        # 输入用户名
        self.login_handle.input_username(username)
        # 输入密码
        self.login_handle.input_password(password)
        # 输入验证码
        self.login_handle.input_code(code)
        # 点击登陆按钮
        self.login_handle.click_login_btn()
