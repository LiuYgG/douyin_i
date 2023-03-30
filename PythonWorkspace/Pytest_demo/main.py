'''

    pytest运行参数命令：
        -s: 输出用例中的调试信息
        -v: 输出用例更加详细的信息
        -q: 简化控制台的输出
        -k: 执行用例含 ”关键字“ 的用例
        -m: 执行指定的用例
            使用方法: pytest.main([’参数1‘,'参数2',...])

'''
import pytest
import allure
from untils import sen_report_mail


# 主程序文件，方便集中运行编写的case
if __name__ == '__main__':
    pytest.main()

    # 发送测试报告
    sen_report_mail.Mail().send_email()
