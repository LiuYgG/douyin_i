import os.path
import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLineEdit, QMessageBox, QInputDialog
from main_ui import Ui_MainWindow
import logging
import configparser

class Example(QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        # 创建UI界面实例
        self.ui = Ui_MainWindow()
        # 将UI界面与主窗口相关联
        self.ui.setupUi(self)

        """
        顶部菜单
        """
        self.ui.btn_Software_activation.clicked.connect(self.activation_software) # 软件激活按钮

        """
        功能专区：
        """
        # 内容区域组件
        self.ui.input_Browser_path.textChanged.connect(self.input_path) # 输入浏览器路径
        # 读取配置文件，设置默认路径
        self.configs = configparser.ConfigParser()
        self.configs.read(os.path.join('config', 'config.ini'))
        self.defalut_paths = self.configs.get('DEFAULT', 'browser_path')
        self.ui.input_Browser_path.setText(self.defalut_paths)
        self.ui.btn_Choose_browser_path.clicked.connect(self.btn_Choose_browser_path) # 选择浏览器安装目录


        """
        底部功能按钮
        """
        self.ui.btn_Open_browser.clicked.connect(self.run_browser_btn) # 运行浏览器
        self.ui.btn_Open_daren_path.clicked.connect(self.open_daren_Path) # 打开达人信息存储路径
    """
    创建组件对象方法
    """

    # 文件路径输入框
    def input_path(self, defalut_paths=""):

        if defalut_paths:
            print(f'输入的内容为: {defalut_paths}')

            # 缓存路径到配置文件
            try:
                configs = configparser.ConfigParser()
                configs['DEFAULT'] = {'browser_path': defalut_paths}
                with open('config/config.ini', 'w') as configfile:
                    configs.write(configfile)
            except Exception as i:
                print(i)
        else:
            print("输入的内容为空，不写入配置文件。")

    # 选择文件目录按钮
    def btn_Choose_browser_path(self):

        try:
            # 创建文件对话框
            file_dialog = QFileDialog()
            # 设置对话框只显示目录
            file_dialog.setFileMode(QFileDialog.DirectoryOnly)
            # 显示对话框，等待用户选择
            if file_dialog.exec_() == QFileDialog.Accepted:
                # 获取用户选择的文件夹路径
                selected_directory = file_dialog.selectedFiles()[0]
                # 输出路径到文本输入框
                self.ui.input_Browser_path.setText(selected_directory)
                # 缓存路径到配置文件
                configs = configparser.ConfigParser()
                configs['DEFAULT'] = {'browser_path' : selected_directory}
                with open('config/config.ini', 'w') as configfile:
                    configs.write(configfile)

        except Exception as e:
            logging.exception(e)

    # 软件激活按钮
    def activation_software(self):
        print('激活按钮被点击')
        # 弹出一个消息框，要求用户输入激活码
        text, ok = QInputDialog.getText(self, '软件激活', '请输入激活码：')
        try:
            if ok:
                if text == '123':
                    # 用户单击了"确定"按钮并输入了激活码
                    print('激活码: ', text)
                    QMessageBox.information(self, '提示', '软件已激活', QMessageBox.Ok)
                elif text == '':
                    QMessageBox.warning(self, '警告', '输入内容为空', QMessageBox.Ok)
                    text, ok = QInputDialog.getText(self, '软件激活', '请输入激活码：')
                    if ok:
                        # 用户单击了"确定"按钮并输入了激活码
                        print('激活码: ', text)
                    else:
                        # 用户单击了"取消"按钮
                        print('取消激活')
                else:
                    QMessageBox.warning(self, '警告', '激活码错误', QMessageBox.Ok)
                    text, ok = QInputDialog.getText(self, '软件激活', '请输入激活码：')
                    if ok:
                        # 用户单击了"确定"按钮并输入了激活码
                        print('激活码: ', text)
                    else:
                        # 用户单击了"取消"按钮
                        print('取消激活')
            else:
                # 用户单击了"取消"按钮
                print('取消激活')

        except Exception as m:
            logging.exception(m)

    # 运行浏览器按钮操作
    def run_browser_btn(self):
        try:
            # 重新读取配置文件中的browser_path的值
            self.configs.read(os.path.join('config', 'config.ini'))
            browser_path = self.configs.get('DEFAULT', 'browser_path')
            if not browser_path:
                raise ValueError('browser_path not found in config.ini')
            paths = subprocess.run([os.path.join(browser_path, 'chrome.exe'), '--remote-debugging-port=5247'])
            print(paths.stdout)
        except Exception as a:
            logging.exception(a)

    # 打开达人信息存储路径
    def open_daren_Path(self):

        paths = os.path.join('datas')
        os.startfile(paths)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Example()
    example.show()
    example.setWindowTitle('抖音达人工具箱')
    sys.exit(app.exec_())
