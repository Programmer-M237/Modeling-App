from PySide6.QtWidgets import QFileDialog, QWidget, QMessageBox, QCheckBox, QButtonGroup, QVBoxLayout
from PySide6.QtCore import Qt, Signal, QStandardPaths
from pathlib import Path
import json
from cryptography.fernet import Fernet
from object_14_ui import Ui_Dialog
from objects import Id14
from object_manager import ObjectsManager
from entities import EntityManager
from collections import defaultdict

class Object_14(QWidget, Ui_Dialog):
    cancel_clicked = Signal()
    is_denom_chkbox_valid = False
    is_name_valid = False
    combobox_current_selection = "CFA francs"
    denominations = defaultdict(bool)
    denominations_check_boxes = QButtonGroup()
    denominations_info = defaultdict(lambda: defaultdict(bool))
    previous_currentText = ""
    ENCRYPTION_KEY = 'Rll0H4fZf5TvH1E-mk0qwcZ1cETu6jlA_2PiwZ9cvls='
    cipher = Fernet(ENCRYPTION_KEY)
    documents = Path(QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation))
    m_app_folder = documents / "M App" / "Objects 14"
    m_app_folder.mkdir(parents=True, exist_ok=True)
    documents_dir = m_app_folder
    untitled_x = 1 # Use to name the untitled files of the Save As Window
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_5.hide()
        self.label_9.hide()
        self.label_3.hide()
        self.spinBox_3.setRange(0, 1000000000)
        self.spinBox_3.setValue(0)
        self.pushButton.setEnabled(False)
        
        self.pushButton_2.clicked.connect(self.cancel_clicked.emit)
        
        self.lineEdit_3.textChanged.connect(self.check_if_name_exist)
        
        # Adding currencies to combobox
        self.combobox_items = ["US Dollar", "CFA francs", "Euro", "British Pounds", "Japanese Yen"]
        self.combobox_items = sorted(self.combobox_items)
        #print(self.combobox_items)
        self.comboBox.addItems(self.combobox_items)
        self.comboBox.setCurrentText("British Pounds")
        self.comboBox.currentTextChanged.connect(self.combo_value_changed)
        
        self.pushButton_4.setToolTip(f"Save this object creation session")
        self.pushButton_5.setToolTip("Save this object creation session")
        self.pushButton_6.setToolTip("Load object creation session with object id '01'")
        
        self.config_data = {"object_id": "14", "object_name": str, "currency": str, "amount": int, "denominations_info": defaultdict(lambda: defaultdict(bool)), "previous_currency": str, "next_currency": str}
        
        self.pushButton_4.clicked.connect(self.save_config)
        self.pushButton_5.clicked.connect(self.save_as_config)
        self.pushButton_6.clicked.connect(self.load_config_dialog)
        
        self.current_file = None
        
        self.pushButton.clicked.connect(self.create_object)
        
        self.denominations_info = {
            "US Dollar": {100: False, 50: False, 20: False, 10: False, 5: False, 1: False, 0.25: False, 0.1: False, 0.05: False, 0.01: False},
            "CFA francs": {10000: False, 5000: False, 2000: False, 1000: False, 500: False, 200: False, 100: False, 50: False, 25: False},
            "Euro" : {500: False, 200: False, 100: False, 50: False, 20: False, 10: False, 5: False, 2: False, 1: False, 0.50: False, 0.20: False, 0.10: False, 0.05: False, 0.02: False, 0.01: False},
            "British Pounds": {50: False, 20: False, 10: False, 5: False, 2: False, 1: False, 0.50: False, 0.20: False, 0.10: False, 0.05: False, 0.02: False, 0.01: False},
            "Japanese Yen": {10000: False, 5000: False, 2000: False, 1000: False, 500: False, 100: False, 50: False, 10: False, 5: False, 1: False}
        }
        
        self.initial_generate_check_boxes_denominations()
        
        self.comboBox.currentTextChanged.connect(self.generate_check_boxes_denominations)
        
        self.lineEdit_3.textChanged.connect(self.check_entries)
        self.denominations_check_boxes.buttonClicked.connect(self.check_entries)
        
    def check_if_name_exist(self) -> None:
        name = self.lineEdit_3.text().strip()
        
        if not(name):
            self.pushButton.setEnabled(False)
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
            
    def combo_value_changed(self):
        self.combobox_current_selection = self.comboBox.currentText()
        #print(self.combobox_current_selection)
        
    def get_config_data(self) -> dict:
        self.config_data["object_name"] = self.lineEdit_3.text().strip()
        self.config_data["currency"] = self.comboBox.currentText()
        self.config_data["amount"] = self.spinBox_3.value()
        self.config_data["denominations_info"] = self.denominations_info
        self.config_data["previous_currency"] = self.previous_currentText
        self.config_data["next_currency"] = self.comboBox.currentText()
        
        layout = self.widget.layout()
        currency = self.previous_currentText # Previous text of combobox
        ### Stores the data on the UI
        if currency == "CFA francs":
            denominations = self.denominations_info["CFA francs"]
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    check_box = row.findChild(QCheckBox)
                    denominations[list(denominations.keys())[i]] = check_box.isChecked()
            self.denominations_info["CFA francs"] = denominations
        
        if currency == "US Dollar":
            denominations = self.denominations_info["US Dollar"]
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    check_box = row.findChild(QCheckBox)
                    denominations[list(denominations.keys())[i]] = check_box.isChecked()
            self.denominations_info["US Dollar"] = denominations
                
        if currency == "Euro":
            denominations = self.denominations_info["Euro"]
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    check_box = row.findChild(QCheckBox)
                    denominations[list(denominations.keys())[i]] = check_box.isChecked()
            self.denominations_info["Euro"] = denominations
                
        if currency == "British Pounds":
            denominations = self.denominations_info["British Pounds"]
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    check_box = row.findChild(QCheckBox)
                    denominations[list(denominations.keys())[i]] = check_box.isChecked()
            self.denominations_info["British Pounds"] = denominations
        
        if currency == "Japanese Yen":
            denominations = self.denominations_info["Japanese Yen"]
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    check_box = row.findChild(QCheckBox)
                    denominations[list(denominations.keys())[i]] = check_box.isChecked()
            self.denominations_info["Japanese Yen"] = denominations
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
            if config_data["object_id"] == "14":
                self.denominations_info = config_data["denominations_info"]
                print("Loaded config:", config_data)
                self.lineEdit_3.setText(config_data["object_name"])
                self.spinBox_3.setValue(config_data["amount"])
                self.comboBox.setCurrentText(config_data["currency"])
                self.previous_currentText = config_data["previous_currency"]
                self.generate_check_boxes_denominations()
                next_currency = self.comboBox.currentText()
                layout = self.widget.layout()
                
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.deleteLater()
                        
                if next_currency == "CFA francs":
                    denominations = self.denominations_info["CFA francs"]
                    layout = self.widget.layout()
                    layout.setAlignment(Qt.AlignmentFlag.AlignTop)
                    
                    for i in range(len(denominations)):
                        check_box = QCheckBox(f"{str(list(denominations.keys())[i])} CFA frs")
                        check_box.setChecked(denominations[list(denominations.keys())[i]])
                        row_widget = QWidget()
                        row_layout = QVBoxLayout(row_widget)
                        row_layout.addWidget(check_box)
                        layout.addWidget(row_widget)
                
                if next_currency == "US Dollar":
                    denominations = self.denominations_info["US Dollar"]
                    layout = self.widget.layout()
                    layout.setAlignment(Qt.AlignmentFlag.AlignTop)
                    
                    for i in range(len(denominations)):
                        check_box = QCheckBox(f"$ {str(list(denominations.keys())[i])}")
                        #print(denominations[list(denominations.keys())[i]])
                        check_box.setChecked(denominations[list(denominations.keys())[i]])
                        row_widget = QWidget()
                        row_layout = QVBoxLayout(row_widget)
                        row_layout.addWidget(check_box)
                        layout.addWidget(row_widget)
                        
                if next_currency == "Euro":
                    denominations = self.denominations_info["Euro"]
                    #print("Loaded config:", config_data)
                    layout = self.widget.layout()
                    layout.setAlignment(Qt.AlignmentFlag.AlignTop)
                    
                    for i in range(len(denominations)):
                        check_box = QCheckBox(f"€ {str(list(denominations.keys())[i])}")
                        check_box.setChecked(denominations[list(denominations.keys())[i]])
                        row_widget = QWidget()
                        row_layout = QVBoxLayout(row_widget)
                        row_layout.addWidget(check_box)
                        layout.addWidget(row_widget)
                        
                if next_currency == "British Pounds":
                    denominations = self.denominations_info["British Pounds"]
                    layout = self.widget.layout()
                    layout.setAlignment(Qt.AlignmentFlag.AlignTop)
                    
                    for i in range(len(denominations)):
                        check_box = QCheckBox(f"£ {str(list(denominations.keys())[i])}")
                        check_box.setChecked(denominations[list(denominations.keys())[i]])
                        row_widget = QWidget()
                        row_layout = QVBoxLayout(row_widget)
                        row_layout.addWidget(check_box)
                        layout.addWidget(row_widget)
                
                if next_currency == "Japanese Yen":
                    denominations = self.denominations_info["Japanese Yen"]
                    layout = self.widget.layout()
                    layout.setAlignment(Qt.AlignmentFlag.AlignTop)
                    
                    for i in range(len(denominations)):
                        check_box = QCheckBox(f"¥ {str(list(denominations.keys())[i])}")
                        check_box.setChecked(denominations[list(denominations.keys())[i]])
                        row_widget = QWidget()
                        row_layout = QVBoxLayout(row_widget)
                        row_layout.addWidget(check_box)
                        layout.addWidget(row_widget)
                
    def create_object(self) -> None:
        name = self.lineEdit_3.text().strip()
        amount = self.spinBox_3.value()
        currency = self.comboBox.currentText()
        denominations = []
        
        for i in self.denominations_info[currency].keys():
            bool_val = self.denominations_info[currency][i]
            if bool_val:
                denominations.append(float(i))
        print(denominations)

        if EntityManager.name_exists_with_different_type(EntityManager, name, "object") == True:
                ret = QMessageBox.warning(self, "Warning", "An object with the same name already exists", QMessageBox.Ok | QMessageBox.Cancel)
                if ret == QMessageBox.Ok:
                    obj = Id14(name, currency, amount, denominations)
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
            obj = Id14(name, currency, amount, denominations)
            ObjectsManager.add(ObjectsManager, obj)
            print(obj.number_system)
            self.label_3.setText(f"Object '{name.strip()}' created")
            self.label_3.show()
            self.lineEdit_3.clear()
            self.pushButton.setEnabled(False)
        print(EntityManager._items)
        self.pushButton.setEnabled(False)
        
    # def switch_to_valid_denominations(self):
        #if self.comboBox.
        
    def initial_generate_check_boxes_denominations(self):
        currency = self.comboBox.currentText()
        if currency == "CFA francs":
            denominations = self.denominations_info["CFA francs"]
            layout = self.widget.layout()
            layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            
            for i in denominations.keys():
                check_box = QCheckBox(f"{str(i)} CFA frs")
                row_widget = QWidget()
                row_layout = QVBoxLayout(row_widget)
                row_layout.addWidget(check_box)
                layout.addWidget(row_widget)
        
        if currency == "US Dollar":
            denominations = self.denominations_info["US Dollar"]
            layout = self.widget.layout()
            layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            
            for i in denominations.keys():
                check_box = QCheckBox(f"$ {str(i)}")
                row_widget = QWidget()
                row_layout = QVBoxLayout(row_widget)
                row_layout.addWidget(check_box)
                layout.addWidget(row_widget)
                
        if currency == "Euro":
            denominations = self.denominations_info["Euro"]
            layout = self.widget.layout()
            layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            
            for i in denominations.keys():
                check_box = QCheckBox(f"€ {str(i)}")
                row_widget = QWidget()
                row_layout = QVBoxLayout(row_widget)
                row_layout.addWidget(check_box)
                layout.addWidget(row_widget)
                
        if currency == "British Pounds":
            denominations = self.denominations_info["British Pounds"]
            layout = self.widget.layout()
            layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            
            for i in denominations.keys():
                check_box = QCheckBox(f"£ {str(i)}")
                row_widget = QWidget()
                row_layout = QVBoxLayout(row_widget)
                row_layout.addWidget(check_box)
                layout.addWidget(row_widget)
        
        if currency == "Japanese Yen":
            denominations = self.denominations_info["Japanese Yen"]
            layout = self.widget.layout()
            layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            
            for i in denominations.keys():
                check_box = QCheckBox(f"¥ {str(i)}")
                row_widget = QWidget()
                row_layout = QVBoxLayout(row_widget)
                row_layout.addWidget(check_box)
                layout.addWidget(row_widget)
                
        self.setup_btn_group()
        
        self.previous_currentText = self.comboBox.currentText() # Store the previous currency chosen
                
    def setup_btn_group(self):
        self.denominations_check_boxes = QButtonGroup()
        self.denominations_check_boxes.setExclusive(False)
        self.denominations_check_boxes.buttonClicked.connect(self.check_entries)
        layout = self.widget.layout()
        for i in range(layout.count()):
            row = layout.itemAt(i).widget()
            if row:
                check_box = row.findChild(QCheckBox)
                self.denominations_check_boxes.addButton(check_box)
                
    def generate_check_boxes_denominations(self):
        #print("Hello")
        layout = self.widget.layout()
        currency = self.previous_currentText # Previous text of combobox
        next_currency = self.comboBox.currentText() # Current text of combobox
        ### Stores the data on the UI
        if currency == "CFA francs":
            denominations = self.denominations_info["CFA francs"]
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    check_box = row.findChild(QCheckBox)
                    denominations[list(denominations.keys())[i]] = check_box.isChecked()
            self.denominations_info["CFA francs"] = denominations
        
        if currency == "US Dollar":
            denominations = self.denominations_info["US Dollar"]
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    check_box = row.findChild(QCheckBox)
                    denominations[list(denominations.keys())[i]] = check_box.isChecked()
            self.denominations_info["US Dollar"] = denominations
                
        if currency == "Euro":
            denominations = self.denominations_info["Euro"]
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    check_box = row.findChild(QCheckBox)
                    denominations[list(denominations.keys())[i]] = check_box.isChecked()
            self.denominations_info["Euro"] = denominations
                
        if currency == "British Pounds":
            denominations = self.denominations_info["British Pounds"]
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    check_box = row.findChild(QCheckBox)
                    denominations[list(denominations.keys())[i]] = check_box.isChecked()
            self.denominations_info["British Pounds"] = denominations
        
        if currency == "Japanese Yen":
            denominations = self.denominations_info["Japanese Yen"]
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    check_box = row.findChild(QCheckBox)
                    denominations[list(denominations.keys())[i]] = check_box.isChecked()
            self.denominations_info["Japanese Yen"] = denominations
                    
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
                
        if next_currency == "CFA francs":
            denominations = self.denominations_info["CFA francs"]
            layout = self.widget.layout()
            layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            
            for i in range(len(denominations)):
                check_box = QCheckBox(f"{str(list(denominations.keys())[i])} CFA frs")
                check_box.setChecked(denominations[list(denominations.keys())[i]])
                row_widget = QWidget()
                row_layout = QVBoxLayout(row_widget)
                row_layout.addWidget(check_box)
                layout.addWidget(row_widget)
        
        if next_currency == "US Dollar":
            denominations = self.denominations_info["US Dollar"]
            layout = self.widget.layout()
            layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            
            for i in range(len(denominations)):
                check_box = QCheckBox(f"$ {str(list(denominations.keys())[i])}")
                check_box.setChecked(denominations[list(denominations.keys())[i]])
                row_widget = QWidget()
                row_layout = QVBoxLayout(row_widget)
                row_layout.addWidget(check_box)
                layout.addWidget(row_widget)
                
        if next_currency == "Euro":
            denominations = self.denominations_info["Euro"]
            layout = self.widget.layout()
            layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            
            for i in range(len(denominations)):
                check_box = QCheckBox(f"€ {str(list(denominations.keys())[i])}")
                check_box.setChecked(denominations[list(denominations.keys())[i]])
                row_widget = QWidget()
                row_layout = QVBoxLayout(row_widget)
                row_layout.addWidget(check_box)
                layout.addWidget(row_widget)
                
        if next_currency == "British Pounds":
            denominations = self.denominations_info["British Pounds"]
            layout = self.widget.layout()
            layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            
            for i in range(len(denominations)):
                check_box = QCheckBox(f"£ {str(list(denominations.keys())[i])}")
                check_box.setChecked(denominations[list(denominations.keys())[i]])
                row_widget = QWidget()
                row_layout = QVBoxLayout(row_widget)
                row_layout.addWidget(check_box)
                layout.addWidget(row_widget)
        
        if next_currency == "Japanese Yen":
            denominations = self.denominations_info["Japanese Yen"]
            layout = self.widget.layout()
            layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            
            for i in range(len(denominations)):
                check_box = QCheckBox(f"¥ {str(list(denominations.keys())[i])}")
                check_box.setChecked(denominations[list(denominations.keys())[i]])
                row_widget = QWidget()
                row_layout = QVBoxLayout(row_widget)
                row_layout.addWidget(check_box)
                layout.addWidget(row_widget)
                
        self.previous_currentText = next_currency
        
    def check_entries(self):
        layout = self.widget.layout()
        currency = self.previous_currentText # Previous text of combobox
        next_currency = self.comboBox.currentText() # Current text of combobox
        ### Stores the data on the UI
        if currency == "CFA francs":
            denominations = self.denominations_info["CFA francs"]
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    check_box = row.findChild(QCheckBox)
                    denominations[list(denominations.keys())[i]] = check_box.isChecked()
            self.denominations_info["CFA francs"] = denominations
        
        if currency == "US Dollar":
            denominations = self.denominations_info["US Dollar"]
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    check_box = row.findChild(QCheckBox)
                    denominations[list(denominations.keys())[i]] = check_box.isChecked()
            self.denominations_info["US Dollar"] = denominations
                
        if currency == "Euro":
            denominations = self.denominations_info["Euro"]
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    check_box = row.findChild(QCheckBox)
                    denominations[list(denominations.keys())[i]] = check_box.isChecked()
            self.denominations_info["Euro"] = denominations
                
        if currency == "British Pounds":
            denominations = self.denominations_info["British Pounds"]
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    check_box = row.findChild(QCheckBox)
                    denominations[list(denominations.keys())[i]] = check_box.isChecked()
            self.denominations_info["British Pounds"] = denominations
        
        if currency == "Japanese Yen":
            denominations = self.denominations_info["Japanese Yen"]
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    check_box = row.findChild(QCheckBox)
                    denominations[list(denominations.keys())[i]] = check_box.isChecked()
            self.denominations_info["Japanese Yen"] = denominations
            
        #print("Testing")
        denominations = []
        for i in self.denominations_info[currency].keys():
            bool_val = self.denominations_info[currency][i]
            if bool_val:
                #print("This piece of code executes")
                denominations.append(int(i))
        #print(denominations)
        if len(denominations) > 0:
            self.is_denom_chkbox_valid = True
        else:
            self.is_denom_chkbox_valid = False
        #print(f"{self.is_name_valid}|||{self.is_denom_chkbox_valid}")
        self.pushButton.setEnabled(self.is_denom_chkbox_valid and self.is_name_valid)