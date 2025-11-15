from PySide6.QtWidgets import QPushButton, QMessageBox, QFileDialog, QWidget
from PySide6.QtCore import Qt, Signal, QTimer, QStandardPaths
from pathlib import Path
import json
from cryptography.fernet import Fernet
from object_07_ui import Ui_Dialog
from entities import EntityManager
from object_07_group_info_view import Group_data_info
from object_07_property_forms import Properties_forms
from temp_objects import Id07
from temp_events import Events
from step_2_of_event_creation import Event_properties
from data_store import DataStore3

class EObject_07(QWidget):
    cancel_clicked = Signal()
    is_name_valid = True # Problem 001
    is_numits_valid = True
    numits = 1
    is_nop_valid = False
    is_forms_valid = False
    is_numits_valid = False
    saved_data = []
    properties_id_list = {}
    ENCRYPTION_KEY = 'Rll0H4fZf5TvH1E-mk0qwcZ1cETu6jlA_2PiwZ9cvls='
    cipher = Fernet(ENCRYPTION_KEY)
    documents = Path(QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation))
    m_app_folder = documents / "M App" / "Objects 07"
    m_app_folder.mkdir(parents=True, exist_ok=True)
    documents_dir = m_app_folder
    untitled_x = 1 # Use to name the untitled files of the Save As Window
    config_data = {"object_id": "07", "object_name": str, "nOp": int, "properties_data": dict, "gtpnum": int, "numits": int, "order": bool, "repetitions": bool}
    current_file = None
    repetitions = False
    order = False
    close_by_code_initiated = Signal()
    
    def __init__(self, stacked_widget, top_window, event_name):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.name = "page_7"
        self.ui.label_2.hide()
        self.ui.spinBox.setRange(1, 1000)
        self.ui.spinBox.setValue(1)
        self.ui.spinBox_2.setRange(1, 1000)
        self.ui.spinBox_2.setValue(1)
        self.ui.spinBox_3.setRange(1, 1000)
        self.ui.spinBox_3.setValue(1)
        self.ui.label_5.hide()
        self.table_window = None
        self.top_window = top_window
        self.event_name = event_name
        self.stacked_widget = stacked_widget
        self.ui.label_9.setText('<a href="#">Click here to view a summary of the groups information</a>')
        
        self.ui.label_9.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.ui.label_9.setOpenExternalLinks(False)
        self.ui.label_9.linkActivated.connect(self.open_table_window)
        
        #### Problem 001
        self.ui.lineEdit.setText(f"{self.event_name}'s object")
        self.ui.lineEdit.setEnabled(False)
        ####
        
        self.top_window_close_signal = Signal()
        self.stacked_widget_page_change_signal = Signal()
        self.top_window.destroyed.connect(self.close_group_info_window)
        self.stacked_widget.currentChanged.connect(self.close_group_info_window)
        
        self.ui.pushButton_6.clicked.connect(self.cancel_clicked.emit)
        #self.ui.label_6
        
        self.prev_data_store = {}
        
        self.ui.pushButton_2.clicked.connect(self.save_config)
        self.ui.pushButton_3.clicked.connect(self.save_as_config)
        self.ui.pushButton_4.clicked.connect(self.load_config_dialog)
        self.ui.pushButton_5.clicked.connect(self.create_object)
        
        self.ui.label_2.hide()
        self.ui.pushButton_5.setEnabled(False)
        
        self.ui.pushButton_6.clicked.connect(self.cancel_clicked.emit)
        
        #self.ui.lineEdit.textChanged.connect(self.check_if_name_exist) # Problem 001
        self.ui.spinBox.valueChanged.connect(self.generate_property_widgets)
        self.ui.pushButton.clicked.connect(self.go_to_form)
        
        self.initial_generate_property_widgets()
        
        self.ui.frame_7.hide()
        
        self.ui.spinBox.valueChanged.connect(self.check_entries)
        self.ui.spinBox_2.valueChanged.connect(self.check_entries)
        self.ui.lineEdit.textEdited.connect(self.check_entries)
        self.ui.spinBox.valueChanged.connect(self.check_forms)
        self.ui.spinBox_2.valueChanged.connect(self.check_forms)
        self.ui.lineEdit.textEdited.connect(self.check_forms)
        
        self.check_forms()
        self.ui.widget.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        
        self.ui.pushButton_7.clicked.connect(self.go_to_property_error)
        
        self.ui.pushButton_2.setToolTip(f"Save this object creation session")
        self.ui.pushButton_3.setToolTip("Save this object creation session")
        self.ui.pushButton_4.setToolTip("Load object creation session with object id '07'")
        
        self.ui.checkBox_3.stateChanged.connect(self.order_check_box_toggle)
        self.ui.checkBox_4.stateChanged.connect(self.repetitions_check_box_toggle)
        
        self.ui.spinBox_3.valueChanged.connect(self.check_entries)
        self.ui.label_8.hide()
        
    def focusInEvent(self, event):
        self.check_forms()
        self.check_entries()
        super().focusInEvent(event)
    
    def focusOutEvent(self, event):
        self.check_forms()
        self.check_entries()
        super().focusOutEvent(event)
    
    def mousePressEvent(self, event):
        self.check_forms()
        self.check_entries()
        super().mousePressEvent(event)
        
    def keyPressEvent(self, event):
        self.check_forms()
        self.check_entries()
        super().keyPressEvent(event)
        
    def mouseMoveEvent(self, event):
        self.check_forms()
        self.check_entries()
        super().mouseMoveEvent(event)
        
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
            
    def initial_generate_property_widgets(self):
        self.properties_id_list = {}
        layout = self.ui.widget.layout()
        self.ui.widget.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
        for i in range(self.ui.spinBox.value()):
            button = QPushButton(f"Edit group {i + 1}")
            DataStore3.data_store[str(i)] = {"property_name": "", "is_valid": False, "form_type": "default", "prev_form_type": "default", "forms": [], "prev_nof": 1, "go_to_form": 1, "alt_base": "", "nof": 1}
            button.clicked.connect(lambda _, index=i: self.open_data_dialog(index))
            button.clicked.connect(self.check_forms)
            self.properties_id_list[f"Group {i + 1}"] = i + 1
            layout.addWidget(button)
        
    
        scrollbar = self.ui.scrollArea.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
    
    def open_data_dialog(self, index):
        existing = DataStore3.data_store.get(str(index))
        dialog = Properties_forms(index, existing_data=existing, parent=self)
        if dialog.exec():
            DataStore3.data_store[str(index)] = dialog.data
            #print(DataStore3.data_store[str(index)])
            
    def check_forms(self):
        self.ui.comboBox.clear()
        layout = self.ui.widget.layout()
        for i in range(layout.count()):
            if DataStore3.data_store[str(i)].get("is_valid") == True:
                self.is_forms_valid = True
            else:
                self.is_forms_valid = False
                self.ui.comboBox.addItem(f"Property {i + 1}")
                self.ui.frame_7.show()
        if self.is_forms_valid == True:
            self.ui.frame_7.hide()
        self.is_forms_valid = all(DataStore3.data_store[str(i)].get("is_valid", False) for i in range(layout.count()))
        self.check_entries()
        
    def check_entries(self):
        #self.check_if_name_exist()
        self.check_numits()
        if self.ui.spinBox.value():
            self.is_nop_valid = True
        else:
            self.is_nop_valid = False
        self.ui.pushButton_5.setEnabled(self.is_nop_valid and self.is_name_valid and self.is_forms_valid and self.check_numits1)
        
    def generate_property_widgets(self):
        self.properties_id_list = {}
        #print(len(DataStore.data_store))
        for i in range(len(DataStore3.data_store)):
            self.prev_data_store[str(i)] = DataStore3.data_store[str(i)]
            if i > self.ui.spinBox.value():
                del DataStore3.data_store[str(i)]
        DataStore3.data_store.clear()
                
        layout = self.ui.widget.layout()
        self.ui.widget.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
        for i in range(self.ui.spinBox.value()):
            button = QPushButton(f"Edit group {i + 1}")
            if str(i) not in self.prev_data_store.keys():
                self.prev_data_store[str(i)] = {"property_name": "", "form_type": "default", "prev_form_type": "default", "forms": [], "go_to_form": 1, "alt_base": "", "nof": 1}
            DataStore3.data_store[str(i)] = self.prev_data_store[str(i)]
            button.clicked.connect(lambda _, index=i: self.open_data_dialog(index))
            button.clicked.connect(self.check_forms)
            self.properties_id_list[f"Property {i + 1}"] = i + 1
            layout.addWidget(button)
        
        #print(DataStore.data_store)
        self.prev_data_store.clear()
        scrollbar = self.ui.scrollArea.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
        
    def order_check_box_toggle(self, state):
        if state == 2:
            self.order = True
        else:
            self.order = False
    
    def repetitions_check_box_toggle(self, state):
        if state == 2:
            self.repetitions = True
        else:
            self.repetitions = False
    
    def go_to_form(self) -> None:
        index = self.ui.spinBox_2.value()
        layout = self.ui.widget.layout()
        total_properties = layout.count()
        
        if index < 1 or index > total_properties:
            QMessageBox.warning(self, "Navigation Error", "Property not found")
            return
        target_widget = layout.itemAt(index - 1).widget()
        if target_widget:
            self.ui.scrollArea.ensureWidgetVisible(target_widget)
        else:
            QMessageBox.warning(self, "Navigation Error", "Property not found")
        self.highlight_temporarily(layout.itemAt(index - 1).widget(), duration=2000)
        
    def go_to_property_error(self) -> None:
        #print(self.ui.comboBox.currentText())
        index = self.properties_id_list[self.ui.comboBox.currentText()] # They only difference between the two functions
        layout = self.ui.widget.layout()
        total_properties = layout.count()
        
        if index < 1 or index > total_properties:
            QMessageBox.warning(self, "Navigation Error", "Property not found")
            return
        target_widget = layout.itemAt(index - 1).widget()
        if target_widget:
            self.ui.scrollArea.ensureWidgetVisible(target_widget)
        else:
            QMessageBox.warning(self, "Navigation Error", "Property not found")
        self.highlight_temporarily(layout.itemAt(index - 1).widget(), duration=2000)
        
    def highlight_temporarily(self, widget: QWidget, duration: int = 2000):
        widget.setStyleSheet("""
                             QPushButton {
                                 border: 2px solid #00ffff;
                                 border-radius: 6px;
                             }
                             """)
        QTimer.singleShot(2000, lambda: widget.setStyleSheet(""))
    
    def properties_form(self):
        dialog = Properties_forms(self)
        dialog.exec()

    def get_config_data(self) -> dict:
        self.config_data["object_name"] = self.ui.lineEdit.text().strip()
        self.config_data["nOp"] = self.ui.spinBox.value()
        self.config_data["properties_data"] = DataStore3.data_store
        self.config_data["gtpnum"] = self.ui.spinBox_2.value()
        self.config_data["numits"] = self.ui.spinBox_3.value()
        self.config_data["order"] = self.order
        self.config_data["repetitions"] = self.repetitions
        return self.config_data
    
    def save_config(self) -> None:
        #print("Testing")
        self.config_data = self.get_config_data()
        if not self.config_data:
            QMessageBox.warning(self, "Error", "An unknown problem occurred")
            return
        
        if not self.current_file:
            self.save_as_config()
            #print("Hello")
            return
        
        reply = QMessageBox.question(self, "Replace File", f"Do you want to replace {self.current_file}?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            json_data = json.dumps(self.config_data).encode()
            encrypted_data = self.cipher.encrypt(json_data)
            with open(self.current_file, 'wb') as f:
                f.write(encrypted_data)
                self.ui.label_5.setText(f"Object creation session data saved to {self.current_file}")
                self.ui.label_5.show()
                return
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
        
        file_name, _ = QFileDialog.getSaveFileName(self, "Save As", str(self.documents_dir / f"untitled{self.untitled_x}.ocs"), "Object Creation Session Files (*.ocs)")
        self.untitled_x += 1
        if file_name:
            if not file_name.endswith(".ocs"):
                file_name += ".ocs"
                
            with open(file_name, 'wb') as f:
                self.current_file = file_name
                self.ui.pushButton_2.setToolTip(f"Save to file {self.current_file}")
                f.write(encrypted_data)
                self.ui.label_5.setText(f"Object creation session data saved to {self.current_file}")
                self.ui.label_5.show()
            
    def load_config_dialog(self):
        file_name, selectected_filter = QFileDialog.getOpenFileName(self, "Load object creation session", str(self.documents_dir), "Object Creation Session (*.ocs)")
        self.current_file = file_name
        if file_name:
            with open(file_name, 'rb') as f:
                encrypted_data = f.read()
            
            decrypted_data = self.cipher.decrypt(encrypted_data)
            data = json.loads(decrypted_data.decode())
            self.load_config(data)
            self.current_file = file_name
            self.ui.pushButton_2.setToolTip(f"Save to file {self.current_file}")
        else:
            return
        if not isinstance(file_name, str):
            QMessageBox.warning(self, "Error", "Invalid file")
            return
    
    def load_config(self, config_data):
        DataStore3.data_store.clear()
        if config_data["object_id"] == "07":
            DataStore3.data_store = config_data["properties_data"]
            #self.ui.lineEdit.setText(config_data["object_name"]) # Problem 001
            self.ui.spinBox.setValue(config_data["nOp"])
            self.ui.spinBox_2.setValue(config_data["gtpnum"])
            self.ui.spinBox_3.setValue(config_data["numits"])
            self.order = config_data["order"]
            self.repetitions = config_data["repetitions"]
            if self.order == True:
                self.ui.checkBox_3.setChecked(True)
            else:
                self.ui.checkBox_3.setChecked(False)
            if self.repetitions == True:
                self.ui.checkBox_4.setChecked(True)
            else:
                self.ui.checkBox_4.setChecked(False)
            self.generate_property_widgets()
            self.ui.label_5.setText(f"Object creation session {self.current_file} loaded")
            self.ui.label_5.show()
            #### Problem 001
            self.ui.lineEdit.setText(f"{self.event_name}'s object")
            self.ui.lineEdit.setEnabled(False)
            ####
        else:
            QMessageBox.warning(self, "Error", f"The object type of the loaded file has id {config_data["object_id"]} which doesn't correspond to the id of the present object creation\n\nSearch for the id {config_data["object_id"]} in the search bar and load this file into it")
        #self.check_if_name_exist()
        self.check_forms()
    
    def create_object(self):
        nop = self.ui.spinBox.value()
        numits = self.ui.spinBox_3.value()
        order = self.order
        repetitions = self.repetitions
        p_data = {}
        p_names = []
        for i in DataStore3.data_store:
            p_data[str(i)] = {}
            p_data[str(i)]["name"] = DataStore3.data_store[str(i)]["property_name"]
            p_data[str(i)]["forms"] = DataStore3.data_store[str(i)]["forms"]
            p_data[str(i)]["nof"] = DataStore3.data_store[str(i)]["nof"]
            p_names.append(DataStore3.data_store[str(i)]["property_name"])
            
        obj = Id07(nop, numits, order, repetitions, p_names, p_data)
        event = Events(self.event_name, obj.number_system)
        window = Event_properties(event)
        self.top_window.hide()
        window.exec()
        self.close_by_code_initiated.emit()
        return
    
    def check_numits(self):
        numits1 = self.ui.spinBox_3.value()
        sum = 0
        for i in range(len(DataStore3.data_store)):
            sum += DataStore3.data_store[str(i)]["nof"]
        if numits1 > sum:
            self.ui.label_8.setText("❌ The number of items to select cannot be greater than the sum of all items")
            self.ui.label_8.show()
            self.check_numits1 = False
        else:
            self.ui.label_8.hide()
            self.check_numits1 = True
            
    def open_table_window(self):
        total = 0 # Total number of forms (items)
        for i in range(len(DataStore3.data_store)):
            total += DataStore3.data_store[str(i)].get("nof")
        data = []
        item = []
        for i in range(len(DataStore3.data_store)):
            item = []
            item.append(DataStore3.data_store[str(i)].get("property_name"))
            item.append(DataStore3.data_store[str(i)].get("nof"))
            if DataStore3.data_store[str(i)].get("is_valid") == None:
                item.append(False)
            elif DataStore3.data_store[str(i)].get("is_valid") == 1:
                item.append(True)
            else:
                item.append(DataStore3.data_store[str(i)].get("is_valid"))
            data.append(item)
        #print(data)
        if self.table_window and self.table_window.isVisible():
            self.table_window.close()
            self.table_window = Group_data_info(data, total, self.order, self.repetitions, self.ui.spinBox_3.value())
            self.table_window.show()
        else:
            self.table_window = Group_data_info(data, total, self.order, self.repetitions, self.ui.spinBox_3.value())
            self.table_window.show()
    
    def close_group_info_window(self):
        if self.table_window and self.table_window.isVisible():
            self.table_window.close()
            self.table_window = None