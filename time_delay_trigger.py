from PySide6.QtWidgets import QWidget, QButtonGroup
from PySide6.QtCore import Signal
from time_delay_trigger_ui import Ui_Dialog
from global_var import Global


class Time_delay(QWidget, Ui_Dialog):
    closed = Signal()
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.doubleSpinBox.setMinimum(0.1)
        self.doubleSpinBox.setValue(1.0)
        self.doubleSpinBox_3.setMinimum(0.1)
        self.doubleSpinBox_4.setMinimum(0.1)
        
        option = QButtonGroup(self)
        option.addButton(self.radioButton)
        option.addButton(self.radioButton_3)
        self.radioButton.setChecked(True)
        self.option_f()
        
        option.buttonClicked.connect(self.option_f)
        option.buttonClicked.connect(self.check_entries)
        
        # Connections to slots
        self.doubleSpinBox.valueChanged.connect(self.check_entries)
        self.doubleSpinBox_3.valueChanged.connect(self.check_entries)
        self.doubleSpinBox_4.valueChanged.connect(self.check_entries)
        
        # Add Trigger button
        self.pushButton.clicked.connect(self.returnTrigger)
        
        # Clearing the entries of the global_var module which may be a singleton
        # Global.trigger.clear()
        # Global.triggers_list.clear()
        
    def option_f(self):
        if self.radioButton.isChecked():
            self.frame.show()
            self.frame_2.hide()
        else:
            self.frame.hide()
            self.frame_2.show()
            
    def check_entries(self):
        '''Checks if the time entered is in the right range'''
        if self.radioButton_3.isChecked():
            boolr = not (self.doubleSpinBox_4.value() >= self.doubleSpinBox_3.value())
        else:
            boolr = True
        self.pushButton.setEnabled(boolr)
        
    def returnTrigger(self):
        Global.trigger.clear()
        if self.radioButton.isChecked():
            Global.trigger["option"] = 1
            Global.trigger["time"] = self.doubleSpinBox.value()
        elif self.radioButton_3.isChecked():
            Global.trigger["option"] = 2
            Global.trigger["lower time"] = self.doubleSpinBox_4.value()
            Global.trigger["upper time"] = self.doubleSpinBox_3.value()
        Global.triggers_list.append(Global.trigger.copy())
        self.closed.emit()
        print(Global.triggers_list)
