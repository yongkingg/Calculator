from sys import _xoptions
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui:
    def __init__(self):
        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindow.resize(500,810)
        self.mainWindow.setMaximumSize(500,810)
        self.mainWindow.setMinimumSize(500,810)

        self.mainWindow.setWindowTitle("계산기")
        self.centralWidget = QtWidgets.QWidget(self.mainWindow)
        self.centralWidget.setGeometry(0,0,800,1000)
        
        self.resultBox = QtWidgets.QLabel(self.mainWindow)
        self.resultBox.setGeometry(40,20,430,110)
        self.resultBox.setStyleSheet(
            "border : 2px solid black;"
            )
        self.resultBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.resultBox.setFont(QtGui.QFont("궁서",30))

        self.operatorBtn = []
        self.operatorList = ["=","+","-","×","÷","Del"]
        for index in range(0,len(self.operatorList)):
            tmpBtn = QtWidgets.QPushButton(self.centralWidget)
            yPos = 690 - 110*index
            tmpBtn.setGeometry(370,yPos,100,100)
            tmpBtn.setStyleSheet(
                "border : 2px solid black;"
                "background-color : lightgrey;"
                )
            tmpBtn.setText(self.operatorList[index])
            self.operatorBtn.append(tmpBtn)
        
        self.numberBtn = []
        self.additionList = ["+/-","0","."]
        for index in range(0,12):
            tmpBtn = QtWidgets.QPushButton(self.centralWidget)
            xPos = 40 + 110*(index%3)
            yPos = 360 + 110*(index//3)
            tmpBtn.setGeometry(xPos,yPos,100,100)
            tmpBtn.setStyleSheet(
                "border : 1px solid black;"
                "background-color : lightgrey;"
                )
            if index < 9:
                tmpBtn.setText(str(index + 1))
            else:
                tmpBtn.setText(self.additionList[index-9])
            self.numberBtn.append(tmpBtn)
            
        self.toolBtn = []
        self.toolList = ["%","CE","C","1/x","x^2","√"]
        for index in range(0,len(self.toolList)):
            tmpBtn = QtWidgets.QPushButton(self.centralWidget)
            xPos = 40 + 110*(index%3)
            yPos = 140 + 110*(index//3)
            tmpBtn.setGeometry(xPos,yPos,100,100)
            tmpBtn.setStyleSheet(
                "border : 2px solid black;"
                "background-color : lightgrey;"
                )
            tmpBtn.setText(self.toolList[index])
            self.toolBtn.append(tmpBtn)
        self.mainWindow.show()
