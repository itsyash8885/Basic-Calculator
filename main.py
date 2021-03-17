from PyQt5.QtWidgets import QMainWindow
from window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import sys
import operator
#just a text
class Calci(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.stack = [0]
        self.deciactive = False
        self.decicounter = 0
        self.curop=None
        self.nextop=None
        self.ready=True
        for i in range(0,10):
            getattr(self.ui,"pushButton_%d"%i).pressed.connect(lambda n=i: self.inputnum(n))
        
        self.ui.pushButton_c.pressed.connect(lambda : self.clear())
        self.ui.pushButton_deci.pressed.connect(lambda : self.decipressed())
        self.ui.pushButton_b.pressed.connect(lambda: self.back())

        self.ui.pushButton_add.pressed.connect(lambda: self.operate(operator.add))
        self.ui.pushButton_sub.pressed.connect(lambda: self.operate(operator.sub))
        self.ui.pushButton_mul.pressed.connect(lambda: self.operate(operator.mul))
        self.ui.pushButton_div.pressed.connect(lambda: self.operate(operator.truediv))
        self.ui.pushButton_eq.pressed.connect(lambda: self.equals("butcall"))
    
    def inputnum(self,num):
        if self.stack[-1]<999999999 and self.deciactive == False:
            self.stack[-1] = self.stack[-1]*10 + num
        elif self.stack[-1]<float(9999999999) and self.deciactive == True and self.decicounter<4:
            self.decicounter += 1
            print("inputnum-> decicounter",self.decicounter)
            self.stack[-1] = self.stack[-1] + num/(10**self.decicounter)
            
        print("stack changed in inputnum function to ",self.stack)
        self.display()
        
    def operate(self,curop):
        if self.curop:
           self.equals("funcall")

        self.stack.append(0)
        print("operate-> self.stack",self.stack)
        self.curop=curop

    def equals(self,check):
        if check=="butcall":
            try:
                self.stack[0]=self.curop(self.stack[0],self.stack[-1])
                print("equals butcall-> self.stack before pop",self.stack)
                self.stack.pop()
                print("equals butcall-> self.stack after pop",self.stack)
                self.display()
                self.curop=None
            except ZeroDivisionError:
                self.clear()

        if check=="funcall":
            self.stack[0]=self.curop(self.stack[0],self.stack[-1])
            print("equals-> self.stack before pop",self.stack)
            self.stack.pop()
            print("equals-> self.stack after pop",self.stack)





    def display(self):
        self.ui.label_display.setText(f"{self.stack[-1]}")
    
    def clear(self):
        self.stack = [0]
        self.decicounter = 1
        self.deciactive = False
        self.curop=None
        self.ui.label_display.setText("0")
        self.display()
        
    def decipressed(self):
        self.deciactive = True


    def back(self):
        if self.deciactive == False:
            self.stack[-1] = int(self.stack[-1]//10)
        elif self.deciactive == True :
            print("back-> decicounter before",self.decicounter)
            self.stack[-1] = self.stack[-1]*(10**self.decicounter)
            print("back-> mul ",self.stack)
            self.stack[-1] = self.stack[-1]//10
            print("back-> floordiv",self.stack)
            
            self.decicounter-=1

            if self.decicounter>0:
                print("back-> decicounter mid",self.decicounter)
                self.stack[-1] = self.stack[-1]/(10**self.decicounter)
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