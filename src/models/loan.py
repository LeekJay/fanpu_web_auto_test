"""
借款数据模型
"""

from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Loan:
    """借款数据类"""

    project_name: Optional[str] = None  # 项目名称
    borrower: Optional[str] = None  # 借款人
    loan_amount: Optional[str] = None  # 借款金额
    loan_purpose: Optional[str] = None  # 借款事由
    payment_method: Optional[str] = None  # 支付方式
    repayment_method: Optional[str] = None  # 还款方式
    loan_period: Optional[datetime] = None  # 借款日期
    borrower_bank: Optional[str] = None  # 借款人开户银行
    bank_account: Optional[str] = None  # 借款人银行账号
    bank_branch: Optional[str] = None  # 开户银行地址
    handler: Optional[str] = None  # 经办人
    application_date: Optional[datetime] = None  # 申请日期
    account_name: Optional[str] = None  # 开户行名称
    bank_account_number: Optional[str] = None  # 银行账户

    def to_dict(self) -> dict:
        """转换为字典格式"""
        return {k: v for k, v in self.__dict__.items() if v is not None}

    @property
    def is_valid(self) -> bool:
        """
        验证必填字段是否已填写
        :return: 是否有效
        """
        required_fields = [
            self.project_name,
            self.borrower,
            self.loan_amount,
            self.loan_purpose,
        ]
        return all(field is not None for field in required_fields)
