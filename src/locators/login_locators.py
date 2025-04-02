"""
登录页面元素定位器
"""


class LoginLocators:
    # 登录表单相关
    USERNAME_INPUT = "#Panel_txtUserID-inputEl"  # 用户名输入框
    PASSWORD_INPUT = "#Panel_txtPassword-inputEl"  # 密码输入框
    LOGIN_BUTTON = "#Panel_btnLogin"  # 登录按钮

    # 提示信息相关
    ERROR_MESSAGE = ".f-messagebox-message"  # 错误信息
    WELCOME_MESSAGE = ".welcome-message"  # 欢迎信息
