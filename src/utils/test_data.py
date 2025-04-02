"""
测试数据工具，用于生成和管理测试数据
"""

import json
import os
import random
from faker import Faker
from config.config import TEST_DATA_PATH
from models.customer import Customer
from models.loan import Loan


class TestData:
    """测试数据生成与管理类"""

    project_names = [
        "让我哥很温柔",
        "清远供电局500kV库湾站 等11个站点通信蓄电池远程核容装置加装",
        "沙塘村#3台区新建",
        "名润居10KV配电工程",
        "某某大厦",
        "A园区装饰项目",
        "湖南洞庭湖水库引水工程施工I标",
        "SM广场地下车库更换摄像机及硬盘项目",
        "广安邓小平纪念馆安全防范系统维护保养项目",
        "晟铭园林绿化工程",
        "重庆太极制药有限公司亳州中药材仓储物流基地项目成品仓库和设备仓库消防系统工程",
        "天津市应急管理局项目",
        "广佛高速",
        "重庆市鹅岭公园绿化景观提升工程施工",
        "贵阳项目样板间、大堂、电梯厅装修工程",
        "港珠澳大桥施工总承包项目",
        "龙湖三千里小区",
        "螺丝厂办公室装饰",
    ]

    person_name = [
        "陈菲",
        "陈丹",
        "陈华健",
        "蔡江平",
        "陈巧凤",
        "程亚雄",
        "杜春门",
        "邓琴",
        "邓林",
        "董清平",
        "断郎",
        "付安琼",
        "发生",
        "范思哲",
        "付伟璐",
        "胡建",
        "黄敏",
        "黄思璐",
        "胡广生",
        "胡雪",
        "胡学辉",
        "黄小强",
        "黄燕",
        "黄一飞",
        "何芷茵",
        "蒋德帧",
        "蒋丽",
        "金伟",
        "柯英",
        "龙波",
        "罗成",
        "罗丹",
        "刘东林",
        "罗广明",
        "李红",
        "李华",
        "李朗",
        "李帅",
        "李婷",
        "刘健",
        "李佳怡",
        "林康平",
        "柳琳",
        "李林辉",
        "李勤丽",
        "李若若",
        "罗静",
        "李卫东",
        "罗毅",
        "马东",
        "孟浩",
        "任晓渠",
        "任晓燕",
        "宋浩然",
        "陶伟",
        "田静",
        "王可可",
        "吴彪",
        "王伟健",
        "王志远",
        "薛保丰",
        "薛宝峰",
        "肖晴",
        "熊三林",
        "许利",
        "徐贤",
        "肖亚军",
        "阳强",
        "杨彪",
        "野朝阳",
        "游恢",
        "袁鑫",
        "余小琴",
        "苑子豪",
        "张成功",
        "张浩",
        "郑义",
        "臻逸",
        "周琳",
        "曾晚霞",
        "张鑫",
        "张小东",
        "章燕",
        "张永银",
    ]

    def __init__(self, locale="zh_CN"):
        """
        初始化测试数据生成器
        :param locale: 区域设置，默认为中文
        """
        self.faker = Faker(locale)

    def generate_customer_data(self) -> Customer:
        """
        生成客户数据
        :return: 客户数据字典
        """
        # 客户类型选项
        customer_types = ["民营企业", "外资企业", "事业单位", "政府单位"]
        # 行业选项
        industries = [
            "农林牧渔",
            "医药卫生",
            "建筑建材",
            "冶金矿产",
            "石油化工",
            "水利水电",
            "交通运输",
            "信息产业",
            "机械机电",
            "轻工食品",
            "服装纺织",
            "安全防护",
            "环保绿化",
            "旅游休闲",
            "办公文教",
        ]
        # 区域选项
        regions = ["华南", "华东", "亚洲", "美洲"]
        # 规模选项
        scales = ["大", "中", "小", "其他"]
        # 客户来源
        sources = ["电话营销", "客户介绍", "朋友介绍", "百度广告", "公开招标"]
        # 部门选项
        departments = [
            "总经办",
            "经营部",
            "财务部",
            "工程部",
            "材料采购",
            "机械队",
            "成本核算部",
            "项目中心",
            "成都项目部",
            "项目一部",
            "项目二部",
            "项目三部",
            "贵阳项目部",
            "西安项目部",
            "遵义项目部",
            "行政部",
            "营销部",
            "重庆分公司",
            "人事部",
            "市场营销部",
            "工程管理部",
            "成控采购部",
            "重庆项目部",
            "人事部",
            "采购部",
            "设计部",
            "材料部",
            "市场部",
            "开发",
        ]
        # 客户等级
        levels = ["1星", "2星", "3星", "4星", "5星"]

        return Customer(
            name=self.faker.company(),  # 使用公司名称
            type=random.choice(customer_types),  # 客户类型
            code=f"CUS{self.faker.random_number(digits=6)}",  # 生成6位客户编号
            industry=random.choice(industries),  # 所属行业
            phone=self.faker.phone_number(),  # 电话
            region=random.choice(regions),  # 所属区域
            mobile=self.faker.phone_number(),  # 手机
            scale=random.choice(scales),  # 规模
            qq=str(self.faker.random_number(digits=9)),  # 生成QQ号
            source=random.choice(sources),  # 客户来源
            department=random.choice(departments),  # 所属部门
            level=random.choice(levels),  # 客户等级
            responsible_person="张鑫",  # 负责人姓名
            shared_persons=random.sample(
                self.person_name, k=random.randint(1, 6)
            ),  # 共享人姓名（多选1-6人）
        )

    def generate_loan_data(self) -> Loan:
        """
        生成借款申请数据
        :return: 借款申请数据字典
        """
        payment_methods = ["现金支付", "银行转账", "支票支付"]
        repayment_methods = ["等额本息", "等额本金", "先息后本", "一次性还本付息"]

        return Loan(
            project_name=random.choice(self.project_names),  # 项目名称
            borrower=random.choice(self.person_name),  # 借款人
            loan_amount=str(round(random.uniform(10000, 1000000))),  # 借款金额
            loan_purpose=self.faker.sentence(),  # 借款事由
            payment_method=random.choice(payment_methods),  # 支付方式
            repayment_method=random.choice(repayment_methods),  # 还款方式
            loan_period=self.faker.date_this_year().strftime("%Y-%m-%d"),  # 借款日期
            borrower_bank=self.faker.bank(),  # 借款人开户银行
            bank_account="".join(
                [str(random.randint(0, 9)) for _ in range(19)]
            ),  # 借款人银行账号
            bank_branch=self.faker.address(),  # 开户银行地址
            handler="张鑫",  # 经办人
            application_date=self.faker.date_this_year().strftime(
                "%Y-%m-%d"
            ),  # 申请日期
            account_name=self.faker.bank(),  # 开户行名称
            bank_account_number="".join(
                [str(random.randint(0, 9)) for _ in range(19)]
            ),  # 银行账户
        )

    def load_test_data(self, file_path=TEST_DATA_PATH):
        """
        从文件加载测试数据
        :param file_path: 测试数据文件路径
        :return: 测试数据
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"加载测试数据失败: {e}")
            return None

    def save_test_data(self, data, file_path=TEST_DATA_PATH):
        """
        保存测试数据到文件
        :param data: 测试数据
        :param file_path: 测试数据文件路径
        """
        dir_path = os.path.dirname(file_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"保存测试数据失败: {e}")


# 创建全局测试数据生成器实例
test_data_generator = TestData()
