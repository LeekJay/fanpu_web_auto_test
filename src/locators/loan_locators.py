"""
借款页面元素定位器
"""


class LoanLocators:
    # 页面导航相关
    LOAN_PAGE = "#Panel2_bodyRegion_topPanel_Panel1_23"  # 财务
    LOAN_MENU = "span >> text=借支管理"  # 借支管理

    # 页面链接
    LOAN_LIST_PAGE = 'a[href*="Loadlists.aspx"][href*="listid=10643"][href*="ModuleID=30013823"]'  # 借款申请列表

    # iframe 相关
    SELECT_GRID_IFRAME = 'iframe[src*="SelectGrid.aspx"]'  # 选择搜索iframe
    LOAN_LIST_IFRAME = 'iframe[src*="Loadlists.aspx"][src*="listid=10643"][src*="ModuleID=30013823"]'  # 借款申请列表
    ADD_LOAN_FORM_IFRAME = 'iframe[src*="LoadForms.aspx"][src*="formid=2879"][src*="ModuleID=30013823"]'  # 新增借款申请
    EDIT_LOAN_FORM_IFRAME = 'iframe[src*="LoadForms.aspx"][src*="formid=2879"][src*="ModuleID=30013823"]'  # 修改借款申请
    LOAN_DETAIL_IFRAME = 'iframe[src*="LoadForms.aspx"][src*="formid=2879"][src*="Soflag=1"]'  # 借款申请详情

    # 搜索相关
    SEARCH_LOAN_PROJECT_NAME = "#Panel1_panelTop_k12578-inputEl"  # 项目名称
    SEARCH_LOAN_BORROWER = "#Panel1_panelTop_k12579-inputEl"  # 借款人
    SEARCH_LOAN_PERIOD_START = "#Panel1_panelTop_k12580-inputEl"  # 借款日期开始
    SEARCH_LOAN_PERIOD_END = "#Panel1_panelTop_k12580_end-inputEl"  # 借款日期结束
    SEARCH_LOAN_BUTTON = "#Panel1_panelTop_BtnSearch"  # 搜索
    SEARCH_LOAN_LIST = 'tr.f-grid-row[data-rowid="frow0"]'  # 借款申请列表
    SEARCH_LOAN_RESULT = 'a >> text="{loan.borrower}"'  # 借款申请结果
    SEARCH_LOAN_RESULT_CHECK = 'td[data-columnid="fineui_14"]'  # 借款申请结果项目名称

    # 表单字段
    PROJECT_NAME = "#Panel2_ContentPanel1_xmmc-inputEl"  # 项目名称
    BORROWER = "#Panel2_ContentPanel1_jkr-inputEl"  # 借款人
    LOAN_AMOUNT = "#Panel2_ContentPanel1_je-inputEl"  # 借款金额
    LOAN_PURPOSE = "#Panel2_ContentPanel1_jksy-inputEl"  # 借款事由
    PAYMENT_METHOD = "#Panel2_ContentPanel1_zffs-inputEl"  # 支付方式
    REPAYMENT_METHOD = "#Panel2_ContentPanel1_hkfs-inputEl"  # 还款方式
    LOAN_PERIOD = "#Panel2_ContentPanel1_jkrq-inputEl"  # 借款日期
    BORROWER_BANK = "#Panel2_ContentPanel1_khyh-inputEl"  # 借款人开户银行
    BANK_ACCOUNT = "#Panel2_ContentPanel1_yhzh-inputEl"  # 借款人银行账号
    BANK_BRANCH = "#Panel2_ContentPanel1_dz-inputEl"  # 开户银行地址
    HANDLER = "#Panel2_ContentPanel1_jbr-inputEl"  # 经办人
    APPLICATION_DATE = "#Panel2_ContentPanel1_sqrq-inputEl"  # 申请日期
    ACCOUNT_NAME = "#Panel2_ContentPanel1_khh-inputEl"  # 开户行名称
    BANK_ACCOUNT_NUMBER = "#Panel2_ContentPanel1_zh-inputEl"  # 银行账户

    # 项目名称相关
    PROJECT_SEARCH = "#Panel2_ContentPanel1_xmmc i.f-triggerbox-trigger1.f-triggericon-search"  # 项目名称搜索
    PROJECT_SEARCH_INPUT = "#PanMain_Toolbar1_TextBox1-inputEl"  # 项目名称搜索输入
    PROJECT_SEARCH_BTN = "#PanMain_Toolbar1_Button3"  # 项目名称搜索按钮
    PROJECT_SELECT_BTN = "#PanMain_Toolbar1_Button1"  # 项目名称选择按钮
    PROJECT_RESULT = 'div.f-grid-cell-inner >> text={loan.project_name}'  # 项目名称结果

    # 借款人相关
    BORROWER_SEARCH = "#Panel2_ContentPanel1_jkr i.f-triggerbox-trigger1.f-triggericon-search"  # 借款人搜索
    BORROWER_SEARCH_INPUT = "#PanMain_Toolbar1_TextBox1-inputEl"  # 借款人搜索输入
    BORROWER_SEARCH_BTN = "#PanMain_Toolbar1_Button3"  # 借款人搜索按钮
    BORROWER_SELECT_BTN = "#PanMain_Toolbar1_Button1"  # 借款人选择按钮
    BORROWER_RESULT = 'div.f-grid-cell-inner >> text={loan.borrower}'  # 借款人结果

    # 经办人相关
    HANDLER_SEARCH = "#Panel2_ContentPanel1_jbr i.f-triggerbox-trigger1.f-triggericon-search"  # 经办人搜索
    HANDLER_SEARCH_INPUT = "#PanMain_Toolbar1_TextBox1-inputEl"  # 经办人搜索输入
    HANDLER_SEARCH_BTN = "#PanMain_Toolbar1_Button3"  # 经办人搜索按钮
    HANDLER_SELECT_BTN = "#PanMain_Toolbar1_Button1"  # 经办人选择按钮
    HANDLER_RESULT = 'div.f-grid-cell-inner >> text={loan.handler}'  # 经办人结果

    # 列表按钮（借款申请列表）
    ADD_LOAN_BUTTON = "#Panel1_Toolbar1_Button2"  # 新增
    EDIT_LOAN_BUTTON = "#Panel1_Toolbar1_Button3"  # 修改
    DELETE_LOAN_BUTTON = "#Panel1_Toolbar1_Button4"  # 删除

    # 表单按钮（借款申请表单）
    SAVE_BUTTON = "#Panel2_Toptb_Button2"  # 保存
    SAVE_AND_NEW_BUTTON = "#Panel2_Toptb_Button3"  # 保存并新增

    # 借款申请详情相关
    LOAN_DETAIL_CONTENT = "#Panel2_ContentPanel1_MainTitleTD"  # 借款申请详情内容

    # 提示信息
    SUCCESS_ADD_LOAN_MESSAGE = "div.f-messagebox-message >> text=保存数据成功！"  # 保存数据成功
    SUCCESS_EDIT_LOAN_MESSAGE = "div.f-messagebox-message >> text=保存数据成功！"  # 修改数据成功
    CONFIRM_DELETE_DIALOG = "div.f-messagebox-message >> text=是否确定要删除选中记录？"  # 是否确定要删除选中记录
    CONFIRM_DELETE_YES = "span.f-btn-text >> text=确定"  # 确定
