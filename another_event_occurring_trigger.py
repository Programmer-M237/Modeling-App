from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from another_event_occurring_trigger_ui import Ui_Dialog
from Entities import Entity
from global_var import Global


class Another_event_occurring(QWidget, Ui_Dialog):
    closed = Signal()
    is_comboBox_filled = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.setEnabled(False)
        
        self.add_events()
        
        self.check_entries()
        self.comboBox.currentTextChanged.connect(self.check_entries)
        
        self.pushButton.clicked.connect(self.returnTrigger)
        
    def add_events(self):
        entity_registry = Entity()
        objects_dict = entity_registry.get_entities_by_type("event")

        if len(objects_dict) < 1:
            self.is_comboBox_filled = False
        else:
            self.is_comboBox_filled = True

        self.comboBox.clear()
        for (name, type_), obj in objects_dict.items():
            self.comboBox.addItem(name)
            
    def check_entries(self):
        if self.is_comboBox_filled:
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)
            
    def returnTrigger(self):
        Global.trigger.clear()
        Global.trigger["option"] = 3
        Global.trigger["event"] = self.comboBox.currentText()
        Global.triggers_list.append(Global.trigger.copy())
        self.closed.emit()
        print(Global.triggers_list)