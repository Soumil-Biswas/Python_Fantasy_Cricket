from PyQt5.QtCore import Qt

from Fantasy_Cricket import Ui_MainWindow
from Evaluation import Ui_Form

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import mvp

import os

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
Team_name = "NewTeam"
Team_members = []


class MainWindow (QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionNEW_Team.triggered.connect(self.displayPlayers)
        self.ui.actionOPEN_Team.triggered.connect(self.fileOpen)
        self.ui.actionSAVE_Team.triggered.connect(self.fileSave)
        self.ui.actionEVALUATE_Team.triggered.connect(self.evaluation)

        self.ui.Player_list.itemDoubleClicked.connect(self.removePlayerList)
        self.ui.Team_select.itemDoubleClicked.connect(self.removeTeamSelect)

        self.ui.BAT_rb.toggled.connect(self.sortBAT)
        self.ui.BOW_rb.toggled.connect(self.sortBOW)
        self.ui.AR_rb.toggled.connect(self.sortAR)
        self.ui.WK_rb.toggled.connect(self.sortWK)

        self.ui.Set_Team_Name.clicked.connect(self.saveTeamName)

        global all_score
        self.ui.Points_available_field.setText(str(all_score))

    # Saving Team name
    def saveTeamName(self):
        global Team_name
        Team_name = self.ui.Team_name_field.text()
        print(Team_name)

    # Display Players Function
    def displayPlayers(self):
        self.ui.Player_list.clear()
        self.ui.Team_select.clear()
        cur.execute("SELECT player FROM stats;")
        record = cur.fetchall()
        for row in record:
            self.ui.Player_list.addItem(row[0])

    # Gamerule Violation: Duplicate Players
    def gamerule_duplicate(self):
        QtWidgets.QMessageBox.information(self, "Gamerule Violation", "Cannot have Duplicate Players.")

    # Gamerule Violation: Wicketkeeper Limit Exceeded
    def gamerule_wkt_lmt(self):
        QtWidgets.QMessageBox.information(self, "Gamerule Violation",
                                          "Cannot have More than one Wicketkeeper in the Team. "
                                          "Please Remove a Wicketkeeper")

    # Gamerule too OP
    def gamerule_too_op(self):
        QtWidgets.QMessageBox.information(self, "Gamerule Violation",
                                          "Total Points must be below 1000 "
                                          "Please substitute a team member.")

    # Check strength of Team
    def gamerule_team_strength(self):
        QtWidgets.QMessageBox.information(self, "Gamerule Violation",
                                          "Cannot have More than 11 Players in a Team"
                                          "Please Remove Extra Members from the team.")

    # Sort Players by Batsmen
    def sortBAT(self):
        self.ui.Player_list.clear()
        cur.execute("SELECT player FROM stats WHERE ctg = 'BAT';")
        record = self.filterPlayers(cur.fetchall())
        for row in record:
            self.ui.Player_list.addItem(row)

    # Sort Players by Bowlers
    def sortBOW(self):
        self.ui.Player_list.clear()
        cur.execute("SELECT player FROM stats WHERE ctg = 'BWL';")        
        record = self.filterPlayers(cur.fetchall())        
        for row in record:
            self.ui.Player_list.addItem(row)

    # Sort Players by All Rounders
    def sortAR(self):
        self.ui.Player_list.clear()
        cur.execute("SELECT player FROM stats WHERE ctg = 'AR';")
        record = self.filterPlayers(cur.fetchall())
        for row in record:
            self.ui.Player_list.addItem(row)

    # Sort Players by Wicket Keepers
    def sortWK(self):
        self.ui.Player_list.clear()
        cur.execute("SELECT player FROM stats WHERE ctg = 'WK';")
        record = self.filterPlayers(cur.fetchall())
        for row in record:
            self.ui.Player_list.addItem(row)

    # Filter out PLayers that have already been chosen
    def filterPlayers(self, input_players):
        global Team_members
        # print("Input: ", input_players)
        filtered_players = [row[0] for row in input_players if row[0] not in Team_members]
        # print("Filtered: ", filtered_players)
        return filtered_players

    # Move Players from PLayer_List to Team_Select
    def removePlayerList(self, item):
        global strength, team_score
        check_wicket_keepers = self.wktCheck()       
        # Check If the team already has a wicket keeper
        if check_wicket_keepers == 1:
            #  check if the team's score exceeds 1000
            if team_score <= 1000:
                # Check if player already exists on the other side
                try:
                    comp = self.ui.Team_select.findItems(item.text(), Qt.MatchContains)
                except AttributeError as e:  # Catch only specific errors
                    print(f"Error finding item: {e}")
                    comp = []
                except Exception as e:  # Catch all other exceptions
                    print(f"Unexpected error in removePlayerList: {e}")
                    comp = []

                # if player doesn't exist, move them to the other column
                if comp == []:
                    strength = self.ui.Team_select.count()
                    # Check if the team already have 11 players
                    if strength < 11:
                        self.ui.Player_list.takeItem(self.ui.Player_list.row(item))
                        self.ui.Team_select.addItem(item.text())
                        self.addToCategory(item)
                        self.scoreAdd(item)
                        self.setTeamMembers()
                    else:
                        self.gamerule_team_strength()
                else:
                    self.gamerule_duplicate()
            else:
                self.gamerule_too_op()

    # Move Players from Team_Select to PLayer_List
    def removeTeamSelect(self, item):
        try:
            comp = self.ui.Player_list.findItems(item.text(), Qt.MatchContains)
        except AttributeError as e:  # Catch only specific errors
            print(f"Error finding item: {e}")
            comp = []
        except Exception as e:  # Catch all other exceptions
            print(f"Unexpected error in removeTeamSelect: {e}")
            comp = []

        if comp == []:
            self.ui.Team_select.takeItem(self.ui.Team_select.row(item))
            self.ui.Player_list.addItem(item.text())
        else:
            self.ui.Team_select.takeItem(self.ui.Team_select.row(item))
        self.removeFromCategory(item)
        self.scoreSubtract(item)
        self.setTeamMembers()


    # Check no. of wicketkeepers
    def wktCheck(self):
        global wk_count
        if wk_count > 1:
            wk_count = 1
            self.gamerule_wkt_lmt()
            return 0
        return 1

    def addToCategory(self, item):
        global wk_count, bat_count, bow_count, ar_count, strength
        # Get the name of the selected player
        checker = str(item.text())

        cur.execute("SELECT ctg FROM stats WHERE Player = ?", (checker,))
        categories = cur.fetchall()
        for row in categories:
            cat = (row[0])
        if cat == "WK":
            if strength < 10:
                wk_count = wk_count + 1
                self.ui.WK_no.setText(str(wk_count))
            else:
                self.ui.WK_no.setText(str(wk_count))
        elif cat == "BAT":
            if strength < 10:
                bat_count = bat_count + 1
                self.ui.BAT_no.setText((str(bat_count)))
            else:
                self.ui.BAT_no.setText((str(bat_count)))
        elif cat == "BWL":
            if strength < 10:
                bow_count = bow_count + 1
                self.ui.BOW_no.setText((str(bow_count)))
            else:
                self.ui.BOW_no.setText((str(bow_count)))
        elif cat == "AR":
            if strength < 10:
                ar_count = ar_count + 1
                self.ui.AR_no.setText((str(ar_count)))
            else:
                self.ui.AR_no.setText((str(ar_count)))

    def removeFromCategory(self, item):
        global wk_count, bat_count, bow_count, ar_count
        checker = str(item.text())

        cur.execute("SELECT ctg FROM stats WHERE Player = ?", (checker,))
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

    # Open Team
    def fileOpen(self):
        global team_score, all_score, Team_name
        file_location, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        if not file_location:
            return

        Team_name = os.path.basename(file_location)  # Extract only the filename
        self.ui.Team_name_field.setText(Team_name)  # Set filename in input field

        self.ui.Team_select.clear()
        team = self.ui.Team_select
        team_score = 0
        all_score = 1000

        with open(file_location, 'r') as file:
            entries = [e.strip() for e in file.readlines()]
        team.insertItems(0, entries)

    # Save Team
    def fileSave(self):
        global Team_name
        file_location, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', Team_name)
        if not file_location:
            return        
        
        print(file_location)
        team = self.ui.Team_select
        entries = '\n'.join(team.item(ii).text() for ii in range(team.count()))

        with open(file_location, 'w') as file:
            file.write(entries)

    # Score Calculation Module
    def scoreAdd(self, item):
        checker = str(item.text())
        global team_score, all_score
        cur.execute("SELECT value FROM stats WHERE Player = ?", (checker,))
        top = cur.fetchall()
        for row in top:
            player_points = (row[0])
        team_score = team_score + player_points
        all_score = all_score - player_points
        self.ui.Points_used_field.setText(str(team_score))
        self.ui.Points_available_field.setText((str(all_score)))

    def scoreSubtract(self, item):
        checker = str(item.text())
        global team_score, all_score
        cur.execute("SELECT value FROM stats WHERE Player = ?", (checker,))
        top = cur.fetchall()
        for row in top:
            player_points = (row[0])
        team_score = team_score - player_points
        all_score = all_score + player_points
        self.ui.Points_used_field.setText(str(team_score))
        self.ui.Points_available_field.setText((str(all_score)))

    # Set Team members
    def setTeamMembers(self):
        global Team_members
        team = self.ui.Team_select
        Team_members.clear()
        for ii in range(team.count()):
            entries = team.item(ii).text()
            Team_members.append(entries)
        print("Team_members: ", Team_members)

    # Team Evaluation
    def evaluation(self):
        #  check if the team's score exceeds 1000
        if team_score <= 1000:
            self.setTeamMembers()
            ev = Evaluation()
            ev.exec()
        else:
            self.gamerule_too_op()


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
            self.ui.label.setText("Add more members to your Team!")

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