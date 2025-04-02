"""
Pytest配置文件，包含测试固件
"""

import os
import pytest
import allure
from datetime import datetime

from utils.browser_factory import BrowserFactory
from utils.logger import logger
from pages.login_page import LoginPage
from pages.customer_page import CustomerPage
from pages.loan_page import LoanPage
from config.config import SCREENSHOT_PATH


@pytest.fixture(scope="session")
def browser_context_args():
    """
    设置浏览器上下文参数
    """
    return {"viewport": {"width": 800, "height": 600}}


@pytest.fixture(scope="session")
def browser(request):
    """
    创建浏览器实例
    """
    browser_type = request.config.getoption("--browser-type")
    headless = request.config.getoption("--headless-mode")

    browser_factory = BrowserFactory()
    browser_instance, playwright_instance = browser_factory.get_browser(
        browser_type=browser_type, headless=headless
    )

    logger.info(f"启动{browser_type}浏览器实例，无头模式：{headless}")
    yield browser_instance

    logger.info("关闭浏览器实例")
    browser_instance.close()
    playwright_instance.stop()


@pytest.fixture(scope="function")
def context(browser):
    """
    创建浏览器上下文
    """
    browser_factory = BrowserFactory()
    context = browser_factory.get_context(browser)

    logger.info("创建浏览器上下文")
    yield context

    logger.info("关闭浏览器上下文")
    context.close()


@pytest.fixture(scope="function")
def page(context):
    """
    创建页面实例
    """
    page = context.new_page()
    logger.info("创建新页面")
    yield page
    logger.info("关闭页面")
    page.close()


@pytest.fixture(scope="function")
def login_page(page):
    """
    创建登录页面实例
    """
    return LoginPage(page)


@pytest.fixture(scope="function")
def customer_page(page, login_page):
    """
    创建客户管理页面实例，并确保已登录
    """
    login_page.login()
    return CustomerPage(page)

@pytest.fixture(scope="class")
def shared_customer_data():
    """用于在测试用例之间共享客户数据的fixture"""
    return {}


@pytest.fixture(scope="function")
def loan_page(page, login_page):
    """
    创建借款申请页面实例，并确保已登录
    """
    login_page.login()
    return LoanPage(page)


@pytest.fixture(scope="class")
def shared_loan_data():
    """用于在测试用例之间共享借款数据的fixture"""
    return {}


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    在测试失败时截图
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        try:
            page = item.funcargs.get("page")
            if page:
                # 确保截图目录存在
                if not os.path.exists(SCREENSHOT_PATH):
                    os.makedirs(SCREENSHOT_PATH)

                # 生成截图文件名
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                test_name = (
                    item.nodeid.replace("/", "_").replace(":", "_").replace("::", "_")
                )
                screenshot_path = os.path.join(
                    SCREENSHOT_PATH, f"fail_{test_name}_{timestamp}.png"
                )

                # 保存截图
                page.screenshot(path=screenshot_path)
                logger.info(f"测试失败，截图保存至: {screenshot_path}")

                # 将截图附加到Allure报告
                allure.attach.file(
                    screenshot_path,
                    name="失败截图",
                    attachment_type=allure.attachment_type.PNG,
                )
        except Exception as e:
            logger.error(f"保存失败截图时出错: {e}")


def pytest_addoption(parser):
    """
    添加命令行选项
    """
    parser.addoption(
        "--browser-type",
        action="store",
        default="chromium",
        help="指定浏览器类型: chromium, firefox, webkit",
    )
    parser.addoption(
        "--headless-mode", action="store_true", default=False, help="以无头模式运行"
    )
