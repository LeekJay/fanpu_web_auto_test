"""
客户管理模块测试用例
"""

import allure
import pytest
from assertpy import assert_that
from models.customer import Customer
from utils.test_data import test_data_generator
from pages.customer_page import CustomerPage


@allure.epic("客户管理模块")
@pytest.mark.usefixtures("shared_customer_data")
class TestCustomer:
    """客户管理模块测试类"""

    def ensure_customer_exists(self, customer_page: CustomerPage, shared_customer_data):
        """确保测试客户存在，如果不存在则创建"""
        customer_page.navigate_to_customer_page()
        customer_page.click_customer_menu()
        if not shared_customer_data:
            customer_data = test_data_generator.generate_customer_data()
            customer_page.add_customer(customer_data)
            assert_that(customer_page.is_customer_exists(customer_data)).is_true()
            shared_customer_data.update(vars(customer_data))
            customer_page.exit_frame()
        return Customer(**shared_customer_data)

    @pytest.mark.order(1)
    @allure.feature("添加客户")
    @allure.story("成功添加客户")
    @allure.title("测试添加新客户功能")
    def test_add_customer(self, customer_page: CustomerPage, shared_customer_data):
        """测试添加客户功能"""
        with allure.step("生成测试客户数据"):
            customer_data = test_data_generator.generate_customer_data()

        with allure.step("导航到客户管理页面"):
            customer_page.navigate_to_customer_page()

        with allure.step("点击客户管理菜单"):
            customer_page.click_customer_menu()

        with allure.step("添加新客户"):
            customer_page.add_customer(customer_data)

        with allure.step("验证客户是否添加成功"):
            assert_that(customer_page.is_customer_exists(customer_data)).is_true()

        with allure.step("保存客户数据供后续测试使用"):
            shared_customer_data.update(vars(customer_data))

    @pytest.mark.order(2)
    @allure.feature("查看客户")
    @allure.story("查看客户详情")
    @allure.title("测试查看客户详情功能")
    def test_view_customer(self, customer_page: CustomerPage, shared_customer_data):
        """测试查看客户详情功能"""
        with allure.step("确保测试客户存在"):
            customer_data = self.ensure_customer_exists(customer_page, shared_customer_data)

        with allure.step("查看客户详情"):
            customer_page.view_customer(customer_data)

        with allure.step("验证客户详情是否正确显示"):
            assert_that(customer_page.is_visible(customer_page.locators.CUSTOMER_DETAIL_IFRAME)).is_true()

    @pytest.mark.order(3)
    @allure.feature("修改客户")
    @allure.story("修改客户信息")
    @allure.title("测试修改客户信息功能")
    def test_edit_customer(self, customer_page: CustomerPage, shared_customer_data):
        """测试修改客户信息功能"""
        with allure.step("确保测试客户存在"):
            customer_data = self.ensure_customer_exists(customer_page, shared_customer_data)

        with allure.step("修改客户信息"):
            updated_data = Customer(
                phone=test_data_generator.generate_customer_data().phone,
                qq=test_data_generator.generate_customer_data().qq,
                source=test_data_generator.generate_customer_data().source,
            )
            customer_page.edit_customer(customer_data, updated_data)

        with allure.step("验证客户信息是否更新成功"):
            assert_that(
                customer_page.is_customer_edited(customer_data, updated_data)
            ).is_true()

        with allure.step("更新共享的客户数据"):
            updated_fields = {k: v for k, v in vars(updated_data).items() if v is not None}
            current_data = vars(customer_data)
            current_data.update(updated_fields)
            shared_customer_data.update(current_data)

    @pytest.mark.order(4)
    @allure.feature("删除客户")
    @allure.story("删除客户信息")
    @allure.title("测试删除客户功能")
    def test_delete_customer(self, customer_page: CustomerPage, shared_customer_data):
        """测试删除客户功能"""
        with allure.step("确保测试客户存在"):
            customer_data = self.ensure_customer_exists(customer_page, shared_customer_data)

        with allure.step("删除客户"):
            customer_page.delete_customer(customer_data)

        with allure.step("验证客户是否删除成功"):
            assert_that(customer_page.is_customer_exists(customer_data)).is_false()
