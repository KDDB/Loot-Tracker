import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
import os

counter = 1
lmao = []


class UiMainWindow(object):
    def __init__(self):
        self.centralwidget = None
        self.finishButton = None
        self.mfWindow = None
        self.mf = None
        self.itemWindow = None
        self.items = None
        self.farm = None
        self.runNumber = None
        self.runs = None
        self.disableButton = None
        self.farmWindow = None
        self.lootButton = None
        self.addRun = None
        self.lootWidget = None
        self.menubar = None
        self.menuok = None
        self.statusbar = None

    def setupUi(self, mainwindow):
        mainwindow.setObjectName("MainWindow")
        mainwindow.resize(479, 887)
        font = QtGui.QFont()
        font.setFamily("AvQest")
        mainwindow.setFont(font)
        mainwindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        mainwindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.finishButton = QtWidgets.QPushButton(self.centralwidget)
        self.finishButton.setGeometry(QtCore.QRect(180, 170, 111, 21))
        font = QtGui.QFont()
        font.setFamily("AvQest")
        font.setPointSize(14)
        self.finishButton.setFont(font)
        self.finishButton.setStyleSheet("color: rgb(255, 0, 0);\n"
                                        "background-color: rgb(152, 169, 170);")
        self.finishButton.setObjectName("finishButton")
        self.mfWindow = QtWidgets.QLineEdit(self.centralwidget)
        self.mfWindow.setGeometry(QtCore.QRect(90, 50, 61, 31))
        font = QtGui.QFont()
        font.setFamily("AvQest")
        font.setPointSize(12)
        self.mfWindow.setFont(font)
        self.mfWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mfWindow.setObjectName("mfWindow")
        self.mf = QtWidgets.QLabel(self.centralwidget)
        self.mf.setGeometry(QtCore.QRect(20, 60, 31, 21))
        font = QtGui.QFont()
        font.setFamily("AvQest")
        font.setPointSize(14)
        self.mf.setFont(font)
        self.mf.setStyleSheet("color: rgb(255, 0, 0);")
        self.mf.setObjectName("mf")
        self.itemWindow = QtWidgets.QLineEdit(self.centralwidget)
        self.itemWindow.setGeometry(QtCore.QRect(90, 100, 251, 31))
        font = QtGui.QFont()
        font.setFamily("AvQest")
        font.setPointSize(12)
        self.itemWindow.setFont(font)
        self.itemWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.itemWindow.setObjectName("itemWindow")
        self.items = QtWidgets.QLabel(self.centralwidget)
        self.items.setGeometry(QtCore.QRect(10, 100, 41, 21))
        font = QtGui.QFont()
        font.setFamily("AvQest")
        font.setPointSize(14)
        self.items.setFont(font)
        self.items.setStyleSheet("color: rgb(255, 0, 0);")
        self.items.setObjectName("items")
        self.farm = QtWidgets.QLabel(self.centralwidget)
        self.farm.setGeometry(QtCore.QRect(10, 10, 51, 16))
        font = QtGui.QFont()
        font.setFamily("AvQest")
        font.setPointSize(14)
        self.farm.setFont(font)
        self.farm.setStyleSheet("color: rgb(255, 0, 0);")
        self.farm.setObjectName("farm")
        self.runNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.runNumber.setGeometry(QtCore.QRect(393, -8, 61, 41))
        font = QtGui.QFont()
        font.setFamily("AvQest")
        font.setPointSize(12)
        self.runNumber.setFont(font)
        self.runNumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.runNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.runNumber.setDigitCount(4)
        self.runNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.runNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.runNumber.setProperty("value", 1.0)
        self.runNumber.setObjectName("runNumber")
        self.runs = QtWidgets.QLabel(self.centralwidget)
        self.runs.setGeometry(QtCore.QRect(320, 10, 47, 21))
        font = QtGui.QFont()
        font.setFamily("AvQest")
        font.setPointSize(14)
        self.runs.setFont(font)
        self.runs.setStyleSheet("color: rgb(255, 0, 0);")
        self.runs.setObjectName("runs")
        self.disableButton = QtWidgets.QRadioButton(self.centralwidget)
        self.disableButton.setGeometry(QtCore.QRect(30, 170, 141, 17))
        font = QtGui.QFont()
        font.setFamily("AvQest")
        font.setPointSize(14)
        self.disableButton.setFont(font)
        self.disableButton.setStyleSheet("color: rgb(255, 0, 0);")
        self.disableButton.setObjectName("disableButton")
        self.farmWindow = QtWidgets.QLineEdit(self.centralwidget)
        self.farmWindow.setGeometry(QtCore.QRect(90, 0, 151, 31))
        font = QtGui.QFont()
        font.setFamily("AvQest")
        font.setPointSize(12)
        self.farmWindow.setFont(font)
        self.farmWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.farmWindow.setObjectName("farmWindow")
        self.lootButton = QtWidgets.QPushButton(self.centralwidget)
        self.lootButton.setGeometry(QtCore.QRect(360, 110, 75, 23))
        font = QtGui.QFont()
        font.setFamily("AvQest")
        font.setPointSize(14)
        self.lootButton.setFont(font)
        self.lootButton.setStyleSheet("color: rgb(255, 0, 0);\n"
                                      "background-color: rgb(152, 169, 170);")
        self.lootButton.setObjectName("lootButton")
        self.addRun = QtWidgets.QPushButton(self.centralwidget)
        self.addRun.setGeometry(QtCore.QRect(400, 40, 51, 23))
        self.addRun.setStyleSheet("color: rgb(255, 0, 0);\n"
                                  "background-color: rgb(152, 169, 170);")
        self.addRun.setObjectName("addRun")
        self.lootWidget = QtWidgets.QListWidget(self.centralwidget)
        self.lootWidget.setGeometry(QtCore.QRect(30, 220, 421, 621))
        font = QtGui.QFont()
        font.setFamily("AvQest")
        font.setPointSize(14)
        self.lootWidget.setFont(font)
        self.lootWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lootWidget.setObjectName("lootWidget")
        mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 479, 21))
        self.menubar.setObjectName("menubar")
        self.menuok = QtWidgets.QMenu(self.menubar)
        self.menuok.setTitle("")
        self.menuok.setObjectName("menuok")
        mainwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainwindow)
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuok.menuAction())

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)
        self.addRun.clicked.connect(self.increaseRun)
        self.finishButton.clicked.connect(self.close_app)
        self.lootButton.clicked.connect(self.addItem)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("MainWindow", "Loot Tracker"))
        self.finishButton.setText(_translate("MainWindow", "Finished"))
        self.mfWindow.setPlaceholderText(_translate("MainWindow", "0"))
        self.mf.setText(_translate("MainWindow", "MF"))
        self.items.setText(_translate("MainWindow", "Item"))
        self.farm.setText(_translate("MainWindow", "Farm"))
        self.runs.setText(_translate("MainWindow", "Runs"))
        self.disableButton.setText(_translate("MainWindow", "Disable Logs"))
        self.lootButton.setText(_translate("MainWindow", "Loot"))
        self.addRun.setText(_translate("MainWindow", "+"))

    def increaseRun(self):
        global counter
        counter = counter + 1
        self.runNumber.setProperty("value", counter)

    def addItem(self):
        text = self.itemWindow.text()
        if text == "":
            self.itemWindow.clear()
        else:
            output = str(counter) + "- " + str(text)
            lmao.append(output)
            self.lootWidget.addItem(output)
            self.itemWindow.clear()

    def checkButton(self):
        if self.disableButton.isChecked():
            sys.exit()

    def outputLogs(self):
        farmLoc = self.farmWindow.text()
        magicFind = self.mfWindow.text()
        properHour = datetime.datetime.now().strftime('%H:%M')
        Hair = str(datetime.date.today()) + ".txt"
        directory = './Logs/'
        filename = Hair
        file_path = os.path.join(directory, filename)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        with open(file_path, "a") as file:
            file.write(properHour + '\n')
            file.write(
                "I farmed " + farmLoc + " with " + magicFind + "% magic find " + "for " + str(
                    counter) + " runs." + '\n')
            for x in lmao:
                file.write(x + '\n')
            file.write('\n')
            file.close()

    def close_app(self):
        self.checkButton()
        if len(lmao) == 0:
            sys.exit()
        else:
            self.outputLogs()
            sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('chest.ico'))
    mainWindow = QtWidgets.QMainWindow()
    mainWindow.setWindowIcon(QtGui.QIcon('chest.ico'))
    ui = UiMainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
