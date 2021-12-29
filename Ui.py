from sys import _xoptions
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui:
    def __init__(self):
        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindow.resize(400,500)
        self.mainWindow.setWindowTitle("계산기")
        self.centralWidget = QtWidgets.QWidget(self.mainWindow)
        self.centralWidget.setGeometry(0,0,400,500)

        self.resultBox = QtWidgets.QLabel(self.mainWindow)
        self.resultBox.setGeometry(40,20,320,70)
        self.resultBox.setStyleSheet(
            "border : 1px solid black;"
            )
        self.resultBox.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.resultBox.setFont(QtGui.QFont("궁서",30))

        self.calculate = []
        self.sign = ["+","-","X","/"]
        for index in range(0,4):
            tmpBtn = QtWidgets.QPushButton(self.centralWidget)
            if index < 2:
                xPos = 40 + 50*index
            else:
                xPos = 150 + 50*(index-2)
            tmpBtn.setGeometry(xPos,100,50,50)
            tmpBtn.setStyleSheet(
                "border : 1px solid black;"
                "background-color : lightgrey"
                )
            tmpBtn.setText(self.sign[index])
            self.calculate.append(tmpBtn)

        self.toolBtn = []
        self.toolList = ["C","="]
        for index in range(0,2):
            tmpBtn = QtWidgets.QPushButton(self.centralWidget)
            xPos = 260 + 50*index
            tmpBtn.setGeometry(xPos,100,50,50)
            tmpBtn.setStyleSheet(
                "border : 1px solid black;"
                "background-color : lightgrey"
                )
            tmpBtn.setText(self.toolList[index])
            self.toolBtn.append(tmpBtn)

        self.numberBtn = []
        for index in range(0,9):
            tmpBtn = QtWidgets.QPushButton(self.centralWidget)
            if index < 3:
                yPos = 160
            elif index < 6:
                yPos = 270
            else:
                yPos = 380
            xPos = 40 + 110*(index%3)
            tmpBtn.setGeometry(xPos,yPos,100,100)
            tmpBtn.setStyleSheet(
                "border : 1px solid black;"
                "background-color : lightgrey;"
                )
            tmpBtn.setText(str(index + 1))
            self.numberBtn.append(tmpBtn)
            
        self.mainWindow.show()
