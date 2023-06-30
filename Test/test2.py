import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from QTApplication.Main import Ui_MainWindow  # 替换为你的UI模块的导入语句


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建UI对象
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())

