import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWindow import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create the main window
    mainWindow = QMainWindow()

    # Create an instance of the generated UI
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)

    # Show the main window
    mainWindow.show()

    # Start the application event loop
    sys.exit(app.exec_())
