import sys
import qdarkstyle
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from MainWindow import Ui_MainWindow

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)

    # Create the main window
    mainWindow = QMainWindow()

    # Create an instance of the generated UI
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)

    # # setup stylesheet
    # apply_stylesheet(app, theme='dark_teal.xml')

    # setup stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    # app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=LightPalette()))

    # Show the main window
    mainWindow.show()

    # Start the application event loop
    sys.exit(app.exec_())
