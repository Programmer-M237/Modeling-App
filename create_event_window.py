from PySide6.QtWidgets import QDialog, QApplication, QButtonGroup, QMessageBox
from step_1_of_event_creation_ui import Ui_Dialog
from entities import EntityManager
from create_Eobject_window import Create_new_Eobject
from step_2_of_event_creation import Event_properties
from temp_events import Events

import sys

class Create_new_event(QDialog, Ui_Dialog):
    is_name_valid = False
    is_comboBox_filled = False
    is_close_initiated_by_code = False
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.frame_3.hide()
        self.label_3.hide()
        self.resize(1400, 900)
        self.setMinimumSize(800, 600)
        self.pushButton_2.setEnabled(False)
        self.label.hide()
        
        obj = QButtonGroup(self)
        self.radioButton.setChecked(True)
        obj.addButton(self.radioButton)
        obj.addButton(self.radioButton_2)
        obj.buttonClicked.connect(self.update_object_type_list)
        obj.buttonClicked.connect(self.check_entries)
        self.update_object_type_list()
        
        self.pushButton.clicked.connect(self.cancel_clicked)
        
        self.pushButton_2.clicked.connect(self.next_step)
        
        self.lineEdit.textChanged.connect(self.check_if_name_exist)
        self.lineEdit.textChanged.connect(self.check_entries)
        
    def update_object_type_list(self):
        if self.radioButton.isChecked():
            self.frame_3.show()
            self.update_existx_objects()
        else:
            self.frame_3.hide()
        if self.radioButton_2.isChecked():
            self.label_3.show()
        else:
            self.label_3.hide()
            
    def update_existx_objects(self):
        objects_list = []
        for obj in EntityManager._items:
            if obj[1] == "object":
                objects_list.append(obj)
        #print(objects_list)
        if len(objects_list) < 1:
            self.is_comboBox_filled = False
        else:
            self.is_comboBox_filled = True
        self.comboBox.clear()
        for obj in objects_list:
            self.comboBox.addItem(EntityManager._items[obj].name)
            
    def cancel_clicked(self):
        self.close() # Problem 004
    
    #### Problem 004
    def closeEvent(self, event):
        if self.is_close_initiated_by_code == True:
            event.accept()
        else:
            cancel = QMessageBox.question(self, "Exit", "Do you want to cancel this event creation process?",QMessageBox.Yes | QMessageBox.No)
            if cancel == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
    #### Problem 004
    
    def next_step(self):
        if self.radioButton.isChecked():
            sel_obj = self.comboBox.currentText()
            obj = EntityManager._items[(sel_obj, "object")]
            event = Events(self.lineEdit.text().strip(), obj.number_system)
            window = Event_properties(event)
            self.hide()
            window.close_by_code_initiated.connect(self.close_by_code)
            window.exec()
            self.close()
            return
        elif self.radioButton_2.isChecked():
            #self.close()
            window = Create_new_Eobject(f"Object or database of event's {self.lineEdit.text().strip()}", event_name=self.lineEdit.text().strip()) # The word "event" will be sent to all the components of the objects creation to adjust themselves for event database creation
            self.hide()
            window.close_by_code_initiated.connect(self.close_by_code)
            window.exec()
            self.close()
            return
            
    def check_if_name_exist(self) -> None:
        name = self.lineEdit.text().strip()
        
        if not(name):
            self.is_name_valid = False
        elif (name, "event") in EntityManager._items:
            self.label.setText("❌ An event with the same name already exists")
            self.label.show()
            self.is_name_valid = False
        elif EntityManager.name_exists_with_different_type(EntityManager, name, "object"):
            self.label.setText("⚠️ An object or system with the same name already exists")
            self.label.show()
            self.is_name_valid = True
        else:
            self.label.hide()
            self.is_name_valid = True
        self.check_entries()
        
    def check_entries(self):
        if self.radioButton.isChecked():
            self.pushButton_2.setEnabled(self.is_comboBox_filled and self.is_name_valid)
        elif self.radioButton_2.isChecked():
            self.pushButton_2.setEnabled(self.is_name_valid)
            
    def close_by_code(self):
        self.is_close_initiated_by_code = True
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Create_new_event()
    window.show()
    app.exec()
    # if app.exec():
    #     window = Create_new_event()
    #     app.exec()