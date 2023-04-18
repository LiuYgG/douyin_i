# -*- coding:utf-8 -*-
"""
# FileName    : daren_profile_data.py
# CreateTime  : 2023 年 04 月 11 日
# Version     : 
# Description :
"""
import datetime

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import openpyxl
import time
from bases import profiles_page


class DarenProfiles():

    def __init__(self):
        # 创建一个 workbook 对象
        self.workbook = openpyxl.Workbook()
        # 创建一个 worksheet 对象
        self.worksheet = self.workbook.active
        # 指定服务器
        self.options = Options()
        # 服务器地址
        self.options.add_experimental_option("debuggerAddress", "127.0.0.1:5247")
        # 打开浏览器
        self.driver_path = 'drivers/112.0.5615.50_chromedriver.exe'
        self.d = webdriver.Chrome(executable_path=self.driver_path, options=self.options)
        self.data_list = []

    def run(self):
        self.setup_worksheet()
        self.get_daren_info()
        self.write_to_worksheet()
        self.save_workboot()

    def setup_worksheet(self):

        # 设置列名
        self.worksheet.cell(row=1, column=1, value='姓名')
        self.worksheet.cell(row=1, column=2, value='联系方式')
        self.worksheet.cell(row=1, column=3, value='粉丝数')
        self.worksheet.cell(row=1, column=4, value='网址')

    def get_daren_info(self):

        # 达人列表
        # self.d.get('https://buyin.jinritemai.com/dashboard/servicehall/daren-square')
        # 循环次数定义
        nicke_name_elements = self.d.find_elements(By.CLASS_NAME, 'list-table-info-right-name__nickname')
        time.sleep(3)
        count = int(input("请输入你要爬取的人数: "))
        # 循环获取
        for i in range(len(nicke_name_elements)):
            if i == count:
                break
            try:

                self.daren = nicke_name_elements[i].click()
                count += 1
                # 获取所有打开的浏览器窗口
                handle_tab_all = self.d.window_handles
                # 获取当前浏览器的窗口
                self.d.current_window_handle
                # print("当前浏览器窗口" + handle_tab_singe)
                self.d.switch_to.window(handle_tab_all[1])
                time.sleep(5)
                '''
                若不支持邀约则抛出异常并继续下面的操作， 否则点击【发送邀约】
                '''
                try:
                    send_message = self.d.find_element(By.XPATH, profiles_page.send_message)  # 发送邀约按钮
                    '''
                    发送邀约判断
                    '''
                    if send_message is not None:
                        time.sleep(3)
                        # 点击发送邀约
                        send_message.click()
                        time.sleep(3)
                        # 点击上次邀约商品
                        last_add_commodity = self.d.find_element(By.XPATH, profiles_page.last_add_commodity)
                        last_add_commodity.click()
                        time.sleep(3)
                        # 点击取消
                        cancel = self.d.find_element(By.XPATH, profiles_page.cancel)
                        cancel.click()
                except Exception as s:
                    print(f'发送邀约异常错误信息：{s}')

                time.sleep(5)
                '''
                 联系方式相关操作
                '''
                try:
                    contact_info_block = self.d.find_element(By.XPATH, profiles_page.contact_info_block)
                    if contact_info_block is not None:
                        contact_hide_btn = self.d.find_elements(By.CLASS_NAME, 'img-default-wrapper')
                        # time.sleep(3)
                        for h in range(len(contact_hide_btn)):
                            if h == 3:
                                break
                            time.sleep(2)
                            contact_hide_btn[h].click()
                        print(contact_info_block.text)
                        print('-' * 30)
                    else:
                        print("此用户没有联系方式: ", self.d.find_element(By.XPATH, profiles_page.daren_name).text)
                        time.sleep(2)
                        # 关闭窗口
                        self.d.close()
                        self.d.switch_to.window((handle_tab_all[0]))
                except Exception as c:
                    print(f"联系方式异常错误信息: {c}")
                    time.sleep(3)
                    daren_name = self.d.find_element(By.XPATH, profiles_page.daren_name).text  # 达人的昵称
                    daren_fans = self.d.find_element(By.XPATH, profiles_page.daren_fans).text  # 达人的粉丝数
                    daren_type = self.d.find_element(By.XPATH, profiles_page.daren_type).text  # 达人的标签
                    daren_city = self.d.find_element(By.CLASS_NAME, profiles_page.daren_city).text  # 达人的地址
                    daren_contact = contact_info_block.text  # 达人的联系方式
                    print(
                        f'姓名：{daren_name} | 联系方式: {daren_contact} | 粉丝数：{daren_fans}|{daren_type}|{daren_city}|网址：{self.d.current_url}')
                    self.data_list.append({'姓名': daren_name,
                                           '联系方式': daren_contact,
                                           '粉丝数': daren_fans + '·' + daren_type + '·' + daren_city,
                                           '网址': self.d.current_url})
                    time.sleep(1)
                    print(f"已联系: [ {i + 1} ]个")
                    # 关闭窗口
                    self.d.close()
                    self.d.switch_to.window((handle_tab_all[0]))
                    time.sleep(2)  # 等待去下一个操作
                    # 向下滚动页面
                    while True:
                        self.d.execute_script("window.scrollBy(0, 800);")
                        break
                    time.sleep(5)
            except Exception as e:
                print(f'总循环错误信息: {e}')



    def write_to_worksheet(self):
        # 写入 Excel 表格
        for i, data in enumerate(self.data_list):
            self.worksheet.cell(row=i + 2, column=1, value=data['姓名'])
            self.worksheet.cell(row=i + 2, column=2, value=data['联系方式'])
            self.worksheet.cell(row=i + 2, column=3, value=data['粉丝数'])
            self.worksheet.cell(row=i + 2, column=4, value=data['网址'])
    def save_workboot(self):
        self.workbook.save(f'datas/{time.strftime("%Y-%m-%d")}.xlsx')

if __name__ == '__main__':
    dd = DarenProfiles()
    dd.run()