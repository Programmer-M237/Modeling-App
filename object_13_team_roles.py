from PySide6.QtWidgets import QDialog, QMessageBox, QLineEdit, QWidget, QHBoxLayout, QLabel, QVBoxLayout, QGroupBox, QFrame, QSpinBox
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont
from object_13_team_roles_ui import Ui_Dialog
from collections import defaultdict
from data_store import DataStore4
from object_13_teams_table_view import Teams_data_info
import logging

class Team_roles(QDialog, Ui_Dialog):
    is_name_valid = False
    prev_roles_data = {}
    roles_names_ids = {}
    is_num_of_roles_valid = False
    is_roles_name_duplicate = True
    def __init__(self, index, existing_data=None, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.index = index
        self.data = {}
        self.setWindowTitle(f"Team {self.index + 1}")
        self.setWindowFlags(Qt.Window | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.spinBox_2.setRange(1, 1000)
        self.spinBox.setRange(1, 1000)
        self.spinBox_3.setRange(1, 1000)
        self.spinBox.setValue(1)
        self.spinBox_2.setValue(1)
        self.spinBox_3.setValue(1)
        self.label_3.hide()
        self.label_4.hide()
        self.label_9.hide()
        self.frame_9.hide()
        self.parent = parent
        
        self.debounce_timer = QTimer()
        self.debounce_timer.setSingleShot(True)
        self.debounce_timer.timeout.connect(self.check_duplicate_names)
        
        self.pushButton_6.setToolTip("Automatically saves your data when window closes")
        
        self.label.setText(f"Team {self.index + 1}")
        
        if existing_data:
            logging.basicConfig(level=logging.DEBUG)
            logging.info(f"Displaying existing_data to check (used for debugging):\n{existing_data}")
            self.team_name = existing_data.get("name", "")
            self.is_valid = existing_data.get("is_valid", False)
            self.nom = existing_data.get("nom", 1)
            self.nor = existing_data.get("nor", 1)
            self.go_to_role_var = existing_data.get("go_to_role", 1)
            self.members_order = existing_data.get("members_order_matters", False)
            self.roles_data = existing_data.get("roles_data", {})
            
            self.lineEdit_3.setText(self.team_name)
            self.spinBox_2.setValue(self.nom)
            self.spinBox_3.setValue(self.nor)
            self.spinBox.setValue(self.go_to_role_var)
            
            if self.members_order == True:
                self.checkBox.setChecked(True)
            else:
                self.checkBox.setChecked(False)
                
            layout = self.widget.layout()
            layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            
            for i in range(self.spinBox_3.value()):
                group_widget = QWidget()
                group_layout = QVBoxLayout(group_widget)
                
                groupbox = QGroupBox(f"Role {i + 1}")
                frame = QFrame()
                frame_l = QHBoxLayout(frame)
                label = QLabel("Name")
                line_edit = QLineEdit()
                frame1 = QFrame()
                frame1_l = QHBoxLayout(frame1)
                label1 = QLabel("Number of members")
                spin_box = QSpinBox()
                spin_box.setRange(1, 1000)
                
                
                if i < len(self.roles_data):
                    line_edit.setText(self.roles_data[i]["name"])
                    spin_box.setValue(self.roles_data[i]["nor"])
                
                line_edit.textChanged.connect(self.check_duplicate_names)
                spin_box.valueChanged.connect(self.check_duplicate_names)
                line_edit.textChanged.connect(self.check_entries)
                spin_box.valueChanged.connect(self.check_entries)
                line_edit.textChanged.connect(self.update_roles_data)
                spin_box.valueChanged.connect(self.update_roles_data)
                spin_box.valueChanged.connect(self.check_number_of_roles)
                line_edit.textChanged.connect(self.is_roles_valid)
                
                frame_l.addWidget(label)
                frame_l.addWidget(line_edit)
                frame_l.setContentsMargins(0, 0, 0, 0)
                frame_l.setSpacing(2)
                frame1_l.addWidget(label1, 0)
                frame1_l.addWidget(spin_box, 7)
                frame1_l.setContentsMargins(0, 0, 0, 0)
                frame1_l.setSpacing(2)
                groupbox_l = QVBoxLayout(groupbox)
                groupbox_l.addWidget(frame)
                groupbox_l.addWidget(frame1)
                groupbox_l.setContentsMargins(6, 6, 6, 6)
                groupbox_l.setSpacing(2)
                group_layout.addWidget(groupbox)
                
                layout.addWidget(group_widget)
                
            scrollbar = self.scrollArea.verticalScrollBar()
            scrollbar.setValue(scrollbar.maximum())
            self.check_duplicate_names()
        
        self.pushButton_6.clicked.connect(self.close)
        
        self.lineEdit_3.textChanged.connect(self.check_if_name_exist)
        
        self.spinBox_3.valueChanged.connect(self.generate_roles_widgets)
        
        self.checkBox.stateChanged.connect(self.member_order_check_box_toggle)
        
        self.spinBox_3.valueChanged.connect(self.check_duplicate_names)
        
        self.pushButton.clicked.connect(self.go_to_role)
        self.pushButton_9.clicked.connect(self.go_to_role_error)
        
        self.spinBox_2.valueChanged.connect(self.check_number_of_members)
        
        self.spinBox_2.valueChanged.connect(self.check_number_of_roles)
        self.spinBox_3.valueChanged.connect(self.check_number_of_roles)
        
        self.lineEdit_3.textChanged.connect(self.check_entries)
        self.spinBox_2.valueChanged.connect(self.check_entries)
        self.spinBox_3.valueChanged.connect(self.check_entries)
        
        self.spinBox_3.valueChanged.connect(self.calibrate_number_of_members)
        
        self.check_if_name_exist()
        self.check_duplicate_names()
        self.check_number_of_members()
        self.check_number_of_roles()
            
    def initial_generate_role_widgets(self):
        layout = self.widget.layout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
        for i in range(self.spinBox_3.value()):
            self.roles_data[i] = {"name": "", "nor": 1}
            
            group_widget = QWidget()
            group_layout = QVBoxLayout(group_widget)
            
            groupbox = QGroupBox(f"Role {i + 1}")
            frame = QFrame()
            frame_l = QHBoxLayout(frame)
            label = QLabel("Name")
            line_edit = QLineEdit()
            frame1 = QFrame()
            frame1_l = QHBoxLayout(frame1)
            label1 = QLabel("Number of members")
            spin_box = QSpinBox()
            spin_box.setRange(1, 1000)
            
            if i < len(self.roles_data):
                line_edit.setText(self.roles_data[i]["name"])
                spin_box.setValue(self.roles_data[i]["nor"])
                
            
            frame_l.addWidget(label)
            frame_l.addWidget(line_edit)
            frame_l.setContentsMargins(0, 0, 0, 0)
            frame_l.setSpacing(2)
            frame1_l.addWidget(label1, 0)
            frame1_l.addWidget(spin_box, 7)
            frame1_l.setContentsMargins(0, 0, 0, 0)
            frame1_l.setSpacing(2)
            groupbox_l = QVBoxLayout(groupbox)
            groupbox_l.addWidget(frame)
            groupbox_l.addWidget(frame1)
            groupbox_l.setContentsMargins(6, 6, 6, 6)
            groupbox_l.setSpacing(2)
            group_layout.addWidget(groupbox)
            
            layout.addWidget(group_widget)
            
            line_edit.textChanged.connect(self.check_duplicate_names)
            spin_box.valueChanged.connect(self.check_duplicate_names)
            line_edit.textChanged.connect(self.check_entries)
            spin_box.valueChanged.connect(self.check_entries)
            line_edit.textChanged.connect(self.update_roles_data)
            spin_box.valueChanged.connect(self.update_roles_data)
            spin_box.valueChanged.connect(self.check_number_of_roles)
            line_edit.textChanged.connect(self.is_roles_valid)
            spin_box.valueChanged.connect(self.calibrate_number_of_members)
            
        scrollbar = self.scrollArea.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
        
    def generate_roles_widgets(self):
        layout = self.widget.layout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.prev_roles_data.clear()
        self.roles_data.clear()
        for i in range(layout.count()):
            self.prev_roles_data[i] = {"name": "", "nor": 1}
            group = layout.itemAt(i).widget()
            if group:
                line_edit = group.findChild(QLineEdit)
                if line_edit:
                    self.prev_roles_data[i]["name"] = line_edit.text().strip()
                else:
                    self.prev_roles_data[i]["name"] = ""
                spin_box = group.findChild(QSpinBox)
                if spin_box:
                    self.prev_roles_data[i]["nor"] = spin_box.value()
                else:
                    self.prev_roles_data[i]["nor"] = 1
        
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
        for i in range(self.spinBox_3.value()):
            self.roles_data[i] = {"name": "", "nor": 1}
            
            group_widget = QWidget()
            group_layout = QVBoxLayout(group_widget)
            
            groupbox = QGroupBox(f"Role {i + 1}")
            frame = QFrame()
            frame_l = QHBoxLayout(frame)
            label = QLabel("Name")
            line_edit = QLineEdit()
            frame1 = QFrame()
            frame1_l = QHBoxLayout(frame1)
            label1 = QLabel("Number of members")
            spin_box = QSpinBox()
            spin_box.setRange(1, 1000)
            
            
            if i < len(self.prev_roles_data):
                line_edit.setText(self.prev_roles_data[i]["name"])
                spin_box.setValue(self.prev_roles_data[i]["nor"])
            
            line_edit.textChanged.connect(self.check_duplicate_names)
            spin_box.valueChanged.connect(self.check_duplicate_names)
            line_edit.textChanged.connect(self.check_entries)
            spin_box.valueChanged.connect(self.check_entries)
            line_edit.textChanged.connect(self.update_roles_data)
            spin_box.valueChanged.connect(self.update_roles_data)
            spin_box.valueChanged.connect(self.check_number_of_roles)
            line_edit.textChanged.connect(self.is_roles_valid)
            spin_box.valueChanged.connect(self.calibrate_number_of_members)
            
            frame_l.addWidget(label)
            frame_l.addWidget(line_edit)
            frame_l.setContentsMargins(0, 0, 0, 0)
            frame_l.setSpacing(2)
            frame1_l.addWidget(label1, 0)
            frame1_l.addWidget(spin_box, 7)
            frame1_l.setContentsMargins(0, 0, 0, 0)
            frame1_l.setSpacing(2)
            groupbox_l = QVBoxLayout(groupbox)
            groupbox_l.addWidget(frame)
            groupbox_l.addWidget(frame1)
            groupbox_l.setContentsMargins(6, 6, 6, 6)
            groupbox_l.setSpacing(2)
            group_layout.addWidget(groupbox)
            
            layout.addWidget(group_widget)
            
        scrollbar = self.scrollArea.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
        
    def check_if_name_exist(self) -> None:
        name = self.lineEdit_3.text().strip()
        if not(name):
            self.is_name_valid = False
            self.label_3.hide()
            #self.check_entries()
            return
        for i in range(len(DataStore4.data_store)):
            data = DataStore4.data_store[str(i)]
            if i == self.index:
                continue
            elif name == data['name']:
                self.label_3.setText("❌ A team with the same name already exists")
                self.label_3.show()
                self.is_name_valid = False
                return
            else:
                self.label_3.hide()
        self.is_name_valid = True
        return
    
    def check_duplicate_names(self):
        if self.debounce_timer.isActive():
            self.debounce_timer.stop()
        self.debounce_timer.start(300)
        if not hasattr(self, "model") or self.model is None:
            self.model = QStandardItemModel()
            self.comboBox_2.setModel(self.model)
        self.comboBox_2.clear()
        self.model.clear()
        self.roles_names_ids.clear()
        layout = self.widget.layout()
        total_forms = layout.count()
        
        name_counts = defaultdict(list)
        for i in range(total_forms):
            widget = layout.itemAt(i).widget()
            if widget:
                line_edit = widget.findChild(QLineEdit).text().strip()
                if line_edit:
                    name_counts[line_edit].append(i)
        
        duplicates = {name: idxs for name, idxs in name_counts.items() if len(idxs) > 1}
        
        if duplicates:
            self.frame_9.show()
            self.is_roles_name_duplicate = False

            for name, indexes in duplicates.items():
                header = QStandardItem(name)
                flags = header.flags()
                flags &= ~Qt.ItemIsEnabled
                flags &= ~Qt.ItemIsSelectable
                header.setFlags(flags)
                font = QFont()
                font.setBold(True)
                header.setFont(font)
                self.model.appendRow(header)
                for j in indexes:
                    self.model.appendRow(QStandardItem(f" Role {j + 1}"))
                    self.roles_names_ids[f" Role {j + 1}"] = j
                    
            if self.model.rowCount() > 0:
                self.comboBox_2.setCurrentIndex(0)
        else:
            self.frame_9.hide()
            self.is_roles_name_duplicate = True
    
    def check_entries(self):
        self.check_if_name_exist()
        self.check_duplicate_names()
        self.check_number_of_members()
        self.check_number_of_roles()
        self.is_valid = self.is_name_valid and self.is_num_of_roles_valid and self.is_roles_name_duplicate
    
    def update_roles_data(self):
        layout = self.widget.layout()
        
        self.roles_data.clear()
        for i in range(layout.count()):
            self.roles_data[i] = {"name": "", "nor": 1}
            group = layout.itemAt(i).widget()
            if group:
                line_edit = group.findChild(QLineEdit)
                if line_edit:
                    self.roles_data[i]["name"] = line_edit.text().strip()
                    DataStore4.data_store[str(self.index)]["roles_data"][i]["name"] = line_edit.text().strip()
                else:
                    self.roles_data[i]["name"] = ""
                    DataStore4.data_store[str(self.index)]["roles_data"][i]["name"] = ""
                spin_box = group.findChild(QSpinBox)
                if spin_box:
                    self.roles_data[i]["nor"] = spin_box.value()
                    DataStore4.data_store[str(self.index)]["roles_data"][i]["nor"] = spin_box.value()
                else:
                    self.roles_data[i]["nor"] = 1
                    DataStore4.data_store[str(self.index)]["roles_data"][i]["nor"] = 1
    
    def check_number_of_members(self):
        sum = self.spinBox_2.value()
        for i in range(len(DataStore4.data_store)):
            if i == self.index:
                continue
            else:
                sum += DataStore4.data_store[str(i)]["nom"]
        if sum != DataStore4.total_number_of_members:
            self.label_4.setText("Total sum of members of teams must be equal to the number of members to distribute")
            self.label_4.show()
        else:
            self.label_4.hide()
    
    def check_number_of_roles(self):
        sum = 0
        layout = self.widget.layout()
        for i in range(layout.count()):
            group = layout.itemAt(i).widget()
            if group:
                spin_box = group.findChild(QSpinBox)
                sum += spin_box.value()
        if sum != self.spinBox_2.value():
            self.label_9.setText("Total sum of members of roles must be equal to the number of members of the team")
            self.label_9.show()
            self.is_num_of_roles_valid = False
        else:
            self.label_9.hide()
            self.is_num_of_roles_valid = True
    
    def is_roles_valid(self):
        pass
    
    def get_data(self):
        layout = self.widget.layout()
        
        self.roles_data.clear()
        for i in range(layout.count()):
            self.roles_data[i] = {"name": "", "nor": 1}
            group = layout.itemAt(i).widget()
            if group:
                line_edit = group.findChild(QLineEdit)
                if line_edit:
                    self.roles_data[i]["name"] = line_edit.text().strip()
                else:
                    self.roles_data[i]["name"] = ""
                spin_box = group.findChild(QSpinBox)
                if spin_box:
                    self.roles_data[i]["nor"] = spin_box.value()
                else:
                    self.roles_data[i]["nor"] = 1
        #print(self.roles_data)
        return {
            "name": self.lineEdit_3.text().strip(),
            "is_valid": self.is_valid,
            "nom": self.spinBox_2.value(),
            "nor": self.spinBox_3.value(),
            "roles_data": self.roles_data,
            "go_to_role": self.spinBox.value(),
            "members_order_matters": self.members_order
        }
        
    def accept(self):
        self.data = self.get_data()
        DataStore4.data_store[str(self.index)] = self.data
        #print(self.data)
        super().accept()
        
    def closeEvent(self, event):
        self.accept()
        super().closeEvent(event)
        
    def member_order_check_box_toggle(self, state):
        if state == 2:
            self.members_order = True
        else:
            self.members_order = False
            
    def go_to_role(self) -> None:
        index = self.spinBox.value()
        layout = self.widget.layout()
        total_forms = layout.count()
        
        if index < 1 or index > total_forms:
            QMessageBox.warning(self, "Navigation Error", "Role not found")
            return
        target_widget = layout.itemAt(index - 1).widget()
        if target_widget:
            self.scrollArea.ensureWidgetVisible(target_widget)
        else:
            QMessageBox.warning(self, "Navigation Error", "Role not found")
        self.highlight_temporarily(layout.itemAt(index - 1).widget(), duration=2000)
        
    def go_to_role_error(self) -> None:
        logging.warning("I don't know why, but this function goes to the user desire minus 1. Why? It has the same code structure as go_to_role() which runs perfectly")
        index = self.roles_names_ids[self.comboBox_2.currentText()] + 1 # This additional 1 fixes the problem in the above log
        layout = self.widget.layout()
        total_properties = layout.count()
        
        if index < 1 or index > total_properties:
            QMessageBox.warning(self, "Navigation Error", "Role not found")
            return
        target_widget = layout.itemAt(index - 1).widget()
        if target_widget:
            self.scrollArea.ensureWidgetVisible(target_widget)
        else:
            QMessageBox.warning(self, "Navigation Error", "Role not found")
        self.highlight_temporarily(target_widget, duration=2000)
        
    def highlight_temporarily(self, widget: QWidget, duration: int = 2000):
        widget.setStyleSheet("""
                             QWidget {
                                 border: 2px solid #00ffff;
                                 border-radius: 6px;
                             }
                             """)
        QTimer.singleShot(2000, lambda: widget.setStyleSheet(""))
            
    def calibrate_number_of_members(self):
        #print("The function runs perfectly") # Practically the function auto-corrected itself. But it was normally supposed to, every logic was correct. i don't know why it should misbehave 
        sum = 0
        for i in range(len(DataStore4.data_store[str(self.index)]["roles_data"])):
            sum += DataStore4.data_store[str(self.index)]["roles_data"][i]["nor"]
        self.spinBox_2.setValue(sum)
        DataStore4.data_store[str(self.index)]["nom"] = sum
        self.check_number_of_members()
        self.check_number_of_roles()