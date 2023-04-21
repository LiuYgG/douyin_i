"""
# FileName    : send_invitation_page.py
# CreateTime  : 2023 年 04 月 22 日
# Version     : 0.0.1
# Description : 发送合作邀约小窗口
"""

# 添加商品按钮[1]
add_operate_btn_class = 'add-product-operate'
# 添加商品按钮[2] - 定位到button
add_operate_btn_xpath = '/html/body/div[3]/div/div[2]/div/div/div[2]/div/div/form/div[1]/div[2]/div[1]/button'
# 添加商品按钮[3] - 定位到span
add_operate_btn_span_xpath = '/html/body/div[3]/div/div[2]/div/div/div[2]/div/div/form/div[1]/div[2]/div[1]/button/span'

# 添加上次邀约商品[1]
add_last_operate_class = 'add-product-last-operate'
# 添加上次邀约商品[2]
add_last_operate_xpath = '/html/body/div[3]/div/div[2]/div/div/div[2]/div/div/form/div[1]/div[2]/div[2]/span[1]'


# 发送邀约按钮[1]
send_invitation_btn_class = 'auxo-btn-primary'
# 发送邀约按钮[2] - 定位到button
send_invitation_btn_xpath = '/html/body/div[3]/div/div[2]/div/div/div[3]/div/div[2]/button[1]'
# 发送邀约按钮[3] - 定位到span
send_invitation_btn_span_xpath = '/html/body/div[3]/div/div[2]/div/div/div[3]/div/div[2]/button[1]/span'

# 取消按钮[1]
send_cancel_class = 'auxo-btn'
# 取消按钮[2] - 定位到button
send_cancel_xpath = '/html/body/div[3]/div/div[2]/div/div/div[3]/div/div[2]/button[2]'
# 取消按钮[3] - 定位到span
send_cancel_span_xpath = '/html/body/div[3]/div/div[2]/div/div/div[3]/div/div[2]/button[2]/span'