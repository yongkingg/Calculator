from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Ui
import random

# "종류가 다르면 분리한다. 이벤트 내용이 다르면"
# 이벤트의 결과가 같으면 같으 함수로 처리한다 



class Main:
    def __init__(self):
        self.ui = Ui.Ui()
        self.connectEvent()
        self.inputNumber = ""
        self.firstNum = []
        self.secondNum = []

    def connectEvent(self):
        for index in range(0,len(self.ui.numberBtn)):
            self.ui.numberBtn[index].mousePressEvent = lambda event, num = index: self.numberEvent(event, num)
            self.ui.numberBtn[index].enterEvent = lambda event, num = index: self.EnterEvent(event, num, 1)
            self.ui.numberBtn[index].leaveEvent = lambda event, num = index: self.LeaveEvent(event, num, 1)

        for index in range(0,len(self.ui.operatorBtn)):
            self.ui.operatorBtn[index].enterEvent = lambda event, num = index: self.EnterEvent(event, num, 2)
            self.ui.operatorBtn[index].leaveEvent = lambda event, num = index: self.LeaveEvent(event, num, 2)

        for index in range(0,len(self.ui.toolBtn)):
            self.ui.toolBtn[index].mousePressEvent = lambda event, num = index: self.calculate(event, num)
            self.ui.toolBtn[index].enterEvent = lambda event, num = index: self.EnterEvent(event, num, 3)
            self.ui.toolBtn[index].leaveEvent = lambda event, num = index: self.LeaveEvent(event, num, 3)
        self.ui.operatorBtn[0].clicked.connect(self.showResult)
        self.ui.operatorBtn[1].clicked.connect(self.plus)
        self.ui.operatorBtn[2].clicked.connect(self.minus)
        self.ui.operatorBtn[3].clicked.connect(self.multiply)
        self.ui.operatorBtn[4].clicked.connect(self.division)
        self.ui.operatorBtn[5].clicked.connect(self.delete)

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

    def numberEvent(self,event,index):
        initNumber = []
        initNumber.append(index+1)
        for index in range(0,len(initNumber)):
            self.inputNumber = self.inputNumber + str(initNumber[index])
            self.ui.resultBox.setText(self.inputNumber)
        if len(self.firstNum) == 0:
            self.firstNum.append(self.inputNumber)        
        else:
            self.secondNum.append(self.inputNumber)

    def plus(self):
        self.inputNumber = ""
        self.ui.resultBox.clear()
        operator = "+"
        if len(self.firstNum) == 1 and len(self.secondNum) == 1:
            self.calculate(operator)

    def minus(self):
        self.inputNumber = ""
        self.ui.resultBox.clear()
        operator = "-"
        if len(self.firstNum) == 1 and len(self.secondNum) == 1:
            self.calculate(operator)
    def multiply(self):
        pass
    def division(self):
        pass
    def calculate(self,operator):
        print(self.firstNum)
        print(self.secondNum)

        if operator == "+":
            result = int(self.firstNum[0])+int(self.secondNum[0])
            print(result)
            self.firstNum.clear()
            self.secondNum.clear()
            self.firstNum.append(result)
            print(self.firstNum)
        elif operator == "-":
            result = int(self.firstNum[0])-int(self.secondNum[0])
            print(result)
            self.firstNum.clear()
            self.secondNum.clear()
            self.firstNum.append(result)
            print(self.firstNum)
        else:
            pass
    def delete(self):
        pass
    def showResult(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = Main()

    sys.exit(app.exec_())