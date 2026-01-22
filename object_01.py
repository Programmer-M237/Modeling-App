from PySide6.QtWidgets import QButtonGroup, QHBoxLayout, QLabel, QWidget, QLineEdit, QMessageBox, QFileDialog
from PySide6.QtCore import Signal, Qt, QTimer, QStandardPaths
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont
import json
from cryptography.fernet import Fernet
from collections import defaultdict
from pathlib import Path
from object_01_ui import Ui_Dialog
from Entities import Entity
from objects import Id01
import symbols


class Object_01(QWidget, Ui_Dialog):
    # Constants
    MIN_PROPERTIES = 1
    MAX_PROPERTIES = 5
    MIN_FORMS = 1
    MAX_FORMS = 5
    HIGHLIGHT_DURATION = 2000
    
    # Signals
    cancel_clicked = Signal()
    
    # Class variables
    is_name_valid = False
    saved_properties = []
    saved_forms = []
    previous_number_of_forms = 1
    previous_form_type = "default"
    form_type = "default"
    with_repetition = True
    properties_name = defaultdict(list)
    properties_names_ids = defaultdict(int)
    check_properties_name = False
    check_forms = False
    repetition_valid = False
    
    documents = Path(QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation))
    m_app_folder = documents / "M App" / "Objects 01"
    m_app_folder.mkdir(parents=True, exist_ok=True)
    documents_dir = m_app_folder
    untitled_x = 1  # Use to name the untitled files of the Save As Window

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Initialize encryption
        self._initialize_encryption()
        
        # UI Setup
        self.label_9.hide()
        self.pushButton_6.setEnabled(False)
        self.label_8.hide()
        self.spinBox_2.setRange(self.MIN_PROPERTIES, self.MAX_PROPERTIES)
        self.spinBox_2.setValue(1)
        self.spinBox_3.setRange(self.MIN_FORMS, self.MAX_FORMS)
        self.spinBox_3.setValue(1)
        self.spinBox.setValue(1)
        self.spinBox_4.setValue(1)

        self.label_7.hide()
        self.lineEdit.textChanged.connect(self.check_if_name_exist)
        
        self.spinBox_2.valueChanged.connect(self.generate_property_widgets)
        self.generate_property_widgets()
        
        self.pushButton.clicked.connect(self.go_to_property)
        
        self.forms_type = QButtonGroup()
        self.radioButton.setChecked(True)
        self.forms_type.addButton(self.radioButton)
        self.forms_type.addButton(self.radioButton_2)
        self.forms_type.addButton(self.radioButton_3)
        self.forms_type.buttonClicked.connect(self.forms_type_radio_btn_clicked)
        self.forms_type_radio_btn_clicked()

        self.spinBox_3.valueChanged.connect(self.generate_form_widgets)
        self.generate_form_widgets()

        self.pushButton_2.clicked.connect(self.go_to_form)
        
        self.checkBox.setChecked(True)
        self.checkBox.toggled.connect(self.checkbox_toggle)
        self.checkBox.toggled.connect(self.check_entries)
        
        self.pushButton_3.setToolTip("Save this object creation session")
        self.pushButton_4.setToolTip("Save this object creation session")
        self.pushButton_5.setToolTip("Load object creation session with object id '01'")
        
        self.config_data = {
            "object_id": "01", 
            "object_name": str, 
            "nOt": int, 
            "nOf": int, 
            "form_type": str,
            "form": str, 
            "forms": list, 
            "properties": list, 
            "gtfnum": int, 
            "gtpro": int, 
            "prev_form_type": str, 
            "repetition?": bool,
            "repetition_valid": bool
        }
        
        self.pushButton_3.clicked.connect(self.save_config)
        self.pushButton_4.clicked.connect(self.save_as_config)
        self.pushButton_5.clicked.connect(self.load_config_dialog)
        
        self.model = QStandardItemModel()
        self.comboBox.setModel(self.model)
        self.comboBox.currentTextChanged.connect(self.go_to_property_name_error)
        
        self.current_file = None
        
        self.pushButton_7.clicked.connect(self.cancel_clicked.emit)
        
        self.pushButton_8.clicked.connect(self.go_to_property_name_error)
        
        self.pushButton_6.clicked.connect(self.create_object)
        
        self.spinBox_2.valueChanged.connect(self.checkbox_toggle)
        self.spinBox_3.valueChanged.connect(self.checkbox_toggle)
        
        self.lineEdit.textChanged.connect(self.check_if_name_exist)
        self.lineEdit_2.textChanged.connect(self.check_entries)
        self.spinBox_2.valueChanged.connect(self.check_if_same_property_name_exist)
        

    def _initialize_encryption(self):
        """Initialize encryption cipher with error handling"""
        try:
            encryption_file = Path('Encrypt.txt')
            if not encryption_file.exists():
                QMessageBox.critical(
                    self, 
                    "Error", 
                    "Encryption key file 'Encrypt.txt' not found. Please set up encryption."
                )
                self.cipher = None
                return
            
            with open(encryption_file, 'r') as file:
                self.ENCRYPTION_KEY = file.read().strip()
                if not self.ENCRYPTION_KEY:
                    raise ValueError("Encryption key is empty")
                self.cipher = Fernet(self.ENCRYPTION_KEY)
        except Exception as e:
            QMessageBox.critical(
                self, 
                "Error", 
                f"Failed to load encryption key: {str(e)}"
            )
            self.cipher = None

    def check_if_name_exist(self):
        name = self.lineEdit.text().strip()

        if not name:
            self.is_name_valid = False
        elif Entity.entity_exists(Entity, name, "object"):
            self.label_7.show()
            self.is_name_valid = False
        else:
            self.label_7.hide()
            self.is_name_valid = True
        self.check_entries()
        
    def _generate_input_widgets(self, layout, count, label_prefix, saved_values):
        """Generic method to generate property or form input widgets"""
        # Save current values
        saved = []
        for i in range(layout.count()):
            row = layout.itemAt(i).widget()
            if row:
                line_edit = row.findChild(QLineEdit)
                saved.append(line_edit.text() if line_edit else "")
        
        # Clear layout
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
        # Generate new widgets
        for i in range(count):
            row_widget = QWidget()
            row_layout = QHBoxLayout(row_widget)
            
            label = QLabel(f"{label_prefix} {i + 1}")
            line_edit = QLineEdit()
            
            line_edit.textChanged.connect(self.check_entries)
            
            if i < len(saved):
                line_edit.setText(saved[i])
            
            row_layout.addWidget(label)
            row_layout.addWidget(line_edit)
            layout.addWidget(row_widget)
        
        return saved
        
    def generate_property_widgets(self):
        layout = self.scrollAreaWidgetContents_2.layout()
        self.scrollAreaWidgetContents_2.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.saved_properties = self._generate_input_widgets(
            layout,
            self.spinBox_2.value(),
            "Property",
            self.saved_properties
        )
        
        # Connect signals after generation
        for i in range(layout.count()):
            row = layout.itemAt(i).widget()
            if row:
                line_edit = row.findChild(QLineEdit)
                
                if line_edit:
                    line_edit.textChanged.connect(self.check_entries)
                    line_edit.textChanged.connect(self.check_if_same_property_name_exist)
            
        scrollbar = self.scrollArea_2.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
        self.spinBox.setRange(1, self.spinBox_2.value())  # Making the go to text box range dynamic

    def go_to_property(self) -> None:
        index = self.spinBox.value()
        layout = self.scrollAreaWidgetContents_2.layout()
        total_forms = layout.count()
        
        if index < 1 or index > total_forms:
            QMessageBox.warning(self, "Navigation Error", "Property not found")
            return
        target_widget = layout.itemAt(index - 1).widget()
        if target_widget:
            self.scrollArea_2.ensureWidgetVisible(target_widget)
            self.highlight_temporarily(target_widget, duration=self.HIGHLIGHT_DURATION)
        else:
            QMessageBox.warning(self, "Navigation Error", "Property not found")

    def go_to_form(self) -> None:
        index = self.spinBox_4.value()
        layout = self.scrollAreaWidgetContents.layout()
        total_forms = layout.count()
        
        if index < 1 or index > total_forms:
            QMessageBox.warning(self, "Navigation Error", "Form not found")
            return
        target_widget = layout.itemAt(index - 1).widget()
        if target_widget:
            self.scrollArea.ensureWidgetVisible(target_widget)
            self.highlight_temporarily(target_widget, duration=self.HIGHLIGHT_DURATION)
        else:
            QMessageBox.warning(self, "Navigation Error", "Form not found")

    def highlight_temporarily(self, widget: QWidget, duration: int = 2000):
        widget.setStyleSheet("""
                             QWidget {
                                 border: 2px solid #00ffff;
                                 border-radius: 6px;
                             }
                             """)
        QTimer.singleShot(duration, lambda: widget.setStyleSheet(""))

    def forms_type_radio_btn_clicked(self):
        if self.radioButton.isChecked():
            if self.previous_form_type == "alternative":
                layout = self.scrollAreaWidgetContents.layout()
                self.saved_forms = []
                for i in range(layout.count()):
                    row = layout.itemAt(i).widget()
                    if row:
                        line_edit = row.findChild(QLineEdit)
                        if line_edit:
                            self.saved_forms.append(line_edit.text())
                        else:
                            self.saved_forms.append("")
                self.previous_number_of_forms = self.spinBox_3.value()
            layout = self.scrollAreaWidgetContents.layout()
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
            self.form_type = "default"
            self.previous_form_type = "default"
            self.lineEdit_2.setEnabled(False)
            self.spinBox_4.setEnabled(False)
            self.pushButton_2.setEnabled(False)
        elif self.radioButton_2.isChecked():
            if self.previous_form_type == "alternative":
                layout = self.scrollAreaWidgetContents.layout()
                self.saved_forms = []
                for i in range(layout.count()):
                    row = layout.itemAt(i).widget()
                    if row:
                        line_edit = row.findChild(QLineEdit)
                        if line_edit:
                            self.saved_forms.append(line_edit.text())
                        else:
                            self.saved_forms.append("")
                self.previous_number_of_forms = self.spinBox_3.value()
            layout = self.scrollAreaWidgetContents.layout()
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
            self.previous_form_type = "default"
            self.form_type = "alternative_base"
            self.lineEdit_2.setEnabled(True)
            self.spinBox_4.setEnabled(False)
            self.pushButton_2.setEnabled(False)
        elif self.radioButton_3.isChecked():
            for i in range(self.previous_number_of_forms):
                layout = self.scrollAreaWidgetContents.layout()
                self.scrollAreaWidgetContents.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
                row_widget = QWidget()
                row_layout = QHBoxLayout(row_widget)
                
                label = QLabel(f"Form {i + 1}")
                line_edit = QLineEdit()
                
                if i < len(self.saved_forms):
                    line_edit.setText(self.saved_forms[i])
                
                row_layout.addWidget(label)
                row_layout.addWidget(line_edit)
            
                layout.addWidget(row_widget)
                
                line_edit.textChanged.connect(self.check_entries)
                
            scrollbar = self.scrollArea.verticalScrollBar()
            scrollbar.setValue(scrollbar.maximum())
            self.spinBox_3.setValue(self.previous_number_of_forms)
            self.previous_number_of_forms = self.spinBox_3.value()
            self.form_type = "alternative"
            self.previous_form_type = "alternative"
            self.lineEdit_2.setEnabled(False)
            self.spinBox_4.setEnabled(True)
            self.pushButton_2.setEnabled(True)
        self.check_if_name_exist()
        self.check_entries()

    def generate_form_widgets(self):
        if self.form_type == "alternative":
            layout = self.scrollAreaWidgetContents.layout()
            self.scrollAreaWidgetContents.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
            
            self.saved_forms = self._generate_input_widgets(
                layout,
                self.spinBox_3.value(),
                "Form",
                self.saved_forms
            )
            
            # Connect signals after generation
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    line_edit = row.findChild(QLineEdit)
                    if line_edit:
                        line_edit.textChanged.connect(self.check_entries)
                
            scrollbar = self.scrollArea.verticalScrollBar()
            scrollbar.setValue(scrollbar.maximum())
            self.spinBox_4.setRange(1, self.spinBox_3.value())
            
    def checkbox_toggle(self):
        self.with_repetition = self.checkBox.isChecked()
        if not self.with_repetition:
            if self.spinBox_3.value() < self.spinBox_2.value():
                self.label_8.show()
                self.repetition_valid = False
            else:
                self.label_8.hide()
                self.repetition_valid = True
        else:
            self.label_8.hide()
            self.repetition_valid = True

    def check_if_same_property_name_exist(self):
        self.comboBox.clear()
        self.properties_name.clear()
        self.properties_names_ids.clear()
        layout = self.scrollAreaWidgetContents_2.layout()
        total_forms = layout.count()
        
        for i in range(total_forms):
            widget = layout.itemAt(i).widget()
            if widget:
                line_edit = widget.findChild(QLineEdit).text().strip()
                if line_edit:
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
                self.model.appendRow(QStandardItem(f" Property {j + 1}"))  # Indent for clarity
                self.properties_names_ids[f" Property {j + 1}"] = j
        
        if self.comboBox.count() > 0:
            self.frame_10.show()
            self.check_properties_name = False
        else:
            all_filled = all(
                layout.itemAt(i).widget().findChild(QLineEdit).text().strip() 
                for i in range(layout.count())
            )
            if all_filled:
                self.frame_10.hide()
                self.check_properties_name = True
            else:
                self.frame_10.hide()
                self.check_properties_name = False
                
    def go_to_property_name_error(self):
        current_text = self.comboBox.currentText()
        if current_text not in self.properties_names_ids:
            return
            
        index = self.properties_names_ids[current_text]
        layout = self.scrollAreaWidgetContents_2.layout()
        target_widget = layout.itemAt(index).widget()
        if target_widget:
            self.scrollArea_2.ensureWidgetVisible(target_widget)
            self.highlight_temporarily(target_widget, duration=self.HIGHLIGHT_DURATION)
        else:
            QMessageBox.warning(self, "Navigation Error", "Property not found")

    def check_entries(self):
        self.check_if_same_property_name_exist()
        self.checkbox_toggle()
        
        if self.form_type == "default":
            self.pushButton_6.setEnabled(
                self.is_name_valid and 
                self.check_properties_name and
                self.repetition_valid
            )
        elif self.form_type == "alternative_base":
            is_alt_base = bool(self.lineEdit_2.text().strip())
            self.pushButton_6.setEnabled(
                self.is_name_valid and 
                is_alt_base and 
                self.check_properties_name and
                self.repetition_valid
            )
        elif self.form_type == "alternative":
            layout = self.scrollAreaWidgetContents.layout()
            # Check ALL forms are filled
            all_forms_filled = all(
                layout.itemAt(i).widget().findChild(QLineEdit).text().strip()
                for i in range(layout.count())
            )
            self.pushButton_6.setEnabled(
                self.is_name_valid and 
                all_forms_filled and 
                self.check_properties_name and
                self.repetition_valid
            )
    
    def get_config_data(self) -> dict:
        self.config_data["object_name"] = self.lineEdit.text().strip()
        self.config_data["nOt"] = self.spinBox_2.value()
        self.config_data["nOf"] = self.spinBox_3.value()
        self.config_data["form_type"] = self.form_type
        self.config_data["gtfnum"] = self.spinBox_4.value()
        self.config_data["gtpro"] = self.spinBox.value()
        self.config_data["prev_form_type"] = self.previous_form_type
        self.config_data["repetition?"] = self.with_repetition
        self.config_data["form"] = self.lineEdit_2.text().strip()
        self.config_data["repetition_valid"] = self.repetition_valid
        
        layout = self.scrollAreaWidgetContents.layout()
        self.saved_forms = []
        for i in range(layout.count()):
            row = layout.itemAt(i).widget()
            if row:
                line_edit = row.findChild(QLineEdit)
                if line_edit:
                    self.saved_forms.append(line_edit.text())
                else:
                    self.saved_forms.append("")
        
        layout = self.scrollAreaWidgetContents_2.layout()
        self.saved_properties = []
        for i in range(layout.count()):
            row = layout.itemAt(i).widget()
            if row:
                line_edit = row.findChild(QLineEdit)
                if line_edit:
                    self.saved_properties.append(line_edit.text())
                else:
                    self.saved_properties.append("")
        
        self.config_data["forms"] = self.saved_forms
        self.config_data["properties"] = self.saved_properties
        return self.config_data
    
    def save_config(self):
        if self.cipher is None:
            QMessageBox.warning(self, "Error", "Encryption not initialized")
            return
            
        self.config_data = self.get_config_data()
        if not self.config_data:
            QMessageBox.warning(self, "Error", "An unknown problem occurred")
            return
            
        if not self.current_file:
            self.save_as_config()
            return
        
        reply = QMessageBox.question(
            self, 
            "Replace File", 
            f"Do you want to replace {self.current_file}?", 
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            try:
                json_data = json.dumps(self.config_data).encode()
                encrypted_data = self.cipher.encrypt(json_data)
                with open(self.current_file, 'wb') as f:
                    f.write(encrypted_data)
                self.label_9.setText(f"Object creation session data saved to {self.current_file}")
                self.label_9.show()
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to save file: {str(e)}")
        elif reply == QMessageBox.No:
            self.save_as_config()
        
    def save_as_config(self):
        if self.cipher is None:
            QMessageBox.warning(self, "Error", "Encryption not initialized")
            return
            
        self.config_data = self.get_config_data()
        if not self.config_data:
            QMessageBox.warning(self, "Error", "An unknown problem occurred")
            return
        
        try:
            json_data = json.dumps(self.config_data).encode()
            encrypted_data = self.cipher.encrypt(json_data)
            
            file_name, _ = QFileDialog.getSaveFileName(
                self, 
                "Save As", 
                str(self.documents_dir / f"untitled{self.untitled_x}.ocs"), 
                "Object Creation Session Files (*.ocs)"
            )
            
            if not file_name:
                return
                
            self.untitled_x += 1
            if not file_name.endswith(".ocs"):
                file_name += ".ocs"
                    
            with open(file_name, 'wb') as f:
                self.current_file = file_name
                self.pushButton_3.setToolTip(f"Save to file {self.current_file}")
                f.write(encrypted_data)
                self.label_9.setText(f"Object creation session data saved to {self.current_file}")
                self.label_9.show()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to save file: {str(e)}")
            
    def load_config_dialog(self):
        if self.cipher is None:
            QMessageBox.warning(self, "Error", "Encryption not initialized")
            return
            
        file_name, _ = QFileDialog.getOpenFileName(
            self, 
            "Load object creation session", 
            str(self.documents_dir / "untitled.ocs"), 
            "Object Creation Session Files (*.ocs)"
        )
        
        if not file_name:
            return
            
        try:
            with open(file_name, "rb") as f:
                encrypted_data = f.read()
                
            decrypted_data = self.cipher.decrypt(encrypted_data)
            data = json.loads(decrypted_data.decode())
            
            # Validate data structure
            required_keys = [
                "object_id", "object_name", "nOt", "nOf", 
                "form_type", "properties", "forms",
                "prev_form_type", "repetition?"
            ]
            if not all(key in data for key in required_keys):
                raise ValueError("Invalid file format - missing required keys")
            
            self.load_config(data)
            self.current_file = file_name
            self.pushButton_3.setToolTip(f"Save to file {self.current_file}")
            self.label_9.setText(f"Object creation session {Path(self.current_file).name} loaded")
            self.label_9.show()
            
        except json.JSONDecodeError:
            QMessageBox.warning(self, "Error", "File is corrupted or invalid JSON format")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to load file: {str(e)}")

    def load_config(self, config_data):
        if config_data["object_id"] != "01":
            QMessageBox.warning(
                self, 
                "Error", 
                f"The object type of the loaded file has id {config_data['object_id']} "
                f"which doesn't correspond to the id of the present object creation\n\n"
                f"Search for the id {config_data['object_id']} in the search bar and load this file into it"
            )
            return
        
        # Block all signals during loading to prevent premature updates
        self.lineEdit.blockSignals(True)
        self.spinBox_2.blockSignals(True)
        self.spinBox_3.blockSignals(True)
        self.spinBox_4.blockSignals(True)
        self.spinBox.blockSignals(True)
        self.lineEdit_2.blockSignals(True)
        self.radioButton.blockSignals(True)
        self.radioButton_2.blockSignals(True)
        self.radioButton_3.blockSignals(True)
        self.checkBox.blockSignals(True)
        
        try:
            # Store the data FIRST
            self.saved_forms = config_data["forms"]
            self.saved_properties = config_data["properties"]
            self.form_type = config_data["form_type"]
            self.previous_form_type = config_data["prev_form_type"]
            self.with_repetition = config_data["repetition?"]
            self.previous_number_of_forms = config_data["nOf"]
            self.repetition_valid = config_data["repetition_valid"]
            
            # Set basic fields
            self.lineEdit.setText(config_data["object_name"])
            self.lineEdit_2.setText(config_data["form"])
            
            # Set spin boxes
            self.spinBox_2.setValue(config_data["nOt"])
            self.spinBox_3.setValue(config_data["nOf"])
            self.spinBox_4.setValue(config_data["gtfnum"])
            self.spinBox.setValue(config_data["gtpro"])
            
            # Set form type radio buttons
            if config_data["form_type"] == "default":
                self.radioButton.setChecked(True)
            elif config_data["form_type"] == "alternative_base":
                self.radioButton_2.setChecked(True)
            elif config_data["form_type"] == "alternative":
                self.radioButton_3.setChecked(True)
            
            # Set checkbox
            self.checkBox.setChecked(config_data["repetition?"])
            
        finally:
            # Unblock all signals
            self.lineEdit.blockSignals(False)
            self.spinBox_2.blockSignals(False)
            self.spinBox_3.blockSignals(False)
            self.spinBox_4.blockSignals(False)
            self.spinBox.blockSignals(False)
            self.lineEdit_2.blockSignals(False)
            self.radioButton.blockSignals(False)
            self.radioButton_2.blockSignals(False)
            self.radioButton_3.blockSignals(False)
            self.checkBox.blockSignals(False)
        
        # Manually generate and populate property widgets
        layout = self.scrollAreaWidgetContents_2.layout()
        self.scrollAreaWidgetContents_2.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # Clear existing widgets
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
        # Generate property widgets with loaded data
        for i in range(config_data["nOt"]):
            row_widget = QWidget()
            row_layout = QHBoxLayout(row_widget)
            
            label = QLabel(f"Property {i + 1}")
            line_edit = QLineEdit()
            
            # Set the loaded text
            if i < len(self.saved_properties):
                line_edit.setText(self.saved_properties[i])
            
            row_layout.addWidget(label)
            row_layout.addWidget(line_edit)
            layout.addWidget(row_widget)
            
            # Connect signals
            line_edit.textChanged.connect(self.check_entries)
            line_edit.textChanged.connect(self.check_if_same_property_name_exist)
        
        scrollbar = self.scrollArea_2.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
        
        # Now set the go to property spinbox range and value
        self.spinBox.setRange(1, self.spinBox_2.value())
        self.spinBox.setValue(config_data["gtpro"])
        
        # Generate and populate forms based on form_type
        self.forms_type_radio_btn_clicked()
        
        # Set the go to form spinbox value
        self.spinBox_4.setValue(config_data["gtfnum"])
        
        # Final validation checks
        
        self.check_if_name_exist()
        self.check_entries()
        
    def create_object(self):
        name = self.lineEdit.text().strip()
        number_of_forms = self.spinBox_3.value()
        number_of_properties = self.spinBox_2.value()
        forms = []
        properties = []
        
        if self.form_type == "default":
            for i in range(number_of_forms):
                forms.append(symbols.get_symbol(i))
        elif self.form_type == "alternative_base":
            word = self.lineEdit_2.text().strip()
            for i in range(number_of_forms):
                frm = f"{word}{i + 1}"
                forms.append(frm)
        elif self.form_type == "alternative":
            layout = self.scrollAreaWidgetContents.layout()
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    line_edit = row.findChild(QLineEdit)
                    if line_edit:  # else part could have been considered, but it was not considered because, generally before this function is accessed by the user all fields must be filled
                        forms.append(line_edit.text().strip())

        layout = self.scrollAreaWidgetContents_2.layout()
        for i in range(layout.count()):
            row = layout.itemAt(i).widget()
            if row:
                line_edit = row.findChild(QLineEdit)
                if line_edit:  # else part could have been considered, but it was not considered because, generally before this function is accessed by the user all fields must be filled
                    property_dict = {}
                    property_dict["name"] = line_edit.text().strip()
                    property_dict["forms"] = forms  # This is for the case of this object type
                    properties.append(property_dict)
        
        obj = Id01(name, number_of_forms, number_of_properties, properties, forms, self.with_repetition)
        Entity.add_entity(Entity, name, "object", obj)
        print(obj.system)
        self.label_9.setText(f"Object '{name.strip()}' created")
        self.label_9.show()
        self.lineEdit.clear()
        self.pushButton_6.setEnabled(False)
