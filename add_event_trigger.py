# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QDialog
from add_event_trigger_ui import Ui_Dialog
from PySide6.QtCore import Qt, Signal
from time_delay_trigger import Time_delay
from another_event_occurring_trigger import Another_event_occurring
from another_event_state_of_property_trigger import Another_event_state_of_property
from another_event_state_trigger import Another_event_state


class Add_event_trigger(QDialog, Ui_Dialog):
    is_comboBox_filled = False
    closed_time_delay = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Add event trigger")
        self.setWindowFlags(Qt.Window | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.resize(700, 450)
        self.setMinimumSize(400, 300)

        # Creating and adding event trigger pages to stacked widget
        self.time_delay = Time_delay()
        self.another_event_state = Another_event_state()
        self.another_event_state_of_property = Another_event_state_of_property()
        self.another_event_occurring = Another_event_occurring()
        
        self.stackedWidget.addWidget(self.time_delay)
        self.stackedWidget.addWidget(self.another_event_state_of_property)
        self.stackedWidget.addWidget(self.another_event_occurring)
        self.stackedWidget.addWidget(self.another_event_state)
        
        # Add default event triggers to combo box
        self.comboBox_3.clear()
        self.comboBox_3.addItem("Time delay")
        self.comboBox_3.addItem("Another event state")
        self.comboBox_3.addItem("Another event occurring")
        self.comboBox_3.addItem("Another event state of property")
        
        self.comboBox_3.setCurrentText("Time delay")
        self.stackedWidget.setCurrentWidget(self.time_delay)
        
        self.comboBox_3.currentTextChanged.connect(self.switch_to_page)  # Switch to page when combo box item changed
        
        self.time_delay.closed.connect(self.add_trigger)
        self.another_event_occurring.closed.connect(self.add_trigger)
        self.another_event_state_of_property.closed.connect(self.add_trigger)
        self.another_event_state.closed.connect(self.add_trigger)
        
    def switch_to_page(self):
        #print(self.comboBox_3.currentText())
        if self.comboBox_3.currentText() == "Time delay":
            self.stackedWidget.setCurrentWidget(self.time_delay)
        elif self.comboBox_3.currentText() == "Another event state":
            self.stackedWidget.setCurrentWidget(self.another_event_state)
        elif self.comboBox_3.currentText() == "Another event occurring":
            self.stackedWidget.setCurrentWidget(self.another_event_occurring)
        elif self.comboBox_3.currentText() == "Another event state of property":
            self.stackedWidget.setCurrentWidget(self.another_event_state_of_property)
            
    def add_trigger(self):
        self.closed_time_delay.emit()
        self.close()
