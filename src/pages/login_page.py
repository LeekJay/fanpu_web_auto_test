"""
登录页面对象，实现用户登录相关操作
"""

from pages.base.base_page import BasePage
from utils.logger import logger
from config.config import LOGIN_USERNAME, LOGIN_PASSWORD
from playwright.async_api import Page
from locators.login_locators import LoginLocators


class LoginPage(BasePage):
    """登录页面对象类"""

    def __init__(self, page: Page):
        """
        初始化登录页面
        :param page: playwright页面对象
        """
        super().__init__(page)
        # 登录页面URL，使用相对路径
        self.login_url = "/login.aspx"
        self.selectors = LoginLocators()

    def navigate_to_login(self):
        """
        导航到登录页面
        """
        logger.info("导航到登录页面")
        self.navigate(f"{self.base_url}{self.login_url}")

    def login(self, username=LOGIN_USERNAME, password=LOGIN_PASSWORD):
        """
        执行登录操作
        :param username: 用户名
        :param password: 密码
        """
        logger.info(f"使用用户名 {username} 登录")
        self.navigate_to_login()
        self.fill(self.selectors.USERNAME_INPUT, username)
        self.fill(self.selectors.PASSWORD_INPUT, password)
        self.click(self.selectors.LOGIN_BUTTON)
        self.wait_for_navigation()

    def is_login_successful(self):
        """
        判断登录是否成功
        :return: 登录是否成功
        """
        return self.is_visible(self.selectors.WELCOME_MESSAGE)

    def get_error_message(self):
        """
        获取登录失败时的错误信息
        :return: 错误信息文本
        """
        if self.is_visible(self.selectors.ERROR_MESSAGE):
            return self.get_text(self.selectors.ERROR_MESSAGE)
        return None
