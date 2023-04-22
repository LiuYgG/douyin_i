import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建标签和输入框
        browser_label = QLabel('浏览器地址:', self)
        browser_label.move(20, 20)
        self.browser_edit = QLineEdit(self)
        self.browser_edit.move(100, 20)
        self.browser_edit.resize(280, 25)

        # 创建选择文件的按钮
        file_button = QPushButton('选择文件', self)
        file_button.move(20, 60)
        file_button.clicked.connect(self.showFileDialog)

        # 创建保存地址标签和显示选择文件的输入框
        save_label = QLabel('保存地址:', self)
        save_label.move(20, 100)
        self.save_edit = QLineEdit(self)
        self.save_edit.move(100, 100)
        self.save_edit.resize(280, 25)

        # 创建运行按钮
        run_button = QPushButton('运行', self)
        run_button.move(20, 140)
        run_button.clicked.connect(self.runScript)

        # 设置窗口大小和标题
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('PyQt5界面')

        self.show()

    def showFileDialog(self):
        # 打开文件选择对话框
        filename, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "All Files (*);;Python Files (*.py)")
        if filename:
            self.save_edit.setText(filename)

    def runScript(self):
        # 获取浏览器地址和保存地址，并执行脚本
        browser_path = self.browser_edit.text()
        save_path = self.save_edit.text()
        print('浏览器地址:', browser_path)
        print('保存地址:', save_path)
        # TODO: 在此处添加执行脚本的代码


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
