from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from direct_protocol_ui import Ui_Dialog
from global_var import Global


class Direct_event_protocol(QWidget, Ui_Dialog):
    closed = Signal()
    is_comboBox_filled = False
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Add default direct protocols to combo box
        self.comboBox_2.addItem("Previous state")
        self.comboBox_2.addItem("Present state")
        self.comboBox_2.addItem("Random state")
        
        self.comboBox_2.setCurrentText("Random state")
        self.switch_random()
        
        self.comboBox_2.currentTextChanged.connect(self.switch_random)
        self.comboBox_2.currentTextChanged.connect(self.check_entries)
        self.check_entries()
        self.spinBox.valueChanged.connect(self.check_entries)
        self.spinBox_2.valueChanged.connect(self.check_entries)
        
        self.set_spin_box_limit()
        
        self.pushButton.clicked.connect(self.returnProtocol)
        
    def switch_random(self):
        if self.comboBox_2.currentText() == "Random state":
            self.frame.show()
        else:
            self.frame.hide()
    
    def check_entries(self):
        if self.comboBox_2.currentText() != "Random state":
            self.pushButton.setEnabled(True)
        else:
            boolr = not (self.spinBox_2.value() >= self.spinBox.value())
            self.pushButton.setEnabled(boolr)
            
    def set_spin_box_limit(self):
        '''Sets the limit of the index of state index by getting the number of states from the event object or database'''
        self.spinBox.setRange(0, len(Global.obj[0].system) - 1)
        self.spinBox_2.setRange(0, len(Global.obj[0].system) - 1)
        self.spinBox.setValue(0)
        self.spinBox_2.setValue(0)
        
    def returnProtocol(self):
        Global.protocol.clear()
        if self.comboBox_2.currentText() == "Random state":
            Global.protocol["option"] = 1
            Global.protocol["lower state"] = self.spinBox_2.value()
            Global.protocol["upper state"] = self.spinBox.value()
        else:
            Global.protocol["option"] = 2
            Global.protocol["state"] = self.comboBox_2.currentText()
        Global.protocols_list.append(Global.protocol.copy())
        self.closed.emit()
        print(Global.protocols_list)