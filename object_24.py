from PySide6.QtWidgets import QMessageBox, QApplication, QFileDialog, QWidget, QButtonGroup, QHBoxLayout, QLabel, QLineEdit
from PySide6.QtCore import Qt, Signal, QTimer, QStandardPaths
from pathlib import Path
import json
from cryptography.fernet import Fernet
from object_24_ui import Ui_Dialog
from objects import Id24
from object_manager import ObjectsManager
from entities import EntityManager

class Object_24(QWidget, Ui_Dialog):
    cancel_clicked = Signal()
    direction_matters = True
    reflection_identical = True
    check_forms = False
    is_name_valid = False
    ENCRYPTION_KEY = 'Rll0H4fZf5TvH1E-mk0qwcZ1cETu6jlA_2PiwZ9cvls='
    cipher = Fernet(ENCRYPTION_KEY)
    documents = Path(QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation))
    m_app_folder = documents / "M App" / "Objects 24"
    m_app_folder.mkdir(parents=True, exist_ok=True)
    documents_dir = m_app_folder
    untitled_x = 1 # Use to name the untitled files of the Save As Window
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.spin_box_3.setRange(1, 1000)
        self.spin_box_3.setValue(1)
        self.spinBox.setRange(1, 1000)
        self.spinBox.setValue(1)
        self.label_5.hide()
        self.label_7.hide()
        self.pushButton.setChecked(False)
        
        self.pushButton_2.clicked.connect(self.cancel_clicked.emit)
        
        self.lineEdit_3.textChanged.connect(self.check_if_name_exist)
        
        self.spin_box_3.valueChanged.connect(self.generate_item_widgets)
        self.generate_item_widgets()
        
        self.pushButton_3.clicked.connect(self.go_to_item)
        
        direction = QButtonGroup(self)
        self.radioButton.setChecked(True)
        direction.addButton(self.radioButton)
        direction.addButton(self.radioButton_2)
        direction.buttonClicked.connect(self.update_direction)
        self.update_direction()
        
        reflection = QButtonGroup(self)
        self.radioButton_3.setChecked(True)
        reflection.addButton(self.radioButton_3)
        reflection.addButton(self.radioButton_7)
        reflection.buttonClicked.connect(self.update_reflection)
        self.update_reflection()
        
        self.lineEdit_3.textChanged.connect(self.check_entries)
        self.spin_box_3.valueChanged.connect(self.check_entries)
        self.check_entries()
        
        self.pushButton_4.setToolTip(f"Save this object creation session")
        self.pushButton_5.setToolTip("Save this object creation session")
        self.pushButton_6.setToolTip("Load object creation session with object id '24'")
        
        self.config_data = {"object_id": "24", "object_name": str, "nOt": int, "items": list, "gtform": int, "direction_matters": bool, "reflection_identical": bool}
        
        self.pushButton_4.clicked.connect(self.save_config)
        self.pushButton_5.clicked.connect(self.save_as_config)
        self.pushButton_6.clicked.connect(self.load_config_dialog)
        
        self.current_file = None
        
        self.pushButton.clicked.connect(self.create_object)
        
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
            
    def generate_item_widgets(self):
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

        for i in range(self.spin_box_3.value()):
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
        
    def go_to_item(self) -> None:
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
        layout = self.widget.layout()
        self.check_forms = all(
            layout.itemAt(i).widget().findChild(QLineEdit).text().strip()
            for i in range(layout.count())
            if layout.itemAt(i).widget()
        )
        self.pushButton.setEnabled(self.is_name_valid and self.check_forms)
    
    def update_direction(self):
        if self.radioButton.isChecked():
            self.direction_matters = True
        elif self.radioButton_2.isChecked():
            self.direction_matters = False
            
    def update_reflection(self):
        if self.radioButton_3.isChecked():
            self.reflection_identical = True
        elif self.radioButton_7.isChecked():
            self.reflection_identical = False
        #print(self.reflection_identical)
            
    def get_config_data(self) -> dict:
        self.config_data["object_name"] = self.lineEdit_3.text().strip()
        self.config_data["nOt"] = self.spin_box_3.value()
        self.config_data["gtform"] = self.spinBox.value()
        self.config_data["direction_matters"] = self.direction_matters
        self.config_data["reflection_identical"] = self.reflection_identical
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
                self.label_7.setText(f"Object creation session data saved to {self.current_file}")
                self.label_7.show()
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
            if config_data["object_id"] == "24":
                self.lineEdit_3.setText(config_data["object_name"])
                self.spin_box_3.setValue(config_data["nOt"])
                self.spinBox.setValue(config_data["gtform"])
                self.direction_matters = config_data["direction_matters"]
                self.reflection_identical = config_data["reflection_identical"]
                
                if self.direction_matters == True:
                    self.radioButton.setChecked(True)
                elif self.direction_matters == False:
                    self.radioButton_2.setChecked(True)
                    
                if self.reflection_identical == True:
                    self.radioButton_3.setChecked(True)
                elif self.reflection_identical == False:
                    self.radioButton_7.setChecked(True)
                layout = self.widget.layout()
                self.widget.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.deleteLater()
                self.saved_data = config_data["items"]
                for i in range(config_data["nOt"]):
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
            else:
                QMessageBox.warning(self, "Error", f"The object type of the loaded file has id {config_data["object_id"]} which doesn't correspond to the id of the present object creation\n\nSearch for the id {config_data["object_id"]} in the search bar and load this file into it")
            self.check_entries()
            
    def create_object(self) -> None:
        name = self.lineEdit_3.text().strip()
        number_of_times = self.spin_box_3.value()
        direction_matters = self.direction_matters
        reflection_identical = self.reflection_identical
        forms = []
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
                obj = Id24(name, number_of_times, forms, direction_matters, reflection_identical)
                ObjectsManager.add(ObjectsManager, obj)
                print(obj.number_system)
                self.label_7.setText(f"Object '{name.strip()}' created")
                self.label_7.show()
                self.lineEdit_3.clear()
                self.pushButton.setEnabled(False)
            if ret == QMessageBox.Cancel:
                self.lineEdit_3.clear()
                self.pushButton.setEnabled(False)
        else:
            obj = Id24(name, number_of_times, forms, direction_matters, reflection_identical)
            ObjectsManager.add(ObjectsManager, obj)
            print(obj.number_system)
            print(obj.number_of_elements)
            self.label_7.setText(f"Object '{name.strip()}' created")
            self.label_7.show()
            self.lineEdit_3.clear()
            self.pushButton.setEnabled(False)
        print(EntityManager._items)
        self.pushButton.setEnabled(False)