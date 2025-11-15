"""This is a complex stuff, it will be added in the next versions of the app"""

from PySide6.QtWidgets import QMessageBox, QFileDialog, QWidget, QButtonGroup, QHBoxLayout, QLabel, QLineEdit
from PySide6.QtCore import Qt, Signal, QTimer, QStandardPaths
from pathlib import Path
import json
from cryptography.fernet import Fernet
from object_26_ui import Ui_Dialog
from objects import Id25
from object_manager import ObjectsManager
from entities import EntityManager
import symbols
from typing import List, Tuple, Dict

class Object_26(QWidget, Ui_Dialog):
    cancel_clicked = Signal()
    is_name_valid = False
    include_inclusion = False
    include_exclusion = False
    include_togetherness = False
    include_separation = False
    include_position_based = False
    inclusion_set = []
    exclusion_set = []
    togetherness_set = [[]]
    separation_set = [[]]
    position_set = {}
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.spin_box_3.setRange(1, 1000)
        self.spin_box_3.setValue(1)
        self.spinBox.setRange(1, 1000)
        self.spinBox.setValue(1)
        self.label_5.hide()
        
        self.pushButton_12.clicked.connect(self.cancel_clicked.emit)
        
        self.lineEdit_3.textChanged.connect(self.check_if_name_exist)
        
        self.spin_box_3.valueChanged.connect(self.generate_item_widgets)
        self.generate_item_widgets()
        
        self.pushButton_3.clicked.connect(self.go_to_item)
        
        restriction = QButtonGroup(self)
        restriction.setExclusive(False)
        self.checkBox.setChecked(False)
        restriction.addButton(self.checkBox)
        self.checkBox_2.setChecked(False)
        restriction.addButton(self.checkBox_2)
        self.checkBox_3.setChecked(False)
        restriction.addButton(self.checkBox_3)
        self.checkBox_4.setChecked(False)
        restriction.addButton(self.checkBox_4)
        self.checkBox_5.setChecked(False)
        restriction.addButton(self.checkBox_5)
        restriction.buttonClicked.connect(self.update_restriction)
        self.update_restriction()
        
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
        pass
    
    def update_restriction(self):
        if self.checkBox.isChecked():
            self.include_inclusion = True
            self.frame.show()
            self.update_inclusion_widgets()
        else:
            self.include_inclusion = False
            self.frame.hide()
            
        if self.checkBox_2.isChecked():
            self.include_exclusion = True
            self.frame_2.show()
            self.update_exclusion_widgets()
        else:
            self.include_exclusion = False
            self.frame_2.hide()
            
        if self.checkBox_3.isChecked():
            self.include_togetherness = True
            self.frame_3.show()
            self.update_togetherness_widgets()
        else:
            self.include_togetherness = False
            self.frame_3.hide()
            
        if self.checkBox_4.isChecked():
            self.include_separation = True
            self.frame_4.show()
            self.update_separation_widgets()
        else:
            self.include_separation = False
            self.frame_4.hide()
            
        if self.checkBox_5.isChecked():
            self.include_position_based = True
            self.frame_5.show()
        else:
            self.include_position_based = False
            self.frame_5.hide()
            
    def update_inclusion_widgets(self):
        list_text = ""
        for item in self.inclusion_set:
            list_text += " {" + item + "} "
        self.label.setText(f"Items:{list_text}")
        self.comboBox.clear()
        combo_box_items_list = []
        for item in self.saved_data:
            if (item) and (item not in self.inclusion_set):
                combo_box_items_list.append(item)
        for item in combo_box_items_list:
            self.comboBox.addItem(item)
            
    def update_exclusion_widgets(self):
        list_text = ""
        for item in self.exclusion_set:
            list_text += " {" + item + "} "
        self.label_7.setText(f"Items:{list_text}")
        self.comboBox_2.clear()
        combo_box_items_list = []
        for item in self.saved_data:
            if (item) and (item not in self.exclusion_set):
                combo_box_items_list.append(item)
        for item in combo_box_items_list:
            self.comboBox_2.addItem(item)
            
    def update_togetherness_widgets(self):
        list_text = ""
        for item in self.togetherness_set:
            list_text += " {" + item[0] + ", " + item[1] + "} "
        self.label_10.setText(f"Items:{list_text}")
        list1 = set()
        for item in self.togetherness_set:
            list1.add(item[0])
            list1.add(item[1])
        combo_box_items_list = []
        for item in self.saved_data:
            if (item) and (item not in list1):
                combo_box_items_list.append(item)
        self.comboBox_3.clear()
        self.comboBox_4.clear()
        for item in combo_box_items_list:
            self.comboBox_3.addItem(item)
            self.comboBox_4.addItem(item)
            
    def update_separation_widgets(self):
        list_text = ""
        for item in self.separation_set:
            list_text += " {" + item[0] + ", " + item[1] + "} "
        self.label_13.setText(f"Items:{list_text}")
        list1 = set()
        for item in self.separation_set:
            list1.add(item[0])
            list1.add(item[1])
        combo_box_items_list = []
        for item in self.saved_data:
            if (item) and (item not in list1):
                combo_box_items_list.append(item)
        self.comboBox_5.clear()
        self.comboBox_6.clear()
        for item in combo_box_items_list:
            self.comboBox_5.addItem(item)
            self.comboBox_6.addItem(item)
    
    def update_position_based_widgets(self):
        list_text = ""
        for item in list(self.position_set.keys()):
            list_text += " {" + item + ": " + self.position_set[item] + "} "
        self.label_16.setText(f"Items:{list_text}")
        list1 = set()
        for item in self.separation_set:
            list1.add(item[0])
            list1.add(item[1])
        combo_box_items_list = []
        for item in self.saved_data:
            if (item) and (item not in list1):
                combo_box_items_list.append(item)
        self.comboBox_5.clear()
        self.comboBox_6.clear()
        for item in combo_box_items_list:
            self.comboBox_5.addItem(item)
            self.comboBox_6.addItem(item)