import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 初始化UI界面
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('浏览器自动化测试工具')
        self.setFixedSize(500, 300)

        # 创建浏览器路径的输入框和选择浏览器按钮
        self.browser_path_label = QLabel('浏览器路径:', self)
        self.browser_path_label.move(50, 50)

        self.browser_path_input = QLineEdit(self)
        self.browser_path_input.move(150, 50)
        self.browser_path_input.setFixedWidth(250)

        self.browser_path_select_button = QPushButton('选择浏览器', self)
        self.browser_path_select_button.move(410, 50)
        self.browser_path_select_button.clicked.connect(self.selectBrowserPath)

        # 创建打开浏览器的按钮
        self.open_browser_button = QPushButton('打开浏览器', self)
        self.open_browser_button.move(50, 100)
        self.open_browser_button.clicked.connect(self.openBrowser)

        # 创建执行次数的输入框和执行脚本的按钮
        self.run_times_label = QLabel('执行次数:', self)
        self.run_times_label.move(50, 150)

        self.run_times_input = QLineEdit(self)
        self.run_times_input.move(150, 150)
        self.run_times_input.setFixedWidth(250)

        self.run_script_button = QPushButton('执行脚本', self)
        self.run_script_button.move(410, 150)
        self.run_script_button.clicked.connect(self.runScript)

        # 创建选择Excel保存路径的按钮
        self.excel_path_label = QLabel('Excel保存路径:', self)
        self.excel_path_label.move(50, 200)

        self.excel_path_input = QLineEdit(self)
        self.excel_path_input.move(150, 200)
        self.excel_path_input.setFixedWidth(250)

        self.excel_path_select_button = QPushButton('选择路径', self)
        self.excel_path_select_button.move(410, 200)
        self.excel_path_select_button.clicked.connect(self.selectExcelPath)

    def selectBrowserPath(self):
        # 弹出选择文件对话框
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter('Executable files (*.exe)')
        if file_dialog.exec_():
            selected_file = file_dialog.selectedFiles()[0]
            self.browser_path_input.setText(selected_file)

    def openBrowser(self):
        # 获取浏览器路径
        browser_path = self.browser_path_input.text()

        # 打开浏览器
        browser_open = self.open_browser_button

    def runScript(self):
        # 获取执行次数
        run_times = int(self.run_times_input.text())

        # 执行脚本
        # TODO

    def selectExcelPath(self):
        # 弹出选择文件对话框
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setNameFilter('Excel files (*.xlsx)')
        if file_dialog.exec_():
            selected_file = file_dialog.selectedFiles()[0]
            self.excel_path_input.setText(selected_file)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())