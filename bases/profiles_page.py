# -*- coding:utf-8 -*-
"""
# FileName    : profiles_page.py
# CreateTime  : 2023 年 04 月 16 日
# Version     : 
# Description :
"""

# 联系方式窗口的相关元素
contact_info_block = '//*[@id="app"]/div/div/div[1]/div[1]/div[2]/div[7]/div' # 联系方式窗口
contact_hide_btn = '//*[@id="app"]/div/div/div[1]/div[1]/div[2]/div[7]/div/div[1]/div[2]/div/img' # 隐藏按钮
contact_copy_btn = '//*[@id="app"]/div/div/div[1]/div[1]/div[2]/div[7]/div/div[1]/span' # 复制按钮

# 发送合作邀约窗口相关元素
agree_or_wait_btn = '//*[@id="app"]/div/div/div[1]/div[1]/div[2]/div[6]/div[1]/span/button/span' # 已同意按钮 or 待回复
send_message = '//*[@id="app"]/div/div/div[1]/div[1]/div[2]/div[6]/div[1]/button/span' # 发送邀约按钮
send_me = '/html/body/div[4]/div/div[2]/div/div/div[3]/div/div[2]/button[1]/span' # 发送邀约
add_commodity = '/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/form/div[1]/div[2]/div[1]/button/span' # 点击添加商品
last_add_commodity = '/html/body/div[3]/div/div[2]/div/div/div[2]/div/div/form/div[1]/div[2]/div[2]/span[1]' # 点击上次邀约商品
cancel = '/html/body/div[3]/div/div[2]/div/div/div[3]/div/div[2]/button[2]/span' # 取消

# 达人个人资料的相关元素
daren_name = '//*[@id="app"]/div/div/div[1]/div[1]/div[2]/div[2]/div' # 达人的昵称
daren_fans = '//*[@id="app"]/div/div/div[1]/div[1]/div[2]/div[3]/div[1]' # 达人的粉丝数
daren_type = '//*[@id="app"]/div/div/div[1]/div[1]/div[2]/div[3]/div[3]' # 达人的标签
daren_city = 'daren-overview-base-traitblock__city' # 达人的地址