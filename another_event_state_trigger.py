from PySide6.QtWidgets import QWidget, QButtonGroup
from PySide6.QtCore import Signal
from another_event_state_trigger_ui import Ui_Dialog
from global_var import Global
from Entities import Entity


class Another_event_state(QWidget, Ui_Dialog):
    closed = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.setEnabled(False)
        
        option = QButtonGroup(self)
        option.addButton(self.radioButton_8)
        option.addButton(self.radioButton_9)
        option.addButton(self.radioButton_10)
        
        self.radioButton_8.setChecked(True)
        self.switch_option()
        option.buttonClicked.connect(self.switch_option)
        
        option.buttonClicked.connect(self.fill_event_combo_box)
        self.comboBox_10.currentTextChanged.connect(self.fill_states)
        self.comboBox_11.currentTextChanged.connect(self.fill_states)
        self.comboBox_12.currentTextChanged.connect(self.fill_states)
        
        self.fill_event_combo_box()
        
        self.pushButton.clicked.connect(self.returnTrigger)
        
        self.check_entries()
        
    def switch_option(self):
        if self.radioButton_8.isChecked():
            self.frame.show()
            self.frame_2.hide()
            self.frame_3.hide()
        elif self.radioButton_9.isChecked():
            self.frame.hide()
            self.frame_2.show()
            self.frame_3.hide()
        elif self.radioButton_10.isChecked():
            self.frame.hide()
            self.frame_2.hide()
            self.frame_3.show()
            
    def fill_event_combo_box(self):
        entity_registry = Entity()
        events_dict = entity_registry.get_entities_by_type("event")
        
        if self.radioButton_8.isChecked():
            self.comboBox_10.clear()
            for (name, type_), obj in events_dict.items():
                self.comboBox_10.addItem(name)
        elif self.radioButton_9.isChecked():
            self.comboBox_11.clear()
            for (name, type_), obj in events_dict.items():
                self.comboBox_11.addItem(name)
        elif self.radioButton_10.isChecked():
            self.comboBox_12.clear()
            for (name, type_), obj in events_dict.items():
                self.comboBox_12.addItem(name)
                
    def fill_states(self):
        self.comboBox_13.clear()
        self.comboBox_14.clear()
        self.comboBox_15.clear()
        
        if self.radioButton_8.isChecked():
            name = self.comboBox_10.currentText()
        elif self.radioButton_9.isChecked():
            name = self.comboBox_11.currentText()
        elif self.radioButton_10.isChecked():
            name = self.comboBox_12.currentText()
            
        states = Entity.get_entity(Entity, name, "event").database
        
        for item in range(len(states)):
            text = states[item][0]
            for i in range(len(states[item])):
                if (i + 1) == len(states[item]):
                    break
                text = f"{text}, {states[item][i + 1]}"
            text = f"{text} - Index {item}"
            
            if self.radioButton_8.isChecked():
                self.comboBox_13.addItem(text)
            elif self.radioButton_9.isChecked():
                self.comboBox_14.addItem(text)
            elif self.radioButton_10.isChecked():
                self.comboBox_15.addItem(text)
                
    def returnTrigger(self):
        Global.trigger.clear()
        Global.trigger["option"] = 5
        if self.radioButton_8.isChecked():
            Global.trigger["event"] = self.comboBox_10.currentText()
            Global.trigger["state"] = self.comboBox_13.currentIndex()
            Global.trigger["state_t"] = "Previous State"
        elif self.radioButton_9.isChecked():
            Global.trigger["event"] = self.comboBox_11.currentText()
            Global.trigger["state"] = self.comboBox_14.currentIndex()
            Global.trigger["state_t"] = "Present State"
        elif self.radioButton_10.isChecked():
            Global.trigger["event"] = self.comboBox_12.currentText()
            Global.trigger["state"] = self.comboBox_15.currentIndex()
            Global.trigger["state_t"] = "Next State"
        Global.triggers_list.append(Global.trigger.copy())
        self.closed.emit()
        print(Global.triggers_list)
        
    def check_entries(self):
        if self.radioButton_8.isChecked():
            boolr = (self.comboBox_10.count() > 0)
        elif self.radioButton_9.isChecked():
            boolr = (self.comboBox_11.count() > 0)
        elif self.radioButton_10.isChecked():
            boolr = (self.comboBox_12.count() > 0)
        self.pushButton.setEnabled(boolr)