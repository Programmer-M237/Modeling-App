from PySide6.QtWidgets import QWidget, QButtonGroup
from PySide6.QtCore import Signal
from another_event_state_of_property_trigger_ui import Ui_Dialog
from Entities import Entity
from global_var import Global


class Another_event_state_of_property(QWidget, Ui_Dialog):
    closed = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.setEnabled(False)
        
        option = QButtonGroup(self)
        option.addButton(self.radioButton_5)
        option.addButton(self.radioButton_6)
        option.addButton(self.radioButton_7)
        
        self.radioButton_7.setChecked(True)
        self.switch_option()
        option.buttonClicked.connect(self.switch_option)
        
        option.buttonClicked.connect(self.fill_event_combo_box)
        self.comboBox_18.currentTextChanged.connect(self.fill_properties)
        self.comboBox_16.currentTextChanged.connect(self.fill_properties)
        self.comboBox_15.currentTextChanged.connect(self.fill_properties)
        
        self.comboBox_21.currentTextChanged.connect(self.fill_states)
        self.comboBox_22.currentTextChanged.connect(self.fill_states)
        self.comboBox_23.currentTextChanged.connect(self.fill_states)
        
        self.fill_event_combo_box()
        
        self.pushButton.clicked.connect(self.returnTrigger)
        
        self.check_entries()
        
    def switch_option(self):
        if self.radioButton_5.isChecked():
            self.frame_3.show()
            self.frame_2.hide()
            self.frame.hide()
        elif self.radioButton_6.isChecked():
            self.frame_3.hide()
            self.frame_2.show()
            self.frame.hide()
        elif self.radioButton_7.isChecked():
            self.frame_3.hide()
            self.frame_2.hide()
            self.frame.show()
    
    def fill_event_combo_box(self):
        entity_registry = Entity()
        events_dict = entity_registry.get_entities_by_type("event")

        if self.radioButton_5.isChecked():
            self.comboBox_18.clear()
            for (name, type_), obj in events_dict.items():
                self.comboBox_18.addItem(name)
        elif self.radioButton_6.isChecked():
            self.comboBox_16.clear()
            for (name, type_), obj in events_dict.items():
                self.comboBox_16.addItem(name)
        elif self.radioButton_7.isChecked():
            self.comboBox_15.clear()
            for (name, type_), obj in events_dict.items():
                self.comboBox_15.addItem(name)
    
    def fill_properties(self):
        if self.radioButton_5.isChecked():
            name = self.comboBox_18.currentText()
        elif self.radioButton_6.isChecked():
            name = self.comboBox_16.currentText()
        elif self.radioButton_7.isChecked():
            name = self.comboBox_15.currentText()
        
        properties = Entity.get_entity(Entity, name, "event").properties
        self.comboBox_21.clear()
        self.comboBox_22.clear()
        self.comboBox_23.clear()
        for i in properties:
            if self.radioButton_5.isChecked():
                self.comboBox_23.addItem(i["name"])
            elif self.radioButton_6.isChecked():
                self.comboBox_22.addItem(i["name"])
            elif self.radioButton_7.isChecked():
                self.comboBox_21.addItem(i["name"])
    
    def fill_states(self):
        if self.radioButton_5.isChecked():
            name = self.comboBox_18.currentText()
        elif self.radioButton_6.isChecked():
            name = self.comboBox_16.currentText()
        elif self.radioButton_7.isChecked():
            name = self.comboBox_15.currentText()
        
        properties = Entity.get_entity(Entity, name, "event").properties
        
        if self.radioButton_5.isChecked():
            name = self.comboBox_23.currentText()
        elif self.radioButton_6.isChecked():
            name = self.comboBox_22.currentText()
        elif self.radioButton_7.isChecked():
            name = self.comboBox_21.currentText()
        
        self.comboBox_14.clear()
        self.comboBox_17.clear()
        self.comboBox_19.clear()
        
        for i in properties:
            print(i)
            if i["name"] == name:
                list_e = i["forms"]
                print(list_e)
                print(i["forms"])
                for j in list_e:
                    if self.radioButton_5.isChecked():
                        self.comboBox_19.addItem(j)
                    elif self.radioButton_6.isChecked():
                        self.comboBox_17.addItem(j)
                    if self.radioButton_7.isChecked():
                        self.comboBox_14.addItem(j)
                        
    def returnTrigger(self):
        Global.trigger.clear()
        Global.trigger["option"] = 4
        if self.radioButton_5.isChecked():
            Global.trigger["event"] = self.comboBox_18.currentText()
            Global.trigger["property"] = self.comboBox_23.currentText()
            Global.trigger["state"] = self.comboBox_19.currentText()
            Global.trigger["state_t"] = "Next State"
        elif self.radioButton_6.isChecked():
            Global.trigger["event"] = self.comboBox_16.currentText()
            Global.trigger["property"] = self.comboBox_22.currentText()
            Global.trigger["state"] = self.comboBox_17.currentText()
            Global.trigger["state_t"] = "Present State"
        elif self.radioButton_7.isChecked():
            Global.trigger["event"] = self.comboBox_15.currentText()
            Global.trigger["property"] = self.comboBox_21.currentText()
            Global.trigger["state"] = self.comboBox_14.currentText()
            Global.trigger["state_t"] = "Previous State"
        Global.triggers_list.append(Global.trigger.copy())
        self.closed.emit()
        print(Global.triggers_list)
        
    def check_entries(self):
        if self.radioButton_5.isChecked():
            boolr = (self.comboBox_18.count() > 0)
        elif self.radioButton_6.isChecked():
            boolr = (self.comboBox_16.count() > 0)
        elif self.radioButton_7.isChecked():
            boolr = (self.comboBox_15.count() > 0)
        self.pushButton.setEnabled(boolr)
