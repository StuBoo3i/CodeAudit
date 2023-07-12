from untitled import Ui_Form
from PyQt5 import  QtWidgets,uic

class UI(Ui_Form):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('untitled.ui', self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec_())