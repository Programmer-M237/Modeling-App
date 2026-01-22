# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QDialog, QTreeWidgetItem
from create_event_ui import Ui_Dialog
from PySide6.QtCore import Qt
from Entities import Entity
from add_event_trigger import Add_event_trigger
from add_event_protocol import Add_event_protocol
from global_var import Global
from events import Events


class Create_new_event(QDialog, Ui_Dialog):
    is_comboBox_filled = False
    is_name_valid = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Create new event")
        self.setWindowFlags(Qt.Window | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.resize(1400, 900)
        self.setMinimumSize(800, 600)
        self.doubleSpinBox.setDecimals(1)
        self.pushButton_3.setEnabled(False)
        self.label_6.hide()

        # When switch to step 1 of the stacked widget
        self.stackedWidget.setCurrentIndex(3)
        self.update_existx_objects()
        
        # Required connections
        self.lineEdit.textChanged.connect(self.check_step_1)
        
        # Step 2 (event triggers) functionalities
        self.pushButton_3.clicked.connect(self.switch_to_step_2)  # Switches to page 2 when next clicked
        self.pushButton.clicked.connect(self.open_add_event_trigger_window)
        self.treeWidget.clear()
        
        self.pushButton_7.clicked.connect(self.delete_tree_widget_event_item)
        
        self.pushButton_4.clicked.connect(self.switch_to_step_3)  # Switches to page 3 when next clicked
        self.pushButton_2.clicked.connect(self.open_add_event_protocol_window)
        
        self.pushButton_8.clicked.connect(self.delete_tree_widget_protocol_item)
        
        self.pushButton_5.clicked.connect(self.switch_to_step_4)
        
        self.pushButton_6.clicked.connect(self.create_event)

    def update_existx_objects(self):
        '''
        This gets all the created objects stored in the entity class and add them to the comboBox
        '''
        entity_registry = Entity()
        objects_dict = entity_registry.get_entities_by_type("object")

        if len(objects_dict) < 1:
            self.is_comboBox_filled = False
        else:
            self.is_comboBox_filled = True

        self.comboBox.clear()
        for (name, type_), obj in objects_dict.items():
            self.comboBox.addItem(name)

    def open_add_event_trigger_window(self):
        add_event_trigger_window = Add_event_trigger()
        add_event_trigger_window.closed_time_delay.connect(self.add_time_delay_trigger)
        add_event_trigger_window.exec()
        
    def open_add_event_protocol_window(self):
        add_event_protocol_window = Add_event_protocol()
        add_event_protocol_window.closed.connect(self.add_protocol)
        add_event_protocol_window.exec()
        
    def check_if_name_exist(self):
        '''
        Checks if the name for the event to be created with is already used by an existing event
        '''
        name = self.lineEdit.text().strip()
        
        if not name:
            self.is_name_valid = False
        elif Entity.entity_exists(Entity, name, "event"):
            self.label_6.show()
            self.is_name_valid = False
        else:
            self.label_6.hide()
            self.is_name_valid = True
            
    def check_step_1(self):
        '''Check the entries of step 1 page, so that it can enable the next button if valid'''
        self.check_if_name_exist()
        boolean = self.is_name_valid and self.is_comboBox_filled
        # print(f"{self.is_comboBox_filled} || {self.is_name_valid}")
        if boolean:
            self.pushButton_3.setEnabled(True)
        else:
            self.pushButton_3.setEnabled(False)
            
    def switch_to_step_2(self):
        '''Simply moves to the add event triggers page'''
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_4.setEnabled(False)
        self.treeWidget.clear()
        Global.trigger.clear()
        Global.triggers_list.clear()
        
        Global.obj.clear()
        Global.obj.append(Entity.get_entity(Entity, self.comboBox.currentText(), "object"))
        print(Global.obj[0])
        self.check_event_triggers()
        
    def add_time_delay_trigger(self):
        """Adds the time delay trigger created to the tree widget of the create event window and the triggers_list list of dictionaries (triggers)"""
        # print("Test")
        # print(Global.triggers_list)
        if Global.trigger["option"] == 1:
            # print("Test XXX")
            item = QTreeWidgetItem([f"After {Global.trigger["time"]} seconds delay from previous occurrance"])
        elif Global.trigger["option"] == 2:
            # print("Test XXX")
            item = QTreeWidgetItem([f"After random time delay between the range of {Global.trigger["lower time"]} and {Global.trigger["upper time"]} seconds from previous occurrance"])
        elif Global.trigger["option"] == 3:
            item = QTreeWidgetItem([f"When event {Global.trigger["event"]} is occurring"])
        elif Global.trigger["option"] == 4:
            item = QTreeWidgetItem([f"When {Global.trigger["state_t"]} of property {Global.trigger["property"]} of event {Global.trigger["event"]} is {Global.trigger["state"]}"])
        elif Global.trigger["option"] == 5:
            item = QTreeWidgetItem([f"When {Global.trigger["state_t"]} of {Global.trigger["event"]} is state of index {Global.trigger["state"]}"])
        self.treeWidget.addTopLevelItem(item)
        self.check_event_triggers()
        
    def add_protocol(self):
        """Add protocol created to the tree widget of the create protocol window and the protocols_list list of dictionaries (protocols)"""
        if Global.protocol["option"] == 1:
            item = QTreeWidgetItem([f"Next state == Random state between state {Global.protocol["lower state"]} and state {Global.protocol["upper state"]} of the event's object or database"])
        elif Global.protocol["option"] == 2:
            item = QTreeWidgetItem([f"Next state == {Global.protocol["state"]}"])
        elif Global.protocol["option"] == 3:
            if Global.protocol["sub-option"] == 1:
                item = QTreeWidgetItem([f"Next state == {Global.protocol["state"]} + {Global.protocol["value"]}"])
            else:
                item = QTreeWidgetItem([f"Next state == {Global.protocol["state"]} - {Global.protocol["value"]}"])
        self.treeWidget_2.addTopLevelItem(item)
        self.check_event_protocols()
        
    def delete_tree_widget_event_item(self):
        '''Delete the selected event trigger(s) from the triggers_list and the create new event window tree widget'''
        selected_items = self.treeWidget.selectedItems()
        
        for item in selected_items:
            index = self.treeWidget.indexOfTopLevelItem(item)
            del Global.triggers_list[index]  # delete the trigger from the list
            self.treeWidget.takeTopLevelItem(index)  # delete the trigger in the UI
            print(Global.triggers_list)
        self.check_event_triggers()
        
    def delete_tree_widget_protocol_item(self):
        '''Delete the selected event protocol(s) from the protocols_list and the create new event window tree widget'''
        selected_items = self.treeWidget_2.selectedItems()
        
        for item in selected_items:
            index = self.treeWidget_2.indexOfTopLevelItem(item)
            del Global.protocols_list[index]  # delete the protocol from the list
            self.treeWidget_2.takeTopLevelItem(index)  # delete the protocol in the UI
        print(Global.protocols_list)
        self.check_event_protocols()

    def check_event_triggers(self):
        '''Enables or disables the next button to step 2, if the triggers_list has triggers'''
        if len(Global.triggers_list) > 0:
            self.pushButton_4.setEnabled(True)
            self.pushButton_7.setEnabled(True)
        else:
            self.pushButton_4.setEnabled(False)
            self.pushButton_7.setEnabled(False)
            
    def check_event_protocols(self):
        '''Enables or disables the next button to step 3, if the protocols_list has protocols. And ensure that only one protocol is created'''
        if len(Global.protocols_list) > 0:
            self.pushButton_5.setEnabled(True)
            self.pushButton_2.setEnabled(False)
            self.pushButton_8.setEnabled(True)
        else:
            self.pushButton_5.setEnabled(False)
            self.pushButton_2.setEnabled(True)
            self.pushButton_8.setEnabled(False)

    def switch_to_step_3(self):
        '''Simply moves to the add event protocol page'''
        self.stackedWidget.setCurrentIndex(1)
        self.treeWidget_2.clear()
        Global.protocol.clear()
        Global.protocols_list.clear()
        self.check_event_protocols()

    def switch_to_step_4(self):
        '''Simply moves to the add initial conditions page'''
        self.stackedWidget.setCurrentIndex(2)
        self.fill_with_states()
        
    def fill_with_states(self):
        for item in range(len(Global.obj[0].system)):
            text = Global.obj[0].system[item][0]
            for i in range(len(Global.obj[0].system[item])):
                if (i + 1) == len(Global.obj[0].system[item]):
                    break
                text = f"{text}, {Global.obj[0].system[item][i + 1]}"
            text = f"{text} - Index {item}"
            self.comboBox_2.addItem(text)
            self.comboBox_3.addItem(text)
            
    def create_event(self):
        '''Note that, the present previous, and next state will store the index of their state and not the state'''
        name = self.lineEdit.text().strip()
        present_state = self.comboBox_3.currentIndex()
        previous_state = self.comboBox_2.currentIndex()
        database = Global.obj[0].system
        triggers = Global.triggers_list.copy()
        protocol = Global.protocols_list.copy()
        properties = Global.obj[0].properties
        
        event = Events(name, present_state, previous_state, database, triggers, protocol, properties)
        Entity.add_entity(Entity, name, "event", event)
        for i in Entity.get_all_entities(Entity):
            print(i)
        print(f"{event.present_state} | {event.previous_state}")
        
        Global.trigger.clear()
        Global.triggers_list.clear()
        Global.obj.clear()
        Global.protocol.clear()
        Global.protocols_list.clear()
        
        self.close()
