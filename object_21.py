from PySide6.QtWidgets import QMessageBox, QFileDialog, QWidget
from PySide6.QtCore import Signal, QStandardPaths
from pathlib import Path
import json
from cryptography.fernet import Fernet
from object_21_ui import Ui_Dialog
from objects import Id21
from object_manager import ObjectsManager
from entities import EntityManager
import symbols

class Object_21(QWidget, Ui_Dialog):
    cancel_clicked = Signal()
    is_name_valid = False
    is_num_of_items_to_be_selected_valid = False
    ENCRYPTION_KEY = 'Rll0H4fZf5TvH1E-mk0qwcZ1cETu6jlA_2PiwZ9cvls='
    cipher = Fernet(ENCRYPTION_KEY)
    documents = Path(QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation))
    m_app_folder = documents / "M App" / "Objects 21"
    m_app_folder.mkdir(parents=True, exist_ok=True)
    documents_dir = m_app_folder
    untitled_x = 1 # Use to name the untitled files of the Save As Window
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.spin_box.setRange(1, 1000)
        self.spin_box.setValue(1)
        self.spin_box_2.setRange(1, 1000)
        self.spin_box_2.setValue(1)
        self.label_5.hide()
        self.label_3.hide()
        self.label.hide()
        self.pushButton.setEnabled(False)
        
        self.pushButton_2.clicked.connect(self.cancel_clicked.emit)
        
        self.lineEdit_3.textChanged.connect(self.check_if_name_exist)
        
        self.lineEdit_3.textChanged.connect(self.check_entries)
        self.spin_box.valueChanged.connect(self.check_entries)
        self.spin_box_2.valueChanged.connect(self.check_entries)
        
        self.pushButton_4.setToolTip(f"Save this object creation session")
        self.pushButton_5.setToolTip("Save this object creation session")
        self.pushButton_6.setToolTip("Load object creation session with object id '21'")
        
        self.config_data = {"object_id": "21", "object_name": str, "nOf": int, "numits": int}
        
        self.pushButton_4.clicked.connect(self.save_config)
        self.pushButton_5.clicked.connect(self.save_as_config)
        self.pushButton_6.clicked.connect(self.load_config_dialog)
        
        self.current_file = None
        
        self.pushButton.clicked.connect(self.create_object)
        
        self.spin_box.valueChanged.connect(self.check_num_of_items_to_be_selected)
        self.spin_box_2.valueChanged.connect(self.check_num_of_items_to_be_selected)
        
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
            
    def check_entries(self):
        #print("check_entries functions is called successful") # Good everywhere
        self.check_if_name_exist()
        self.check_num_of_items_to_be_selected()
        self.pushButton.setEnabled(self.is_name_valid and self.is_num_of_items_to_be_selected_valid)
        
    def get_config_data(self) -> dict:
        self.config_data["object_name"] = self.lineEdit_3.text().strip()
        self.config_data["nOf"] = self.spin_box.value()
        self.config_data["numits"] = self.spin_box_2.value()
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
                self.label_3.setText(f"Object creation session data saved to {self.current_file}")
                self.label_3.show()
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
            self.label_3.setText(f"Object creation session data saved to {self.current_file}")
            self.label_3.show()
            
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
            self.label_3.setText(f"Object creation session {self.current_file} loaded")
            self.label_3.show()
        else:
            return
        if not isinstance(file_name, str):
            QMessageBox.warning(self, "Error", "Invalid file")
            return

    def load_config(self, config_data):
            if config_data["object_id"] == "21":
                self.lineEdit_3.setText(config_data["object_name"])
                self.spin_box.setValue(config_data["nOf"])
                self.spin_box_2.setValue(config_data["numits"])
            else:
                QMessageBox.warning(self, "Error", f"The object type of the loaded file has id {config_data["object_id"]} which doesn't correspond to the id of the present object creation\n\nSearch for the id {config_data["object_id"]} in the search bar and load this file into it")
            self.check_entries()
            
    def create_object(self) -> None:
        name = self.lineEdit_3.text().strip()
        number_of_forms = self.spin_box.value()
        r = self.spin_box_2.value()
        forms = []
        for i in range(number_of_forms):
            forms.append(i + 1)
            
        if EntityManager.name_exists_with_different_type(EntityManager, name, "object") == True:
            ret = QMessageBox.warning(self, "Warning", "An object with the same name already exists", QMessageBox.Ok | QMessageBox.Cancel)
            if ret == QMessageBox.Ok:
                obj = obj = Id21(name, number_of_forms, r, forms)
                ObjectsManager.add(ObjectsManager, obj)
                print(obj.number_system)
                self.label_3.setText(f"Object '{name.strip()}' created")
                self.label_3.show()
                self.lineEdit_3.clear()
                self.pushButton.setEnabled(False)
            if ret == QMessageBox.Cancel:
                self.lineEdit_3.clear()
                self.pushButton.setEnabled(False)
        else:
            obj = Id21(name, number_of_forms, r, forms)
            ObjectsManager.add(ObjectsManager, obj)
            print(obj.number_system)
            print(obj.number_of_elements)
            self.label_3.setText(f"Object '{name.strip()}' created")
            self.label_3.show()
            self.lineEdit_3.clear()
            self.pushButton.setEnabled(False)
        print(EntityManager._items)
        self.pushButton.setEnabled(False)
        
    def check_num_of_items_to_be_selected(self):
        if self.spin_box_2.value() > self.spin_box.value():
            self.label.setText("❌ Number of items to select can be greater than the number of items")
            self.label.show()
            self.is_num_of_items_to_be_selected_valid = False
        else:
            self.label.hide()
            self.is_num_of_items_to_be_selected_valid = True