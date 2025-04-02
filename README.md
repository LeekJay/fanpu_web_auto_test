# Web自动化测试项目 🚀

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.51.0-green)](https://playwright.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-8.3.5-red)](https://docs.pytest.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> 本项目是一个基于Python的Web自动化测试框架，主要针对 [泛普软件 demo 网站](demo.fanpusoft.com) 的用户管理模块和借款申请模块进行自动化测试。

## ✨ 特性

- 🎯 完整的用户管理和借款申请模块测试
- 📝 详细的测试报告（支持HTML和Allure）
- 🔄 跨浏览器测试支持
- 🛠️ 页面对象模式（POM）设计
- 📊 动态测试数据生成

## 📋 测试模块

### 1. 用户管理模块 👥

- ✅ **添加客户**：验证系统是否能够成功添加新客户
- 👀 **查看客户**：验证系统是否能够正确显示客户详细信息
- 📝 **修改客户**：验证系统是否能够成功修改客户信息
- ❌ **删除客户**：验证系统是否能够成功删除客户信息

### 2. 借款申请模块 💰

- ➕ **新增借款申请**：验证系统是否能够成功添加新的借款申请
- 🔍 **查看借款申请**：验证系统是否能够正确显示借款申请的详细信息
- ✏️ **修改借款申请**：验证系统是否能够成功修改借款申请信息
- 🗑️ **删除借款申请**：验证系统是否能够成功删除借款申请

## 🛠️ 技术栈

- Python 3.11+
- Playwright 1.51.0
- Pytest 8.3.5
- Allure (用于测试报告)

## 📁 项目结构

```bash
web_auto_test/
├── src/
│   ├── config/                      # 配置文件目录
│   │   └── config.py                # 配置参数
│   ├── models/                      # 数据模型目录
│   │   ├── customer.py              # 客户数据模型
│   │   └── loan_page.py             # 借款数据模型
│   ├── locators/                    # 页面元素定位器目录
│   │   ├── customer_locators.py     # 客户页面元素定位器
│   │   ├── loan_locators.py         # 借款页面元素定位器
│   │   └── login_locators.py        # 登录页面元素定位器
│   ├── pages/                       # 页面对象模式目录
│   │   ├── base_page.py             # 基础页面类
│   │   ├── customer_page.py         # 客户管理页面
│   │   └── loan_page.py             # 借款申请页面
│   ├── tests/                       # 测试用例目录
│   │   ├── conftest.py              # Pytest配置
│   │   ├── test_customer.py         # 客户管理测试用例
│   │   └── test_loan.py             # 借款申请测试用例
│   └── utils/                       # 工具类
│       ├── browser_factory.py       # 浏览器工厂
│       ├── logger.py                # 日志工具
│       └── test_data.py             # 测试数据生成
├── reports/                         # 测试报告目录
├── pytest.ini                       # 测试配置
├── requirements.txt                 # 项目依赖
└── README.md                        # 项目说明文档
```

## 🚀 快速开始

### 1. 环境准备

首先创建并激活虚拟环境：

```bash
# 使用 venv
python -m venv venv

# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# 或使用 Conda
conda create -n web_auto_test python=3.11
conda activate web_auto_test
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 安装Playwright浏览器

```bash
playwright install
```

## 🧪 运行测试

### 运行全部测试

```bash
pytest
```

### 运行特定模块测试

```bash
# 运行用户管理模块测试
pytest tests/test_customer.py

# 运行借款申请模块测试
pytest tests/test_loan.py
```

### 生成测试报告

```bash
# 生成HTML报告
pytest --html=reports/report.html

# 生成Allure报告
pytest --alluredir=./reports/allure
allure serve ./reports/allure
```

## ⚙️ 配置说明

在 `config/config.py` 中可以设置以下配置：

| 配置项 | 说明 |
|--------|------|
| URL | 目标网站URL |
| 浏览器类型 | Chrome/Firefox/Safari |
| 超时时间 | 页面加载超时设置 |
| 截图路径 | 失败截图保存位置 |
| 登录凭据 | 测试账号信息 |

## 🎯 项目特性

1. **跨浏览器测试** 🌐
   - 支持Chrome、Firefox和Safari浏览器
   - 支持无头模式运行

2. **智能测试** 🧠
   - 参数化测试
   - 动态测试数据生成
   - 自动失败重试

3. **完善的报告** 📊
   - HTML报告
   - Allure报告
   - 失败自动截图

4. **数据管理** 📝
   - 使用Faker库生成测试数据
   - 支持外部数据源
   - 灵活的数据模型

## 📝 测试流程

1. 🚀 启动浏览器并创建页面对象
2. 🔐 登录系统
3. 📊 生成测试数据
4. ▶️ 执行测试操作
5. ✅ 验证测试结果
6. 📋 生成测试报告

## 🤝 贡献

欢迎提交问题和改进建议！

## 📄 开源协议

本项目采用 MIT 协议开源，详情请参阅 [LICENSE](LICENSE) 文件。
