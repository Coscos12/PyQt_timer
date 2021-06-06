import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel
places = [0, 30, 120, 210, 300, 390, 480]
new_places = [0, 30, 120, 210, 300, 390, 480]
class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.counter1 = 0
        self.counter2 = 0
        self.counter3 = 0
        self.counter4 = 0
        self.counter5 = 0
        self.counter6 = 0

        self.flag1 = False
        self.flag2 = False
        self.flag3 = False
        self.flag4 = False
        self.flag5 = False
        self.flag6 = False

        self.setWindowTitle('second window')
        self.setFixedWidth(500)
        self.setStyleSheet("""
            QLineEdit{
                font-size: 30px
            }
            QPushButton{
                font-size: 30px
            }
            """)
        mainLayout = QVBoxLayout()

        self.input1 = QLabel()
        self.input2 = QLabel()
        self.input3 = QLabel()
        self.input4 = QLabel()
        self.input5 = QLabel()
        self.input6 = QLabel()
        self.input7 = QLabel()

        mainLayout.addWidget(self.input1)
        mainLayout.addWidget(self.input2)
        mainLayout.addWidget(self.input3)
        mainLayout.addWidget(self.input4)
        mainLayout.addWidget(self.input5)
        mainLayout.addWidget(self.input6)
        mainLayout.addWidget(self.input7)


        self.closeButton = QPushButton('Close')
        self.closeButton.clicked.connect(self.close)
        mainLayout.addWidget(self.closeButton)

        self.setLayout(mainLayout)

    def displayInfo(self):
        self.showMaximized()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.resize(776, 482)
        self.secondWindow = SecondWindow()

        mainLayout = QVBoxLayout()
        self.setStyleSheet("""
            QLineEdit{height: 30px; font-size: 30px}

        """)

        self.lineEdit = QLineEdit()
        self.lineEdit_2 = QLineEdit()
        self.lineEdit_3 = QLineEdit()
        self.lineEdit_4 = QLineEdit()
        self.lineEdit_5 = QLineEdit()
        self.lineEdit_6 = QLineEdit()
        self.lineEdit_7 = QLineEdit()

        self.lineEdit.setGeometry(QtCore.QRect(80, 130, 400, 30))
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 170, 400, 30))
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 210, 400, 30))
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 250, 400, 30))
        self.lineEdit_5.setGeometry(QtCore.QRect(80, 290, 400, 30))
        self.lineEdit_6.setGeometry(QtCore.QRect(80, 330, 400, 30))
        self.lineEdit_7.setGeometry(QtCore.QRect(210, 40, 400, 30))

        mainLayout.addWidget(self.lineEdit)
        mainLayout.addWidget(self.lineEdit_2)
        mainLayout.addWidget(self.lineEdit_3)
        mainLayout.addWidget(self.lineEdit_4)
        mainLayout.addWidget(self.lineEdit_5)
        mainLayout.addWidget(self.lineEdit_6)
        mainLayout.addWidget(self.lineEdit_7)

        self.Confirm = QPushButton('Confirm')
        self.Confirm.setStyleSheet('font-size: 30px')
        self.Confirm.clicked.connect(self.passingInformation)
        mainLayout.addWidget(self.Confirm)

        self.setLayout(mainLayout)

    def passingInformation(self):
        self.secondWindow.input1.setText(self.lineEdit.text())
        self.secondWindow.input2.setText(self.lineEdit_2.text())
        self.secondWindow.input3.setText(self.lineEdit_3.text())
        self.secondWindow.input4.setText(self.lineEdit_4.text())
        self.secondWindow.input5.setText(self.lineEdit_5.text())
        self.secondWindow.input6.setText(self.lineEdit_6.text())
        self.secondWindow.input7.setText(self.lineEdit_7.text())

        self.secondWindow.displayInfo()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())