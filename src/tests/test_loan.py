"""
借款管理模块测试用例
"""

import allure
import pytest
from assertpy import assert_that
from models.loan import Loan
from utils.test_data import test_data_generator
from pages.loan_page import LoanPage


@allure.epic("借款管理模块")
@pytest.mark.usefixtures("shared_loan_data")
class TestLoan:
    """借款管理模块测试类"""

    def ensure_loan_exists(self, loan_page: LoanPage, shared_loan_data):
        """确保测试借款存在，如果不存在则创建"""
        loan_page.navigate_to_loan_page()
        loan_page.click_loan_menu()
        loan_page.click_loan_list()
        if not shared_loan_data:
            loan_data = test_data_generator.generate_loan_data()
            loan_page.add_loan(loan_data)
            assert_that(loan_page.is_loan_exists(loan_data)).is_true()
            shared_loan_data.update(vars(loan_data))
            loan_page.exit_frame()
        return Loan(**shared_loan_data)

    @pytest.mark.order(5)
    @allure.feature("添加借款")
    @allure.story("成功添加借款")
    @allure.title("测试添加新借款功能")
    def test_add_loan(self, loan_page: LoanPage, shared_loan_data):
        """测试添加借款功能"""
        with allure.step("生成测试借款数据"):
            loan_data = test_data_generator.generate_loan_data()

        with allure.step("导航到借款管理页面"):
            loan_page.navigate_to_loan_page()

        with allure.step("点击借款管理菜单"):
            loan_page.click_loan_menu()

        with allure.step("点击借款申请列表"):
            loan_page.click_loan_list()

        with allure.step("添加新借款"):
            loan_page.add_loan(loan_data)

        with allure.step("验证借款是否添加成功"):
            assert_that(loan_page.is_loan_exists(loan_data)).is_true()

        with allure.step("保存借款数据供后续测试使用"):
            shared_loan_data.update(vars(loan_data))

    @pytest.mark.order(6)
    @allure.feature("查看借款")
    @allure.story("查看借款详情")
    @allure.title("测试查看借款详情功能")
    def test_view_loan(self, loan_page: LoanPage, shared_loan_data):
        """测试查看借款详情功能"""

        with allure.step("确保测试借款存在"):
            loan_data = self.ensure_loan_exists(loan_page, shared_loan_data)

        with allure.step("查看借款详情"):
            loan_page.view_loan(loan_data)

        with allure.step("验证借款详情是否正确显示"):
            assert_that(loan_page.is_visible(loan_page.locators.LOAN_DETAIL_IFRAME)).is_true()

    @pytest.mark.order(7)
    @allure.feature("修改借款")
    @allure.story("修改借款信息")
    @allure.title("测试修改借款信息功能")
    def test_edit_loan(self, loan_page: LoanPage, shared_loan_data):
        """测试修改借款信息功能"""

        with allure.step("确保测试借款存在"):
            loan_data = self.ensure_loan_exists(loan_page, shared_loan_data)

        with allure.step("修改借款信息"):
            updated_data = Loan(
                loan_amount=test_data_generator.generate_loan_data().loan_amount,  # 借款金额
                loan_purpose=test_data_generator.generate_loan_data().loan_purpose,  # 借款事由
                payment_method=test_data_generator.generate_loan_data().payment_method,  # 支付方式
                repayment_method=test_data_generator.generate_loan_data().repayment_method,  # 还款方式
            )
            loan_page.edit_loan(loan_data, updated_data)

        with allure.step("验证借款信息是否更新成功"):
            assert_that(loan_page.is_loan_edited(loan_data, updated_data)).is_true()

        with allure.step("更新共享的借款数据"):
            updated_fields = {
                k: v for k, v in vars(updated_data).items() if v is not None
            }
            current_data = vars(loan_data)
            current_data.update(updated_fields)
            shared_loan_data.update(current_data)

    @pytest.mark.order(8)
    @allure.feature("删除借款")
    @allure.story("删除借款信息")
    @allure.title("测试删除借款功能")
    def test_delete_loan(self, loan_page: LoanPage, shared_loan_data):
        """测试删除借款功能"""
        with allure.step("确保测试借款存在"):
            loan_data = self.ensure_loan_exists(loan_page, shared_loan_data)

        with allure.step("删除借款"):
            loan_page.delete_loan(loan_data)

        with allure.step("验证借款是否删除成功"):
            assert_that(loan_page.is_loan_exists(loan_data)).is_false()
