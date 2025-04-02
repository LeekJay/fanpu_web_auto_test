"""
配置文件，包含项目所需的全局配置参数
"""
import os

# 目标网站URL
BASE_URL = "https://demo.fanpusoft.com"  # 替换为实际测试网站URL

# 浏览器配置
BROWSER_TYPE = "chromium"  # 可选: chromium, firefox, webkit
HEADLESS = False  # 设置为True可以无头模式运行
SLOW_MO = 50  # 浏览器操作之间的延迟(毫秒)

# 超时设置(毫秒)
DEFAULT_TIMEOUT = 30000
NAVIGATION_TIMEOUT = 60000

# 截图设置
SCREENSHOT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "reports", "screenshots")

# 登录凭据
LOGIN_USERNAME = "zx"  # 替换为实际用户名
LOGIN_PASSWORD = "123"  # 替换为实际密码

# 测试数据路径
TEST_DATA_PATH = "./utils/test_data.json"
