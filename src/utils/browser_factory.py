"""
浏览器工厂类，负责创建和管理Playwright浏览器实例
"""
from playwright.sync_api import sync_playwright
from config.config import BROWSER_TYPE, HEADLESS, SLOW_MO, DEFAULT_TIMEOUT, NAVIGATION_TIMEOUT


class BrowserFactory:
    """浏览器工厂类，用于创建和管理Playwright浏览器实例"""

    @staticmethod
    def get_browser(browser_type=BROWSER_TYPE, headless=HEADLESS, slow_mo=SLOW_MO):
        """
        获取浏览器实例
        :param browser_type: 浏览器类型：chromium, firefox, webkit
        :param headless: 是否无头模式
        :param slow_mo: 操作延迟(毫秒)
        :return: 浏览器实例
        """
        playwright = sync_playwright().start()
        
        if browser_type.lower() == "chromium":
            browser = playwright.chromium.launch(headless=headless, slow_mo=slow_mo)
        elif browser_type.lower() == "firefox":
            browser = playwright.firefox.launch(headless=headless, slow_mo=slow_mo)
        elif browser_type.lower() == "webkit":
            browser = playwright.webkit.launch(headless=headless, slow_mo=slow_mo)
        else:
            raise ValueError(f"不支持的浏览器类型: {browser_type}")
        
        return browser, playwright

    @staticmethod
    def get_context(browser):
        """
        创建浏览器上下文
        :param browser: 浏览器实例
        :return: 浏览器上下文
        """
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            accept_downloads=True
        )
        # 设置超时
        context.set_default_timeout(DEFAULT_TIMEOUT)
        context.set_default_navigation_timeout(NAVIGATION_TIMEOUT)
        return context

    @staticmethod
    def get_page(context):
        """
        创建页面
        :param context: 浏览器上下文
        :return: 页面实例
        """
        return context.new_page() 