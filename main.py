import logging
import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QFileDialog

import daren_profile_data


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("抖音达人")
        self.setGeometry(100, 100, 400, 300)
        self.initUI()

    def initUI(self):

        # 浏览器路径标签和输入框
        self.browser_path_label = QLabel('浏览器路径：', self)
        self.browser_path_label.move(20, 20)
        self.browser_path_input = QLineEdit(self)
        self.browser_path_input.setPlaceholderText("请输入您的浏览器地址")
        self.browser_path_input.setGeometry(50,50,200,30)

        # 选择浏览器位置按钮
        self.select_browser_button = QPushButton('浏览', self)
        self.select_browser_button.move(260, 50)
        self.select_browser_button.clicked.connect(self.select_browser)

        # 保存浏览器位置按钮
        self.save_browser_button = QPushButton('保存', self)
        self.save_browser_button.move(50, 100)
        self.save_browser_button.clicked.connect(self.save_browser)

        # 打开浏览器按钮
        self.open_browser_button = QPushButton('打开浏览器', self)
        self.open_browser_button.move(150, 100)
        self.open_browser_button.clicked.connect(self.open_browser)

        # 创建设置运行脚本次数标签和输入框
        self.script_count_label = QLabel('设置脚本运行次数：', self)
        self.script_count_label.move(50,250)
        self.script_count_label = QLineEdit(self)
        self.script_count_label.move(160,255)
        self.script_count_label.resize(50, 20)

        # 运行脚本按钮
        self.run_script_button = QPushButton('运行脚本', self)
        self.run_script_button.move(250, 250)
        self.run_script_button.clicked.connect(self.execute_script)



        self.show()

    def select_browser(self):
        # 弹出文件选择对话框
        file_path, _ = QFileDialog.getOpenFileName(self, "选择浏览器位置", "", "可执行文件 (*.exe)")
        if file_path:
            self.browser_path_input.setText(file_path)

    def save_browser(self):
        # 保存浏览器位置
        with open("browser_path.txt", "w") as f:
            f.write(self.browser_path_input.text())

    def open_browser(self):
        # 打开浏览器相关操作代码
        open_web = webbrowser.open(self.browser_path_input.text(), '--remote-debugging-port=5247')
        print(f" 浏览器启动: {open_web} ")

    def execute_script(self):

        # 执行脚本相关操作代码
        daren_profile_data
        print(daren_profile_data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()

    # 如果存在浏览器位置的缓存文件，则自动填充输入框
    try:
        with open("browser_path.txt", "r") as f:
            browser_path = f.read()
            if browser_path:
                main_window.browser_path_input.setText(browser_path)
    except FileNotFoundError:
        pass

    main_window.show()
    sys.exit(app.exec_())
