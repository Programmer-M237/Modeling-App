from PySide6.QtWidgets import QDialog, QButtonGroup, QMessageBox, QLineEdit, QWidget, QHBoxLayout, QLabel
from PySide6.QtCore import Qt, QTimer
from object_5_property_forms_ui import Ui_Dialog
from data_store import DataStore1
from object_05_group_info_view import Group_data_info
import symbols

class Properties_forms(QDialog):
    property_name = ""
    is_valid = False
    is_name_valid = False
    is_nof_valid = False
    is_numits_valid = False
    is_forms_valid = False
    is_alt_base = False
    form_type = "default"
    previous_form_type = "default"
    forms = []
    prev_nof = 1
    alt_base = ""
    nof = 1
    num_of_its = 1
    order = False
    repetitions = False
    check_numits_val = False
    
    def __init__(self, index, existing_data=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #self.setEnabled(True)
        self.index = index
        self.setWindowTitle(f"Group {index + 1}")
        self.setWindowFlags(Qt.Window | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.ui.spinBox_3.setRange(1, 1000)
        self.ui.spinBox_3.setValue(1)
        self.ui.spinBox_2.setRange(1, 1000)
        self.ui.spinBox_2.setValue(1)
        self.ui.spinBox.setRange(1, 1000)
        self.ui.spinBox.setValue(1)
        self.ui.label_5.hide()
        
        self.ui.pushButton_6.clicked.connect(self.close)
        
        self.ui.checkBox_2.stateChanged.connect(self.order_check_box_toggle)
        self.ui.checkBox.stateChanged.connect(self.repetitions_check_box_toggle)
        
        self.form_types = QButtonGroup()
        self.ui.radioButton.setChecked(True)
        self.form_types.addButton(self.ui.radioButton)
        self.form_types.addButton(self.ui.radioButton_2)
        self.form_types.addButton(self.ui.radioButton_3)
        self.form_types.buttonClicked.connect(self.forms_type_radio_btn_clicked)
        self.forms_type_radio_btn_clicked()
        self.form_types.setExclusive(True)
        
        self.ui.spinBox_2.valueChanged.connect(self.generate_form_widgets)
        
        self.saved_data = []
        
        self.ui.pushButton.clicked.connect(self.go_to_property)
        
        if existing_data:
            self.property_name = existing_data.get("property_name", "")
            self.is_valid = existing_data.get("is_valid", False)
            self.form_type = existing_data.get("form_type", "")
            self.forms = existing_data.get("forms", [])
            self.prev_nof = existing_data.get("prev_nof", 1)
            self.go_to_form_value = existing_data.get("go_to_form", 1)
            self.alt_base = existing_data.get("alt_base", "")
            self.nof = existing_data.get("nof", 1)
            self.num_of_its = existing_data.get("num_of_its", 1)
            self.order = existing_data.get("order", False)
            self.repetitions = existing_data.get("repetitions", False)
            self.previous_form_type = existing_data.get("prev_form_type", "default")
            
            self.ui.lineEdit_3.setText(self.property_name)
            self.ui.spinBox.setValue(self.go_to_form_value)
            self.ui.lineEdit.setText(self.alt_base)
            self.ui.spinBox_2.setValue(self.nof)
            self.ui.spinBox_3.setValue(self.num_of_its)
            if self.order == True:
                self.ui.checkBox_2.setChecked(True)
            else:
                self.ui.checkBox_2.setChecked(False)
            if self.repetitions == True:
                self.ui.checkBox.setChecked(True)
            else:
                self.ui.checkBox.setChecked(False)
            if self.form_type == "default":
                self.ui.radioButton.setChecked(True)
                self.ui.lineEdit.setEnabled(False)
                self.ui.spinBox.setEnabled(False)
                self.ui.pushButton.setEnabled(False)
            if self.form_type == "alternative_base":
                self.ui.radioButton_2.setChecked(True)
                self.ui.lineEdit.setEnabled(True)
                self.ui.spinBox.setEnabled(False)
                self.ui.pushButton.setEnabled(False)
            if self.form_type == "alternative":
                self.ui.radioButton_3.setChecked(True)
                self.ui.lineEdit.setEnabled(False)
                self.ui.spinBox.setEnabled(True)
                self.ui.pushButton.setEnabled(True)
                
                self.saved_data = self.forms[:]
                
                layout = self.ui.scrollAreaWidgetContents.layout()
                self.ui.scrollAreaWidgetContents.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
                
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                        widget.setParent(None)
                        widget.deleteLater()
                
                for i in range(self.ui.spinBox_2.value()):
                    row_widget = QWidget()
                    row_layout = QHBoxLayout(row_widget)
                    
                    label = QLabel(f"Form {i + 1}")
                    line_edit = QLineEdit()
                    
                    line_edit.setText(self.saved_data[i])
                    
                    row_layout.addWidget(label)
                    row_layout.addWidget(line_edit)
                
                    layout.addWidget(row_widget)
                    
                    line_edit.textChanged.connect(self.check_entries)
                    
                scrollbar = self.ui.scrollArea.verticalScrollBar()
                scrollbar.setValue(scrollbar.maximum())
        
        self.ui.pushButton_6.clicked.connect(self.close)
        
        self.ui.label_3.hide()
        
        self.ui.lineEdit_3.textChanged.connect(self.check_if_name_exist)
        
        self.ui.spinBox_2.valueChanged.connect(self.generate_form_widgets)
        self.ui.spinBox_2.valueChanged.connect(self.check_entries)
        
        self.ui.lineEdit.textChanged.connect(self.check_entries)
        self.ui.spinBox.valueChanged.connect(self.check_entries)
        self.ui.lineEdit_3.textChanged.connect(self.check_entries)
        self.ui.spinBox_2.valueChanged.connect(self.check_entries)
        self.ui.spinBox_3.valueChanged.connect(self.check_entries)
        self.ui.lineEdit_3.textChanged.connect(self.check_entries)
        
        self.check_entries()
        
        self.ui.label.setText(f"Group {index + 1}")
    
    def check_if_name_exist(self) -> None:
        name = self.ui.lineEdit_3.text().strip()
        #print(DataStore.data_store)
        if not(name):
            self.is_name_valid = False
            self.ui.label_3.hide()
            #self.check_entries()
            return
        for i in range(len(DataStore1.data_store)):
            #print(data)
            data = DataStore1.data_store[str(i)]
            if i == self.index:
                continue
            elif name == data['property_name']:
                self.ui.label_3.setText("❌ A property with the same name already exists")
                self.ui.label_3.show()
                self.is_name_valid = False
                return
            else:
                self.ui.label_3.hide()
        self.is_name_valid = True
        return
    
    def generate_form_widgets(self):
        if self.form_type == "alternative":
            layout = self.ui.scrollAreaWidgetContents.layout()
            layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            
            self.saved_data = []
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    line_edit = row.findChild(QLineEdit)
                    if line_edit.text().strip():
                        self.saved_data.append(line_edit.text().strip())
                    else:
                        self.saved_data.append("")
            
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
                    
            for i in range(self.ui.spinBox_2.value()):
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
    
    def get_data(self):
        if self.form_type == "default":
            self.forms = []
            for i in range(self.ui.spinBox_2.value()):
                self.forms.append(symbols.get_symbol(i))
        elif self.form_type == "alternative_base":
            self.forms = []
            for i in range(self.ui.spinBox_2.value()):
                self.forms.append(f"{self.ui.lineEdit.text().strip()}{i + 1}")
        elif self.form_type == "alternative":
            layout = self.ui.scrollAreaWidgetContents.layout()
            
            self.saved_data = []
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    line_edit = row.findChild(QLineEdit)
                    if line_edit.text().strip():
                        self.saved_data.append(line_edit.text().strip())
                    else:
                        self.saved_data.append("")
            self.forms = self.saved_data
        return{
            "property_num": self.index + 1,
            "is_valid" : self.is_valid,
            "property_name": self.ui.lineEdit_3.text().strip(),
            "form_type": self.form_type,
            "forms": self.forms,
            "prev_nof": self.prev_nof,
            "go_to_form": self.ui.spinBox.value(),
            "alt_base": self.ui.lineEdit.text().strip(),
            "nof": self.ui.spinBox_2.value(),
            "num_of_its": self.ui.spinBox_3.value(),
            "order": self.order,
            "repetitions": self.repetitions,
            "prev_form_type": self.previous_form_type
        }
        
    def accept(self):
        self.data = self.get_data()
        return super().accept()
    
    def closeEvent(self, event):
        self.accept()
        return super().closeEvent(event)
    
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
            
    def forms_type_radio_btn_clicked(self):
        if self.ui.radioButton.isChecked():
            if self.previous_form_type == "alternative":
                self.prev_nof = self.ui.spinBox_2.value()
                layout = self.ui.scrollAreaWidgetContents.layout()
                
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
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
                    
            self.form_type = "default"
            self.previous_form_type = "default"
            self.ui.lineEdit.setEnabled(False)
            self.ui.spinBox.setEnabled(False)
            self.ui.pushButton.setEnabled(False)
        if self.ui.radioButton_2.isChecked():
            if self.previous_form_type == "alternative":
                self.prev_nof = self.ui.spinBox_2.value()
                layout = self.ui.scrollAreaWidgetContents.layout()
                
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
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()

            self.form_type = "alternative_base"
            self.previous_form_type = "alternative_base"
            self.ui.lineEdit.setEnabled(True)
            self.ui.spinBox.setEnabled(False)
            self.ui.pushButton.setEnabled(False)
        if self.ui.radioButton_3.isChecked():
            #print(self.saved_data)
            self.ui.lineEdit.setEnabled(False)
            self.ui.spinBox.setEnabled(True)
            self.ui.pushButton.setEnabled(True)
            #print(self.prev_nof)
            self.ui.spinBox_2.setValue(self.prev_nof)
            layout = self.ui.scrollAreaWidgetContents.layout()
            self.ui.scrollAreaWidgetContents.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
            
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
            
            for i in range(self.ui.spinBox_2.value()):
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
            self.form_type = "alternative"
            self.previous_form_type = "alternative"
        self.check_if_name_exist()
        self.check_entries()
        
    def go_to_property(self) -> None:
        index = self.ui.spinBox.value()
        layout = self.ui.scrollAreaWidgetContents.layout()
        total_forms = layout.count()
        
        if index < 1 or index > total_forms:
            QMessageBox.warning(self, "Navigation Error", "Property not found")
            return
        target_widget = layout.itemAt(index - 1).widget()
        if target_widget:
            self.ui.scrollArea.ensureWidgetVisible(target_widget)
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
        self.check_numits()
        if self.form_type == "default":
            if self.ui.spinBox_2.value():
                self.is_nof_valid = True
            else:
                self.is_nof_valid = False
            if self.ui.spinBox_3.value():
                self.is_numits_valid = True
            else:
                self.is_numits_valid = False
            self.is_valid = self.is_name_valid and self.is_nof_valid and self.is_numits_valid and self.check_numits_val
        elif self.form_type == "alternative_base":
            if self.ui.spinBox_2.value():
                self.is_nof_valid = True
            else:
                self.is_nof_valid = False
            if self.ui.spinBox_3.value():
                self.is_numits_valid = True
            else:
                self.is_numits_valid = False
            if self.ui.lineEdit.text().strip():
                self.is_alt_base = True
            else:
                self.is_alt_base = False
            self.is_valid = self.is_name_valid and self.is_nof_valid and self.is_alt_base and self.is_numits_valid and self.check_numits_val
        elif self.form_type == "alternative":
            if self.ui.spinBox_2.value():
                self.is_nof_valid = True
            else:
                self.is_nof_valid = False
            if self.ui.spinBox_3.value():
                self.is_numits_valid = True
            else:
                self.is_numits_valid = False
            layout = self.ui.scrollAreaWidgetContents.layout()
            self.ui.scrollAreaWidgetContents.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
            
            self.saved_data = []
            for i in range(layout.count()):
                row = layout.itemAt(i).widget()
                if row:
                    line_edit = row.findChild(QLineEdit)
                    self.is_forms_valid = all(layout.itemAt(i).widget().findChild(QLineEdit).text().strip() for i in range(layout.count()))
            self.is_valid = self.is_name_valid and self.is_nof_valid and self.is_forms_valid and self.is_numits_valid and self.check_numits_val
        #print(self.is_valid)
    
    def check_numits(self):
        if self.ui.spinBox_3.value() > self.ui.spinBox_2.value():
            self.ui.label_5.setText("❌ Number of items to select cannot be greater than number of forms")
            self.ui.label_5.show()
            self.check_numits_val = False
        else:
            self.ui.label_5.hide()
            self.check_numits_val = True