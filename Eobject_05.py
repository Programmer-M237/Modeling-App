from PySide6.QtWidgets import QPushButton, QMessageBox, QFileDialog, QWidget, QDialog
from PySide6.QtCore import Qt, Signal, QTimer, QStandardPaths
from pathlib import Path
import json
from cryptography.fernet import Fernet
from Eobject_05_ui import Ui_Dialog
from object_05_group_info_view import Group_data_info
from object_05_property_forms import Properties_forms
from temp_objects import Id05
from temp_events import Events
from step_2_of_event_creation import Event_properties
from data_store import DataStore1

class EObject_05(QWidget):
    cancel_clicked = Signal()
    is_name_valid = True # This goes along with a set of modification that was done when a problem was noticed. "The name textbox still checks whether the name is duplicate in the pool of object names. But this is used for event creations, so the object name is not important since the event will always have one object, so the object can be addressed as the object of that event. So the problem is that the presence of the object name in the event creation process is not right".
    # Another problem is that removing the object name out of the event's object creation process is quite tough. So I decided to autofill the object's name textbox and block it, so that the user won't have to fill it. And also, I set the is_name_valid variable to always true, so that it doesn't interfere with the event's object creation UI filling validation
    properties_id_list = {}
    prev_data_store = {}
    ENCRYPTION_KEY = 'Rll0H4fZf5TvH1E-mk0qwcZ1cETu6jlA_2PiwZ9cvls='
    cipher = Fernet(ENCRYPTION_KEY)
    documents = Path(QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation))
    m_app_folder = documents / "M App" / "Objects 05"
    m_app_folder.mkdir(parents=True, exist_ok=True)
    documents_dir = m_app_folder
    untitled_x = 1 # Use to name the untitled files of the Save As Window
    config_data = {"object_id": "05", "object_name": str, "nOp": int, "properties_data": dict, "gtpnum": int}
    current_file = None
    close_by_code_initiated = Signal()
    
    def __init__(self, stacked_widget, top_window, event_name):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.name = "page_5"
        self.event_name = event_name
        self.ui.spinBox_5.setRange(1, 1000)
        self.ui.spinBox_5.setValue(1)
        self.ui.spinBox_3.setRange(1, 1000)
        self.ui.spinBox_3.setValue(1)
        self.ui.label_17.hide()
        self.ui.label.hide()
        self.ui.label_6
        self.table_window = None
        self.top_window = top_window
        self.stacked_widget = stacked_widget
        self.ui.label_2.setText('<a href="#">Click here to view a summary of the groups information</a>')
        
        self.ui.label_2.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.ui.label_2.setOpenExternalLinks(False)
        self.ui.label_2.linkActivated.connect(self.open_table_window)
        
        #### Problem 001
        self.ui.lineEdit_6.setText(f"{self.event_name}'s object")
        self.ui.lineEdit_6.setEnabled(False)
        ####
        
        self.top_window_close_signal = Signal()
        self.stacked_widget_page_change_signal = Signal()
        self.top_window.destroyed.connect(self.close_group_info_window)
        self.stacked_widget.currentChanged.connect(self.close_group_info_window)
        
        self.ui.pushButton_3.clicked.connect(self.save_config)
        self.ui.pushButton_4.clicked.connect(self.save_as_config)
        self.ui.pushButton_6.clicked.connect(self.load_config_dialog)
        #self.ui.pushButton_5.clicked.connect(self.create_object)
        
        self.initial_generate_group_widgets()
        self.ui.spinBox_5.valueChanged.connect(self.generate_group_widgets)
        
        self.ui.pushButton_2.clicked.connect(self.cancel_clicked.emit)
        
        self.ui.pushButton_7.clicked.connect(self.go_to_property)
        
        self.check_forms()
        self.ui.spinBox_5.valueChanged.connect(self.check_forms)
        
        self.ui.label_6.setText("Groups with invalid inputs")
        
        self.ui.pushButton_8.clicked.connect(self.go_to_property_error)
        
        self.ui.pushButton_3.setToolTip(f"Save this object creation session")
        self.ui.pushButton_4.setToolTip("Save this object creation session")
        self.ui.pushButton_6.setToolTip("Load object creation session with object id '05'")
        
        self.ui.lineEdit_6.textChanged.connect(self.check_forms)
        
        self.ui.pushButton.clicked.connect(self.create_object)
        
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
    #     name = self.ui.lineEdit_6.text().strip()
        
    #     if not(name):
    #         self.is_name_valid = False
    #     elif (name, "object") in EntityManager._items:
    #         self.ui.label_17.setText("❌ An object with the same name already exists")
    #         self.ui.label_17.show()
    #         self.is_name_valid = False
    #     elif EntityManager.name_exists_with_different_type(EntityManager, name, "object"):
    #         self.ui.label_17.setText("⚠️ An event or system with the same name already exists")
    #         self.ui.label_17.show()
    #         self.is_name_valid = True
    #     else:
    #         self.ui.label_17.hide()
    #         self.is_name_valid = True
    
    def initial_generate_group_widgets(self):
        self.properties_id_list = {}
        layout = self.ui.scrollAreaWidgetContents.layout()
        self.ui.scrollAreaWidgetContents.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
        for i in range(self.ui.spinBox_5.value()):
            button = QPushButton(f"Edit group {i + 1}")
            DataStore1.data_store[str(i)] = {"property_name": "", "is_valid": False, "form_type": "default", "forms": [], "prev_nof": 1, "go_to_form": 1, "alt_base": "", "nof": 1, "num_of_its": 1, "order": False, "repetitions": False, "prev_form_type": "default"}
            button.clicked.connect(lambda _, index=i: self.open_data_dialog(index))
            button.clicked.connect(self.check_forms)
            self.properties_id_list[f"Group {i + 1}"] = i + 1
            layout.addWidget(button)
        
        scrollbar = self.ui.scrollArea_2.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
        
    def generate_group_widgets(self):
        self.properties_id_list = {}
        #print(len(DataStore.data_store))
        for i in range(len(DataStore1.data_store)):
            self.prev_data_store[str(i)] = DataStore1.data_store[str(i)]
            if i > self.ui.spinBox_5.value():
                del DataStore1.data_store[str(i)]
        DataStore1.data_store.clear()
                
        layout = self.ui.scrollAreaWidgetContents.layout()
        self.ui.scrollAreaWidgetContents.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
        for i in range(self.ui.spinBox_5.value()):
            button = QPushButton(f"Edit group {i + 1}")
            if str(i) not in self.prev_data_store.keys():
                self.prev_data_store[str(i)] = {"property_name": "", "form_type": "default", "forms": [], "go_to_form": 1, "alt_base": "", "nof": 1, "prev_form_type": "default"}
            DataStore1.data_store[str(i)] = self.prev_data_store[str(i)]
            button.clicked.connect(lambda _, index=i: self.open_data_dialog(index))
            button.clicked.connect(self.check_forms)
            self.properties_id_list[f"Group {i + 1}"] = i + 1
            layout.addWidget(button)
        
        #print(DataStore.data_store)
        self.prev_data_store.clear()
        scrollbar = self.ui.scrollArea_2.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
        
    def open_data_dialog(self, index):
        #print(index)
        existing = DataStore1.data_store.get(str(index))
        #print(existing)
        dialog = Properties_forms(index, existing_data=existing, parent=self)
        dialog.finished.connect(lambda result: self.save_if_accepted(result, index, dialog))
        dialog.setModal(True)
        dialog.show()
        
        if not hasattr(self, '_dialogs'):
            self._dialogs = {}
            self._dialogs[index] = dialog
    
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
                             QPushButton {
                                 border: 2px solid #00ffff;
                                 border-radius: 6px;
                             }
                             """)
        QTimer.singleShot(2000, lambda: widget.setStyleSheet(""))
        
    def go_to_property_error(self) -> None:
        #print(self.ui.comboBox.currentText())
        index = self.properties_id_list[self.ui.comboBox.currentText()] # They only difference between the two functions
        layout = self.ui.scrollAreaWidgetContents.layout()
        total_properties = layout.count()
        
        if index < 1 or index > total_properties:
            QMessageBox.warning(self, "Navigation Error", "Property not found")
            return
        target_widget = layout.itemAt(index - 1).widget()
        if target_widget:
            self.ui.scrollArea_2.ensureWidgetVisible(target_widget)
        else:
            QMessageBox.warning(self, "Navigation Error", "Property not found")
        self.highlight_temporarily(layout.itemAt(index - 1).widget(), duration=2000)
        
    def check_forms(self):
        self.ui.comboBox.clear()
        layout = self.ui.scrollAreaWidgetContents.layout()
        for i in range(layout.count()):
            if DataStore1.data_store[str(i)].get("is_valid") == True:
                self.is_forms_valid = True
            else:
                self.is_forms_valid = False
                self.ui.comboBox.addItem(f"Group {i + 1}")
                self.ui.frame_7.show()
        if self.is_forms_valid == True:
            self.ui.frame_7.hide()
        self.is_forms_valid = all(DataStore1.data_store[str(i)].get("is_valid", False) for i in range(layout.count()))
        self.check_entries()
    
    def check_entries(self):
        if self.ui.spinBox_5.value():
            self.is_nop_valid = True
        else:
            self.is_nop_valid = False
        self.ui.pushButton.setEnabled(self.is_nop_valid and self.is_name_valid and self.is_forms_valid)
        
    def get_config_data(self) -> dict:
        self.config_data["object_name"] = self.ui.lineEdit_6.text().strip()
        self.config_data["nOp"] = self.ui.spinBox_5.value()
        self.config_data["properties_data"] = DataStore1.data_store
        self.config_data["gtpnum"] = self.ui.spinBox_3.value()
        return self.config_data
    
    def save_config(self) -> None:
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
                self.ui.label.setText(f"Object creation session data saved to {self.current_file}")
                self.ui.label.show()
                
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
        DataStore1.data_store.clear()
        if config_data["object_id"] == "05":
            DataStore1.data_store = config_data["properties_data"]
            self.ui.lineEdit_6.setText(config_data["object_name"])
            self.ui.spinBox_5.setValue(config_data["nOp"])
            self.ui.spinBox_3.setValue(config_data["gtpnum"])
            self.generate_group_widgets()
            self.ui.label.setText(f"Object creation session {self.current_file} loaded")
            self.ui.label.show()
            #### Problem 001
            self.ui.lineEdit_6.setText(f"{self.event_name}'s object")
            self.ui.lineEdit_6.setEnabled(False)
            ####
        else:
            QMessageBox.warning(self, "Error", f"The object type of the loaded file has id {config_data["object_id"]} which doesn't correspond to the id of the present object creation\n\nSearch for the id {config_data["object_id"]} in the search bar and load this file into it")
        self.check_forms()
        
    def create_object(self) -> None:
        nop = self.ui.spinBox_5.value()
        p_data = {}
        p_names = []
        #print(DataStore1.data_store)
        for i in DataStore1.data_store:
            p_data[str(i)] = {}
            p_data[str(i)]["name"] = DataStore1.data_store[str(i)]["property_name"]
            p_data[str(i)]["forms"] = DataStore1.data_store[str(i)]["forms"]
            p_data[str(i)]["nof"] = DataStore1.data_store[str(i)]["nof"]
            p_data[str(i)]["numits"] = DataStore1.data_store[str(i)]["num_of_its"]
            p_data[str(i)]["order"] = DataStore1.data_store[str(i)]["order"]
            p_data[str(i)]["repetitions"] = DataStore1.data_store[str(i)]["repetitions"]
            p_names.append(DataStore1.data_store[str(i)]["property_name"])
        
        #print(p_data)   
        obj = Id05(nop, p_names, p_data)    
        event = Events(self.event_name, obj.number_system)
        window = Event_properties(event)
        self.top_window.hide()
        window.exec()
        self.close_by_code_initiated.emit()
        return
        
    def close_group_info_window(self):
        if self.table_window and self.table_window.isVisible():
            self.table_window.close()
            self.table_window = None
            
    def open_table_window(self):
        total = 0 # Total number of forms (items)
        sum = 0 # Total number of items to select
        for i in range(len(DataStore1.data_store)):
            sum += DataStore1.data_store[str(i)].get("num_of_its")
            total += DataStore1.data_store[str(i)].get("nof")
        data = []
        item = []
        for i in range(len(DataStore1.data_store)):
            item = []
            item.append(DataStore1.data_store[str(i)].get("property_name"))
            item.append(DataStore1.data_store[str(i)].get("nof"))
            if DataStore1.data_store[str(i)].get("num_of_its") == None:
                item.append(1)
            else:
                item.append(DataStore1.data_store[str(i)].get("num_of_its"))
            if DataStore1.data_store[str(i)].get("is_valid") == None:
                item.append(False)
            elif DataStore1.data_store[str(i)].get("is_valid") == 1:
                item.append(True)
            else:
                item.append(DataStore1.data_store[str(i)].get("is_valid"))
            if DataStore1.data_store[str(i)].get("order") == None:
                item.append(False)
            else:
                item.append(DataStore1.data_store[str(i)].get("order"))
            if DataStore1.data_store[str(i)].get("repetitions") == None:
                item.append(False)
            else:
                item.append(DataStore1.data_store[str(i)].get("repetitions"))
            data.append(item)
        
        if self.table_window and self.table_window.isVisible():
            self.table_window.close()
            self.table_window = Group_data_info(data, sum, total)
            self.table_window.show()
        else:
            self.table_window = Group_data_info(data, sum, total)
            self.table_window.show()
            
    def save_if_accepted(self, result, index, dialog):
        if result == QDialog.Accepted:
            DataStore1.data_store[str(index)] = dialog.data
            self.check_entries()
            
        if hasattr(self, '_dialog') and index in self._dialogs:
            del self._dialogs[index]