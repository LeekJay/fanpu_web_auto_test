"""
借款管理页面对象，实现借款管理相关操作
"""

from playwright.sync_api import Page
from pages.base.base_page import BasePage
from locators.loan_locators import LoanLocators
from models.loan import Loan
from utils.logger import logger


class LoanPage(BasePage):
    """借款管理页面对象类"""

    def __init__(self, page: Page):
        """
        初始化借款管理页面
        :param page: playwright页面对象
        """
        super().__init__(page)
        self.locators = LoanLocators()

    def navigate_to_loan_page(self):
        """导航到借款管理页面"""
        logger.info("导航到借款管理页面")
        self.click(self.locators.LOAN_PAGE)
        self.wait_for_selector(self.locators.LOAN_MENU)

    def click_loan_menu(self):
        """点击借款管理菜单"""
        logger.info("点击借款管理菜单")
        self.click(self.locators.LOAN_MENU)
        self.wait_for_selector(self.locators.LOAN_LIST_PAGE)

    def click_loan_list(self):
        """点击借款申请列表"""
        logger.info("点击借款申请列表")
        self.click(self.locators.LOAN_LIST_PAGE)
        self.wait_for_selector(self.locators.LOAN_LIST_IFRAME)

    def _select_person(
        self,
        search_icon: str,
        search_input: str,
        search_btn: str,
        select_btn: str,
        person_result: str,
        person_name: str,
    ):
        """
        通用人员选择方法
        :param search_icon: 搜索图标选择器
        :param search_input: 搜索输入框选择器
        :param search_btn: 搜索按钮选择器
        :param select_btn: 确定按钮选择器
        :param person_result: 人员结果选择器
        :param person_name: 人员姓名
        """
        try:
            self.click(search_icon)
            self.page.wait_for_timeout(3000)

            frame_element = self.wait_for_selector(
                self.locators.SELECT_GRID_IFRAME,
                timeout=30000,
                state="visible",
            )

            if not frame_element:
                raise Exception("无法找到人员选择iframe")

            nested_frame = frame_element.content_frame()
            if not nested_frame:
                raise Exception("无法获取iframe内容")

            self.current_frame = nested_frame

            # 增加稳定等待
            self.page.wait_for_timeout(2000)
            self.stabilize_page()

            self.wait_for_selector(search_input, timeout=20000)
            self.fill(search_input, person_name)
            self.click(search_btn)

            # 等待搜索结果加载
            self.page.wait_for_timeout(2000)

            # 增加对搜索结果的等待
            self.wait_for_selector(person_result, timeout=20000)
            self.click(person_result)

            # 增加选择后的稳定等待
            self.page.wait_for_timeout(1000)
            self.click(select_btn)

            self.current_frame = frame_element.owner_frame()

        except Exception as e:
            logger.error(f"选择人员时发生错误: {str(e)}")
            self.take_screenshot("select_person_error")
            raise

    def _select_project(
        self,
        search_icon: str,
        select_btn: str,
        project_result: str,
    ):
        """
        通用项目选择方法
        :param search_icon: 搜索图标选择器
        :param select_btn: 确定按钮选择器
        :param project_result: 项目结果选择器
        """
        try:
            self.click(search_icon)
            self.page.wait_for_timeout(3000)  # 增加等待时间

            frame_element = self.wait_for_selector(
                self.locators.SELECT_GRID_IFRAME,
                timeout=30000,
                state="visible",
            )

            if not frame_element:
                raise Exception("无法找到人员选择iframe")

            nested_frame = frame_element.content_frame()
            if not nested_frame:
                raise Exception("无法获取iframe内容")

            self.current_frame = nested_frame

            # 等待搜索结果加载
            self.page.wait_for_timeout(2000)

            # 增加对搜索结果的等待
            self.wait_for_selector(project_result, timeout=20000)
            self.click(project_result)

            # 增加选择后的稳定等待
            self.page.wait_for_timeout(1000)
            self.click(select_btn)

            self.current_frame = frame_element.owner_frame()

        except Exception as e:
            logger.error(f"选择项目时发生错误: {str(e)}")
            self.take_screenshot("select_project_error")
            raise

    def select_project(self, loan: Loan):
        """选择项目"""
        self._select_project(
            self.locators.PROJECT_SEARCH,
            self.locators.PROJECT_SELECT_BTN,
            self.locators.PROJECT_RESULT.format(loan=loan),
        )

    def select_borrower(self, loan: Loan):
        """选择借款人"""
        self._select_person(
            self.locators.BORROWER_SEARCH,
            self.locators.BORROWER_SEARCH_INPUT,
            self.locators.BORROWER_SEARCH_BTN,
            self.locators.BORROWER_SELECT_BTN,
            self.locators.BORROWER_RESULT.format(loan=loan),
            loan.borrower,
        )

    def select_handler(self, loan: Loan):
        """选择经办人"""
        self._select_person(
            self.locators.HANDLER_SEARCH,
            self.locators.HANDLER_SEARCH_INPUT,
            self.locators.HANDLER_SEARCH_BTN,
            self.locators.HANDLER_SELECT_BTN,
            self.locators.HANDLER_RESULT.format(loan=loan),
            loan.handler,
        )

    def fill_loan_form(self, loan: Loan):
        """
        填写借款表单
        :param loan: 借款数据对象
        """
        try:
            field_mapping = {
                "project_name": self.locators.PROJECT_NAME,
                "loan_amount": self.locators.LOAN_AMOUNT,
                "loan_purpose": self.locators.LOAN_PURPOSE,
                "payment_method": self.locators.PAYMENT_METHOD,
                "repayment_method": self.locators.REPAYMENT_METHOD,
                "loan_period": self.locators.LOAN_PERIOD,
                "borrower_bank": self.locators.BORROWER_BANK,
                "bank_account": self.locators.BANK_ACCOUNT,
                "bank_branch": self.locators.BANK_BRANCH,
                "application_date": self.locators.APPLICATION_DATE,
                "account_name": self.locators.ACCOUNT_NAME,
                "bank_account_number": self.locators.BANK_ACCOUNT_NUMBER,
            }

            for field, selector in field_mapping.items():
                value = getattr(loan, field, None)
                if value is not None:
                    self.fill(selector, value)
                    self.stabilize_page(500)

            if loan.project_name:
                self.select_project(loan)

            if loan.borrower:
                self.select_borrower(loan)

            if loan.handler:
                self.select_handler(loan)

        except Exception as e:
            logger.error(f"填写借款表单时发生错误: {str(e)}")
            self.take_screenshot("loan_form_fill_error")
            raise

    def add_loan(self, loan: Loan):
        """
        添加借款
        :param loan: 借款数据对象
        """
        logger.info(f"添加借款申请: {loan.project_name}")

        try:
            with self.frame_context(self.locators.LOAN_LIST_IFRAME):
                self.stabilize_page()
                self.click(self.locators.ADD_LOAN_BUTTON)

            with self.frame_context(self.locators.ADD_LOAN_FORM_IFRAME):
                self.stabilize_page()
                self.fill_loan_form(loan)
                self.click(self.locators.SAVE_BUTTON)
                self.wait_for_selector(self.locators.SUCCESS_ADD_LOAN_MESSAGE)
                logger.info("借款申请添加成功")

        except Exception as e:
            logger.error(f"添加借款时发生错误: {str(e)}")
            self.take_screenshot("add_loan_error")
            raise

    def search_loan(self, loan: Loan):
        """
        搜索借款
        :param loan: 借款数据对象
        """
        try:
            self.click(self.locators.LOAN_LIST_PAGE)
            self.wait_for_iframe_ready()

            self.enter_frame(self.locators.LOAN_LIST_IFRAME)
            self.page.wait_for_timeout(5000)
            self.stabilize_page()

            # 填写搜索条件
            self.fill(self.locators.SEARCH_LOAN_PROJECT_NAME, loan.project_name)
            self.fill(self.locators.SEARCH_LOAN_BORROWER, loan.borrower)
            self.fill(self.locators.SEARCH_LOAN_PERIOD_START, loan.loan_period)
            self.fill(self.locators.SEARCH_LOAN_PERIOD_END, loan.loan_period)

            self.click(self.locators.SEARCH_LOAN_BUTTON)
            self.page.wait_for_timeout(5000)
            self.wait_for_selector(self.locators.SEARCH_LOAN_LIST)

        except Exception as e:
            logger.error(f"搜索借款时发生错误: {str(e)}")
            self.take_screenshot("search_loan_error")
            self.exit_frame()
            raise

    def is_loan_exists(self, loan: Loan) -> bool:
        """
        检查借款是否存在
        :param loan: 借款数据对象
        :return: 借款是否存在
        """
        try:
            self.search_loan(loan)
            return self.is_visible(self.locators.SEARCH_LOAN_RESULT.format(loan=loan))
        except Exception as e:
            if "Timeout 10000ms exceeded." in str(e):
                logger.info("借款不存在")
                self.exit_frame()
                return False
            else:
                logger.error(f"检查借款是否存在时发生错误: {str(e)}")
                self.take_screenshot("check_loan_exists_error")
                raise

    def edit_loan(self, loan: Loan, updated_loan: Loan):
        """
        编辑借款信息
        :param loan: 原借款数据对象
        :param updated_loan: 更新的借款数据对象
        """
        try:
            self.search_loan(loan)

            with self.frame_context(self.locators.LOAN_LIST_IFRAME):
                self.click(self.locators.SEARCH_LOAN_RESULT_CHECK)
                self.click(self.locators.EDIT_LOAN_BUTTON)

            self.wait_for_selector(self.locators.EDIT_LOAN_FORM_IFRAME)

            with self.frame_context(self.locators.EDIT_LOAN_FORM_IFRAME):
                self.stabilize_page()
                self.fill_loan_form(updated_loan)
                self.page.wait_for_timeout(3000)
                self.click(self.locators.SAVE_BUTTON)
                self.wait_for_selector(self.locators.SUCCESS_EDIT_LOAN_MESSAGE)
                logger.info(f"借款 {loan.project_name} 更新成功")

        except Exception as e:
            logger.error(f"编辑借款时发生错误: {str(e)}")
            self.take_screenshot("edit_loan_error")
            raise

    def delete_loan(self, loan: Loan):
        """
        删除借款
        :param loan: 借款数据对象
        """
        try:
            self.search_loan(loan)

            with self.frame_context(self.locators.LOAN_LIST_IFRAME):
                self.click(self.locators.SEARCH_LOAN_RESULT_CHECK)
                self.click(self.locators.DELETE_LOAN_BUTTON)

                self.wait_for_selector(self.locators.CONFIRM_DELETE_DIALOG)
                self.click(self.locators.CONFIRM_DELETE_YES)
                logger.info(f"借款 {loan.project_name} 删除成功")

        except Exception as e:
            logger.error(f"删除借款时发生错误: {str(e)}")
            self.take_screenshot("delete_loan_error")
            raise

    def view_loan(self, loan: Loan):
        """
        查看借款详情
        :param loan: 借款数据对象
        """
        logger.info(f"查看借款详情: {loan.project_name}")

        try:
            self.search_loan(loan)

            self.click(self.locators.SEARCH_LOAN_RESULT.format(loan=loan))

            self.page.wait_for_timeout(3000)

            with self.frame_context(self.locators.LOAN_DETAIL_IFRAME):
                self.stabilize_page()
                self.wait_for_selector(self.locators.LOAN_DETAIL_CONTENT)

        except Exception as e:
            logger.error(f"查看借款详情时发生错误: {str(e)}")
            self.exit_frame()
            self.take_screenshot("view_loan_error")
            raise

    def is_loan_edited(self, original_loan: Loan, updated_loan: Loan) -> bool:
        """
        检查借款是否被正确编辑
        :param original_loan: 原借款数据对象
        :param updated_loan: 更新后的借款数据对象
        :return: 借款信息是否被正确更新
        """
        try:
            self.search_loan(original_loan)

            with self.frame_context(self.locators.LOAN_LIST_IFRAME):
                self.click(self.locators.SEARCH_LOAN_RESULT_CHECK)
                self.click(self.locators.EDIT_LOAN_BUTTON)

            self.wait_for_selector(self.locators.EDIT_LOAN_FORM_IFRAME)

            with self.frame_context(self.locators.EDIT_LOAN_FORM_IFRAME):
                self.stabilize_page()

                # 验证更新的字段
                field_mapping = {
                    "loan_amount": self.locators.LOAN_AMOUNT,
                    "loan_purpose": self.locators.LOAN_PURPOSE,
                    "payment_method": self.locators.PAYMENT_METHOD,
                    "repayment_method": self.locators.REPAYMENT_METHOD,
                }

                for field, selector in field_mapping.items():
                    value = getattr(updated_loan, field, None)
                    if value is not None:
                        actual_value = self.get_input_value(selector)
                        if str(actual_value) != str(value):
                            logger.error(
                                f"字段 {field} 的值不匹配: 期望 {value}, 实际 {actual_value}"
                            )
                            return False

                return True

        except Exception as e:
            logger.error(f"验证借款编辑时发生错误: {str(e)}")
            self.take_screenshot("verify_loan_edit_error")
            raise
