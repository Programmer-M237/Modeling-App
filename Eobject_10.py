from PySide6.QtWidgets import QMessageBox, QApplication, QFileDialog, QWidget, QButtonGroup, QHBoxLayout, QLabel, QLineEdit
from PySide6.QtCore import Qt, Signal, QTimer, QStandardPaths
from pathlib import Path
import json
from cryptography.fernet import Fernet
from Eobject_10_ui import Ui_Dialog
from temp_objects import Id10
from temp_events import Events
from step_2_of_event_creation import Event_properties
import symbols
from math import trunc

class EObject_10(QWidget):
    test: str = "Testing" # For debugging purposes
    cancel_clicked = Signal()
    is_name_valid = True # Problem 001
    check_forms = False
    is_nof_valid = False
    is_alt_base = False
    is_nom_valid = False
    form_type: str = "default"
    previous_form_type: str = "default"
    order = False
    saved_data: list = []
    previous_number_of_forms: int = 1
    ENCRYPTION_KEY = 'Rll0H4fZf5TvH1E-mk0qwcZ1cETu6jlA_2PiwZ9cvls='
    cipher = Fernet(ENCRYPTION_KEY)
    documents = Path(QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation))
    m_app_folder = documents / "M App" / "Objects 10"
    m_app_folder.mkdir(parents=True, exist_ok=True)
    documents_dir = m_app_folder
    untitled_x = 1 # Use to name the untitled files of the Save As Window
    close_by_code_initiated = Signal()
    
    def __init__(self, top_window, event_name):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QApplication.processEvents()
        self.ui.label_2.hide()
        self.ui.label_7.hide()
        self.ui.spin_box.setRange(1, 1000)
        self.ui.spin_box.setValue(1)
        self.ui.spin_box_2.setRange(1, 1000)
        self.ui.spin_box_2.setValue(1)
        self.ui.spinBox.setRange(1, 1000)
        self.ui.spinBox.setValue(1)
        self.ui.pushButton.setEnabled(False)
        self.top_window = top_window
        self.event_name = event_name
        
        self.ui.pushButton_2.clicked.connect(self.cancel_clicked.emit)
        
        #self.ui.lineEdit.textChanged.connect(self.check_if_name_exist)
        
        #### Problem 001
        self.ui.lineEdit.setText(f"{self.event_name}'s object")
        self.ui.lineEdit.setEnabled(False)
        ####
        
        self.forms_type = QButtonGroup()
        self.ui.radioButton_4.setChecked(True)
        self.forms_type.addButton(self.ui.radioButton_4)
        self.forms_type.addButton(self.ui.radioButton_5)
        self.forms_type.addButton(self.ui.radioButton_6)
        self.forms_type.buttonClicked.connect(self.forms_type_radio_btn_clicked)
        self.forms_type_radio_btn_clicked()
        
        self.ui.spin_box.valueChanged.connect(self.generate_form_widgets)
        
        self.ui.lineEdit.textChanged.connect(self.check_entries)
        self.ui.spin_box.valueChanged.connect(self.check_entries)
        self.ui.spin_box_2.valueChanged.connect(self.check_entries)
        self.ui.spin_box_2.valueChanged.connect(self.check_number_of_members)
        self.ui.lineEdit_2.textChanged.connect(self.check_entries)
        self.ui.spinBox.valueChanged.connect(self.check_entries)
        self.forms_type.buttonClicked.connect(self.check_entries)
        
        self.ui.pushButton_3.clicked.connect(self.go_to_property)
        
        self.ui.pushButton_4.setToolTip(f"Save this object creation session")
        self.ui.pushButton_5.setToolTip("Save this object creation session")
        self.ui.pushButton_6.setToolTip("Load object creation session with object id '10'")
        
        self.config_data = {"object_id": "10", "object_name": "", "nOf": 1, "form_type": "default", "prev_form_type": "default", "form": "", "forms": [], "gtfnum": 1, "prev_nof": 1, "nom": 1, "order": False}
        
        self.ui.pushButton_4.clicked.connect(self.save_config)
        self.ui.pushButton_5.clicked.connect(self.save_as_config)
        self.ui.pushButton_6.clicked.connect(self.load_config_dialog)
        
        self.current_file = None
        
        self.ui.pushButton.clicked.connect(self.create_object)
        
        self.check_number_of_members()
        
        self.ui.checkBox.stateChanged.connect(self.order_check_box_toggle)
        
    # def check_if_name_exist(self) -> None:
    #     name = self.ui.lineEdit.text().strip()
        
    #     if not(name):
    #         self.is_name_valid = False
    #     elif (name, "object") in EntityManager._items:
    #         self.ui.label_2.setText("❌ An object with the same name already exists")
    #         self.ui.label_2.show()
    #         self.is_name_valid = False
    #     elif EntityManager.name_exists_with_different_type(EntityManager, name, "object"):
    #         self.ui.label_2.setText("⚠️ An event or system with the same name already exists")
    #         self.ui.label_2.show()
    #         self.is_name_valid = True
    #     else:
    #         self.ui.label_2.hide()
    #         self.is_name_valid = True
    
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
            layout = self.ui.widget.layout()
            self.ui.widget.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
            for i in range(self.previous_number_of_forms):
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
            self.previous_number_of_forms = self.ui.spin_box.value()
            self.form_type = "alternative"
            self.previous_form_type = "alternative"
            self.ui.lineEdit_2.setEnabled(False)
            self.ui.spinBox.setEnabled(True)
            self.ui.pushButton_3.setEnabled(True)
        # self.check_if_name_exist()
        self.check_entries()
        
    def check_entries(self) -> None:
        #self.check_if_name_exist()
        self.check_number_of_members()
        if self.form_type == "default":
            if self.ui.spin_box.value():
                self.is_nof_valid = True
            else:
                self.is_nof_valid = False
            # if self.ui.spin_box_2.value(): KIND OF USELESS, IN FACT ALL THESE TYPE RELATED CODE IS USELESS BECAUSE THE SPIN BOXES CAN NEVER BE INVALID SINCE MIN IS 1 AND MAX IS 1000
            #     self.is_nog_valid = True
            # else:
            #     self.is_nog_valid = False
            self.ui.pushButton.setEnabled(self.is_name_valid and self.is_nof_valid and self.is_nom_valid)
        elif self.form_type == "alternative_base":
            if self.ui.spin_box.value():
                self.is_nof_valid = True
            else:
                self.is_nof_valid = False
            if self.ui.spin_box_2.value():
                self.is_nog_valid = True
            else:
                self.is_nog_valid = False
            if self.ui.lineEdit_2.text().strip():
                self.is_alt_base = True
            else:
                self.is_alt_base = False
            self.ui.pushButton.setEnabled(self.is_name_valid and self.is_nof_valid and self.is_alt_base and self.is_nom_valid)
        elif self.form_type == "alternative":
            if self.ui.spin_box.value():
                self.is_nof_valid = True
            else:
                self.is_nof_valid = False
            if self.ui.spin_box_2.value():
                self.is_nog_valid = True
            else:
                self.is_nog_valid = False
            layout = self.ui.widget.layout()
            self.check_forms = all(
                layout.itemAt(i).widget().findChild(QLineEdit).text().strip()
                for i in range(layout.count())
                if layout.itemAt(i).widget()
            )
            self.ui.pushButton.setEnabled(self.is_name_valid and self.is_nof_valid and self.check_forms and self.is_nog_valid)
        
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
    
    def go_to_property(self) -> None:
        #print(self.test)
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
        
    def get_config_data(self) -> dict:
        self.config_data["object_name"] = self.ui.lineEdit.text().strip()
        self.config_data["nOf"] = self.ui.spin_box.value()
        self.config_data["nom"] = self.ui.spin_box_2.value()
        self.config_data["form_type"] = self.form_type
        self.config_data["prev_form_type"] = self.previous_form_type
        self.config_data["gtfnum"] = self.ui.spinBox.value()
        self.config_data["form"] = self.ui.lineEdit_2.text().strip()
        self.config_data["prev_nof"] = self.previous_number_of_forms
        self.config_data["order"] = self.order
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
            if config_data["object_id"] == "10":
                #self.ui.lineEdit.setText(config_data["object_name"])
                self.ui.spin_box.setValue(config_data["nOf"])
                self.ui.spin_box_2.setValue(config_data["nom"])
                self.ui.spinBox.setValue(config_data["gtfnum"])
                self.ui.lineEdit_2.setText(config_data["form"])
                self.previous_number_of_forms = config_data["prev_nof"]
                self.form_type = config_data["form_type"]
                self.previous_form_type = config_data["prev_form_type"]
                self.order = config_data["order"]
                if self.order == True:
                    self.ui.checkBox.setChecked(True)
                else:
                    self.ui.checkBox.setChecked(False)
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
                
                self.saved_data = config_data["forms"] # This is for restoring of data in the alternative mode if the program loads in other modes
                #### Problem 001
                self.ui.lineEdit.setText(f"{self.event_name}'s object")
                self.ui.lineEdit.setEnabled(False)
                ####
            else:
                QMessageBox.warning(self, "Error", f"The object type of the loaded file has id {config_data["object_id"]} which doesn't correspond to the id of the present object creation\n\nSearch for the id {config_data["object_id"]} in the search bar and load this file into it")
            # self.check_if_name_exist()
            self.check_entries()

    def create_object(self) -> None:
        name = self.ui.lineEdit.text().strip()
        number_of_forms = self.ui.spin_box.value()
        number_of_members = self.ui.spin_box_2.value()
        number_of_groups = trunc(self.ui.spin_box.value()/self.ui.spin_box_2.value())
        order_matters = self.order
        form = self.form_type
        forms = []
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
        
        obj = Id10(number_of_forms, number_of_members, number_of_groups, forms, order_matters)
        event = Events(self.event_name, obj.number_system)
        window = Event_properties(event)
        self.top_window.hide()
        window.exec()
        self.close_by_code_initiated.emit()
        return
        
    def check_number_of_members(self):
        if self.ui.spin_box.value() % self.ui.spin_box_2.value() != 0:
            self.ui.label_8.setText("❌ Number of members must be divisible by the number of members to be selected for selection to be possible")
            self.is_nom_valid = False
        else:
            self.ui.label_8.setText(f"Number of groups: {trunc(self.ui.spin_box.value()/self.ui.spin_box_2.value())}")
            self.is_nom_valid = True
    
    def order_check_box_toggle(self, state):
        if state == 2:
            self.order = True
        else:
            self.order = False