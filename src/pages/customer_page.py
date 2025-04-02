"""
客户管理页面对象，实现客户管理相关操作
"""

from playwright.sync_api import Page
from pages.base.base_page import BasePage
from locators.customer_locators import CustomerLocators
from models.customer import Customer
from utils.logger import logger


class CustomerPage(BasePage):
    """客户管理页面对象类"""

    def __init__(self, page: Page):
        """
        初始化客户管理页面
        :param page: playwright页面对象
        """
        super().__init__(page)
        self.locators = CustomerLocators()

    def navigate_to_customer_page(self):
        """导航到客户管理页面"""
        logger.info("导航到客户管理页面")
        self.click(self.locators.CUSTOMER_PAGE)
        self.wait_for_selector(self.locators.CUSTOMER_MENU)

    def click_customer_menu(self):
        """点击客户管理菜单"""
        logger.info("点击客户管理菜单")
        self.click(self.locators.CUSTOMER_MENU)
        self.wait_for_selector(self.locators.CUSTOMER_LIST_PAGE)

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

    def select_responsible_person(self, customer: Customer):
        """
        选择负责人
        :param customer: 客户数据对象
        """
        logger.info(f"选择负责人: {customer.responsible_person}")
        self._select_person(
            self.locators.RESPONSIBLE_PERSON_SEARCH,
            self.locators.RESPONSIBLE_PERSON_INPUT,
            self.locators.RESPONSIBLE_PERSON_SEARCH_BTN,
            self.locators.RESPONSIBLE_PERSON_SELECT_BTN,
            self.locators.RESPONSIBLE_PERSON_RESULT.format(customer=customer),
            customer.responsible_person,
        )

    def select_shared_persons(self, customer: Customer):
        """
        选择共享人
        :param customer: 客户数据对象
        """
        if not customer.shared_persons:
            logger.info("没有需要选择的共享人")
            return

        logger.info(f"选择共享人: {customer.shared_persons}")
        first_person = customer.shared_persons[0]
        self._select_person(
            self.locators.SHARED_PERSON_SEARCH,
            self.locators.SHARED_PERSON_SEARCH_INPUT,
            self.locators.SHARED_PERSON_SEARCH_BTN,
            self.locators.SHARED_PERSON_SELECT_BTN,
            self.locators.SHARED_PERSON_RESULT.format(customer=customer),
            first_person,
        )

        if len(customer.shared_persons) > 1:
            shared_persons_str = ",".join(customer.shared_persons)
            self.wait_for_selector(self.locators.SHARED_PERSON)
            self.page.wait_for_timeout(2000)
            self.fill(self.locators.SHARED_PERSON, shared_persons_str)

    def fill_customer_form(self, customer: Customer):
        """
        填写客户表单
        :param customer: 客户数据对象
        """
        try:
            field_mapping = {
                "name": (self.locators.CUSTOMER_NAME, False),
                "type": (self.locators.CUSTOMER_TYPE, True),
                "code": (self.locators.CUSTOMER_CODE, False),
                "industry": (self.locators.INDUSTRY, True),
                "phone": (self.locators.PHONE, False),
                "region": (self.locators.REGION, True),
                "mobile": (self.locators.MOBILE, False),
                "scale": (self.locators.SCALE, True),
                "qq": (self.locators.QQ, False),
                "source": (self.locators.CUSTOMER_SOURCE, True),
                "department": (self.locators.DEPARTMENT, True),
                "level": (self.locators.CUSTOMER_LEVEL, True),
            }

            for field, (selector, is_select) in field_mapping.items():
                value = getattr(customer, field, None)
                if value is not None:
                    if is_select:
                        self.select_option(selector, value)
                    else:
                        self.fill(selector, value)
                    self.stabilize_page(500)

            if customer.responsible_person:
                self.select_responsible_person(customer)

            if customer.shared_persons:
                self.select_shared_persons(customer)

        except Exception as e:
            logger.error(f"填写表单时发生错误: {str(e)}")
            self.take_screenshot("form_fill_error")
            raise

    def add_customer(self, customer: Customer):
        """
        添加客户
        :param customer: 客户数据对象
        """
        logger.info(f"添加客户: {customer.name}")

        try:
            self.click(self.locators.ADD_CUSTOMER_PAGE)
            self.wait_for_selector(self.locators.ADD_CUSTOMER_FORM_IFRAME)

            with self.frame_context(self.locators.ADD_CUSTOMER_FORM_IFRAME):
                self.stabilize_page()
                self.fill_customer_form(customer)
                self.click(self.locators.SAVE_AND_NEW_BUTTON)
                self.wait_for_selector(self.locators.SUCCESS_ADD_CUSTOMER_MESSAGE)
                logger.info("客户添加成功")

        except Exception as e:
            logger.error(f"添加客户时发生错误: {str(e)}")
            self.take_screenshot("add_customer_error")
            raise

    def search_customer(self, customer: Customer):
        """
        搜索客户
        :param customer: 客户数据对象
        """
        try:
            self.click(self.locators.CUSTOMER_LIST_PAGE)
            self.wait_for_iframe_ready()

            self.enter_frame(self.locators.CUSTOMER_LIST_IFRAME)
            self.page.wait_for_timeout(5000)
            self.stabilize_page()

            # 填写搜索条件
            self.fill(self.locators.SEARCH_CUSTOMER_NAME_INPUT, customer.name)
            if customer.type:
                self.fill(self.locators.SEARCH_CUSTOMER_TYPE_INPUT, customer.type)
            if customer.region:
                self.fill(self.locators.SEARCH_CUSTOMER_REGION_INPUT, customer.region)
            if customer.level:
                self.fill(self.locators.SEARCH_CUSTOMER_LEVEL_INPUT, customer.level)

            self.click(self.locators.SEARCH_CUSTOMER_BUTTON)
            self.page.wait_for_timeout(5000)
            self.wait_for_selector(self.locators.SEARCH_CUSTOMER_LIST)

        except Exception as e:
            logger.error(f"搜索客户时发生错误: {str(e)}")
            self.take_screenshot("search_customer_error")
            self.exit_frame()
            raise

    def is_customer_exists(self, customer: Customer) -> bool:
        """
        检查客户是否存在
        :param customer: 客户数据对象
        :return: 客户是否存在
        """
        try:
            self.search_customer(customer)
            return self.is_visible(self.locators.SEARCH_CUSTOMER_RESULT.format(customer=customer))
        except Exception as e:
            if "Timeout 10000ms exceeded." in str(e):
                logger.info("客户不存在")
                self.exit_frame()
                return False
            else:
                logger.error(f"检查客户是否存在时发生错误: {str(e)}")
                self.exit_frame()
                self.take_screenshot("check_customer_exists_error")
                raise

    def edit_customer(self, customer: Customer, updated_customer: Customer):
        """
        编辑客户信息
        :param customer: 原客户数据对象
        :param updated_customer: 更新的客户数据对象
        """
        try:
            self.search_customer(customer)

            with self.frame_context(self.locators.CUSTOMER_LIST_IFRAME):
                self.click(self.locators.SEARCH_CUSTOMER_RESULT_CHECK)
                self.click(self.locators.EDIT_CUSTOMER_BUTTON)

            self.wait_for_selector(self.locators.EDIT_CUSTOMER_FORM_IFRAME)

            with self.frame_context(self.locators.EDIT_CUSTOMER_FORM_IFRAME):
                self.stabilize_page()
                self.fill_customer_form(updated_customer)
                self.click(self.locators.SAVE_BUTTON)
                logger.info(f"客户 {customer.name} 更新成功")

        except Exception as e:
            logger.error(f"编辑客户时发生错误: {str(e)}")
            self.exit_frame()
            self.take_screenshot("edit_customer_error")
            raise

    def delete_customer(self, customer: Customer):
        """
        删除客户
        :param customer: 客户数据对象
        """
        try:
            self.search_customer(customer)

            with self.frame_context(self.locators.CUSTOMER_LIST_IFRAME):
                self.click(self.locators.SEARCH_CUSTOMER_RESULT_CHECK)
                self.click(self.locators.DELETE_CUSTOMER_BUTTON)

                self.wait_for_selector(self.locators.CONFIRM_DELETE_DIALOG)
                self.click(self.locators.CONFIRM_DELETE_YES)
                logger.info(f"客户 {customer.name} 删除成功")

        except Exception as e:
            if "Timeout 10000ms exceeded." in str(e):
                logger.info("客户不存在")
                return False
            logger.error(f"删除客户时发生错误: {str(e)}")
            self.exit_frame()
            self.take_screenshot("delete_customer_error")
            raise

    def view_customer(self, customer_data: Customer):
        """
        查看客户详情
        :param customer_data: 客户数据对象
        """
        logger.info(f"查看客户详情: {customer_data.name}")

        try:
            self.search_customer(customer_data)
            self.click(self.locators.SEARCH_CUSTOMER_RESULT.format(customer=customer_data))

            self.page.wait_for_timeout(3000)

            with self.frame_context(self.locators.CUSTOMER_DETAIL_IFRAME):
                self.stabilize_page()
                self.wait_for_selector(self.locators.CUSTOMER_DETAIL_CONTENT)

        except Exception as e:
            logger.error(f"查看客户详情时发生错误: {str(e)}")
            self.exit_frame()
            self.take_screenshot("view_customer_error")
            raise

    def is_customer_edited(
        self, original_customer: Customer, updated_customer: Customer
    ) -> bool:
        """
        检查客户是否被正确编辑
        :param original_customer: 原客户数据对象
        :param updated_customer: 更新后的客户数据对象
        :return: 客户信息是否被正确更新
        """
        try:
            self.search_customer(original_customer)

            with self.frame_context(self.locators.CUSTOMER_LIST_IFRAME):
                self.click(self.locators.SEARCH_CUSTOMER_RESULT_CHECK)
                self.click(self.locators.EDIT_CUSTOMER_BUTTON)

            self.wait_for_selector(self.locators.EDIT_CUSTOMER_FORM_IFRAME)

            with self.frame_context(self.locators.EDIT_CUSTOMER_FORM_IFRAME):
                self.stabilize_page()

                # 验证更新的字段
                field_mapping = {
                    "phone": self.locators.PHONE,
                    "qq": self.locators.QQ,
                    "source": self.locators.CUSTOMER_SOURCE,
                }

                for field, selector in field_mapping.items():
                    value = getattr(updated_customer, field, None)
                    if value is not None:
                        actual_value = self.get_input_value(selector)
                        if actual_value != value:
                            logger.error(f"字段 {field} 的值不匹配: 期望 {value}, 实际 {actual_value}")
                            return False

                return True

        except Exception as e:
            logger.error(f"验证客户编辑时发生错误: {str(e)}")
            self.exit_frame()
            self.take_screenshot("verify_customer_edit_error")
            raise
