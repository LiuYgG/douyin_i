"""
# FileName    : add_operate_window.py
# CreateTime  : 2023 年 04 月 22 日
# Version     : 
# Description : 发送合作邀约窗口 - 添加商品
"""

# 品牌列表 item [1] - 使用索引的方式进行选择
colonel_item_class = 'colonel__left-card'

# 品牌 - 商品全选按钮[1] : 使用索引方式选择
colonel_item_checkall_class = 'auxo-table-selection'
# 品牌 - 商品全选按钮[2] : 定位到 span
colonel_item_checkall_span_xpath = '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/table/thead/tr/th[1]/div/label/span'
# 品牌 - 商品全选按钮[3] : 定位到 input
colonel_item_checkall_input_xpath = '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/table/thead/tr/th[1]/div/label/span/input'

# 品牌 - 商品单选按钮[1] : 使用索引方式选择
colonel_item_checkbox_class = 'auxo-checkbox-wrapper'
# 品牌 - 商品单选按钮[2] : 定位到 span
colonel_item_checkbox_span_xpath = '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[1]/label/span'
# 品牌 - 商品单选按钮[3] : 定位到 input
colonel_item_checkbox_input_xpath = '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[1]/label/span/input'