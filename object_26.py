from PySide6.QtWidgets import QMessageBox, QFileDialog, QWidget, QButtonGroup, QHBoxLayout, QLabel, QLineEdit
from PySide6.QtCore import Qt, Signal, QTimer, QStandardPaths
from pathlib import Path
import json
from cryptography.fernet import Fernet
from object_26_ui import Ui_Dialog
from objects import Id26
from object_manager import ObjectsManager
from entities import EntityManager
import symbols

class Object_26(QWidget, Ui_Dialog):
    cancel_clicked = Signal()
    is_name_valid = False
    is_alt_base = False
    check_forms = False
    form_type = "default"
    saved_data = []
    is_num_of_items_to_be_selected_valid = False
    previous_number_of_forms = 1
    repetition_allowed = False
    previous_form_type = "default" # This is used to resolve a problem I found only in this object which is found in at least 6 other objects. The problem is that when the form mode is shift from alternative to another form and not back to alternative, the data stored from the alternative mode is cleared (generally the code was written to store the data if the mode is from alternative to another mode and back to alternative, other scenarios were not considered)
    ENCRYPTION_KEY = 'Rll0H4fZf5TvH1E-mk0qwcZ1cETu6jlA_2PiwZ9cvls='
    cipher = Fernet(ENCRYPTION_KEY)
    documents = Path(QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation))
    m_app_folder = documents / "M App" / "Objects 26"
    m_app_folder.mkdir(parents=True, exist_ok=True)
    documents_dir = m_app_folder
    untitled_x = 1 # Use to name the untitled files of the Save As Window
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.spin_box.setRange(1, 1000)
        self.spin_box.setValue(1)
        self.spin_box_4.setRange(1, 1000)
        self.spin_box_4.setValue(1)
        self.spinBox.setRange(1, 1000)
        self.spinBox.setValue(1)
        self.label_5.hide()
        self.label_11.hide()
        self.label_13.hide()
        self.pushButton.setEnabled(False)
        
        self.pushButton_2.clicked.connect(self.cancel_clicked.emit)
        
        self.lineEdit_3.textChanged.connect(self.check_if_name_exist)
        
        forms_type = QButtonGroup(self)
        self.radioButton_4.setChecked(True)
        forms_type.addButton(self.radioButton_4)
        forms_type.addButton(self.radioButton_5)
        forms_type.addButton(self.radioButton_6)
        forms_type.buttonClicked.connect(self.update_form_type)
        self.update_form_type()
        
        self.spin_box.valueChanged.connect(self.generate_form_widgets)
        
        self.pushButton_3.clicked.connect(self.go_to_form)
        
        self.lineEdit_3.textChanged.connect(self.check_entries)
        self.lineEdit_2.textChanged.connect(self.check_entries)
        self.spin_box.valueChanged.connect(self.check_entries)
        self.spin_box_4.valueChanged.connect(self.check_entries)
        forms_type.buttonClicked.connect(self.check_entries)
        
        self.pushButton_4.setToolTip(f"Save this object creation session")
        self.pushButton_5.setToolTip("Save this object creation session")
        self.pushButton_6.setToolTip("Load object creation session with object id '26'")
        
        self.config_data = {"object_id": "26", "object_name": str, "form_type": str, "form": str, "nOf": int, "items": list, "gtform": int, "prev_nOf": int, "prev_form_type": str, "repetition_allowed": bool, "is_numits_valid": bool, "numits": int}
        
        self.pushButton_4.clicked.connect(self.save_config)
        self.pushButton_5.clicked.connect(self.save_as_config)
        self.pushButton_6.clicked.connect(self.load_config_dialog)
        
        self.checkBox_2.clicked.connect(self.update_repetition)
        
        self.current_file = None
        
        self.pushButton.clicked.connect(self.create_object)
        
        self.spin_box.valueChanged.connect(self.check_num_of_items_to_be_selected)
        self.spin_box_4.valueChanged.connect(self.check_num_of_items_to_be_selected)
        forms_type.buttonClicked.connect(self.check_num_of_items_to_be_selected)
        
    def check_if_name_exist(self) -> None:
        name = self.lineEdit_3.text().strip()
        
        if not(name):
            self.is_name_valid = False
        elif (name, "object") in EntityManager._items:
            self.label_5.setText("❌ An object with the same name already exists")
            self.label_5.show()
            self.is_name_valid = False
        elif EntityManager.name_exists_with_different_type(EntityManager, name, "object"):
            self.label_5.setText("⚠️ An event or system with the same name already exists")
            self.label_5.show()
            self.is_name_valid = True
        else:
            self.label_5.hide()
            self.is_name_valid = True
            
    def update_form_type(self) -> None:
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
            if self.previous_form_type != "alternative":
                layout = self.widget.layout()
                self.widget.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
                for i in range(self.previous_number_of_forms):
                    row_widget = QWidget()
                    row_layout = QHBoxLayout(row_widget)
                    label = QLabel(f"Item {i + 1}")
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
                self.previous_number_of_forms = self.spin_box.value()
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
                
                label = QLabel(f"Item {i + 1}")
                line_edit = QLineEdit()
                
                if i < len(self.saved_data):
                    line_edit.setText(self.saved_data[i])
                
                row_layout.addWidget(label)
                row_layout.addWidget(line_edit)
            
                layout.addWidget(row_widget)
                
                line_edit.textChanged.connect(self.check_entries)
                
            scrollbar = self.scrollArea.verticalScrollBar()
            scrollbar.setValue(scrollbar.maximum())
        self.check_entries()
        
    def go_to_form(self) -> None:
        index = self.spinBox.value()
        layout = self.widget.layout()
        total_forms = layout.count()
        
        if index < 1 or index > total_forms:
            QMessageBox.warning(self, "Navigation Error", "Property not found")
            return
        target_widget = layout.itemAt(index - 1).widget()
        if target_widget:
            self.scrollArea.ensureWidgetVisible(target_widget)
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
        
    def check_entries(self):
        self.check_if_name_exist()
        self.check_num_of_items_to_be_selected()
        if self.form_type == "default":
            self.pushButton.setEnabled(self.is_name_valid and self.is_num_of_items_to_be_selected_valid)
        elif self.form_type == "alternative_base":
            if self.lineEdit_2.text().strip():
                self.is_alt_base = True
            else:
                self.is_alt_base = False
            self.pushButton.setEnabled(self.is_name_valid and self.is_alt_base and self.is_num_of_items_to_be_selected_valid)
        elif self.form_type == "alternative":
            layout = self.widget.layout()
            self.check_forms = all(
                layout.itemAt(i).widget().findChild(QLineEdit).text().strip()
                for i in range(layout.count())
                if layout.itemAt(i).widget()
            )
            self.pushButton.setEnabled(self.is_name_valid and self.check_forms and self.is_num_of_items_to_be_selected_valid)
            
    def get_config_data(self) -> dict:
        self.config_data["object_name"] = self.lineEdit_3.text().strip()
        self.config_data["nOf"] = self.spin_box.value()
        self.config_data["gtform"] = self.spinBox.value()
        self.config_data["form_type"] = self.form_type
        self.config_data["form"] = self.lineEdit_2.text().strip()
        self.config_data["prev_nOf"] = self.previous_number_of_forms
        self.config_data["prev_form_type"] = self.previous_form_type
        self.config_data["repetition_allowed"] = self.repetition_allowed
        self.config_data["numits"] = self.spin_box_4.value()
        self.config_data["is_numits_valid"] = self.is_num_of_items_to_be_selected_valid
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
        
        self.config_data["items"] = self.saved_data
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
                self.label_11.setText(f"Object creation session data saved to {self.current_file}")
                self.label_11.show()
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
            self.label_11.setText(f"Object creation session data saved to {self.current_file}")
            self.label_11.show()
            
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
            self.label_11.setText(f"Object creation session {self.current_file} loaded")
            self.label_11.show()
        else:
            return
        if not isinstance(file_name, str):
            QMessageBox.warning(self, "Error", "Invalid file")
            return

    def load_config(self, config_data):
            if config_data["object_id"] == "26":
                print(config_data)
                self.lineEdit_3.setText(config_data["object_name"])
                self.spin_box.setValue(config_data["nOf"])
                self.spinBox.setValue(config_data["gtform"])
                self.lineEdit_2.setText(config_data["form"])
                self.form_type = config_data["form_type"]
                self.previous_number_of_forms = config_data["prev_nOf"]
                self.previous_form_type = config_data["prev_form_type"]
                self.repetition_allowed = config_data["repetition_allowed"]
                self.spin_box_4.setValue(config_data["numits"])
                self.is_num_of_items_to_be_selected_valid = config_data["is_numits_valid"]
                
                self.checkBox_2.setEnabled(self.repetition_allowed) # It is not being executed, and I don't understand why. Everything is correct, the variable is saved and uploaded corrected, but it doesn't display it
                
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
                    self.spin_box.setValue(config_data["nOf"])
                    
                    layout = self.widget.layout()
                    self.widget.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
                    while layout.count():
                        item = layout.takeAt(0)
                        widget = item.widget()
                        if widget:
                            widget.deleteLater()
                    self.saved_data = config_data["items"]
                    for i in range(config_data["nOf"]):
                        row_widget = QWidget()
                        row_layout = QHBoxLayout(row_widget)
                        
                        label = QLabel(f"Item {i + 1}")
                        line_edit = QLineEdit()
                        
                        if i < len(self.saved_data):
                            line_edit.setText(config_data["items"][i])
                        
                        row_layout.addWidget(label)
                        row_layout.addWidget(line_edit)
                    
                        layout.addWidget(row_widget)
                        
                        line_edit.textChanged.connect(self.check_entries)
                        
                    scrollbar = self.scrollArea.verticalScrollBar()
                    scrollbar.setValue(scrollbar.maximum())
                
                self.saved_data = config_data["items"] # This is for restoring of data in the alternative mode if the program loads in other modes
            else:
                QMessageBox.warning(self, "Error", f"The object type of the loaded file has id {config_data["object_id"]} which doesn't correspond to the id of the present object creation\n\nSearch for the id {config_data["object_id"]} in the search bar and load this file into it")
            self.check_entries()
            
    def create_object(self) -> None:
        name = self.lineEdit_3.text().strip()
        number_of_items = self.spin_box.value()
        repetition_allowed = self.repetition_allowed
        r = self.spin_box_4.value()
        forms = []
        if self.form_type == "default":
            for i in range(number_of_items):
                forms.append(symbols.get_symbol(i))
        elif self.form_type == "alternative_base":
            word = self.lineEdit_2.text().strip()
            for i in range(number_of_items):
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
            
        if EntityManager.name_exists_with_different_type(EntityManager, name, "object") == True:
            ret = QMessageBox.warning(self, "Warning", "An object with the same name already exists", QMessageBox.Ok | QMessageBox.Cancel)
            if ret == QMessageBox.Ok:
                obj = Id26(name, number_of_items, forms, repetition_allowed, r)
                ObjectsManager.add(ObjectsManager, obj)
                print(obj.number_system)
                self.label_11.setText(f"Object '{name.strip()}' created")
                self.label_11.show()
                self.lineEdit_3.clear()
                self.pushButton.setEnabled(False)
            if ret == QMessageBox.Cancel:
                self.lineEdit_3.clear()
                self.pushButton.setEnabled(False)
        else:
            obj = Id26(name, number_of_items, forms, repetition_allowed, r)
            ObjectsManager.add(ObjectsManager, obj)
            print(obj.number_system)
            print(obj.number_of_elements)
            self.label_11.setText(f"Object '{name.strip()}' created")
            self.label_11.show()
            self.lineEdit_3.clear()
            self.pushButton.setEnabled(False)
        #print(EntityManager._items)
        self.pushButton.setEnabled(False)
        
    def update_repetition(self):
        if self.checkBox_2.isChecked():
            self.repetition_allowed = True
        else:
            self.repetition_allowed = False
            
    def check_num_of_items_to_be_selected(self):
        if self.spin_box.value() < self.spin_box_4.value():
            self.label_13.setText("❌ Number of items to select cannot be greater than the number of items")
            self.label_13.show()
            self.is_num_of_items_to_be_selected_valid = False
        else:
            self.label_13.hide()
            self.is_num_of_items_to_be_selected_valid = True