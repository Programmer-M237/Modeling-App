# not === number of members /// CONFUSION AND TIRED OF CODING

from PySide6.QtWidgets import QMessageBox, QFileDialog, QWidget, QButtonGroup, QHBoxLayout, QVBoxLayout, QFrame, QSpinBox, QLabel, QLineEdit, QGroupBox
from PySide6.QtCore import Qt, Signal, QTimer, QStandardPaths
from pathlib import Path
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont
import json
from cryptography.fernet import Fernet
from collections import defaultdict
from object_12_ui import Ui_Dialog
from object_12_teams_table_view import Teams_data_info
from objects import Id12
from object_manager import ObjectsManager
from entities import EntityManager
import symbols

class Object_12(QWidget):
    cancel_clicked = Signal()
    is_name_valid = False
    form_type = "default"
    previous_form_type = "default"
    saved_data = []
    previous_number_of_forms = 1
    properties_name = defaultdict(list) # Not really importance except to check if they are duplicate names
    properties_names_ids = defaultdict(int)
    check_teams_name = False
    check_num_of_members = False
    member_order = False
    team_order = False
    is_alt_base = False
    check_forms = False
    is_teams_valid_var = False
    is_teams_name_duplicate = False
    ENCRYPTION_KEY = 'Rll0H4fZf5TvH1E-mk0qwcZ1cETu6jlA_2PiwZ9cvls='
    cipher = Fernet(ENCRYPTION_KEY)
    documents = Path(QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation))
    m_app_folder = documents / "M App" / "Objects 12"
    m_app_folder.mkdir(parents=True, exist_ok=True)
    documents_dir = m_app_folder
    untitled_x = 1 # Use to name the untitled files of the Save As Window
    
    def __init__(self, stacked_widget, top_window):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.name = "page_12"
        self.ui.spin_box.setRange(1, 1000)
        self.ui.spin_box.setValue(1)
        self.ui.spinBox.setRange(1, 1000)
        self.ui.spinBox.setValue(1)
        self.ui.spinBox_2.setRange(1, 1000)
        self.ui.spinBox_2.setValue(1)
        self.ui.spinBox_3.setRange(1, 1000)
        self.ui.spinBox_3.setValue(1)
        self.ui.frame_9.hide()
        self.ui.pushButton.setEnabled(False)
        self.ui.label_8.setText('<a href="#">Click here to view a summary of the teams information</a>')
        self.ui.label_7.hide()
        self.teams_saved_data = defaultdict(dict)
        self.prev_teams_saved_data = {}
        self.table_window = None
        self.top_window = top_window
        self.stacked_widget = stacked_widget
        
        self.top_window_close_signal = Signal()
        self.stacked_widget_page_change_signal = Signal()
        self.top_window.destroyed.connect(self.close_team_info_window)
        self.stacked_widget.currentChanged.connect(self.close_team_info_window)
    
        self.ui.pushButton_2.clicked.connect(self.cancel_clicked.emit)
        
        self.forms_type = QButtonGroup()
        self.ui.radioButton_4.setChecked(True)
        self.forms_type.addButton(self.ui.radioButton_4)
        self.forms_type.addButton(self.ui.radioButton_5)
        self.forms_type.addButton(self.ui.radioButton_6)
        self.forms_type.buttonClicked.connect(self.forms_type_radio_btn_clicked)
        self.forms_type_radio_btn_clicked()
        
        self.model = QStandardItemModel()
        self.ui.comboBox.setModel(self.model)
        
        self.ui.lineEdit.textChanged.connect(self.check_if_name_exist)
        
        self.ui.spin_box.valueChanged.connect(self.generate_form_widgets)
        
        self.ui.pushButton_3.clicked.connect(self.go_to_form)
        
        self.initial_generate_teams_widgets()
        self.ui.spinBox_3.valueChanged.connect(self.generate_teams_widgets)
        
        self.ui.pushButton_7.clicked.connect(self.go_to_team)
        
        self.ui.pushButton_8.clicked.connect(self.go_to_team_name_error)
        
        self.ui.spinBox_3.valueChanged.connect(self.update_teams_data)
        
        self.ui.spin_box.valueChanged.connect(self.check_number_of_members)
        self.ui.spinBox_3.valueChanged.connect(self.check_number_of_members)
        self.check_number_of_members()
        
        self.ui.checkBox_2.stateChanged.connect(self.team_order_check_box_toggle)
        self.ui.checkBox.stateChanged.connect(self.member_order_check_box_toggle)
        
        self.ui.spinBox_3.valueChanged.connect(self.is_teams_valid)
        
        self.ui.lineEdit.textChanged.connect(self.check_entries)
        self.ui.spin_box.valueChanged.connect(self.check_entries)
        self.ui.lineEdit_2.textChanged.connect(self.check_entries)
        self.forms_type.buttonClicked.connect(self.check_entries)
        self.ui.spinBox_3.valueChanged.connect(self.check_entries)
        
        self.ui.pushButton_4.setToolTip(f"Save this object creation session")
        self.ui.pushButton_5.setToolTip("Save this object creation session")
        self.ui.pushButton_6.setToolTip("Load object creation session with object id '12'")
        
        self.config_data = {"object_id": "12", "object_name": "", "nOf": 1, "form_type": "default", "prev_form_type": "default", "form": "", "forms": [], "gtfnum": 1, "prev_nof": 1, "not": 1, "team_order": False, "member_order": False, "teams": {}, "gtteam": 1}
        
        self.ui.pushButton_4.clicked.connect(self.save_config)
        self.ui.pushButton_5.clicked.connect(self.save_as_config)
        self.ui.pushButton_6.clicked.connect(self.load_config_dialog)
        
        self.current_file = None
        
        self.ui.label_8.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.ui.label_8.setOpenExternalLinks(False)
        self.ui.label_8.linkActivated.connect(self.open_table_window)
        
        self.ui.pushButton.clicked.connect(self.create_object)
        
    def check_if_name_exist(self) -> None:
        name = self.ui.lineEdit.text().strip()
        
        if not(name):
            self.is_name_valid = False
        elif (name, "object") in EntityManager._items:
            self.ui.label_2.setText("❌ An object with the same name already exists")
            self.ui.label_2.show()
            self.is_name_valid = False
        elif EntityManager.name_exists_with_different_type(EntityManager, name, "object"):
            self.ui.label_2.setText("⚠️ An event or system with the same name already exists")
            self.ui.label_2.show()
            self.is_name_valid = True
        else:
            self.ui.label_2.hide()
            self.is_name_valid = True
            
    def forms_type_radio_btn_clicked(self) -> None:
        if self.ui.radioButton_4.isChecked():
            if self.previous_form_type == "alternative":
                self.previous_number_of_forms = self.ui.spin_box.value()
                layout = self.ui.widget.layout()
                
                self.saved_data = []
                for i in range(layout.count()):
                    row = layout.itemAt(i).widget()
                    if row:
                        line_edit = row.findChild(QLineEdit)
                        if line_edit:
                            self.saved_data.append(line_edit.text())
                        else:
                            self.saved_data.append("")
            layout = self.ui.widget.layout()
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
            
            self.form_type = "default"
            self.previous_form_type = "default"
            self.ui.lineEdit_2.setEnabled(False)
            self.ui.spinBox.setEnabled(False)
            self.ui.pushButton_3.setEnabled(False)
        elif self.ui.radioButton_5.isChecked():
            if self.previous_form_type == "alternative":
                self.previous_number_of_forms = self.ui.spin_box.value()
                layout = self.ui.widget.layout()
                
                self.saved_data = []
                for i in range(layout.count()):
                    row = layout.itemAt(i).widget()
                    if row:
                        line_edit = row.findChild(QLineEdit)
                        if line_edit:
                            self.saved_data.append(line_edit.text())
                        else:
                            self.saved_data.append("")
            layout = self.ui.widget.layout()
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
            
            self.form_type = "alternative_base"
            self.previous_form_type = "alternative_base"
            self.ui.lineEdit_2.setEnabled(True)
            self.ui.spinBox.setEnabled(False)
            self.ui.pushButton_3.setEnabled(False)
        elif self.ui.radioButton_6.isChecked():
            for i in range(self.previous_number_of_forms):
                layout = self.ui.widget.layout()
                self.ui.widget.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
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
                
            scrollbar = self.ui.scrollArea.verticalScrollBar()
            scrollbar.setValue(scrollbar.maximum())
            self.ui.spin_box.setValue(self.previous_number_of_forms)
            self.form_type = "alternative"
            self.previous_form_type = "alternative"
            self.ui.lineEdit_2.setEnabled(False)
            self.ui.spinBox.setEnabled(True)
            self.ui.pushButton_3.setEnabled(True)
        self.check_if_name_exist()
        self.check_entries()
        
    def check_entries(self):
        self.check_if_name_exist()
        self.check_number_of_members()
        self.check_duplicate_names()
        self.is_teams_valid()
        if self.form_type == "default":
            self.ui.pushButton.setEnabled(self.is_name_valid and self.check_teams_name and self.is_teams_name_duplicate and self.check_num_of_members)
        elif self.form_type == "alternative_base":
            if self.ui.lineEdit_2.text().strip():
                self.is_alt_base = True
            else:
                self.is_alt_base = False
            self.ui.pushButton.setEnabled(self.is_name_valid and self.check_teams_name and self.is_teams_name_duplicate and self.check_num_of_members and self.is_alt_base)
        elif self.form_type == "alternative":
            layout = self.ui.widget.layout()
            self.check_forms = all(layout.itemAt(i).widget().findChild(QLineEdit).text().strip() for i in range(layout.count()))
            self.ui.pushButton.setEnabled(self.is_name_valid and self.check_teams_name and self.is_teams_name_duplicate and self.check_num_of_members and self.check_forms)
        
        # print("is_name_valid: ", self.is_name_valid) # WAS USED FOR DEBUGGING
        # print("check_teams_name: ", self.check_teams_name)
        # print("is_teams_name_duplicate: ", self.is_teams_name_duplicate)
        # print("check_num_of_members: ", self.check_num_of_members)
        # print("is_alt_base: ", self.is_alt_base)
        # print("check_forms: ", self.check_forms)
        # print("==========================================================")
    
    def generate_form_widgets(self):
        if self.form_type == "alternative":
            layout = self.ui.widget.layout()
            self.ui.widget.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
            
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

            for i in range(self.ui.spin_box.value()):
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
                
            scrollbar = self.ui.scrollArea.verticalScrollBar()
            scrollbar.setValue(scrollbar.maximum())
            
    def go_to_form(self) -> None:
        index = self.ui.spinBox.value()
        layout = self.ui.widget.layout()
        total_forms = layout.count()
        
        if index < 1 or index > total_forms:
            QMessageBox.warning(self, "Navigation Error", "Property not found")
            return
        target_widget = layout.itemAt(index - 1).widget()
        if target_widget:
            self.ui.scrollArea.ensureWidgetVisible(target_widget)
        else:
            QMessageBox.warning(self, "Navigation Error", "Form not found")
        self.highlight_temporarily(layout.itemAt(index - 1).widget(), duration=2000)
        
    def highlight_temporarily(self, widget: QWidget, duration: int = 2000):
        widget.setStyleSheet("""
                             QWidget {
                                 border: 2px solid #00ffff;
                                 border-radius: 6px;
                             }
                             """)
        QTimer.singleShot(2000, lambda: widget.setStyleSheet(""))
        
    def initial_generate_teams_widgets(self):
        layout = self.ui.widget_2.layout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
        for i in range(self.ui.spinBox_3.value()):
            #print(i)
            self.teams_saved_data[i] = {"name": "", "not": 1}
            
            group_widget = QWidget()
            group_layout = QVBoxLayout(group_widget)
            
            groupbox = QGroupBox(f"Team {i + 1}")
            frame = QFrame()
            frame_l = QHBoxLayout(frame)
            label = QLabel("Name")
            line_edit = QLineEdit()
            frame1 = QFrame()
            frame1_l = QHBoxLayout(frame1)
            label1 = QLabel("Number of members")
            spin_box = QSpinBox()
            spin_box.setRange(1, 1000)
            
            if i < len(self.teams_saved_data):
                line_edit.setText(self.teams_saved_data[i]["name"])
                spin_box.setValue(self.teams_saved_data[i]["not"])
                
            
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
            line_edit.textChanged.connect(self.update_teams_data)
            spin_box.valueChanged.connect(self.update_teams_data)
            spin_box.valueChanged.connect(self.check_number_of_members)
            line_edit.textChanged.connect(self.is_teams_valid)
            
        scrollbar = self.ui.scrollArea_2.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
        
    def generate_teams_widgets(self):
        layout = self.ui.widget_2.layout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.prev_teams_saved_data.clear()
        self.teams_saved_data.clear()
        for i in range(layout.count()):
            self.prev_teams_saved_data[i] = {"name": "", "not": 1}
            group = layout.itemAt(i).widget()
            if group:
                line_edit = group.findChild(QLineEdit)
                if line_edit:
                    self.prev_teams_saved_data[i]["name"] = line_edit.text().strip()
                else:
                    self.prev_teams_saved_data[i]["name"] = ""
                spin_box = group.findChild(QSpinBox)
                if spin_box:
                    self.prev_teams_saved_data[i]["not"] = spin_box.value()
                else:
                    self.prev_teams_saved_data[i]["not"] = 1 # Not really important, just for safety reasons
        
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
        for i in range(self.ui.spinBox_3.value()):
            self.teams_saved_data[i] = {"name": "", "not": 1}
            
            group_widget = QWidget()
            group_layout = QVBoxLayout(group_widget)
            
            groupbox = QGroupBox(f"Team {i + 1}")
            frame = QFrame()
            frame_l = QHBoxLayout(frame)
            label = QLabel("Name")
            line_edit = QLineEdit()
            frame1 = QFrame()
            frame1_l = QHBoxLayout(frame1)
            label1 = QLabel("Number of members")
            spin_box = QSpinBox()
            spin_box.setRange(1, 1000)
            
            
            if i < len(self.prev_teams_saved_data):
                line_edit.setText(self.prev_teams_saved_data[i]["name"])
                spin_box.setValue(self.prev_teams_saved_data[i]["not"])
            
            line_edit.textChanged.connect(self.check_duplicate_names)
            spin_box.valueChanged.connect(self.check_duplicate_names)
            line_edit.textChanged.connect(self.check_entries)
            spin_box.valueChanged.connect(self.check_entries)
            line_edit.textChanged.connect(self.update_teams_data)
            spin_box.valueChanged.connect(self.update_teams_data)
            spin_box.valueChanged.connect(self.check_number_of_members)
            line_edit.textChanged.connect(self.is_teams_valid)
            
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
            
        scrollbar = self.ui.scrollArea_2.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
        
    def go_to_team(self) -> None:
        #print(self.test)
        index = self.ui.spinBox_3.value()
        layout = self.ui.widget_2.layout()
        total_forms = layout.count()
        
        if index < 1 or index > total_forms:
            QMessageBox.warning(self, "Navigation Error", "Property not found")
            return
        target_widget = layout.itemAt(index - 1).widget()
        if target_widget:
            self.ui.scrollArea_2.ensureWidgetVisible(target_widget)
        else:
            QMessageBox.warning(self, "Navigation Error", "Form not found")
        self.highlight_temporarily(layout.itemAt(index - 1).widget(), duration=2000)
        
    def check_duplicate_names(self):
        #print("hi")
        if not hasattr(self, "model") or self.model is None:
            self.model = QStandardItemModel()
            self.ui.comboBox.setModel(self.model)
        self.ui.comboBox.clear()
        self.model.clear()
        self.properties_names_ids.clear()
        layout = self.ui.widget_2.layout()
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
            self.ui.frame_9.show()
            self.is_teams_name_duplicate = False

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
                    self.model.appendRow(QStandardItem(f" Team {j + 1}"))
                    self.properties_names_ids[f" Team {j + 1}"] = j
                    
            if self.model.rowCount() > 0:
                self.ui.comboBox.setCurrentIndex(0)
        else:
            self.ui.frame_9.hide()
            self.is_teams_name_duplicate = True
                
    def is_teams_valid(self):
        layout = self.ui.widget_2.layout()
        all_filled = all(layout.itemAt(i).widget().findChild(QLineEdit).text().strip() for i in range(layout.count()))
        if all_filled:
            
            self.check_teams_name = True
        else:
            self.check_teams_name = False
                    
    def go_to_team_name_error(self):
        index = self.properties_names_ids[self.ui.comboBox.currentText()]
        layout = self.ui.widget_2.layout()
        target_widget = layout.itemAt(index).widget()
        if target_widget:
            self.ui.scrollArea_2.ensureWidgetVisible(target_widget)
        else:
            QMessageBox.warning(self, "Navigation Error", "Form not found")
        self.highlight_temporarily(layout.itemAt(index).widget(), duration=2000)
    
    def update_teams_data(self):
        layout = self.ui.widget_2.layout()
        for i in range(layout.count()):
            row = layout.itemAt(i).widget()
            if row:
                line_edit = row.findChild(QLineEdit)
                if line_edit:
                    self.teams_saved_data[i]["name"] = line_edit.text().strip()
                else:
                    self.teams_saved_data[i]["name"] = ""
                spin_box = row.findChild(QSpinBox)
                if spin_box:
                    self.teams_saved_data[i]["not"] = spin_box.value()
                else:
                    self.teams_saved_data[i]["not"] = 1
                    
    def check_number_of_members(self):
        sum = 0
        layout = self.ui.widget_2.layout()
        total = layout.count()
        for i in range(total):
            row = layout.itemAt(i).widget()
            spin_box = row.findChild(QSpinBox)
            sum += spin_box.value()
        if sum == self.ui.spin_box.value():
            self.ui.label_8.setText('<a href="#">Click here to view a summary of the teams information</a>')
            self.check_num_of_members = True
        else:
            self.ui.label_8.setText('The sum of the total number of members in the teams must be equal to the number of members. <a href="#">Click here to view a summary of the teams information</a>')
            self.check_num_of_members = False
    
    def team_order_check_box_toggle(self, state):
        if state == 2:
            self.team_order = True
        else:
            self.team_order = False
            
    def member_order_check_box_toggle(self, state):
        if state == 2:
            self.member_order = True
        else:
            self.member_order = False
            
    def get_config_data(self) -> dict:
        self.config_data["object_name"] = self.ui.lineEdit.text().strip()
        self.config_data["nOf"] = self.ui.spin_box.value()
        self.config_data["not"] = self.ui.spinBox_3.value()
        self.config_data["form_type"] = self.form_type
        self.config_data["prev_form_type"] = self.previous_form_type
        self.config_data["gtfnum"] = self.ui.spinBox.value()
        self.config_data["form"] = self.ui.lineEdit_2.text().strip()
        self.config_data["prev_nof"] = self.previous_number_of_forms
        self.config_data["team_order"] = self.team_order
        self.config_data["member_order"] = self.member_order
        self.config_data["gtteam"] = self.ui.spinBox_2.value()
        if self.form_type == "alternative":
            layout = self.ui.widget.layout()
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
        layout = self.ui.widget_2.layout()
        self.teams_saved_data.clear()
        for i in range(layout.count()):
            self.teams_saved_data[i] = {"name": "", "not": 1}
            group = layout.itemAt(i).widget()
            if group:
                line_edit = group.findChild(QLineEdit)
                if line_edit:
                    self.teams_saved_data[i]["name"] = line_edit.text().strip()
                else:
                    self.teams_saved_data[i]["name"] = ""
                spin_box = group.findChild(QSpinBox)
                if spin_box:
                    self.teams_saved_data[i]["not"] = spin_box.value()
                else:
                    self.teams_saved_data[i]["not"] = 1
        
        self.config_data["teams"] = self.teams_saved_data
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
            self.ui.pushButton_4.setToolTip(f"Save to file {self.current_file}")
            f.write(encrypted_data)
            self.ui.label_7.setText(f"Object creation session data saved to {self.current_file}")
            self.ui.label_7.show()
            
    def load_config_dialog(self):
        file_name, selected_filter = QFileDialog.getOpenFileName(self, "Load object creation session", str(self.documents_dir) + "/untitled.ocs", "Object Creation Session Files (*.ocs)")
        if file_name:
            with open(file_name, "rb") as f:
                encrypted_data = f.read()
                
            decrypted_data = self.cipher.decrypt(encrypted_data)
            data = json.loads(decrypted_data.decode())
            self.load_config(data)
            self.current_file = file_name
            self.ui.pushButton_4.setToolTip(f"Save to file {self.current_file}")
            self.ui.label_7.setText(f"Object creation session {self.current_file} loaded")
            self.ui.label_7.show()
        else:
            return
        if not isinstance(file_name, str):
            QMessageBox.warning(self, "Error", "Invalid file")
            return

    def load_config(self, config_data):
            if config_data["object_id"] == "12":
                self.ui.lineEdit.setText(config_data["object_name"])
                self.ui.spin_box.setValue(config_data["nOf"])
                self.ui.spinBox_3.setValue(config_data["not"])
                self.ui.spinBox.setValue(config_data["gtfnum"])
                self.ui.lineEdit_2.setText(config_data["form"])
                self.previous_number_of_forms = config_data["prev_nof"]
                self.form_type = config_data["form_type"]
                self.previous_form_type = config_data["prev_form_type"]
                self.team_order = config_data["team_order"]
                self.member_order = config_data["member_order"]
                self.ui.spinBox_2.setValue(config_data["gtteam"])
                self.teams_saved_data.clear()
                if self.team_order == True:
                    self.ui.checkBox_2.setChecked(True)
                else:
                    self.ui.checkBox_2.setChecked(False)
                if self.member_order == True:
                    self.ui.checkBox.setChecked(True)
                else:
                    self.ui.checkBox.setChecked(False)
                layout = self.ui.widget_2.layout()
                self.ui.widget_2.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
                
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.deleteLater()
                #print(config_data["teams"])
                for i in range(self.ui.spinBox_3.value()):
                    self.teams_saved_data[i] = {"name": "", "not": 1}
                    self.teams_saved_data[i] = config_data["teams"][str(i)]
                    
                    
                    group_widget = QWidget()
                    group_layout = QVBoxLayout(group_widget)
                    
                    groupbox = QGroupBox(f"Team {i + 1}")
                    frame = QFrame()
                    frame_l = QHBoxLayout(frame)
                    label = QLabel("Name")
                    line_edit = QLineEdit()
                    frame1 = QFrame()
                    frame1_l = QHBoxLayout(frame1)
                    label1 = QLabel("Number of members")
                    spin_box = QSpinBox()
                    spin_box.setRange(1, 1000)
                    
                    if i < len(self.teams_saved_data):
                        print("Data is displayed")
                        print(self.teams_saved_data)
                        line_edit.setText(self.teams_saved_data[i]["name"])
                        spin_box.setValue(self.teams_saved_data[i]["not"])
                    
                    line_edit.textChanged.connect(self.check_duplicate_names)
                    spin_box.valueChanged.connect(self.check_duplicate_names)
                    line_edit.textChanged.connect(self.check_entries)
                    spin_box.valueChanged.connect(self.check_entries)
                    line_edit.textChanged.connect(self.update_teams_data)
                    spin_box.valueChanged.connect(self.update_teams_data)
                    spin_box.valueChanged.connect(self.check_number_of_members)
                    line_edit.textChanged.connect(self.is_teams_valid)
                    
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
                    
                scrollbar = self.ui.scrollArea_2.verticalScrollBar()
                scrollbar.setValue(scrollbar.maximum())
                
                if config_data["form_type"] == "default":
                    self.ui.radioButton_4.setChecked(True)
                    self.ui.lineEdit_2.setEnabled(False)
                    self.ui.spinBox.setEnabled(False)
                    self.ui.pushButton_3.setEnabled(False)
                elif config_data["form_type"] == "alternative_base":
                    self.ui.radioButton_5.setChecked(True)
                    self.ui.lineEdit_2.setEnabled(True)
                    self.ui.spinBox.setEnabled(False)
                    self.ui.pushButton_3.setEnabled(False)
                elif config_data["form_type"] == "alternative":
                    self.ui.radioButton_6.setChecked(True)
                    self.ui.lineEdit_2.setEnabled(False)
                    self.ui.spinBox.setEnabled(True)
                    self.ui.pushButton_3.setEnabled(True)
                    self.saved_data.clear()
                    self.ui.spin_box.setValue(config_data["nOf"])
                    
                    layout = self.ui.widget.layout()
                    self.ui.widget.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
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
                        
                    scrollbar = self.ui.scrollArea.verticalScrollBar()
                    scrollbar.setValue(scrollbar.maximum())
                
                self.saved_data = config_data["forms"]
            else:
                QMessageBox.warning(self, "Error", f"The object type of the loaded file has id {config_data["object_id"]} which doesn't correspond to the id of the present object creation\n\nSearch for the id {config_data["object_id"]} in the search bar and load this file into it")
            self.check_if_name_exist()
            self.check_entries()
            
    def open_table_window(self):
        data = []
        item = []
        for i in range(len(self.teams_saved_data)):
            item = []
            item.append(self.teams_saved_data[i]["name"])
            item.append(self.teams_saved_data[i]["not"])
            data.append(item)
            #print(data)
        
        sum = 0
        layout = self.ui.widget_2.layout()
        total = layout.count()
        for i in range(total):
            row = layout.itemAt(i).widget()
            spin_box = row.findChild(QSpinBox)
            sum += spin_box.value()
        
        if self.table_window and self.table_window.isVisible():
            self.table_window.close()
            self.table_window = Teams_data_info(data, sum, self.ui.spin_box.value(), self.team_order, self.member_order)
            self.table_window.show()
        else:
            self.table_window = Teams_data_info(data, sum, self.ui.spin_box.value(), self.team_order, self.member_order)
            self.table_window.show()
        
    def close_team_info_window(self):
        if self.table_window and self.table_window.isVisible():
            self.table_window.close()
            self.table_window = None
            
    def create_object(self) -> None:
        name = self.ui.lineEdit.text().strip()
        number_of_forms = self.ui.spin_box.value()
        number_of_teams = self.ui.spinBox_3.value()
        team_order = self.team_order
        members_order = self.member_order
        forms = []
        teams_list = []
        teams_sizes = []
        if self.form_type == "default":
            for i in range(number_of_forms):
                forms.append(symbols.get_symbol(i))
        elif self.form_type == "alternative_base":
            word = self.ui.lineEdit_2.text().strip()
            for i in range(number_of_forms):
                frm = f"{word}{i+1}"
                forms.append(frm)
        elif self.form_type == "alternative":
            layout = self.ui.widget.layout()
            self.saved_data = []
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    line_edit = row.findChild(QLineEdit)
                    if line_edit: # else part could have been considered, but it was not considered because, generally before this function is accessed by the user all fields must be filled
                        self.saved_data.append(line_edit.text().strip())
            forms = self.saved_data
        layout = self.ui.widget_2.layout()
        self.saved_data_1 = []
        for i in range(layout.count()):
            row = layout.itemAt(i).widget()
            if row:
                line_edit = row.findChild(QLineEdit)
                spin_box = row.findChild(QSpinBox)
                teams_list.append(line_edit.text().strip())
                teams_sizes.append(spin_box.value())

        if EntityManager.name_exists_with_different_type(EntityManager, name, "object") == True:
            ret = QMessageBox.warning(self, "Warning", "An object with the same name already exists", QMessageBox.Ok | QMessageBox.Cancel)
            if ret == QMessageBox.Ok:
                obj = Id12(name, number_of_forms, number_of_teams, forms, team_order, members_order, teams_list, teams_sizes)
                ObjectsManager.add(ObjectsManager, obj)
                print(obj.number_system)
                self.ui.label_7.setText(f"Object '{name.strip()}' created")
                self.ui.label_7.show()
                self.ui.lineEdit.clear()
                self.ui.pushButton.setEnabled(False)
            if ret == QMessageBox.Cancel:
                self.ui.lineEdit.clear()
                self.ui.pushButton.setEnabled(False)
        else:
            obj = Id12(name, number_of_forms, number_of_teams, forms, team_order, members_order, teams_list, teams_sizes)
            ObjectsManager.add(ObjectsManager, obj)
            print(obj.number_system)
            print(obj.number_of_elements)
            self.ui.label_7.setText(f"Object '{name.strip()}' created")
            self.ui.label_7.show()
            self.ui.lineEdit.clear()
            self.ui.pushButton.setEnabled(False)
        print(EntityManager._items)
        self.ui.pushButton.setEnabled(False)