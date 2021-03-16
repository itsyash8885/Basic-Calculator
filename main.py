from PyQt5.QtWidgets import QMainWindow
from window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import sys

class Calci(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    
    calc=Calci()
    calc.show()

    sys.exit(app.exec_())