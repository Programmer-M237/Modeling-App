from PySide6.QtWidgets import QFileDialog, QWidget, QMessageBox, QButtonGroup
from PySide6.QtCore import Signal, QStandardPaths
from pathlib import Path
import json
from cryptography.fernet import Fernet
from object_15_ui import Ui_Dialog
from objects import Id15
from object_manager import ObjectsManager
from entities import EntityManager

class Object_15(QWidget, Ui_Dialog):
    cancel_clicked = Signal()
    sums_type = "Ordered"
    repetition = False
    ENCRYPTION_KEY = 'Rll0H4fZf5TvH1E-mk0qwcZ1cETu6jlA_2PiwZ9cvls='
    cipher = Fernet(ENCRYPTION_KEY)
    documents = Path(QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation))
    m_app_folder = documents / "M App" / "Objects 15"
    m_app_folder.mkdir(parents=True, exist_ok=True)
    documents_dir = m_app_folder
    untitled_x = 1 # Use to name the untitled files of the Save As Window
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.spinBox.setRange(1, 1000)
        self.spinBox.setValue(1)
        self.pushButton.setEnabled(False)
        self.label_5.hide()
        self.label_3.hide()
        
        self.pushButton_2.clicked.connect(self.cancel_clicked.emit)
        
        self.lineEdit_3.textChanged.connect(self.check_if_name_exist)
        
        sums = QButtonGroup(self)
        self.radioButton.setChecked(True)
        sums.addButton(self.radioButton)
        sums.addButton(self.radioButton_2)
        sums.buttonClicked.connect(self.sums_clicked)
        
        self.checkBox_2.setChecked(False)
        self.checkBox_2.clicked.connect(self.repttion_chkbox_clkd)
        
        self.pushButton_4.setToolTip(f"Save this object creation session")
        self.pushButton_5.setToolTip("Save this object creation session")
        self.pushButton_6.setToolTip("Load object creation session with object id '15'")
        
        self.config_data = {"object_id": "15", "object_name": str, "limit_of_sum": int, "sum_type": str, "order_matters": bool, "repetition": bool}
        
        self.pushButton_4.clicked.connect(self.save_config)
        self.pushButton_5.clicked.connect(self.save_as_config)
        self.pushButton_6.clicked.connect(self.load_config_dialog)
        
        self.current_file = None
        
        self.pushButton.clicked.connect(self.create_object)
        
    def check_if_name_exist(self) -> None:
        name = self.lineEdit_3.text().strip()
        
        if not(name):
            self.pushButton.setEnabled(False)
        elif (name, "object") in EntityManager._items:
            self.label_5.setText("❌ An object with the same name already exists")
            self.label_5.show()
            self.pushButton.setEnabled(False)
        elif EntityManager.name_exists_with_different_type(EntityManager, name, "object"):
            self.label_5.setText("⚠️ An event or system with the same name already exists")
            self.label_5.show()
            self.pushButton.setEnabled(True)
        else:
            self.label_5.hide()
            self.pushButton.setEnabled(True)
            
    def sums_clicked(self):
        if self.radioButton_2.isChecked():
            self.sums_type = "Unordered"
        elif self.radioButton.isChecked():
            self.sums_type = "Ordered"
        print(self.sums_type)
            
    def repttion_chkbox_clkd(self):
        if self.checkBox_2.isChecked():
            self.repetition = True
        else:
            self.repetition = False
            
    def get_config_data(self) -> dict:
        self.config_data["object_name"] = self.lineEdit_3.text().strip()
        self.config_data["limit_of_sum"] = self.spinBox.value()
        self.config_data["sum_type"] = self.sums_type
        self.config_data["repetition"] = self.repetition
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
            if config_data["object_id"] == "15":
                self.lineEdit_3.setText(config_data["object_name"])
                self.spinBox.setValue(config_data["limit_of_sum"])
                self.sums_type = config_data["sum_type"]
                self.repetition = config_data["repetition"]
                
                if self.sums_type == "Ordered":
                    self.radioButton.setChecked(True)
                elif self.sums_type == "Unordered":
                    self.radioButton_2.setChecked(True)
        
                self.checkBox_2.setChecked(self.repetition)
                
    def create_object(self) -> None:
        name = self.lineEdit_3.text().strip()
        n = self.spinBox.value()
        sums = self.sums_type
        repetition = self.repetition

        if EntityManager.name_exists_with_different_type(EntityManager, name, "object") == True:
                ret = QMessageBox.warning(self, "Warning", "An object with the same name already exists", QMessageBox.Ok | QMessageBox.Cancel)
                if ret == QMessageBox.Ok:
                    obj = Id15(name, n, sums, repetition)
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
            obj = Id15(name, n, sums, repetition)
            ObjectsManager.add(ObjectsManager, obj)
            print(obj.number_system)
            self.label_3.setText(f"Object '{name.strip()}' created")
            self.label_3.show()
            self.lineEdit_3.clear()
            self.pushButton.setEnabled(False)
        print(EntityManager._items)
        self.pushButton.setEnabled(False)