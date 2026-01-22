from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from incremental_or_decremental_protocol_ui import Ui_Dialog
from global_var import Global


class Incremental_or_decremental_event_protocol(QWidget, Ui_Dialog):
    closed = Signal()
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Add default protocol type
        self.comboBox_4.addItem("Incremental")
        self.comboBox_4.addItem("Decremental")
        
        self.switch_protocol_type()
        self.comboBox_4.currentTextChanged.connect(self.switch_protocol_type)
        
        # Add default stats
        self.comboBox_5.addItem("Previous state")
        self.comboBox_6.addItem("Previous state")
        self.comboBox_5.addItem("Present state")
        self.comboBox_6.addItem("Present state")
        self.comboBox_5.addItem("Next state")
        self.comboBox_6.addItem("Next state")
        
        # Set spinbox limits
        self.spinBox_3.setRange(1, len(Global.obj[0].system) - 1)
        self.spinBox_4.setRange(1, len(Global.obj[0].system) - 1)
        
        self.pushButton.clicked.connect(self.returnProtocol)
        
    def switch_protocol_type(self):
        if self.comboBox_4.currentText() == "Incremental":
            self.stackedWidget_2.setCurrentIndex(0)
        else:
            self.stackedWidget_2.setCurrentIndex(1)
            
    def returnProtocol(self):
        Global.protocol.clear()
        Global.protocol["option"] = 3
        Global.protocol["type"] = self.comboBox_4.currentText()
        if self.comboBox_4.currentText() == "Incremental":
            Global.protocol["sub-option"] = 1
            Global.protocol["state"] = self.comboBox_5.currentText()
            Global.protocol["value"] = self.spinBox_3.value()
        else:
            Global.protocol["sub-option"] = 2
            Global.protocol["state"] = self.comboBox_6.currentText()
            Global.protocol["value"] = self.spinBox_4.value()
        Global.protocols_list.append(Global.protocol.copy())
        self.closed.emit()
        print(Global.protocols_list)