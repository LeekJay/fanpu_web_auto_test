"""
客户数据模型
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Customer:
    """客户数据类"""

    name: Optional[str] = None  # 客户名称
    type: Optional[str] = None  # 客户分类
    code: Optional[str] = None  # 客户编号
    industry: Optional[str] = None  # 所属行业
    phone: Optional[str] = None  # 电话
    region: Optional[str] = None  # 所在地区
    mobile: Optional[str] = None  # 手机
    scale: Optional[str] = None  # 规模
    qq: Optional[str] = None  # QQ
    source: Optional[str] = None  # 来源
    department: Optional[str] = None  # 部门
    level: Optional[str] = None  # 客户等级
    responsible_person: Optional[str] = None  # 负责人
    shared_persons: Optional[List[str]] = None  # 共享人

    def to_dict(self) -> dict:
        """转换为字典格式"""
        return {k: v for k, v in self.__dict__.items() if v is not None}
