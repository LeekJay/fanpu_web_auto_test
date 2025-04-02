"""
客户页面元素定位器
"""


class CustomerLocators:
    # 页面导航相关
    CUSTOMER_PAGE = "#Panel2_bodyRegion_topPanel_Panel1_17"  # 客户
    CUSTOMER_MENU = "span >> text=客户信息"  # 客户信息

    # 页面链接
    ADD_CUSTOMER_PAGE = 'a[href*="LoadForms.aspx"][href*="formid=646"][href*="ModuleID=30012928"]'  # 客户信息
    CUSTOMER_LIST_PAGE = 'a[href*="Loadlists.aspx"][href*="listid=391"][href*="ModuleID=30012822"]'  # 客户信息列表

    # iframe 相关
    SELECT_GRID_IFRAME = 'iframe[src*="SelectGrid.aspx"]'  # 选择搜索iframe
    CUSTOMER_LIST_IFRAME = 'iframe[src*="Loadlists.aspx"][src*="listid=391"][src*="ModuleID=30012822"]'  # 客户信息列表
    ADD_CUSTOMER_FORM_IFRAME = 'iframe[src*="LoadForms.aspx"][src*="formid=646"][src*="ModuleID=30012928"]'  # 新增客户
    EDIT_CUSTOMER_FORM_IFRAME = 'iframe[src*="LoadForms.aspx"][src*="formid=646"][src*="ModuleID=30012822"]'  # 修改客户
    CUSTOMER_DETAIL_IFRAME = 'iframe[src*="LoadForms.aspx"][src*="formid=646"][src*="Soflag=1"]'  # 客户详情

    # 搜索相关
    SEARCH_CUSTOMER_NAME_INPUT = "#Panel1_panelTop_k1397-inputEl"  # 客户名称
    SEARCH_CUSTOMER_TYPE_INPUT = "#Panel1_panelTop_k1398-inputEl"  # 客户分类
    SEARCH_CUSTOMER_REGION_INPUT = "#Panel1_panelTop_k1399-inputEl"  # 所在地区
    SEARCH_CUSTOMER_LEVEL_INPUT = "#Panel1_panelTop_k1400-inputEl"  # 客户等级
    SEARCH_CUSTOMER_BUTTON = "#Panel1_panelTop_BtnSearch"  # 搜索按钮
    SEARCH_CUSTOMER_LIST = 'tr.f-grid-row[data-rowid="frow0"]'  # 客户列表
    SEARCH_CUSTOMER_RESULT = 'a >> text="{customer.name}"'  # 客户结果
    SEARCH_CUSTOMER_RESULT_CHECK = 'td[data-columnid="fineui_14"]'  # 客户结果检查

    # 表单字段
    CUSTOMER_NAME = "#Panel2_ContentPanel1_mainTabs_Tab1_TabCpl1_mingcheng-inputEl"  # 客户名称
    CUSTOMER_TYPE = "#Panel2_ContentPanel1_mainTabs_Tab1_TabCpl1_leixing-inputEl"  # 客户分类
    CUSTOMER_CODE = "#Panel2_ContentPanel1_mainTabs_Tab1_TabCpl1_bianhao-inputEl"  # 客户编号
    INDUSTRY = "#Panel2_ContentPanel1_mainTabs_Tab1_TabCpl1_hangye-inputEl"  # 所属行业
    PHONE = "#Panel2_ContentPanel1_mainTabs_Tab1_TabCpl1_dianhua-inputEl"  # 电话
    REGION = "#Panel2_ContentPanel1_mainTabs_Tab1_TabCpl1_quyu-inputEl"  # 所在地区
    MOBILE = "#Panel2_ContentPanel1_mainTabs_Tab1_TabCpl1_shouji-inputEl"  # 手机
    SCALE = "#Panel2_ContentPanel1_mainTabs_Tab1_TabCpl1_guimo-inputEl"  # 规模
    QQ = "#Panel2_ContentPanel1_mainTabs_Tab1_TabCpl1_qq-inputEl"  # QQ
    CUSTOMER_SOURCE = "#Panel2_ContentPanel1_mainTabs_Tab1_TabCpl1_laiyuan-inputEl"  # 来源
    DEPARTMENT = "#Panel2_ContentPanel1_mainTabs_Tab1_TabCpl1_bumen-inputEl"  # 部门
    CUSTOMER_LEVEL = "#Panel2_ContentPanel1_mainTabs_Tab1_TabCpl1_dengji-inputEl"  # 客户等级

    # 负责人选择相关
    RESPONSIBLE_PERSON_SEARCH = "#Panel2_ContentPanel1_mainTabs_Tab1_TabCpl1_fzr i.f-triggerbox-trigger1.f-triggericon-search"  # 负责人搜索
    RESPONSIBLE_PERSON_INPUT = "#PanMain_Toolbar1_TextBox1-inputEl"  # 负责人输入
    RESPONSIBLE_PERSON_SEARCH_BTN = "#PanMain_Toolbar1_Button3"  # 负责人搜索按钮
    RESPONSIBLE_PERSON_SELECT_BTN = "#PanMain_Toolbar1_Button1"  # 负责人选择按钮
    RESPONSIBLE_PERSON_RESULT = 'div.f-grid-cell-inner >> text="{customer.responsible_person}"'  # 负责人结果

    # 共享人选择相关
    SHARED_PERSON = "#Panel2_ContentPanel1_mainTabs_Tab1_TabCpl1_gxr-inputEl"  # 共享人
    SHARED_PERSON_SEARCH = "#Panel2_ContentPanel1_mainTabs_Tab1_TabCpl1_gxr i.f-triggerbox-trigger1.f-triggericon-search"  # 共享人搜索
    SHARED_PERSON_SEARCH_INPUT = "#PanMain_Toolbar1_TextBox1-inputEl"  # 共享人搜索输入
    SHARED_PERSON_SEARCH_BTN = "#PanMain_Toolbar1_Button3"  # 共享人搜索按钮
    SHARED_PERSON_SELECT_BTN = "#PanMain_Toolbar1_Button1"  # 共享人选择按钮
    SHARED_PERSON_RESULT = 'div.f-grid-cell-inner >> text="{customer.shared_persons[0]}"'  # 共享人结果

    # 列表按钮（客户信息列表）
    EDIT_CUSTOMER_BUTTON = "#Panel1_Toolbar1_Button3"  # 修改
    DELETE_CUSTOMER_BUTTON = "#Panel1_Toolbar1_Button4"  # 删除

    # 表单按钮（客户信息表单）
    SAVE_BUTTON = "#Panel2_Toptb_Button2"  # 保存
    SAVE_AND_NEW_BUTTON = "#Panel2_Toptb_Button3"  # 保存并新增

    # 客户详情相关
    CUSTOMER_DETAIL_CONTENT = "#Panel2_ContentPanel1_MainTitleTD"  # 客户详情内容

    # 提示信息
    SUCCESS_ADD_CUSTOMER_MESSAGE = "div.f-messagebox-message >> text=保存数据成功！"  # 保存数据成功
    CONFIRM_DELETE_DIALOG = "div.f-messagebox-message >> text=是否确定要删除选中记录？"  # 是否确定要删除选中记录
    CONFIRM_DELETE_YES = "span.f-btn-text >> text=确定"  # 确定
