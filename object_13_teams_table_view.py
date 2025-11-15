from PySide6.QtWidgets import QDialog, QTreeWidgetItem, QHeaderView, QMessageBox, QAbstractItemView
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon, QColor
from object_13_teams_table_view_ui import Ui_Dialog
from data_store import DataStore4

class Teams_data_info(QDialog, Ui_Dialog):
    data = []
    COL_TEAM_ROLE = 0
    
    def __init__(self, team_order, sum): # sum is the total number of members in teams
        super().__init__()
        self.setupUi(self)
        self.team_order = team_order
        self.setWindowTitle("Summary of teams information")
        self.setWindowIcon(QIcon())
        self.resize(700, 360)
        self.spinBox_2.setRange(1, 1000)
        self.sum = sum
        
        self.prepare_data() # It arranges the required data into lists and dictionaries so that they can be displayed. IT NOW CALLS THE populate_data(data) function to populate the data unto the table
        
        self.pushButton_7.clicked.connect(self.go_to_team)
        
    def prepare_data(self):
        row = {}
        role_row = {}
        self.team_keys = sorted(DataStore4.data_store.keys(), key=lambda x: int(x))
        self.data = []
        for key in self.team_keys:
            team_data = DataStore4.data_store[key]
            row = {
                "team_name": "",
                "nom": 1,
                "roles": [],
                "members_order": False,
                "is_valid": False
            }
            row["team_name"] = DataStore4.data_store[key]["name"]
            row["nom"] = DataStore4.data_store[key]["nom"]
            for j in DataStore4.data_store[key]["roles_data"].values():
                role_row = {
                    "role_name": "",
                    "nom": 1
                }
                role_row["role_name"] = j["name"]
                role_row["nom"] = j["nor"]
                row["roles"].append(role_row)
            row["members_order"] = DataStore4.data_store[key]["members_order_matters"]
            row["is_valid"] = DataStore4.data_store[key]["is_valid"]
            self.data.append(row)
        self.populate_data(self.data)
        
    def populate_data(self, data):
        self.team_items = []
        self.treeWidget.setColumnCount(4)
        self.treeWidget.setHeaderLabels(["Team/Role", "Number of members", "Members order matters", "Validity"])
        
        for team_item in data:
            item = QTreeWidgetItem(self.treeWidget, [f"Team {team_item["team_name"]}", str(team_item["nom"]), "", str(team_item["is_valid"])])
            self.team_items.append(item)
            item.setTextAlignment(0, Qt.AlignCenter)
            item.setTextAlignment(1, Qt.AlignCenter)
            item.setTextAlignment(2, Qt.AlignCenter)
            item.setTextAlignment(3, Qt.AlignCenter)
            for role in team_item["roles"]:
                role_item = QTreeWidgetItem(item, [role["role_name"], str(role["nom"]), str(team_item["members_order"]), ""])
                role_item.setTextAlignment(0, Qt.AlignCenter)
                role_item.setTextAlignment(1, Qt.AlignCenter)
                
        self.treeWidget.header().setSectionResizeMode(QHeaderView.Stretch)
        
        nom = 0 # nom: number of members
        valid = True
        for i in range(len(DataStore4.data_store)):
            tnmr = 0 # tmnr: total number of members of roles
            for j in DataStore4.data_store[str(i)]["roles_data"].values():
                print(j)
                tnmr += j["nor"]
            nom = DataStore4.data_store[str(i)]["nom"]
            if tnmr == nom:
                valid = valid and True
            else:
                valid = valid and False
        
        if (self.sum != DataStore4.total_number_of_members) or (valid == False):
            print(f"{self.sum != DataStore4.total_number_of_members}/{valid == False}")
            self.label.setStyleSheet("""
                                     QLabel {
                                         color: red
                                     }
                                     """)
        else:
            self.label.setStyleSheet("""
                                     QLabel {
                                         color: black
                                     }
                                     """)
        self.label.setText(f"Number of members: {DataStore4.total_number_of_members}\nTotal sum of number of members in teams: {self.sum}\nTeams order matters: {self.team_order}")
        
    def go_to_team(self):
        index = self.spinBox_2.value() - 1
        if 0 <= index < len(self.data):
            team_item = self.team_items[index]
            self.treeWidget.setCurrentItem(team_item)
            self.treeWidget.scrollToItem(team_item, QAbstractItemView.PositionAtTop)
            self.scrollArea.ensureWidgetVisible(team_item, xMargin=0, yMaegin=20)
            for i in range(4):
                team_item.setBackground(i, QColor(QColor(135, 206, 250)))
        else:
            QMessageBox.warning(self, "Invalid Index", f"Please enter a team index between 1 and {len(self.data)}")