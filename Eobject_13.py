from PySide6.QtWidgets import QMessageBox, QFileDialog, QWidget, QDialog, QButtonGroup, QHBoxLayout, QVBoxLayout, QFrame, QSpinBox, QLabel, QLineEdit, QGroupBox, QPushButton
from PySide6.QtCore import Qt, Signal, QTimer, QStandardPaths
from pathlib import Path
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont
import json
from cryptography.fernet import Fernet
from collections import defaultdict
from Eobject_13_ui import Ui_Dialog
from data_store import DataStore4
from object_13_team_roles import Team_roles
from object_13_teams_table_view import Teams_data_info
from temp_objects import Id13
from temp_events import Events
from step_2_of_event_creation import Event_properties
import symbols

class EObject_13(QWidget, Ui_Dialog):
    cancel_clicked = Signal()
    is_name_valid = True
    form_type = "default"
    previous_form_type = "default"
    saved_data = []
    previous_number_of_forms = 1
    prev_data_store = {}
    teams_id_list = {}
    team_order = False
    is_num_of_members_valid = False
    is_roles_valid = False
    is_alternative_base = False
    is_forms_valid = False
    ENCRYPTION_KEY = 'Rll0H4fZf5TvH1E-mk0qwcZ1cETu6jlA_2PiwZ9cvls='
    cipher = Fernet(ENCRYPTION_KEY)
    documents = Path(QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation))
    m_app_folder = documents / "M App" / "Objects 13"
    m_app_folder.mkdir(parents=True, exist_ok=True)
    documents_dir = m_app_folder
    untitled_x = 1 # Use to name the untitled files of the Save As Window
    
    close_by_code_initiated = Signal()
    
    def __init__(self, stacked_widget, top_window, event_name):
        super().__init__()
        self.setupUi(self)
        self.name = "page_13"
        self.label_2.hide()
        self.spin_box.setRange(1, 1000)
        self.spin_box.setValue(1)
        self.spinBox.setRange(1, 1000)
        self.spinBox.setValue(1)
        self.spinBox_2.setRange(1, 1000)
        self.spinBox_2.setValue(1)
        self.spinBox_3.setRange(1, 1000)
        self.spinBox_3.setValue(1)
        self.initial_generate_team_widgets()
        self.check_roles()
        self.table_window = None
        self.top_window = top_window
        self.stacked_widget = stacked_widget
        self.event_name = event_name
        self.label_10.hide()
        self.label_7.hide()
        self.label_8.setText('<a href="#">Click here to view a summary of the teams information</a>')
        self.pushButton.setEnabled(False)
        self.frame_9.hide()
        
        self.label_8.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.label_8.setOpenExternalLinks(False)
        self.label_8.linkActivated.connect(self.open_table_window)
        
        #### Problem 001
        self.lineEdit.setText(f"{self.event_name}'s object")
        self.lineEdit.setEnabled(False)
        ####
        
        self.top_window_close_signal = Signal()
        self.stacked_widget_page_change_signal = Signal()
        self.top_window.destroyed.connect(self.close_team_info_window)
        self.stacked_widget.currentChanged.connect(self.close_team_info_window)
        
        self.pushButton_2.clicked.connect(self.cancel_clicked.emit)
        
        #self.lineEdit.textChanged.connect(self.check_if_name_exist)
        
        self.forms_type = QButtonGroup()
        self.radioButton_4.setChecked(True)
        self.forms_type.addButton(self.radioButton_4)
        self.forms_type.addButton(self.radioButton_5)
        self.forms_type.addButton(self.radioButton_6)
        self.forms_type.buttonClicked.connect(self.forms_type_radio_btn_clicked)
        self.forms_type_radio_btn_clicked()
        
        self.spin_box.valueChanged.connect(self.generate_form_widgets)
        self.forms_type.buttonClicked.connect(self.generate_form_widgets)
        
        self.pushButton_3.clicked.connect(self.go_to_form)
        
        self.spinBox_3.valueChanged.connect(self.generate_team_widgets)
        
        self.spinBox_3.valueChanged.connect(self.check_roles)
        
        self.pushButton_8.clicked.connect(self.go_to_team_error)
        self.pushButton_7.clicked.connect(self.go_to_team)
        
        self.checkBox_2.stateChanged.connect(self.team_order_check_box_toggle)
        
        self.spin_box.valueChanged.connect(self.store_total_number_of_members)
        
        self.spin_box.valueChanged.connect(self.check_number_of_members)
        
        self.lineEdit.textChanged.connect(self.check_entries)
        self.spin_box.valueChanged.connect(self.check_entries)
        self.lineEdit_2.textChanged.connect(self.check_entries)
        self.spinBox_3.valueChanged.connect(self.check_entries)
        
        self.pushButton_4.setToolTip(f"Save this object creation session")
        self.pushButton_5.setToolTip("Save this object creation session")
        self.pushButton_6.setToolTip("Load object creation session with object id '13'")
        
        self.config_data = {"object_id": "13", "object_name": "", "nOf": 1, "form_type": "default", "prev_form_type": "default", "form": "", "forms": [], "gtfnum": 1, "prev_nof": 1, "not": 1, "team_order": False, "teams": {}, "gtteam": 1}
        
        self.pushButton_4.clicked.connect(self.save_config)
        self.pushButton_5.clicked.connect(self.save_as_config)
        self.pushButton_6.clicked.connect(self.load_config_dialog)
        
        self.current_file = None
        
        self.pushButton.clicked.connect(self.create_object)
        
    def mouseMoveEvent(self, event):
        self.check_entries()
        return super().mouseMoveEvent(event)
    
    # def check_if_name_exist(self) -> None:
    #     name = self.lineEdit.text().strip()
        
    #     if not(name):
    #         self.is_name_valid = False
    #     elif (name, "object") in EntityManager._items:
    #         self.label_2.setText("❌ An object with the same name already exists")
    #         self.label_2.show()
    #         self.is_name_valid = False
    #     elif EntityManager.name_exists_with_different_type(EntityManager, name, "object"):
    #         self.label_2.setText("⚠️ An event or system with the same name already exists")
    #         self.label_2.show()
    #         self.is_name_valid = True
    #     else:
    #         self.label_2.hide()
    #         self.is_name_valid = True
            
    def forms_type_radio_btn_clicked(self):
        if self.radioButton_4.isChecked():
            if self.previous_form_type == "alternative":
                self.previous_number_of_forms = self.spin_box.value()
                layout = self.widget.layout()
                
                self.saved_data = []
                for i in range(layout.count()):
                    row = layout.itemAt(i).widget()
                    if row:
                        line_edit = row.findChild(QLineEdit)
                        if line_edit:
                            self.saved_data.append(line_edit.text())
                        else:
                            self.saved_data.append("")
            layout = self.widget.layout()
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
                    
            self.form_type = "default"
            self.previous_form_type = "default"
            self.lineEdit_2.setEnabled(False)
            self.spinBox.setEnabled(False)
            self.pushButton_3.setEnabled(False)
        elif self.radioButton_5.isChecked():
            if self.previous_form_type == "alternative":
                self.previous_number_of_forms = self.spin_box.value()
                layout = self.widget.layout()
                
                self.saved_data = []
                for i in range(layout.count()):
                    row = layout.itemAt(i).widget()
                    if row:
                        line_edit = row.findChild(QLineEdit)
                        if line_edit:
                            self.saved_data.append(line_edit.text())
                        else:
                            self.saved_data.append("")
            layout = self.widget.layout()
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
                    
            self.form_type = "alternative_base"
            self.previous_form_type = "alternative_base"
            self.lineEdit_2.setEnabled(True)
            self.spinBox.setEnabled(False)
            self.pushButton_3.setEnabled(False)
        elif self.radioButton_6.isChecked():
            for i in range(self.previous_number_of_forms):
                layout = self.widget.layout()
                self.widget.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
                row_widget = QWidget()
                row_layout = QHBoxLayout(row_widget)
                
                label = QLabel(f"Form {i + 1}")
                line_edit = QLineEdit()
                
                if i < len(self.saved_data):
                    line_edit.setText(self.saved_data[i])
                
                row_layout.addWidget(label)
                row_layout.addWidget(line_edit)
            
                layout.addWidget(row_widget)
                
                line_edit.textChanged.connect(self.check_entries)
                
            scrollbar = self.scrollArea.verticalScrollBar()
            scrollbar.setValue(scrollbar.maximum())
            self.spin_box.setValue(self.previous_number_of_forms)
            self.form_type = "alternative"
            self.previous_form_type = "alternative"
            self.lineEdit_2.setEnabled(False)
            self.spinBox.setEnabled(True)
            self.pushButton_3.setEnabled(True)
    
    def generate_form_widgets(self):
        if self.form_type == "alternative":
            layout = self.widget.layout()
            self.widget.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
            
            self.saved_data = []
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    line_edit = row.findChild(QLineEdit)
                    if line_edit:
                        self.saved_data.append(line_edit.text())
                    else:
                        self.saved_data.append("")
            
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()

            for i in range(self.spin_box.value()):
                row_widget = QWidget()
                row_layout = QHBoxLayout(row_widget)
                
                label = QLabel(f"Form {i + 1}")
                line_edit = QLineEdit()
                
                if i < len(self.saved_data):
                    line_edit.setText(self.saved_data[i])
                
                row_layout.addWidget(label)
                row_layout.addWidget(line_edit)
            
                layout.addWidget(row_widget)
                
                line_edit.textChanged.connect(self.check_entries)
                
            scrollbar = self.scrollArea.verticalScrollBar()
            scrollbar.setValue(scrollbar.maximum())
            
    def initial_generate_team_widgets(self):
        self.teams_id_list = {}
        layout = self.widget_2.layout()
        self.widget_2.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
        for i in range(self.spinBox_3.value()):
            button = QPushButton(f"Edit team {i + 1}")
            DataStore4.data_store[str(i)] = {"name": "", "is_valid": False, "nom": 1, "roles_data": {0: {"name": "", 'nor': 1}}, "go_to_role": 1, "members_order_matters": False}
            button.clicked.connect(lambda _, index=i: self.open_data_dialog(index))
            button.clicked.connect(self.check_roles)
            self.teams_id_list[f"Team {i + 1}"] = i + 1
            layout.addWidget(button)
    
        scrollbar = self.scrollArea.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
        
    def generate_team_widgets(self):
        self.teams_id_list = {}
        for i in range(len(DataStore4.data_store)):
            self.prev_data_store[str(i)] = DataStore4.data_store[str(i)]
            if i > self.spinBox_3.value():
                del DataStore4.data_store[str(i)]
        DataStore4.data_store.clear()
                
        layout = self.widget_2.layout()
        self.widget_2.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
        for i in range(self.spinBox_3.value()):
            button = QPushButton(f"Edit team {i + 1}")
            if str(i) not in self.prev_data_store.keys():
                self.prev_data_store[str(i)] = {"name": "", "is_valid": False, "nom": 1, "nor": 1, "roles_data": {0: {"name": "", 'nor': 1}}, "go_to_role": 1, "members_order_matters": False}
            DataStore4.data_store[str(i)] = self.prev_data_store[str(i)]
            button.clicked.connect(lambda _, index=i: self.open_data_dialog(index))
            button.clicked.connect(self.check_roles)
            self.teams_id_list[f"Team {i + 1}"] = i + 1
            layout.addWidget(button)
        
        self.prev_data_store.clear()
        scrollbar = self.scrollArea.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
            
    def go_to_form(self) -> None:
        index = self.spinBox.value()
        layout = self.widget.layout()
        total_forms = layout.count()
        
        if index < 1 or index > total_forms:
            QMessageBox.warning(self, "Navigation Error", "Form not found")
            return
        target_widget = layout.itemAt(index - 1).widget()
        if target_widget:
            self.scrollArea.ensureWidgetVisible(target_widget)
        else:
            QMessageBox.warning(self, "Navigation Error", "Form not found")
        self.highlight_temporarily_forms(layout.itemAt(index - 1).widget(), duration=2000)
        
    def go_to_team(self) -> None:
        index = self.spinBox_2.value()
        layout = self.widget_2.layout()
        total_forms = layout.count()
        
        if index < 1 or index > total_forms:
            QMessageBox.warning(self, "Navigation Error", "Team not found")
            return
        target_widget = layout.itemAt(index - 1).widget()
        if target_widget:
            self.scrollArea_2.ensureWidgetVisible(target_widget)
        else:
            QMessageBox.warning(self, "Navigation Error", "Team not found")
        self.highlight_temporarily_teams(layout.itemAt(index - 1).widget(), duration=2000)
        
    def go_to_team_error(self) -> None:
        index = self.teams_id_list[self.comboBox.currentText()] - 1 # Adjusted to fix the problem of 0-based layout
        layout = self.widget_2.layout()
        total_properties = layout.count()
        
        if index < 1 or index > total_properties:
            QMessageBox.warning(self, "Navigation Error", "Team not found")
            return
        target_widget = layout.itemAt(index - 1).widget()
        if target_widget:
            self.scrollArea_2.ensureWidgetVisible(target_widget)
        else:
            QMessageBox.warning(self, "Navigation Error", "Team not found")
        self.highlight_temporarily_teams(layout.itemAt(index - 1).widget(), duration=2000)
        
    def highlight_temporarily_forms(self, widget: QWidget, duration: int = 2000):
        widget.setStyleSheet("""
                             QWidget {
                                 border: 2px solid #00ffff;
                                 border-radius: 6px;
                             }
                             """)
        QTimer.singleShot(2000, lambda: widget.setStyleSheet(""))
        
    def highlight_temporarily_teams(self, widget: QWidget, duration: int = 2000):
        widget.setStyleSheet("""
                             QPushButton {
                                 border: 2px solid #00ffff;
                                 border-radius: 6px;
                             }
                             """)
        QTimer.singleShot(2000, lambda: widget.setStyleSheet(""))
        
    def check_roles(self):
        self.comboBox.clear()
        layout = self.widget_2.layout()
        for i in range(layout.count()):
            if DataStore4.data_store[str(i)].get("is_valid") == True:
                pass
            else:
                self.comboBox.addItem(f"Team {i + 1}")
                self.frame_9.show()
        self.is_roles_valid = all(DataStore4.data_store[str(i)].get("is_valid", False) for i in range(layout.count()))
        if self.is_roles_valid == True:
            self.frame_9.hide()
        #self.check_entries()
            
    def check_entries(self):
        # self.check_if_name_exist()
        self.check_number_of_members()
        self.check_roles()
        if self.form_type == "default":
            self.pushButton.setEnabled(self.is_name_valid and self.is_roles_valid and self.is_num_of_members_valid)
            # print(f"{self.is_name_valid}\n{self.is_roles_valid}\n{self.is_num_of_members_valid}\n================")
            # for i in range(len(DataStore4.data_store)):
            #     print(DataStore4.data_store[str(i)]["is_valid"])
        elif self.form_type == "alternative_base":
            if self.lineEdit_2.text().strip():
                self.is_alternative_base = True
            else:
                self.is_alternative_base = False
            self.pushButton.setEnabled(self.is_name_valid and self.is_roles_valid and self.is_num_of_members_valid and self.is_alternative_base)
        elif self.form_type == "alternative":
            layout = self.widget.layout()
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    line_edit = row.findChild(QLineEdit)
                    if not line_edit or not line_edit.text().strip():
                        self.is_forms_valid = False
                        break
            self.pushButton.setEnabled(self.is_name_valid and self.is_roles_valid and self.is_num_of_members_valid and self.is_forms_valid)
        print(self.is_name_valid)
    
    def team_order_check_box_toggle(self, state):
        if state == 2:
            self.team_order = True
            DataStore4.team_order = True
        else:
            self.team_order = False
            DataStore4.team_order = False
    
    def open_data_dialog(self, index):
        existing = DataStore4.data_store.get(str(index))
        if self.table_window != None:
            self.close_team_info_window()
        dialog = Team_roles(index, existing_data=existing, parent=self)
        dialog.finished.connect(lambda result: self.save_if_accepted(result, index, dialog))
        dialog.setModal(True)
        dialog.show()
        
        if not hasattr(self, '_dialogs'):
            self._dialogs = {}
            self._dialogs[index] = dialog
            
    def close_object_info_window(self) -> None:
        pass
    
    def store_total_number_of_members(self):
        DataStore4.total_number_of_members = self.spin_box.value()
        
    def open_table_window(self):
        sum = 0
        for i in range(len(DataStore4.data_store)):
            sum += DataStore4.data_store[str(i)]["nom"]
            
        if self.table_window and self.table_window.isVisible():
            self.table_window.close()
            self.table_window = Teams_data_info(self.team_order, sum)
            self.table_window.show()
        else:
            self.table_window = Teams_data_info(self.team_order, sum)
            self.table_window.show()
    
    def close_team_info_window(self):
        if self.table_window and self.table_window.isVisible():
            self.table_window.close()
            self.table_window = None
            
    def check_number_of_members(self):
        sum = 0
        for i in range(len(DataStore4.data_store)):
            sum += DataStore4.data_store[str(i)]["nom"]
        if sum != self.spin_box.value():
            self.label_10.setText("Total sum of members of teams must be equal to the number of members to distribute")
            self.label_10.show()
            self.is_num_of_members_valid = False
        else:
            self.label_10.hide()
            self.is_num_of_members_valid = True
            
    def get_config_data(self) -> dict:
        self.config_data["object_name"] = self.lineEdit.text().strip()
        self.config_data["nOf"] = self.spin_box.value()
        self.config_data["not"] = self.spinBox_3.value()
        self.config_data["form_type"] = self.form_type
        self.config_data["prev_form_type"] = self.previous_form_type
        self.config_data["gtfnum"] = self.spinBox.value()
        self.config_data["form"] = self.lineEdit_2.text().strip()
        self.config_data["prev_nof"] = self.previous_number_of_forms
        self.config_data["team_order"] = self.team_order
        self.config_data["gtteam"] = self.spinBox_2.value()
        self.config_data["teams"] = DataStore4.data_store
        if self.form_type == "alternative":
            layout = self.widget.layout()
            self.saved_data = []
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    line_edit = row.findChild(QLineEdit)
                    if line_edit:
                        self.saved_data.append(line_edit.text())
                    else:
                        self.saved_data.append("")
            
            self.config_data["forms"] = self.saved_data
        else:
            self.config_data["forms"] = self.saved_data
        return self.config_data
    
    def save_config(self):
        self.config_data = self.get_config_data()
        if not self.config_data:
            QMessageBox.warning(self, "Error", "An unknown problem occurred")
            return
            
        if not self.current_file:
            self.save_as_config()
            return
        
        reply = QMessageBox.question(self, "Replace File", f"Do you want to replace {self.current_file}?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            json_data = json.dumps(self.config_data).encode()
            encrypted_data = self.cipher.encrypt(json_data)
            with open(self.current_file, 'wb') as f:
                f.write(encrypted_data)
                self.ui.label_7.setText(f"Object creation session data saved to {self.current_file}")
                self.ui.label_7.show()
        if reply == QMessageBox.No:
            self.save_as_config()
            return
            
    def save_as_config(self):
        self.config_data = self.get_config_data()
        if not self.config_data:
            QMessageBox.warning(self, "Error", "An unknown problem occurred")
            return
        
        json_data = json.dumps(self.config_data).encode()
        encrypted_data = self.cipher.encrypt(json_data)
        
        file_name, _ = QFileDialog.getSaveFileName(self, "Save As",str(self.documents_dir / f"untitled{self.untitled_x}.ocs"), "Object Creation Session Files (*.ocs)")
        self.untitled_x += 1
        if file_name:
            if not file_name.endswith(".ocs"):
                file_name += ".ocs"
                
        with open(file_name, 'wb') as f:
            self.current_file = file_name
            self.pushButton_4.setToolTip(f"Save to file {self.current_file}")
            f.write(encrypted_data)
            self.label_7.setText(f"Object creation session data saved to {self.current_file}")
            self.label_7.show()
            
    def load_config_dialog(self):
        file_name, selected_filter = QFileDialog.getOpenFileName(self, "Load object creation session", str(self.documents_dir) + "/untitled.ocs", "Object Creation Session Files (*.ocs)")
        if file_name:
            with open(file_name, "rb") as f:
                encrypted_data = f.read()
                
            decrypted_data = self.cipher.decrypt(encrypted_data)
            data = json.loads(decrypted_data.decode())
            self.load_config(data)
            self.current_file = file_name
            self.pushButton_4.setToolTip(f"Save to file {self.current_file}")
            self.label_7.setText(f"Object creation session {self.current_file} loaded")
            self.label_7.show()
        else:
            return
        if not isinstance(file_name, str):
            QMessageBox.warning(self, "Error", "Invalid file")
            return

    def load_config(self, config_data):
            if config_data["object_id"] == "13":
                #self.lineEdit.setText(config_data["object_name"])
                self.spin_box.setValue(config_data["nOf"])
                self.spinBox_3.setValue(config_data["not"])
                self.spinBox.setValue(config_data["gtfnum"])
                self.lineEdit_2.setText(config_data["form"])
                self.previous_number_of_forms = config_data["prev_nof"]
                self.form_type = config_data["form_type"]
                self.previous_form_type = config_data["prev_form_type"]
                self.team_order = config_data["team_order"]
                self.spinBox_2.setValue(config_data["gtteam"])
                length = len(DataStore4.data_store) # To store the number of elements in the data_store dictionary. This is for the deletion of the elements. The issue is that iterating over the elements and deleting them at the same time will cause a problem. So I iterate base on the number of elements before I started deleting, and it is store in this
                DataStore4.data_store.clear()
                DataStore4.data_store.update(config_data["teams"])
                DataStore4.total_number_of_members = config_data["nOf"]
                DataStore4.team_order = self.team_order
                self.generate_team_widgets()
                if self.team_order == True:
                    self.checkBox_2.setChecked(True)
                else:
                    self.checkBox_2.setChecked(False)
                    
                for team_key in list(DataStore4.data_store.keys()):
                    roles_data = DataStore4.data_store[team_key].get("roles_data", {})
                    DataStore4.data_store[team_key]["roles_data"] = {int(k): v for k, v in roles_data.items()}
                
                if config_data["form_type"] == "default":
                    self.radioButton_4.setChecked(True)
                    self.lineEdit_2.setEnabled(False)
                    self.spinBox.setEnabled(False)
                    self.pushButton_3.setEnabled(False)
                elif config_data["form_type"] == "alternative_base":
                    self.radioButton_5.setChecked(True)
                    self.lineEdit_2.setEnabled(True)
                    self.spinBox.setEnabled(False)
                    self.pushButton_3.setEnabled(False)
                elif config_data["form_type"] == "alternative":
                    self.radioButton_6.setChecked(True)
                    self.lineEdit_2.setEnabled(False)
                    self.spinBox.setEnabled(True)
                    self.pushButton_3.setEnabled(True)
                    self.saved_data.clear()
                    
                    layout = self.widget.layout()
                    self.widget.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
                    while layout.count():
                        item = layout.takeAt(0)
                        widget = item.widget()
                        if widget:
                            widget.deleteLater()
                    self.saved_data.clear()
                    self.saved_data = config_data["forms"]
                    for i in range(config_data["nOf"]):
                        row_widget = QWidget()
                        row_layout = QHBoxLayout(row_widget)
                        
                        label = QLabel(f"Form {i + 1}")
                        line_edit = QLineEdit()
                        
                        if i < len(self.saved_data):
                            line_edit.setText(config_data["forms"][i])
                        
                        row_layout.addWidget(label)
                        row_layout.addWidget(line_edit)
                    
                        layout.addWidget(row_widget)
                        
                        line_edit.textChanged.connect(self.check_entries)
                        
                    scrollbar = self.scrollArea.verticalScrollBar()
                    scrollbar.setValue(scrollbar.maximum())
                
                self.saved_data = config_data["forms"]
                #print(DataStore4.data_store)
                #### Problem 001
                self.lineEdit.setText(f"{self.event_name}'s object")
                self.lineEdit.setEnabled(False)
                ####
            else:
                QMessageBox.warning(self, "Error", f"The object type of the loaded file has id {config_data["object_id"]} which doesn't correspond to the id of the present object creation\n\nSearch for the id {config_data["object_id"]} in the search bar and load this file into it")
            self.check_entries()
            
    def create_object(self):
        total_num_of_members = self.spin_box.value()
        num_of_teams = self.spinBox_3.value()
        team_order_matters = self.team_order
        roles_per_team = defaultdict(list)
        teams_list = []
        for i in range(len(DataStore4.data_store)):
            teams_list.append(DataStore4.data_store[str(i)]["name"])
            roles = []
            for j in range(len(DataStore4.data_store[str(i)]["roles_data"])):
                roles.append(DataStore4.data_store[str(i)]["roles_data"][j]["name"])
            roles_per_team[DataStore4.data_store[str(i)]["name"]] = roles
        member_order_matters_per_team = []
        for i in range(0, len(DataStore4.data_store)):
            member_order_matters_per_team.append(DataStore4.data_store[str(i)]["members_order_matters"])
        forms = []
        if self.form_type == "default":
            for i in range(total_num_of_members):
                forms.append(symbols.get_symbol(i))
        elif self.form_type == "alternative_base":
            word = self.lineEdit_2.text().strip()
            for i in range(total_num_of_members):
                frm = f"{word}{i+1}"
                forms.append(frm)
        elif self.form_type == "alternative":
            layout = self.widget.layout()
            self.saved_data = []
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    line_edit = row.findChild(QLineEdit)
                    if line_edit: # else part could have been considered, but it was not considered because, generally before this function is accessed by the user all fields must be filled
                        self.saved_data.append(line_edit.text().strip())
            forms = self.saved_data
        
        obj = Id13(num_of_teams, forms, team_order_matters, member_order_matters_per_team, roles_per_team)    
        event = Events(self.event_name, obj.number_system)
        window = Event_properties(event)
        self.top_window.hide()
        window.exec()
        self.close_by_code_initiated.emit()
        return
        
    def save_if_accepted(self, result, index, dialog):
        if result == QDialog.Accepted:
            DataStore4.data_store[str(index)] = dialog.data
            self.check_entries()
            
        if hasattr(self, '_dialog') and index in self._dialogs:
            del self._dialogs[index]