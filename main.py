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
        self.decicounter = 0

        for i in range(0,10):
            getattr(self.ui,"pushButton_%d"%i).pressed.connect(lambda n=i: self.inputnum(n))
        
        self.ui.pushButton_c.pressed.connect(lambda : self.clear())
        self.ui.pushButton_deci.pressed.connect(lambda : self.decipressed())
        self.ui.pushButton_b.pressed.connect(lambda: self.back())
    
    def inputnum(self,num):
        if self.stack[0]<999999999 and self.deciactive == False:
            self.stack[0] = self.stack[0]*10 + num
        elif self.stack[0]<float(9999999999) and self.deciactive == True and self.decicounter<4:
            self.decicounter += 1
            print("inputnum-> decicounter",self.decicounter)
            self.stack[0] = self.stack[0] + num/(10**self.decicounter)
            
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


    def back(self):
        if self.deciactive == False:
            self.stack[0] = int(self.stack[0]//10)
        elif self.deciactive == True :
            print("back-> decicounter before",self.decicounter)
            self.stack[0] = self.stack[0]*(10**self.decicounter)
            print("back-> mul ",self.stack)
            self.stack[0] = self.stack[0]//10
            print("back-> floordiv",self.stack)
            
            self.decicounter-=1

            if self.decicounter>0:
                print("back-> decicounter mid",self.decicounter)
                self.stack[0] = self.stack[0]/(10**self.decicounter)
                print("back-> div",self.stack)
                print("back-> decicounter after",self.decicounter)
            elif self.decicounter==0:
                self.deciactive = False

        self.display()

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    
    calc=Calci()
    calc.show()

    sys.exit(app.exec_())