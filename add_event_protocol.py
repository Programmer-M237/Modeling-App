# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QDialog
from add_event_trigger_ui import Ui_Dialog
from PySide6.QtCore import Qt, Signal
from direct_event_protocol import Direct_event_protocol
from incremental_or_decremental_event_protocol import Incremental_or_decremental_event_protocol


class Add_event_protocol(QDialog, Ui_Dialog):
    is_comboBox_filled = False
    closed = Signal()
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Add event protocol")
        self.setWindowFlags(Qt.Window | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.resize(700, 450)
        self.setMinimumSize(400, 300)
        
        # Creating and adding event trigger pages to stacked widget
        self.direct_protocol = Direct_event_protocol()
        self.incremental_or_decremental_protocol = Incremental_or_decremental_event_protocol()
        
        self.stackedWidget.addWidget(self.direct_protocol)
        self.stackedWidget.addWidget(self.incremental_or_decremental_protocol)
        
        # Add default event protocols to combo box
        self.comboBox_3.clear()
        self.comboBox_3.addItem("Direct")
        self.comboBox_3.addItem("Incremental or decremental")
        
        self.comboBox_3.setCurrentText("Direct")
        self.stackedWidget.setCurrentWidget(self.direct_protocol)
        
        self.comboBox_3.currentTextChanged.connect(self.switch_to_page)  # Switch to page when combo box item changed
        
        self.direct_protocol.closed.connect(self.add_protocol)
        self.incremental_or_decremental_protocol.closed.connect(self.add_protocol)
        
    def switch_to_page(self):
        if self.comboBox_3.currentText() == "Direct":
            self.stackedWidget.setCurrentWidget(self.direct_protocol)
        elif self.comboBox_3.currentText() == "Incremental or decremental":
            self.stackedWidget.setCurrentWidget(self.incremental_or_decremental_protocol)
            
    def add_protocol(self):
        self.closed.emit()
        self.close()
