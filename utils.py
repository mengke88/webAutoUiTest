import time
import json
from selenium import webdriver


# 公用读取测试数据的函数
def build_data(test_path):
    # 定义一个空列表
    test_case_data = []
    # 打开测试数据文件
    with open(test_path, encoding="utf-8") as f:
        # 读取json文件数据
        test_data = json.load(f)
        print("完整的数据为:", test_data)
        # 遍历字典对象中的键值
        for case_data in test_data.values():
            test_case_data.append(list(case_data.values()))
            print(test_case_data)
    return test_case_data


# 1.定义函数:获取弹出框信息的方法
def get_msg():
    # 2.将具体的要封装的共性代码拷贝
    time.sleep(3)
    # 3.再对于拷贝过来的代码进行错误信息调整
    msg = DriverUtils.get_driver().find_element_by_css_selector(".layui-layer-content").text
    # 4.根据需要来对封装代码进行优化
    print("弹出框的提示信息为:", msg)
    return msg
    # 5.修改要调用的代码


# 定义一个浏览器驱动工具类
class DriverUtils:
    # 定义一个私有变量，__driver用于对执行用例只有一个浏览器
    __driver = None
    # __key用于提供判断，当在关闭浏览器的时候等于False时不让其执行关闭浏览器，就在quit_driver用and和__driver连接起来
    __key = False

    # 创建浏览器驱动方法
    # 为了方便调用将方法设置类级别方法
    @classmethod
    def get_driver(cls):
        # 添加判断的原因是为了保障整个测试用例集中的所有测试用例在运行过程
        # 中只会有一个浏览器驱动对象
        if cls.__driver is None:
            # 2.实例化浏览器驱动
            cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(30)
            # 3.打开测试网址
            cls.__driver.get('http://localhost/')
        return cls.__driver

    # 1、定义关闭浏览器驱动的方法
    @classmethod
    def quit_driver(cls):
        # 2.将具体的要封装的共性代码拷贝
        # 3.再对于拷贝过来的代码进行错误信息调整
        # 4.根据需要来对封装代码进行优化
        # 5.修改要调用的代码
        # 加上判断的原因，只是为加强代码的健壮性
        if cls.__driver is not None and cls.__key is False:
            time.sleep(5)
            cls.__driver.quit()
            # 在调用quit()方法后浏览器驱动对象的私有变量并不为空而是一串内存地址
            # 且界面是看不到浏览器的，那么为了保障后续调用获取浏览器驱动的方法能
            # 成功创建浏览器驱动对象，则在关闭之后，将__driver的重置为None
            cls.__driver = None
    # 设置一个参数，在运行套件run_suite.py中调用时，先给他传一个True，
    # 在执行完所有测试用例后，在传一个False这样就可以执行调用关闭浏览器的方法
    @classmethod
    def change_key(cls, key):
        cls.__key = key
