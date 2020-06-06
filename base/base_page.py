from utils import DriverUtils


# 对象库库层的基类
# 1.定义类
class BasePage:

    def __init__(self):
        # 创建浏览器驱动对象
        self.driver = DriverUtils.get_driver()

    # 2.定义一个公用的元素定位的方法
    def find_ele(self, location):
        # a.拷贝一份具体的实现的代码
        return self.driver.find_element(*location)
        # b.调整错误信息
        # c.执行代码之后有提供信息给调用的地方进行使用，则需要返回


# 1.定义类
class BaseHandle:
    # 2.定义方法:公用的元素信息输入的方法
    def input_text(self, element, text):
        # 清除文本
        element.clear()
        # 输入文本
        element.send_keys(text)
