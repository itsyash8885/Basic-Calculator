from PyQt5.QtWidgets import QMainWindow
from window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import sys
#just a text
class Calci(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.stack = [0]
        self.deciactive = False
        self.decicounter = 1

        for i in range(0,10):
            getattr(self.ui,"pushButton_%d"%i).pressed.connect(lambda n=i: self.inputnum(n))
        
        self.ui.pushButton_c.pressed.connect(lambda : self.clear())
        self.ui.pushButton_deci.pressed.connect(lambda : self.decipressed())
    
    def inputnum(self,num):
        if self.stack[0]<999999999 and self.deciactive == False:
            self.stack[0] = self.stack[0]*10 + num
        elif self.stack[0]<float(9999999999) and self.deciactive == True and self.decicounter<5:
            self.stack[0] = self.stack[0] + num/(10**self.decicounter)
            self.decicounter += 1
        print("stack changed in inputnum function to ",self.stack)
        self.display()
        
            
    def display(self):
        self.ui.label_display.setText(f"{self.stack[0]}")
    
    def clear(self):
        self.stack = [0]
        self.decicounter = 1
        self.deciactive = False
        self.ui.label_display.setText("0")
        self.display()
        
    def decipressed(self):
        self.deciactive = True

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    
    calc=Calci()
    calc.show()

    sys.exit(app.exec_())