#Importing Modules
from PyQt5.QtWidgets import QMainWindow
from window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import sys
import operator

#Class for handling operations and GUI--
class Calci(QMainWindow):
    def __init__(self):
        super().__init__()
        #INitializing and setting GUI
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        ################################################################################
        #Constraints
        self.stack = [0]
        self.deciactive = False
        self.decicounter = 0
        self.curop=None
        
        #Connecting buttons to slots
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
    
    #function for inputing the numbers
    def inputnum(self,num):
        if self.stack[-1]<999999999 and self.deciactive == False:
            self.stack[-1] = self.stack[-1]*10 + num
        elif self.stack[-1]<float(9999999999) and self.deciactive == True and self.decicounter<4:
            self.decicounter += 1
            print("inputnum-> decicounter",self.decicounter)
            self.stack[-1] = self.stack[-1] + num/(10**self.decicounter)
            
        print("stack changed in inputnum function to ",self.stack)
        self.display()

    #function for handling the operators    
    def operate(self,curop):
        self.decicounter=0
        self.deciactive=False
        if self.curop:
           self.equals("funcall")

        self.stack.append(0)
        print("operate-> self.stack",self.stack)
        self.curop=curop
        

    #function for calculating result
    def equals(self,check):
        #equals based on button pressed
        if check=="butcall":
            try:
                self.stack[0]=self.curop(self.stack[0],self.stack[-1])
                print("equals butcall-> self.stack before pop",self.stack)
                self.stack.pop()
                print("equals butcall-> self.stack after pop",self.stack)
                self.display()
                self.curop=None
            except (ZeroDivisionError, TypeError):
                self.clear()
        #equals based on operation pressed
        
        if check=="funcall":
            try:

                self.stack[0]=self.curop(self.stack[0],self.stack[-1])
                print("equals-> self.stack before pop",self.stack)
                self.stack.pop()
                print("equals-> self.stack after pop",self.stack)
            except ZeroDivisionError:
                self.clear()

    #function to display numbers 
    def display(self):
        if self.decicounter>0:
            self.ui.label_display.setText("%.4f"%self.stack[-1])
        else:
            self.ui.label_display.setText(f"{self.stack[-1]}")

    
    #function for clearing the screen and getting back to null state
    def clear(self):
        self.stack = [0]
        self.decicounter = 0
        self.deciactive = False
        self.curop=None
        self.ui.label_display.setText("0")
        self.display()

    #function for checking if the decimal is pressed    
    def decipressed(self):
        self.deciactive = True

    #function for deleting consecutive numbers(backspace)
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
#main 
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    
    calc=Calci()
    calc.show()

    sys.exit(app.exec_())