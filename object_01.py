from PySide6.QtWidgets import QButtonGroup, QHBoxLayout, QLabel, QWidget, QLineEdit, QMessageBox, QFileDialog
from PySide6.QtCore import Signal, Qt, QTimer, QStandardPaths
import json
from cryptography.fernet import Fernet
from collections import defaultdict
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont
from pathlib import Path
from object_01_ui_ui import Ui_Dialog
from entities import EntityManager
from objects import Id01
from object_manager import ObjectsManager
import symbols

class Object_01(QWidget):
    cancel_clicked = Signal()
    previous_form_type = "default"
    form_type = "default"
    is_name_valid = False
    is_not_valid = False # not: number of times
    is_nof_valid = False # nof: number of forms
    table_type = "normal"
    is_perm_or_comb_valid = True
    is_alt_base = False
    saved_data = []
    saved_data_1 = []
    is_previous_data = False
    previous_number_of_forms = 1
    check_forms = False
    check_properties_name = False
    properties_name = defaultdict(list) # No really importance except to check if they are duplicate names
    properties_names_ids = defaultdict(int)
    properties_name_list = []
    ENCRYPTION_KEY = 'Rll0H4fZf5TvH1E-mk0qwcZ1cETu6jlA_2PiwZ9cvls='
    cipher = Fernet(ENCRYPTION_KEY)
    documents = Path(QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation))
    m_app_folder = documents / "M App" / "Objects 01"
    m_app_folder.mkdir(parents=True, exist_ok=True)
    documents_dir = m_app_folder
    untitled_x = 1 # Use to name the untitled files of the Save As Window
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        #print(Fernet.generate_key().decode())
        self.ui.setupUi(self)
        self.ui.label.hide()
        self.ui.spinBox_2.setRange(1, 1000)
        self.ui.spin_box.setRange(1, 1000)
        self.ui.spinBox.setRange(1, 1000)
        self.ui.spinBox_3.setRange(1, 1000)
        self.ui.spinBox_3.setValue(1)
        self.ui.spin_box.setValue(1)
        self.ui.spinBox_2.setValue(1)
        self.ui.spinBox.setValue(1)
        self.ui.lineEdit_3
        
        self.ui.pushButton.setEnabled(False)
        
        self.ui.label_5.hide()
        self.ui.lineEdit_3.textChanged.connect(self.check_if_name_exist)
        
        self.forms_type = QButtonGroup()
        self.ui.radioButton_4.setChecked(True)
        self.forms_type.addButton(self.ui.radioButton_4)
        self.forms_type.addButton(self.ui.radioButton_5)
        self.forms_type.addButton(self.ui.radioButton_6)
        self.forms_type.buttonClicked.connect(self.forms_type_radio_btn_clicked)
        self.forms_type_radio_btn_clicked()
        
        self.table_types = QButtonGroup()
        self.ui.radioButton.setChecked(True)
        self.table_types.addButton(self.ui.radioButton)
        self.table_types.addButton(self.ui.radioButton_2)
        self.table_types.addButton(self.ui.radioButton_3)
        self.table_types.buttonClicked.connect(self.table_type_radio_btn_clicked)
        self.table_types.buttonClicked.connect(self.check_valid_perm_or_comb)
        
        self.ui.spin_box.valueChanged.connect(self.generate_form_widgets)
        
        self.ui.pushButton_2.clicked.connect(self.cancel_clicked.emit)
        self.ui.pushButton.clicked.connect(self.create_object)
        
        self.ui.spinBox_2.valueChanged.connect(self.check_entries)
        self.ui.spinBox_2.valueChanged.connect(self.check_valid_perm_or_comb)
        self.ui.spin_box.valueChanged.connect(self.check_entries)
        self.ui.spin_box.valueChanged.connect(self.check_valid_perm_or_comb)
        self.ui.lineEdit_2.textChanged.connect(self.check_entries)
        
        self.ui.label_8.hide()
        
        self.ui.pushButton_3.clicked.connect(self.go_to_form)
        
        self.ui.pushButton_4.setToolTip(f"Save this object creation session")
        self.ui.pushButton_5.setToolTip("Save this object creation session")
        self.ui.pushButton_6.setToolTip("Load object creation session with object id '01'")
        
        self.config_data = {"object_id": "01", "object_name": str, "nOt": int, "nOf": int, "form_type": str,"form": str, "forms": list, "properties": list, "gtfnum": int, "gtpro": int, "table_type": str, "prev_form_type": str}
        
        self.ui.pushButton_4.clicked.connect(self.save_config)
        self.ui.pushButton_5.clicked.connect(self.save_as_config)
        self.ui.pushButton_6.clicked.connect(self.load_config_dialog)
        
        self.ui.spinBox_2.valueChanged.connect(self.generate_properties_names_widgets)
        self.ui.spinBox_2.valueChanged.connect(self.check_entries)
        self.generate_properties_names_widgets()
        
        self.current_file = None
        
        self.ui.label_9.hide()
        
        self.ui.pushButton_7.clicked.connect(self.go_to_property)
        
        self.model = QStandardItemModel()
        self.ui.comboBox.setModel(self.model)
        
        self.ui.frame_15.hide()
        self.ui.pushButton_8.clicked.connect(self.go_to_property_name_error)
        
    def check_if_name_exist(self) -> None:
        name = self.ui.lineEdit_3.text().strip()
        
        if not(name):
            self.is_name_valid = False
        elif (name, "object") in EntityManager._items:
            self.ui.label_5.setText("❌ An object with the same name already exists")
            self.ui.label_5.show()
            self.is_name_valid = False
        elif EntityManager.name_exists_with_different_type(EntityManager, name, "object"):
            self.ui.label_5.setText("⚠️ An event or system with the same name already exists")
            self.ui.label_5.show()
            self.is_name_valid = True
        else:
            self.ui.label_5.hide()
            self.is_name_valid = True
        self.check_entries()
        
    def check_if_same_property_name_exist(self):
        self.ui.comboBox.clear()
        self.properties_name.clear()
        self.properties_names_ids.clear()
        layout = self.ui.scrollAreaWidgetContents.layout()
        total_forms = layout.count()
        
        for i in range(total_forms):
            widget = layout.itemAt(i).widget()
            if widget:
                line_edit = widget.findChild(QLineEdit).text().strip()
                if line_edit:
                    if line_edit == "":
                        pass
                    else:
                        self.properties_name[line_edit].append(i)
        for i in list(self.properties_name.keys()):
            if len(self.properties_name[i]) == 1:
                del self.properties_name[i]
                
        for i in self.properties_name.keys():
            header = QStandardItem(i)
            flags = header.flags()
            flags &= ~Qt.ItemIsEnabled
            flags &= ~Qt.ItemIsSelectable
            header.setFlags(flags)
            font = QFont()
            font.setBold(True)
            header.setFont(font)
            self.model.appendRow(header)
            for j in self.properties_name[i]:
                self.model.appendRow(QStandardItem(f" Property {j + 1}")) # Indent for clarity
                self.properties_names_ids[f" Property {j + 1}"] = j
        if self.ui.comboBox.count() > 0:
            self.ui.frame_15.show()
            self.check_properties_name = False
        else:
            all_filled = all(layout.itemAt(i).widget().findChild(QLineEdit).text().strip() for i in range(layout.count()))
            if all_filled:
                self.ui.frame_15.hide()
                self.check_properties_name = True
            else:
                self.ui.frame_15.hide()
                self.check_properties_name = False
            
    def go_to_property_name_error(self):
        index = self.properties_names_ids[self.ui.comboBox.currentText()]
        layout = self.ui.scrollAreaWidgetContents.layout()
        target_widget = layout.itemAt(index).widget()
        if target_widget:
            self.ui.scrollArea_2.ensureWidgetVisible(target_widget)
        else:
            QMessageBox.warning(self, "Navigation Error", "Form not found")
        self.highlight_temporarily(layout.itemAt(index).widget(), duration=2000)
            
    def forms_type_radio_btn_clicked(self) -> None:
        
        if self.ui.radioButton_4.isChecked():
            if self.previous_form_type == "alternative":
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
                self.previous_number_of_forms = self.ui.spin_box.value()
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
                self.previous_number_of_forms = self.ui.spin_box.value()
            layout = self.ui.widget.layout()
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
            self.previous_form_type = "default"
            self.form_type = "alternative_base"
            self.ui.lineEdit_2.setEnabled(True)
            self.ui.spinBox.setEnabled(False)
            self.ui.pushButton_3.setEnabled(False)
        elif self.ui.radioButton_6.isChecked():
            #self.ui.widget.clear()
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
            self.previous_number_of_forms = self.ui.spin_box.value()
            self.form_type = "alternative"
            self.previous_form_type = "alternative"
            self.ui.lineEdit_2.setEnabled(False)
            self.ui.spinBox.setEnabled(True)
            self.ui.pushButton_3.setEnabled(True)
        self.check_if_name_exist()
        self.check_entries()
        
    def table_type_radio_btn_clicked(self) -> None:
        if self.ui.radioButton.isChecked():
            self.table_type = "normal"
        if self.ui.radioButton_2.isChecked():
            self.table_type = "permutations"
        if self.ui.radioButton_3.isChecked():
            self.table_type = "combinations"
        self.check_if_name_exist()
        self.check_entries()
            
    def create_object(self) -> None:
        name = self.ui.lineEdit_3.text().strip()
        number_of_forms = self.ui.spin_box.value()
        number_of_times = self.ui.spinBox_2.value()
        table = self.table_type
        form = self.form_type
        forms = []
        properties = []
        layout = self.ui.scrollAreaWidgetContents.layout()
        self.properties_name_list = []
        for i in range(layout.count()):
            row = layout.itemAt(i).widget()
            if row:
                line_edit = row.findChild(QLineEdit)
                if line_edit: # else part could have been considered, but it was not considered because, generally before this function is accessed by the user all fields must be filled
                    self.properties_name_list.append(line_edit.text().strip())
        properties = self.properties_name_list
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

        if EntityManager.name_exists_with_different_type(EntityManager, name, "object") == True:
                ret = QMessageBox.warning(self, "Warning", "An object with the same name already exists", QMessageBox.Ok | QMessageBox.Cancel)
                if ret == QMessageBox.Ok:
                    obj = Id01(name, number_of_forms, number_of_times, table, form, properties, forms)
                    ObjectsManager.add(ObjectsManager, obj)
                    print(obj.number_system)
                    #print(obj.properties_names)
                    self.ui.label.setText(f"Object '{name.strip()}' created")
                    self.ui.label.show()
                    self.ui.lineEdit_3.clear()
                    self.ui.pushButton.setEnabled(False)
                if ret == QMessageBox.Cancel:
                    self.ui.lineEdit_3.clear()
                    self.ui.pushButton.setEnabled(False)
        else:
            obj = Id01(name, number_of_forms, number_of_times, table, form, properties, forms)
            ObjectsManager.add(ObjectsManager, obj)
            print(obj.number_system)
            #print(obj.properties_names)
            self.ui.label.setText(f"Object '{name.strip()}' created")
            self.ui.label.show()
            self.ui.lineEdit_3.clear()
            self.ui.pushButton.setEnabled(False)
        #print(EntityManager._items)
        self.ui.pushButton.setEnabled(False)

    def check_entries(self) -> None:
        #self.check_if_name_exist()
        self.check_valid_perm_or_comb()
        self.check_if_same_property_name_exist()
        if self.form_type == "default":
            if self.ui.spinBox_2.value():
                self.is_not_valid = True
            else:
                self.is_not_valid = False
            if self.ui.spin_box.value():
                self.is_nof_valid = True
            else:
                self.is_nof_valid = False
            self.ui.pushButton.setEnabled(self.is_name_valid and self.is_nof_valid and self.is_not_valid and self.is_perm_or_comb_valid and self.check_properties_name)
        if self.form_type == "alternative_base":
            if self.ui.spinBox_2.value():
                self.is_not_valid = True
            else:
                self.is_not_valid = False
            if self.ui.spin_box.value():
                self.is_nof_valid = True
            else:
                self.is_nof_valid = False
            if self.ui.lineEdit_2.text().strip():
                self.is_alt_base = True
            else:
                self.is_alt_base = False
            self.ui.pushButton.setEnabled(self.is_name_valid and self.is_nof_valid and self.is_not_valid and self.is_perm_or_comb_valid and self.is_alt_base and self.check_properties_name)
        if self.form_type == "alternative":
            if self.ui.spinBox_2.value():
                self.is_not_valid = True
            else:
                self.is_not_valid = False
            if self.ui.spin_box.value():
                self.is_nof_valid = True
            else:
                self.is_nof_valid = False
            layout = self.ui.widget.layout()
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    line_edit = row.findChild(QLineEdit)
                    if line_edit.text().strip():
                        self.check_forms = True
                    else:
                        self.check_forms = False
            self.ui.pushButton.setEnabled(self.is_name_valid and self.is_nof_valid and self.is_not_valid and self.is_perm_or_comb_valid and self.check_forms and self.check_properties_name)
        #print(f"{self.is_name_valid} {self.is_alt_base} {self.is_nof_valid} {self.is_not_valid} {self.is_perm_or_comb_valid} {self.check_forms} {self.check_properties_name}")
        
    def check_valid_perm_or_comb(self) -> None:
        if self.ui.radioButton_2.isChecked() or self.ui.radioButton_3.isChecked():
            nOt = self.ui.spinBox_2.value()
            nof = self.ui.spin_box.value()
            if nOt > nof:
                self.ui.label_8.setText("❌ Permutations or combinations not possible, number of times is greater than number of forms")
                self.ui.label_8.show()
                self.is_perm_or_comb_valid = False
            else:
                self.ui.label_8.hide()
                self.is_perm_or_comb_valid = True
        else:
            self.ui.label_8.hide()
            self.is_perm_or_comb_valid = True
            
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
            
    def generate_properties_names_widgets(self):
        layout = self.ui.scrollAreaWidgetContents.layout()
        self.ui.scrollAreaWidgetContents.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.saved_data_1 = []
        for i in range(layout.count()):
            row = layout.itemAt(i).widget()
            if row:
                line_edit = row.findChild(QLineEdit)
                if line_edit:
                    self.saved_data_1.append(line_edit.text())
                else:
                    self.saved_data_1.append("")
        
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        for i in range(self.ui.spinBox_2.value()):
            row_widget = QWidget()
            row_layout = QHBoxLayout(row_widget)
            
            label = QLabel(f"Property {i + 1}")
            line_edit = QLineEdit()
            
            if i < len(self.saved_data_1):
                line_edit.setText(self.saved_data_1[i])
            
            row_layout.addWidget(label)
            row_layout.addWidget(line_edit)
        
            layout.addWidget(row_widget)
            
            line_edit.textChanged.connect(self.check_entries)
            line_edit.textChanged.connect(self.check_if_same_property_name_exist)
            
        scrollbar = self.ui.scrollArea_2.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
            
    def go_to_form(self) -> None:
        index = self.ui.spinBox.value()
        layout = self.ui.widget.layout()
        total_forms = layout.count()
        
        if index < 1 or index > total_forms:
            QMessageBox.warning(self, "Navigation Error", "Form not found")
            return
        target_widget = layout.itemAt(index - 1).widget()
        if target_widget:
            self.ui.scrollArea.ensureWidgetVisible(target_widget)
        else:
            QMessageBox.warning(self, "Navigation Error", "Form not found")
        self.highlight_temporarily(layout.itemAt(index - 1).widget(), duration=2000)
        
    def go_to_property(self) -> None:
        index = self.ui.spinBox_3.value()
        layout = self.ui.scrollAreaWidgetContents.layout()
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
        
    def highlight_temporarily(self, widget: QWidget, duration: int = 2000):
        widget.setStyleSheet("""
                             QWidget {
                                 border: 2px solid #00ffff;
                                 border-radius: 6px;
                             }
                             """)
        QTimer.singleShot(2000, lambda: widget.setStyleSheet(""))
        
    def get_config_data(self) -> dict:
        self.config_data["object_name"] = self.ui.lineEdit_3.text().strip()
        self.config_data["nOt"] = self.ui.spinBox_2.value()
        self.config_data["nOf"] = self.ui.spin_box.value()
        self.config_data["form_type"] = self.form_type
        self.config_data["gtfnum"] = self.ui.spinBox.value()
        self.config_data["gtpro"] = self.ui.spinBox_3.value()
        self.config_data["table_type"] = self.table_type
        self.config_data["prev_form_type"] = self.previous_form_type
        #print(self.config_data["table_type"])
        self.config_data["form"] = self.ui.lineEdit_2.text().strip()
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
        
        layout = self.ui.scrollAreaWidgetContents.layout()
        self.properties_name_list = []
        for i in range(layout.count()):
            row = layout.itemAt(i).widget()
            if row:
                line_edit = row.findChild(QLineEdit)
                if line_edit:
                    self.properties_name_list.append(line_edit.text())
                else:
                    self.saved_data.append("")
        self.config_data["forms"] = self.saved_data
        self.config_data["properties"] = self.properties_name_list
        #print(self.config_data["properties"])
        #print(self.properties_name)
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
                self.ui.label.setText(f"Object creation session data saved to {self.current_file}")
                self.ui.label.show()
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
            self.ui.label.setText(f"Object creation session data saved to {self.current_file}")
            self.ui.label.show()
            
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
            self.ui.label.setText(f"Object creation session {self.current_file} loaded")
            self.ui.label.show()
        else:
            return
        if not isinstance(file_name, str):
            QMessageBox.warning(self, "Error", "Invalid file")
            return

    def load_config(self, config_data):
            if config_data["object_id"] == "01":
                print("Loaded config:", config_data)
                print("Loaded properties:", config_data.get("properties"))
                self.ui.lineEdit_3.setText(config_data["object_name"])
                self.ui.spinBox_2.setValue(config_data["nOt"])
                self.ui.spin_box.setValue(config_data["nOf"])
                self.ui.spinBox.setValue(config_data["gtfnum"])
                self.ui.spinBox_3.setValue(config_data["gtpro"])
                self.ui.lineEdit_2.setText(config_data["form"])
                self.form_type = config_data["form_type"]
                self.previous_form_type = config_data["prev_form_type"]
                if config_data["form_type"] == "default":
                    self.ui.radioButton_4.setChecked(True)
                elif config_data["form_type"] == "alternative_base":
                    self.ui.radioButton_5.setChecked(True)
                elif config_data["form_type"] == "alternative":
                    self.ui.radioButton_6.setChecked(True)
                    self.saved_data = config_data["forms"]
                    self.properties_name_list = config_data["properties"]
                    
                    layout = self.ui.widget.layout()
                    self.ui.widget.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
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
                            print(f"Set property {i}: {line_edit.text().strip()}")
                        
                        row_layout.addWidget(label)
                        row_layout.addWidget(line_edit)
                    
                        layout.addWidget(row_widget)
                        
                        line_edit.textChanged.connect(self.check_entries)
                        
                    scrollbar = self.ui.scrollArea.verticalScrollBar()
                    scrollbar.setValue(scrollbar.maximum())
                
                layout = self.ui.scrollAreaWidgetContents.layout()
                self.properties_name_list = config_data["properties"]
                print("self.properties_name_list before widget creation:", self.properties_name_list)
                self.ui.scrollAreaWidgetContents.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.deleteLater()
                for i in range(self.ui.spinBox_2.value()):
                    row_widget = QWidget()
                    row_layout = QHBoxLayout(row_widget)
                    
                    label = QLabel(f"Property {i + 1}")
                    line_edit = QLineEdit()
                    
                    row_layout.addWidget(label)
                    row_layout.addWidget(line_edit)
                    layout.addWidget(row_widget)
                    
                    if i < len(self.properties_name_list):
                        line_edit.setText(self.properties_name_list[i])
                    print(f"Set property {i}: {line_edit.text().strip()}")
                    
                    line_edit.textChanged.connect(self.check_entries)
                    
                scrollbar = self.ui.scrollArea_2.verticalScrollBar()
                scrollbar.setValue(scrollbar.maximum())
                
                self.table_type = config_data["table_type"]
                if config_data["table_type"] == "normal":
                    self.ui.radioButton.setChecked(True)
                elif config_data["table_type"] == "permutations":
                    self.ui.radioButton_2.setChecked(True)
                elif config_data["table_type"] == "combinations":
                    self.ui.radioButton_3.setChecked(True)
                
                for i in range(layout.count()):
                    row = layout.itemAt(i).widget()
                    if row:
                        line_edit = row.findChild(QLineEdit)
                        if line_edit:
                            print(f"Final QLineEdit {i}: {line_edit.text().strip()}")
            else:
                QMessageBox.warning(self, "Error", f"The object type of the loaded file has id {config_data["object_id"]} which doesn't correspond to the id of the present object creation\n\nSearch for the id {config_data["object_id"]} in the search bar and load this file into it")
            self.check_if_name_exist()
            self.check_entries()
            self.check_valid_perm_or_comb()
            self.forms_type_radio_btn_clicked()
        
"""
app = QApplication(sys.argv)
window = Object_01()
window.show()
app.exec()
"""