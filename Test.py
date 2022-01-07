from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Ui
import random

# "종류가 다르면 분리한다. 이벤트 내용이 다르면"
# 이벤트의 결과가 같으면 같은 함수로 처리한다 
class Main:
    def __init__(self):
        self.ui = Ui.Ui()
        self.connectEvent()
        self.inputNumber = ""
        self.firstNum = []
        self.secondNum = []
        self.initNumber = []
        self.operator = None
        self.result = 0

    def connectEvent(self):
        for index in range(0,len(self.ui.numberBtn)):
            self.ui.numberBtn[index].mousePressEvent = lambda event, num = index: self.numberEvent(event, num)
            self.ui.numberBtn[index].enterEvent = lambda event, num = index: self.EnterEvent(event, num, 1)
            self.ui.numberBtn[index].leaveEvent = lambda event, num = index: self.LeaveEvent(event, num, 1)

        for index in range(0,len(self.ui.operatorBtn)):
            self.ui.operatorBtn[index].enterEvent = lambda event, num = index: self.EnterEvent(event, num, 2)
            self.ui.operatorBtn[index].leaveEvent = lambda event, num = index: self.LeaveEvent(event, num, 2)

        for index in range(0,len(self.ui.toolBtn)):
            self.ui.toolBtn[index].enterEvent = lambda event, num = index: self.EnterEvent(event, num, 3)
            self.ui.toolBtn[index].leaveEvent = lambda event, num = index: self.LeaveEvent(event, num, 3)

        self.ui.operatorBtn[0].clicked.connect(self.showResult)
        self.ui.operatorBtn[1].clicked.connect(self.plus)
        self.ui.operatorBtn[2].clicked.connect(self.minus)
        self.ui.operatorBtn[3].clicked.connect(self.multiply)
        self.ui.operatorBtn[4].clicked.connect(self.division)
        self.ui.operatorBtn[5].clicked.connect(self.delete)

        self.ui.toolBtn[0].clicked.connect(self.remainder)
        self.ui.toolBtn[1].clicked.connect(self.clear)
        self.ui.toolBtn[2].clicked.connect(self.clear)
        self.ui.toolBtn[3].clicked.connect(self.fraction)
        self.ui.toolBtn[4].clicked.connect(self.square)
        self.ui.toolBtn[5].clicked.connect(self.root)
    # 첫번째 변수 , 연산자 변수 , 두번째 변수를 = 함수에 보내고, 연산자 변수에 따라서 계산하는 로직
    def EnterEvent(self,event,index,judge):
        if judge == 1:
            self.ui.numberBtn[index].setStyleSheet(
                "border : 1px solid black;"
                "background-color : grey;"
                )
        elif judge == 2:
            self.ui.operatorBtn[index].setStyleSheet(
                "border : 2px solid black;"
                "background-color : grey;"
                )
        elif judge == 3:
            self.ui.toolBtn[index].setStyleSheet(
                "border : 2px solid black;"
                "background-color : grey;"
                )

    def LeaveEvent(self,event,index,judge):
        if judge == 1:
            self.ui.numberBtn[index].setStyleSheet(
                "border : 1px solid black;"
                "background-color : lightgrey;"
                )
        elif judge == 2:
            self.ui.operatorBtn[index].setStyleSheet(
                "border : 2px solid black;"
                "background-color : lightgrey;"
                )
        elif judge == 3:
            self.ui.toolBtn[index].setStyleSheet(
                "border : 2px solid black;"
                "background-color : lightgrey;"
                )

    def clearList(self):
        self.firstNum.clear()
        self.secondNum.clear()
        self.ui.calculateBox[1].clear()
        self.firstNum.append(self.result)

    def numberEvent(self,event,index):
        self.initNumber.append(index+1)
        for index in range(0,len(self.initNumber)):
            self.inputNumber = self.inputNumber + str(self.initNumber[index])
            self.ui.calculateBox[0].setText(str(self.inputNumber))
            self.ui.resultBox.setText(self.inputNumber)
        if len(self.firstNum) != 0:
            self.secondNum.append(self.inputNumber)
            self.calculate(self.operator)
        self.initNumber.clear()

    def saveNum(self,operator):
        self.ui.calculateBox[1].setText(str(operator)) 
        if len(self.firstNum) == 0:
            self.firstNum.append(self.inputNumber)            
        else:
            pass
        if operator == "1/x":
            self.calculate(self.operator)
        elif operator == "x^2":
            self.calculate(self.operator)
        elif operator == "√":
            self.calculate(self.operator)
        self.inputNumber = ""
    
    def plus(self):
        self.operator = "+"
        self.saveNum(self.operator)

    def minus(self):
        self.operator = "-"
        self.saveNum(self.operator)

    def multiply(self):
        self.operator = "×"
        self.saveNum(self.operator)

    def division(self):
        self.operator = "÷"
        self.saveNum(self.operator)

    def remainder(self):
        self.operator = "%"
        self.saveNum(self.operator)

    def fraction(self):
        self.operator = "1/x"
        self.saveNum(self.operator)

    def square(self):
        self.operator = "x^2"
        self.saveNum(self.operator)

    def root(self):
        self.operator = "√"
        self.saveNum(self.operator)
                
    def calculate(self,operator):
        if operator == "+":
            self.result = int(self.firstNum[0]) + int(self.secondNum[0])
            self.clearList()

        elif operator == "-":
            self.result = int(self.firstNum[0]) - int(self.secondNum[0])
            self.clearList()

        elif operator == "×":
            self.result = int(self.firstNum[0]) * int(self.secondNum[0])
            self.clearList()

        elif operator == "÷":
            self.result = int(self.firstNum[0]) / int(self.secondNum[0])
            self.clearList()

        elif operator == "%":
            self.result = int(self.firstNum[0]) % int(self.secondNum[0])
            self.clearList()

        elif operator == "1/x":
            self.result = 1 / int(self.firstNum[0])
            self.firstNum.clear()
            self.firstNum.append(self.result)
        
        elif operator == "x^2":
            self.result = int(self.firstNum[0])*int(self.firstNum[0])
            self.firstNum.clear()
            self.firstNum.append(self.result)

        elif operator == "√":
            self.result = int(self.firstNum[0]) ** 0.5
            self.firstNum.clear()
            self.firstNum.append(self.result)

    def delete(self):
        self.inputNumber = list(self.inputNumber)
        numLength = len(self.inputNumber)-1
        self.inputNumber = self.inputNumber[:numLength]
        self.inputNumber = "".join(self.inputNumber)
        self.ui.resultBox.setText(str("".join(self.inputNumber)))
        self.ui.calculateBox[0].setText((str("".join(self.inputNumber))))
        
    def clear(self):
        self.firstNum.clear()
        self.secondNum.clear()
        self.ui.resultBox.setText("0")
        self.ui.calculateBox[0].clear()
        self.ui.calculateBox[1].clear()
        self.inputNumber = ""

    def showResult(self):
        self.ui.resultBox.clear()
        self.ui.resultBox.setText(str(self.firstNum[0]))
        self.ui.calculateBox[0].setText(str(self.firstNum[0]))
        self.ui.calculateBox[1].clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())