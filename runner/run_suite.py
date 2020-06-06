# 测试套件
# 1.导包
import time
import unittest
from BeautifulReport import BeautifulReport
from utils import DriverUtils
from lib.HTMLTestRunner import HTMLTestRunner

# 2.组织测试用例（测试套件、测试加载器）
# 关闭浏览器的开关，先传一个True,作用是执行完所有用例后再关闭浏览器
DriverUtils.change_key(True)
suite = unittest.TestLoader().discover("../script", pattern="test*.py")
# 3.定义测试报告路径
# report_file="../report/test-{}.html".format(time.strftime("%Y%m%d"))
# # 4.打开测试报告
# with open(report_file,'wb') as f:
#     runner= HTMLTestRunner(stream=f,title="TPshop项目测试",description="chrame浏览器，V5版本")
#     runner.run(suite)
# 使用beautifulReport生成测试报告
report_file = "Tpshop综合测试报告{}.html".format(time.strftime("%Y-%m-%d"))
BeautifulReport(suite).report(filename=report_file, description="Tpshop测试", log_path="../report")

# 打开浏览器关闭开关，执行完之后再传一个False，让其能执行关闭浏览器的方法
DriverUtils.change_key(False)
DriverUtils.quit_driver()
