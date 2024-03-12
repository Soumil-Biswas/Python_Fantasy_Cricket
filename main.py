from PyQt5.QtCore import Qt

from Fantasy_Cricket import Ui_MainWindow
from Evaluation import Ui_Form

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import mvp

library = sqlite3.connect('Players.db')
cur = library.cursor()

# global variables
bat_count = 0
bow_count = 0
ar_count = 0
wk_count = 0
strength = 0
team_score = 0
all_score = 1000
Team_name = "nill"
Team_members = []


class MainWindow (QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionNEW_Team.triggered.connect(self.display_players)
        self.ui.actionOPEN_Team.triggered.connect(self.file_open)
        self.ui.actionSAVE_Team.triggered.connect(self.file_save)
        self.ui.actionEVALUATE_Team.triggered.connect(self.evaluation)

        self.ui.Player_list.itemDoubleClicked.connect(self.removeplayerlist)
        self.ui.Team_select.itemDoubleClicked.connect(self.removeteamselect)

        self.ui.BAT_rb.toggled.connect(self.sortBAT)
        self.ui.BOW_rb.toggled.connect(self.sortBOW)
        self.ui.AR_rb.toggled.connect(self.sortAR)
        self.ui.WK_rb.toggled.connect(self.sortWK)

        self.ui.Set_Team_Name.clicked.connect(self.saveteamname)

        global all_score
        self.ui.Points_available_field.setText(str(all_score))

    # Saving Team name
    def saveteamname(self):
        global Team_name
        Team_name = self.ui.Team_name_field.text()
        print(Team_name)

    # Display Players Function
    def display_players(self):
        cur.execute("SELECT player FROM stats;")
        record = cur.fetchall()
        for row in record:
            self.ui.Player_list.addItem(row[0])

    # Gamerule Violation: Duplicate Players
    def gamerule_duplicate(self):
        QtWidgets.QMessageBox.information(self, "Gamerule Violation", "Cannot have Duplicate Players.")

    # Gamerule Violation: Wicketkeeper Limit Exceeded
    def gamerule_wktlmt(self):
        QtWidgets.QMessageBox.information(self, "Gamerule Violation",
                                          "Cannot have More than one Wicketkeeper in the Team. "
                                          "Please Remove a Wicketkeeper")

    # Gamerule too OP
    def too_op(self):
        QtWidgets.QMessageBox.information(self, "Gamerule Violation",
                                          "Total Points must be below 1000 "
                                          "Please substitute a team member.")

    # Sort Players
    def sortBAT(self):
        self.ui.Player_list.clear()
        cur.execute("SELECT player FROM stats WHERE ctg = 'BAT';")
        record = cur.fetchall()
        for row in record:
            self.ui.Player_list.addItem(row[0])

    def sortBOW(self):
        self.ui.Player_list.clear()
        cur.execute("SELECT player FROM stats WHERE ctg = 'BWL';")
        record = cur.fetchall()
        for row in record:
            self.ui.Player_list.addItem(row[0])

    def sortAR(self):
        self.ui.Player_list.clear()
        cur.execute("SELECT player FROM stats WHERE ctg = 'AR';")
        record = cur.fetchall()
        for row in record:
            self.ui.Player_list.addItem(row[0])

    def sortWK(self):
        self.ui.Player_list.clear()
        cur.execute("SELECT player FROM stats WHERE ctg = 'WK';")
        record = cur.fetchall()
        for row in record:
            self.ui.Player_list.addItem(row[0])

    # Move Players from one list to another
    def removeplayerlist(self, item):
        global strength
        a = self.wktcheck(item)
        b = self.scoreadd(item)
        if a == 1:
            if b == 1:
                try:
                    comp = self.ui.Team_select.findItems(item.text(), Qt.MatchContains)
                except:
                    comp = 'honk'

                if comp == []:
                    strength = self.ui.Team_select.count()
                    if strength < 11:
                        self.ui.Player_list.takeItem(self.ui.Player_list.row(item))
                        self.ui.Team_select.addItem(item.text())
                    else:
                        self.teamstrength()
                else:
                    self.gamerule_duplicate()
            else:
                self.too_op()
        else:
            self.gamerule_wktlmt()

    def removeteamselect(self, item):
        try:
            comp = self.ui.Player_list.findItems(item.text(), Qt.MatchContains)
        except:
            comp = 'honk'

        if comp == []:
            self.ui.Team_select.takeItem(self.ui.Team_select.row(item))
            self.ui.Player_list.addItem(item.text())
        else:
            self.ui.Team_select.takeItem(self.ui.Team_select.row(item))

        self.wktreturn(item)
        self.scoresubtract(item)

    # Check no. of wicketkeepers
    def wktcheck(self, Item):
        global wk_count, bat_count, bow_count, ar_count, strength
        checker = str(Item.text())

        cur.execute("SELECT ctg FROM stats WHERE Player = '"+checker+"';")
        top = cur.fetchall()
        for row in top:
            checkee = (row[0])
        if checkee == "WK":
            if strength < 10:
                wk_count = wk_count + 1
                self.ui.WK_no.setText(str(wk_count))
            else:
                self.ui.WK_no.setText(str(wk_count))
        elif checkee == "BAT":
            if strength < 10:
                bat_count = bat_count + 1
                self.ui.BAT_no.setText((str(bat_count)))
            else:
                self.ui.BAT_no.setText((str(bat_count)))
        elif checkee == "BWL":
            if strength < 10:
                bow_count = bow_count + 1
                self.ui.BOW_no.setText((str(bow_count)))
            else:
                self.ui.BOW_no.setText((str(bow_count)))
        elif checkee == "AR":
            if strength < 10:
                ar_count = ar_count + 1
                self.ui.AR_no.setText((str(ar_count)))
            else:
                self.ui.AR_no.setText((str(ar_count)))
        if wk_count > 1:
            wk_count = wk_count - 1
            return 0
        return 1

    def wktreturn(self, Item):
        global wk_count, bat_count, bow_count, ar_count
        checker = str(Item.text())

        cur.execute("SELECT ctg FROM stats WHERE Player = '" + checker + "';")
        top = cur.fetchall()
        for row in top:
            checkee = (row[0])
        if checkee == "WK":
            wk_count = wk_count - 1
            self.ui.WK_no.setText(str(wk_count))
        elif checkee == "BAT":
            bat_count = bat_count - 1
            self.ui.BAT_no.setText((str(bat_count)))
        elif checkee == "BWL":
            bow_count = bow_count - 1
            self.ui.BOW_no.setText((str(bow_count)))
        elif checkee == "AR":
            ar_count = ar_count - 1
            self.ui.AR_no.setText((str(ar_count)))

    # Check strength of Team
    def teamstrength(self):
        QtWidgets.QMessageBox.information(self, "Gamerule Violation",
                                          "Cannot have More than 11 Players in a Team"
                                          "Please Remove Extra Members from the team.")

    # Open Team
    def file_open(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        fname = (name[0])
        self.ui.Team_select.clear()
        team = self.ui.Team_select
        with open(fname, 'r') as file:
            entries = [e.strip() for e in file.readlines()]
        team.insertItems(0, entries)

    # Save Team
    def file_save(self):
        name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')
        fname = (name[0])
        print(fname)
        team = self.ui.Team_select
        entries = '\n'.join(team.item(ii).text() for ii in range(team.count()))
        with open(fname, 'w') as file:
            file.write(entries)
            file.close()

    # Score Calculation Module
    def scoreadd(self, Item):
        checker = str(Item.text())
        global team_score, all_score
        cur.execute("SELECT value FROM stats WHERE Player = '" + checker + "';")
        top = cur.fetchall()
        for row in top:
            checkee = (row[0])
            team_score = team_score + checkee
            all_score = all_score - checkee
            if team_score > 1000:
                return 0
            else:
                self.ui.Points_used_field.setText(str(team_score))
                self.ui.Points_available_field.setText((str(all_score)))
                return 1

    def scoresubtract(self, Item):
        checker = str(Item.text())
        global team_score, all_score
        cur.execute("SELECT value FROM stats WHERE Player = '" + checker + "';")
        top = cur.fetchall()
        for row in top:
            checkee = (row[0])
            team_score = team_score - checkee
            all_score = all_score + checkee
            self.ui.Points_used_field.setText(str(team_score))
            self.ui.Points_available_field.setText((str(all_score)))

    # Team Evaluation
    def evaluation(self):
        global Team_members
        team = self.ui.Team_select
        for ii in range(team.count()):
            entries = team.item(ii).text()
            Team_members.append(entries)
        print(Team_members)
        ev = Evaluation()
        ev.exec()


class Evaluation (QtWidgets.QDialog):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.Teamcheck()

        global Team_name
        print(Team_name)
        self.ui.SelectTeam.addItem(str(Team_name))

        self.eval_seal()
        self.ui.SelectTeam.activated.connect(self.display_team)
        self.ui.SelectMatch.activated.connect(self.eval_activ)

        self.ui.Eval_pushButton.clicked.connect(self.eval_module)

    # Check Gamerules for Team
    def Teamcheck(self):
        global strength
        print("Str = {}" .format(strength))
        if strength < 0:
            QtWidgets.QMessageBox.information(self, "Gamerule Violation", "Teams must have 11 members.")
            self.ui.SelectMatch.setEnabled(False)
            self.ui.SelectTeam.setEnabled(False)
            self.ui.label.setText("              Add more members to your Team!")

    # Display Team from Box
    def display_team(self):
        global Team_members
        self.ui.listWidget_Players.clear()
        for i in Team_members:
            self.ui.listWidget_Players.addItem(str(i))

    # Disable Evaluation Button until activated
    def eval_seal(self):
        self.ui.Eval_pushButton.setEnabled(False)

    # Enable Disabled Evaluation Button
    def eval_activ(self):
        self.ui.Eval_pushButton.setEnabled(True)

    def eval_module(self):
        self.ui.listWidget_Points.clear()
        global Team_members
        total_score = 0
        for i in Team_members:
            print(i)
            score = mvp.evaluate(i)
            self.ui.listWidget_Points.addItem(str(score))

        cot = self.ui.listWidget_Points
        for ii in range(cot.count()):
            total_score = total_score + int(cot.item(ii).text())
        self.ui.Point_Val.setText(str(total_score))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = MainWindow()
    widget.show()
    app.exec_()
