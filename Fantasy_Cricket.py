# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fantasy_Cricket.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Your_selections = QtWidgets.QLabel(self.centralwidget)
        self.Your_selections.setGeometry(QtCore.QRect(50, 40, 111, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Your_selections.setFont(font)
        self.Your_selections.setStyleSheet("font: 75 bold 8pt \"MS Shell Dlg 2\";")
        self.Your_selections.setObjectName("Your_selections")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 30, 721, 101))
        self.textBrowser.setStyleSheet("background-color: rgba(240, 240, 240,50 );")
        self.textBrowser.setObjectName("textBrowser")
        self.Points_available = QtWidgets.QLabel(self.centralwidget)
        self.Points_available.setGeometry(QtCore.QRect(70, 170, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Points_available.setFont(font)
        self.Points_available.setObjectName("Points_available")
        self.Points_used = QtWidgets.QLabel(self.centralwidget)
        self.Points_used.setGeometry(QtCore.QRect(440, 170, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Points_used.setFont(font)
        self.Points_used.setObjectName("Points_used")
        self.Team_Name = QtWidgets.QLabel(self.centralwidget)
        self.Team_Name.setGeometry(QtCore.QRect(460, 210, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Team_Name.setFont(font)
        self.Team_Name.setObjectName("Team_Name")
        self.Points_available_field = QtWidgets.QLabel(self.centralwidget)
        self.Points_available_field.setGeometry(QtCore.QRect(180, 170, 71, 16))
        self.Points_available_field.setStyleSheet("color:rgb(0, 198, 198);\n"
"font: 75 bold 8pt \"Comic Sans MS\";")
        self.Points_available_field.setObjectName("Points_available_field")
        self.Points_used_field = QtWidgets.QLabel(self.centralwidget)
        self.Points_used_field.setGeometry(QtCore.QRect(520, 170, 71, 16))
        self.Points_used_field.setStyleSheet("color:rgb(0, 198, 198);\n"
"font: 75 bold 8pt \"Comic Sans MS\";")
        self.Points_used_field.setObjectName("Points_used_field")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 210, 231, 19))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.BAT_rb = QtWidgets.QRadioButton(self.layoutWidget)
        self.BAT_rb.setObjectName("BAT_rb")
        self.horizontalLayout_2.addWidget(self.BAT_rb)
        self.BOW_rb = QtWidgets.QRadioButton(self.layoutWidget)
        self.BOW_rb.setObjectName("BOW_rb")
        self.horizontalLayout_2.addWidget(self.BOW_rb)
        self.AR_rb = QtWidgets.QRadioButton(self.layoutWidget)
        self.AR_rb.setObjectName("AR_rb")
        self.horizontalLayout_2.addWidget(self.AR_rb)
        self.WK_rb = QtWidgets.QRadioButton(self.layoutWidget)
        self.WK_rb.setObjectName("WK_rb")
        self.horizontalLayout_2.addWidget(self.WK_rb)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(51, 70, 701, 19))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BAT = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BAT.setFont(font)
        self.BAT.setTextFormat(QtCore.Qt.AutoText)
        self.BAT.setObjectName("BAT")
        self.horizontalLayout.addWidget(self.BAT)
        self.BAT_no = QtWidgets.QLabel(self.layoutWidget1)
        self.BAT_no.setStyleSheet("color:rgb(0, 198, 198);\n"
"font: 75 bold 8pt \"Comic Sans MS\";")
        self.BAT_no.setObjectName("BAT_no")
        self.horizontalLayout.addWidget(self.BAT_no)
        self.BOW = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BOW.setFont(font)
        self.BOW.setTextFormat(QtCore.Qt.AutoText)
        self.BOW.setObjectName("BOW")
        self.horizontalLayout.addWidget(self.BOW)
        self.BOW_no = QtWidgets.QLabel(self.layoutWidget1)
        self.BOW_no.setStyleSheet("color:rgb(0, 198, 198);\n"
"font: 75 bold 8pt \"Comic Sans MS\";")
        self.BOW_no.setObjectName("BOW_no")
        self.horizontalLayout.addWidget(self.BOW_no)
        self.AR = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.AR.setFont(font)
        self.AR.setTextFormat(QtCore.Qt.AutoText)
        self.AR.setObjectName("AR")
        self.horizontalLayout.addWidget(self.AR)
        self.AR_no = QtWidgets.QLabel(self.layoutWidget1)
        self.AR_no.setStyleSheet("color:rgb(0, 198, 198);\n"
"font: 75 bold 8pt \"Comic Sans MS\";")
        self.AR_no.setObjectName("AR_no")
        self.horizontalLayout.addWidget(self.AR_no)
        self.WK = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.WK.setFont(font)
        self.WK.setTextFormat(QtCore.Qt.AutoText)
        self.WK.setObjectName("WK")
        self.horizontalLayout.addWidget(self.WK)
        self.WK_no = QtWidgets.QLabel(self.layoutWidget1)
        self.WK_no.setStyleSheet("color:rgb(0, 198, 198);\n"
"font: 75 bold 8pt \"Comic Sans MS\";")
        self.WK_no.setObjectName("WK_no")
        self.horizontalLayout.addWidget(self.WK_no)
        self.Player_list = QtWidgets.QListWidget(self.centralwidget)
        self.Player_list.setGeometry(QtCore.QRect(70, 240, 256, 291))
        self.Player_list.setObjectName("Player_list")
        self.Team_select = QtWidgets.QListWidget(self.centralwidget)
        self.Team_select.setGeometry(QtCore.QRect(440, 240, 256, 291))
        self.Team_select.setObjectName("Team_select")
        self.Team_name_field = QtWidgets.QLineEdit(self.centralwidget)
        self.Team_name_field.setGeometry(QtCore.QRect(540, 210, 113, 20))
        self.Team_name_field.setStyleSheet("color:rgb(0, 198, 198);\n"
"font: 75 bold 8pt \"Comic Sans MS\";")
        self.Team_name_field.setObjectName("Team_name_field")
        self.Set_Team_Name = QtWidgets.QPushButton(self.centralwidget)
        self.Set_Team_Name.setGeometry(QtCore.QRect(660, 210, 31, 20))
        self.Set_Team_Name.setObjectName("Set_Team_Name")
        self.Team_select.raise_()
        self.Player_list.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.textBrowser.raise_()
        self.Your_selections.raise_()
        self.Points_available.raise_()
        self.Points_used.raise_()
        self.Team_Name.raise_()
        self.Points_available_field.raise_()
        self.Points_used_field.raise_()
        self.Team_name_field.raise_()
        self.Set_Team_Name.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Your_selections.setText(_translate("MainWindow", "Your Selections"))
        self.Points_available.setText(_translate("MainWindow", "Points Available"))
        self.Points_used.setText(_translate("MainWindow", "Points Used"))
        self.Team_Name.setText(_translate("MainWindow", "Team Name"))
        self.Points_available_field.setText(_translate("MainWindow", "####"))
        self.Points_used_field.setText(_translate("MainWindow", "####"))
        self.BAT_rb.setText(_translate("MainWindow", "BAT"))
        self.BOW_rb.setText(_translate("MainWindow", "BOW"))
        self.AR_rb.setText(_translate("MainWindow", "AR"))
        self.WK_rb.setText(_translate("MainWindow", "WK"))
        self.BAT.setText(_translate("MainWindow", "Batsmen (BAT)"))
        self.BAT_no.setText(_translate("MainWindow", "##"))
        self.BOW.setText(_translate("MainWindow", "Bowlers (BOW)"))
        self.BOW_no.setText(_translate("MainWindow", "##"))
        self.AR.setText(_translate("MainWindow", "Allrounder (AR)"))
        self.AR_no.setText(_translate("MainWindow", "##"))
        self.WK.setText(_translate("MainWindow", "Wicket-keeper (WK)"))
        self.WK_no.setText(_translate("MainWindow", "##"))
        self.Set_Team_Name.setText(_translate("MainWindow", "Set"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
