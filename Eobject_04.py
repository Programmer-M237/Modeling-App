from PySide6.QtWidgets import QButtonGroup, QHBoxLayout, QLabel, QWidget, QLineEdit, QMessageBox, QFileDialog, QGroupBox, QVBoxLayout, QFrame, QSpinBox
from PySide6.QtCore import Qt, QTimer, Signal, QStandardPaths
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont
from pathlib import Path
import json
from cryptography.fernet import Fernet
from Eobject_04_ui import Ui_Dialog
from object_04_object_info_view import Object_data_info
from entities import EntityManager
from temp_objects import Id04
from temp_events import Events
from step_2_of_event_creation import Event_properties
from collections import defaultdict

class EObject_04(QWidget):
    cancel_clicked = Signal()
    is_name_valid = True # Problem 001
    is_property_valid = False
    table_type = "default"
    saved_data = {}
    prev_saved_data = {}
    properties_names = defaultdict(list)
    properties_names_ids = defaultdict(int)
    ENCRYPTION_KEY = 'Rll0H4fZf5TvH1E-mk0qwcZ1cETu6jlA_2PiwZ9cvls='
    cipher = Fernet(ENCRYPTION_KEY)
    documents = Path(QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation))
    m_app_folder = documents / "M App" / "Objects 04"
    m_app_folder.mkdir(parents=True, exist_ok=True)
    documents_dir = m_app_folder
    untitled_x = 1 # Use to name the untitled files of the Save As Window
    config_data = {"object_id": "04", "object_name": "", "nOp": 1, "properties_data": {}, "gtpnum": 1, "table_type": ""}
    current_file = None
    close_by_code_initiated = Signal()
    
    def __init__(self, stacked_widget, top_window, event_name):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.name = "page_4"
        self.event_name = event_name
        self.ui.spinBox_5.setRange(1, 1000)
        self.ui.spinBox_3.setRange(1, 1000)
        self.ui.spinBox_5.setValue(1)
        self.ui.spinBox_3.setValue(1)
        self.ui.label.hide()
        self.table_window = None
        self.top_window = top_window
        self.stacked_widget = stacked_widget
        self.ui.label_7.setText('<a href="#">Click here to view a summary of the properties information</a>')
        
        self.ui.label_7.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.ui.label_7.setOpenExternalLinks(False)
        self.ui.label_7.linkActivated.connect(self.open_table_window)
        
        #### Problem 001
        self.ui.lineEdit_6.setText(f"{self.event_name}'s object")
        self.ui.lineEdit_6.setEnabled(False)
        ####
        
        self.top_window_close_signal = Signal()
        self.stacked_widget_page_change_signal = Signal()
        self.top_window.destroyed.connect(self.close_object_info_window)
        self.stacked_widget.currentChanged.connect(self.close_object_info_window)
        
        self.initial_generate_properties_widgets()
        self.ui.spinBox_5.valueChanged.connect(self.generate_properties_widgets)
        
        self.ui.label_17.hide()
        # self.ui.lineEdit_6.textChanged.connect(self.check_if_name_exist)
        self.ui.lineEdit_6.textChanged.connect(self.check_entries)
        
        self.table_types = QButtonGroup()
        self.ui.radioButton_10.setChecked(True)
        self.table_types.addButton(self.ui.radioButton_10)
        self.table_types.addButton(self.ui.radioButton_11)
        self.table_types.addButton(self.ui.radioButton_12)
        self.table_types.buttonClicked.connect(self.table_types_radio_btn_clicked)
        self.table_types_radio_btn_clicked()
        
        self.ui.spinBox_5.valueChanged.connect(self.check_if_property_valid)
        self.ui.spinBox_5.valueChanged.connect(self.check_entries)
        self.ui.spinBox_5.valueChanged.connect(self.check_same_name_properties)
        
        self.ui.pushButton_2.clicked.connect(self.cancel_clicked.emit)
        
        self.ui.pushButton_7.clicked.connect(self.go_to_property)
            
        self.model = QStandardItemModel()
        self.ui.comboBox.setModel(self.model)
        
        self.ui.pushButton_8.clicked.connect(self.go_to_property_name_error)
        
        self.ui.frame_7.hide()
        
        self.ui.pushButton_3.setToolTip(f"Save this object creation session")
        self.ui.pushButton_4.setToolTip("Save this object creation session")
        self.ui.pushButton_6.setToolTip("Load object creation session with object id '04'")

        self.ui.pushButton_3.clicked.connect(self.save_config)
        self.ui.pushButton_4.clicked.connect(self.save_as_config)
        self.ui.pushButton_6.clicked.connect(self.load_config_dialog)
        
        self.ui.pushButton.clicked.connect(self.create_object)
        
    def focusInEvent(self, event):
        self.check_same_name_properties()
        super().focusInEvent(event)
        
    def focusOutEvent(self, event):
        self.check_same_name_properties()
        super().focusOutEvent(event)
        
    def mousePressEvent(self, event):
        self.check_same_name_properties()
        super().mousePressEvent(event)
        
    def mouseMoveEvent(self, event):
        self.check_same_name_properties()
        super().mouseMoveEvent(event)
        
    # def check_if_name_exist(self):
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
    #     self.check_entries()
            
    def check_entries(self):
        for i in range(len(self.saved_data)):
            self.is_property_valid = all(self.saved_data[i]["is_valid"] for i in self.saved_data)
        self.ui.pushButton.setEnabled(self.is_name_valid and self.is_property_valid)
    
    def table_types_radio_btn_clicked(self) -> None:
        if self.ui.radioButton_10.isChecked():
            self.table_type = "normal"
        if self.ui.radioButton_11.isChecked():
            self.table_type = "permutations"
        if self.ui.radioButton_12.isChecked():
            self.table_type = "combinations"
        # self.check_if_name_exist()
        self.check_entries()
        
    def initial_generate_properties_widgets(self):
        layout = self.ui.scrollAreaWidgetContents.layout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
        for i in range(self.ui.spinBox_5.value()):
            self.saved_data[i] = {"name": "", "nof": 1, "is_valid": False}
            
            group_widget = QWidget()
            group_layout = QVBoxLayout(group_widget)
            
            groupbox = QGroupBox(f"Property {i + 1}")
            frame = QFrame()
            frame_l = QHBoxLayout(frame)
            label = QLabel("Name")
            line_edit = QLineEdit()
            frame1 = QFrame()
            frame1_l = QHBoxLayout(frame1)
            label1 = QLabel("Number of forms")
            spin_box = QSpinBox()
            spin_box.setRange(1, 1000)
            
            if i < len(self.saved_data):
                line_edit.setText(self.saved_data[i]["name"])
                spin_box.setValue(self.saved_data[i]["nof"])
                
            
            frame_l.addWidget(label)
            frame_l.addWidget(line_edit)
            frame_l.setContentsMargins(0, 0, 0, 0)
            frame_l.setSpacing(2)
            frame1_l.addWidget(label1, 0)
            frame1_l.addWidget(spin_box, 7)
            frame1_l.setContentsMargins(0, 0, 0, 0)
            frame1_l.setSpacing(2)
            groupbox_l = QVBoxLayout(groupbox)
            groupbox_l.addWidget(frame)
            groupbox_l.addWidget(frame1)
            groupbox_l.setContentsMargins(6, 6, 6, 6)
            groupbox_l.setSpacing(2)
            group_layout.addWidget(groupbox)
            
            layout.addWidget(group_widget)
            
            line_edit.textChanged.connect(self.check_entries)
            spin_box.valueChanged.connect(self.check_if_property_valid)
            line_edit.textChanged.connect(self.check_same_name_properties)
            spin_box.valueChanged.connect(self.check_same_name_properties)
            line_edit.textChanged.connect(self.check_if_property_valid)
            spin_box.valueChanged.connect(self.check_if_property_valid)
            line_edit.textChanged.connect(self.update_widgets)
            spin_box.valueChanged.connect(self.update_widgets)
            #print(self.saved_data)
            
        scrollbar = self.ui.scrollArea_2.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
        
    
    def generate_properties_widgets(self):
        layout = self.ui.scrollAreaWidgetContents.layout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.prev_saved_data.clear()
        self.saved_data.clear()
        for i in range(layout.count()):
            self.prev_saved_data[i] = {"name": "", "nof": 1, "is_valid": False}
            #print(self.prev_saved_data[i])
            group = layout.itemAt(i).widget()
            if group:
                line_edit = group.findChild(QLineEdit)
                if line_edit:
                    self.prev_saved_data[i]["name"] = line_edit.text().strip()
                else:
                    self.prev_saved_data[i]["name"] = ""
                spin_box = group.findChild(QSpinBox)
                if spin_box:
                    self.prev_saved_data[i]["nof"] = spin_box.value()
                else:
                    self.prev_saved_data[i]["nof"] = 1 # Not really important, just for safety reasons
        
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
        for i in range(self.ui.spinBox_5.value()):
            self.saved_data[i] = {"name": "", "nof": 1, "is_valid": False}
            
            group_widget = QWidget()
            group_layout = QVBoxLayout(group_widget)
            
            groupbox = QGroupBox(f"Property {i + 1}")
            frame = QFrame()
            frame_l = QHBoxLayout(frame)
            label = QLabel("Name")
            line_edit = QLineEdit()
            frame1 = QFrame()
            frame1_l = QHBoxLayout(frame1)
            label1 = QLabel("Number of forms")
            spin_box = QSpinBox()
            spin_box.setRange(1, 1000)
            
            
            if i < len(self.prev_saved_data):
                line_edit.setText(self.prev_saved_data[i]["name"])
                spin_box.setValue(self.prev_saved_data[i]["nof"])
                
            line_edit.textChanged.connect(self.check_entries)
            spin_box.valueChanged.connect(self.check_if_property_valid)
            line_edit.textChanged.connect(self.check_same_name_properties)
            spin_box.valueChanged.connect(self.check_same_name_properties)
            line_edit.textChanged.connect(self.check_if_property_valid)
            spin_box.valueChanged.connect(self.check_if_property_valid)
            line_edit.textChanged.connect(self.update_widgets)
            spin_box.valueChanged.connect(self.update_widgets)
                
            
            frame_l.addWidget(label)
            frame_l.addWidget(line_edit)
            frame_l.setContentsMargins(0, 0, 0, 0)
            frame_l.setSpacing(2)
            frame1_l.addWidget(label1, 0)
            frame1_l.addWidget(spin_box, 7)
            frame1_l.setContentsMargins(0, 0, 0, 0)
            frame1_l.setSpacing(2)
            groupbox_l = QVBoxLayout(groupbox)
            groupbox_l.addWidget(frame)
            groupbox_l.addWidget(frame1)
            groupbox_l.setContentsMargins(6, 6, 6, 6)
            groupbox_l.setSpacing(2)
            group_layout.addWidget(groupbox)
            
            layout.addWidget(group_widget)
            
            line_edit.textChanged.connect(self.check_entries)
            #print(self.saved_data)
            
        scrollbar = self.ui.scrollArea_2.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
        
    def update_widgets(self):
        layout = self.ui.scrollAreaWidgetContents.layout()
        
        for i in range(layout.count()):
            group = layout.itemAt(i).widget()
            if group:
                line_edit = group.findChild(QLineEdit)
                if line_edit:
                    self.saved_data[i]["name"] = line_edit.text().strip()
                else:
                    self.saved_data[i]["name"] = ""
                spin_box = group.findChild(QSpinBox)
                if spin_box:
                    self.saved_data[i]["nof"] = spin_box.value()
                else:
                    self.saved_data[i]["nof"] = 1 # Not really important, just for safety reasons
        self.check_if_property_valid()
        self.check_entries()
    
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
                             QGroupBox {
                                 border: 2px solid #00ffff;
                                 border-radius: 6px;
                             }
                             """)
        QTimer.singleShot(2000, lambda: widget.setStyleSheet(""))
        
    def check_same_name_properties(self):
        self.ui.comboBox.clear()
        self.properties_names.clear()
        self.properties_names_ids.clear()
        layout = self.ui.scrollAreaWidgetContents.layout()
        total_forms = layout.count()
        
        for i in range(total_forms):
            group = layout.itemAt(i).widget()
            if group:
                line_edit = group.findChild(QLineEdit).text().strip()
                if line_edit:
                    if line_edit == "":
                        pass
                    else:
                        self.properties_names[line_edit].append(i)

        
        for i in list(self.properties_names.keys()):
            if len(self.properties_names[i]) == 1:
                del self.properties_names[i]
                    
        for i in self.properties_names.keys():
            header = QStandardItem(i)
            flags = header.flags()
            flags &= ~Qt.ItemIsEnabled
            flags &= ~Qt.ItemIsSelectable
            header.setFlags(flags)
            font = QFont()
            font.setBold(True)
            header.setFont(font)
            self.model.appendRow(header)
            for j in self.properties_names[i]:
                self.model.appendRow(QStandardItem(f" Property {j + 1}")) # Indent for clarity
                self.properties_names_ids[f" Property {j + 1}"] = j
        if self.ui.comboBox.count() > 0:
            self.ui.frame_7.show()
        else:
            self.ui.frame_7.hide()
        self.check_entries()
        
    def check_if_property_valid(self):
        for i in range(len(self.saved_data)):
            if self.saved_data[i]["name"]:
                self.saved_data[i]["is_valid"] = True
            else:
                self.saved_data[i]["is_valid"] = False

    def go_to_property_name_error(self):
        index = self.properties_names_ids[self.ui.comboBox.currentText()]
        layout = self.ui.scrollAreaWidgetContents.layout()
        target_widget = layout.itemAt(index).widget()
        if target_widget:
            self.ui.scrollArea_2.ensureWidgetVisible(target_widget)
        else:
            QMessageBox.warning(self, "Navigation Error", "Form not found")
        self.highlight_temporarily(layout.itemAt(index).widget(), duration=2000)
        
    def get_config_data(self) -> dict:
        self.config_data["object_name"] = self.ui.lineEdit_6.text().strip()
        self.config_data["nOp"] = self.ui.spinBox_5.value()
        self.config_data["gtpnum"] = self.ui.spinBox_3.value()
        self.config_data["table_type"] = self.table_type
        
        layout = self.ui.scrollAreaWidgetContents.layout()
        
        self.prev_saved_data.clear()
        self.saved_data.clear()
        for i in range(layout.count()):
            self.prev_saved_data[i] = {"name": "", "nof": 1, "is_valid": False}
            #print(self.prev_saved_data[i])
            group = layout.itemAt(i).widget()
            if group:
                line_edit = group.findChild(QLineEdit)
                if line_edit:
                    self.prev_saved_data[i]["name"] = line_edit.text().strip()
                else:
                    self.prev_saved_data[i]["name"] = ""
                spin_box = group.findChild(QSpinBox)
                if spin_box:
                    self.prev_saved_data[i]["nof"] = spin_box.value()
                else:
                    self.prev_saved_data[i]["nof"] = 1 # Not really important, just for safety reasons
                    
        self.config_data["properties_data"] = self.prev_saved_data
        #print(self.config_data["properties_data"])
        #print(self.config_data["table_type"])
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
                self.ui.label.setText(f"Object creation session data saved to {self.current_file}")
                self.ui.label.show()
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
                self.ui.pushButton_3.setToolTip(f"Save to file {self.current_file}")
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
            self.ui.pushButton_3.setToolTip(f"Save to file {self.current_file}")
        else:
            return
        if not isinstance(file_name, str):
            QMessageBox.warning(self, "Error", "Invalid file")
            return
        
    def load_config(self, config_data):
        #print(config_data)
        if config_data["object_id"] == "04":
            self.ui.lineEdit_6.setText(config_data["object_name"])
            self.ui.spinBox_5.setValue(config_data["nOp"])
            self.ui.spinBox_3.setValue(config_data["gtpnum"])
            self.table_type = config_data["table_type"]
            #print(config_data["properties_data"])
            #print(config_data["table_type"])
            
            layout = self.ui.scrollAreaWidgetContents.layout()
            layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            self.prev_saved_data.clear()
            self.saved_data.clear()
            p_data = config_data["properties_data"]
            self.prev_saved_data = {int(k): v for k, v in p_data.items()}
            #print(self.prev_saved_data)
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
            
            for i in range(self.ui.spinBox_5.value()):
                self.saved_data[i] = {"name": "", "nof": 1, "is_valid": False}
                
                group_widget = QWidget()
                group_layout = QVBoxLayout(group_widget)
                
                groupbox = QGroupBox(f"Property {i + 1}")
                frame = QFrame()
                frame_l = QHBoxLayout(frame)
                label = QLabel("Name")
                line_edit = QLineEdit()
                frame1 = QFrame()
                frame1_l = QHBoxLayout(frame1)
                label1 = QLabel("Number of forms")
                spin_box = QSpinBox()
                spin_box.setRange(1, 1000)
                
                
                if i < len(self.prev_saved_data):
                    line_edit.setText(self.prev_saved_data[i]["name"])
                    spin_box.setValue(self.prev_saved_data[i]["nof"])
                    
                line_edit.textChanged.connect(self.check_same_name_properties)
                spin_box.valueChanged.connect(self.check_same_name_properties)
                    
                
                frame_l.addWidget(label)
                frame_l.addWidget(line_edit)
                frame_l.setContentsMargins(0, 0, 0, 0)
                frame_l.setSpacing(2)
                frame1_l.addWidget(label1, 0)
                frame1_l.addWidget(spin_box, 7)
                frame1_l.setContentsMargins(0, 0, 0, 0)
                frame1_l.setSpacing(2)
                groupbox_l = QVBoxLayout(groupbox)
                groupbox_l.addWidget(frame)
                groupbox_l.addWidget(frame1)
                groupbox_l.setContentsMargins(6, 6, 6, 6)
                groupbox_l.setSpacing(2)
                group_layout.addWidget(groupbox)
                
                layout.addWidget(group_widget)
                
                line_edit.textChanged.connect(self.check_entries)
                #print(self.saved_data)
                
            scrollbar = self.ui.scrollArea_2.verticalScrollBar()
            scrollbar.setValue(scrollbar.maximum())
            self.generate_properties_widgets()
            if self.table_type == "normal":
                self.ui.radioButton_10.setChecked(True)
            elif self.table_type == "permutations":
                self.ui.radioButton_11.setChecked(True)
            elif self.table_type == "combinations":
                self.ui.radioButton_12.setChecked(True)
            self.table_types_radio_btn_clicked()
            self.ui.label.setText(f"Object creation session {self.current_file} loaded")
            self.ui.label.show()
            #### Problem 001
            self.ui.lineEdit_6.setText(f"{self.event_name}'s object")
            self.ui.lineEdit_6.setEnabled(False)
            ####
        else:
            QMessageBox.warning(self, "Error", f"The object type of the loaded file has id {config_data["object_id"]} which doesn't correspond to the id of the present object creation\n\nSearch for the id {config_data["object_id"]} in the search bar and load this file into it")
        # self.check_if_name_exist()
        self.update_widgets()
        self.check_same_name_properties()
        self.check_entries()
        
    def create_object(self):
        nop = self.ui.spinBox_5.value()
        table_type = self.table_type
        p_data = {}
        p_names = []
        for i in range(len(self.saved_data)):
            p_data[i] = {}
            p_data[i]["name"] = self.saved_data[i]["name"]
            p_data[i]["nof"] = self.saved_data[i]["nof"]
            p_names.append(self.saved_data[i]["name"])
        
        obj = Id04(nop, p_data, table_type, p_names)    
        event = Events(self.event_name, obj.number_system)
        window = Event_properties(event)
        self.top_window.hide()
        window.exec()
        self.close_by_code_initiated.emit()
        return

        """
        
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.prev_saved_data = {}
        for i in range(layout.count()):
            group = layout.itemAt(i).widget()
            if group:
                groupbox = QGroupBox(f"Property {i + 1}")
                frame_1 = QWidget()
                frame_1.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
                label = QLabel("Name")
                frame_1.layout().addWidget(label)
        """
        
    def close_object_info_window(self):
        if self.table_window and self.table_window.isVisible():
            self.table_window.close()
            self.table_window = None
            
    def open_table_window(self):
        data = []
        item = []
        print(self.saved_data)
        for i in range(len(self.saved_data)):
            item = []
            item.append(self.saved_data[i].get("name"))
            item.append(self.saved_data[i].get("nof"))
            if self.saved_data[i].get("is_valid") == None:
                item.append(False)
            else:
                item.append(self.saved_data[i].get("is_valid"))
            data.append(item)
        
        if self.table_window and self.table_window.isVisible():
            self.table_window.close()
            self.table_window = Object_data_info(data)
            self.table_window.show()
        else:
            self.table_window = Object_data_info(data)
            self.table_window.show()