import sys
from functools import partial
from PyQt5 import QtCore,  QtWidgets
import qdarkstyle
import sys
import qdarkstyle
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from MainWindow import Ui_MainWindow
from Tools.DatabaseOperation import SQL
from PyQt5 import uic
class UI(Ui_MainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('MainWindow.ui', self)
        self.Open.triggered.connect(self.open_directory)  # type: ignore
        self.Find.triggered.connect(self.find_qa)
        self.Function.triggered.connect(self.function_qa)
        self.Pie.triggered.connect(self.pie_qa)
        self.CMD.triggered.connect(self.cmd_qa)
        self.Compile.triggered.connect(self.complie_qa)
        self.Run.triggered.connect(self.run_qa)
        self.Undo.triggered.connect(self.undo_qa)
        self.Copy.triggered.connect(self.copy_qa)
        self.Cut.triggered.connect(self.cut_qa)
        self.Paste.triggered.connect(self.paste_qa)
        self.Goto.triggered.connect(self.goto_qa)
        self.Save.triggered.connect(self.save_qa)
        self.Saveas.triggered.connect(self.saveas_qa)
        self.Close.triggered.connect(self.close_qa)
        self.Closeall.triggered.connect(self.colseall_qa)
        self.Exit.triggered.connect(self.exit_qa)
class Model:
    def __init__(self):
        self.username = ""
        self.password = ""

    def verify_password(self):
        return self.username == "USER" and self.password == "PASS"


class View(QtWidgets.QWidget):
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    verifySignal = QtCore.pyqtSignal()

    def __init__(self):
        # QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        super(View, self).__init__()

        self.username = ""
        self.password = ""
        self.initUi()

    def initUi(self):
        # QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        self.setWindowTitle("Login")
        self.setGeometry(300, 300, 640, 320)

        layout = QtWidgets.QVBoxLayout(self)
        title = QtWidgets.QLabel("<b>LOGIN</b>")
        title.setAlignment(QtCore.Qt.AlignHCenter)
        layout.addWidget(title)

        form_widget = QtWidgets.QWidget()
        form_layout = QtWidgets.QFormLayout(form_widget)
        self.usernameInput = QtWidgets.QLineEdit()
        self.usernameInput.textChanged.connect(partial(setattr, self, "username"))
        self.passwordInput = QtWidgets.QLineEdit(echoMode=QtWidgets.QLineEdit.Password)
        self.passwordInput.textChanged.connect(partial(setattr, self, "password"))
        self.loginButton = QtWidgets.QPushButton("Login")
        self.loginButton.clicked.connect(self.verifySignal)

        form_layout.addRow("Username: ", self.usernameInput)
        form_layout.addRow("Password: ", self.passwordInput)
        form_layout.addRow(self.loginButton)

        layout.addWidget(form_widget)
        layout.addStretch()

    def clear(self):
        self.usernameInput.clear()
        self.passwordInput.clear()

    def showMessage(self):
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        self.mainwin = UI()
        self.mainwin.show()



    def showError(self):
        messageBox = QtWidgets.QMessageBox(self)
        messageBox.setText("Your credentials are not valid. Try again...")
        messageBox.setIcon(QtWidgets.QMessageBox.Critical)
        messageBox.exec_()


class Controller:
    def __init__(self):
        self._app = QtWidgets.QApplication(sys.argv)
        self._model = Model()
        self._view = View()
        self.init()

    def init(self):
        self._view.verifySignal.connect(self.verify_credentials)

    def verify_credentials(self):
        self._model.username = self._view.username
        self._model.password = self._view.password
        self._view.clear()
        mysql = SQL()
        flag = mysql.SQL_Login(mysql.cursor,self._model.username,self._model.password)
        if flag:
            self._view.showMessage()
        else:
            self._view.showError()

    def run(self):
        # QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        self._view.show()
        self._app.setStyleSheet(qdarkstyle.load_stylesheet())
        return self._app.exec_()


if __name__ == '__main__':
    c = Controller()
    sys.exit(c.run())
