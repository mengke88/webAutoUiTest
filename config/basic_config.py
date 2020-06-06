"""
生成日志
"""

import logging.handlers


# 定义日志配置方法
def log_config():
    # 创建日志生成器，并且设置日志的级别
    logger = logging.getLogger()
    logger.setLevel(level=logging.DEBUG)
    # 创建处理器，输出到控制台
    ls = logging.StreamHandler()
    # 创建处理器，输出到指定文件夹生成文件
    lht = logging.handlers.TimedRotatingFileHandler(filename="../log/test.log", when="midnight", backupCount=2)
    # 创建格式化器，设置输出什么内容，以什么格式进行输出，以后可以百度，不用记
    formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    # 给处理器添加我们上面创建的格式化形式输出
    ls.setFormatter(formatter)
    lht.setFormatter(formatter)
    # 给日志添加上面设置好的处理器
    logger.addHandler(ls)
    logger.addHandler(lht)
