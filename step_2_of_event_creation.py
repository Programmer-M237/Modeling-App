import signal
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal
from step_2_of_event_creation_ui import Ui_Dialog
from temp_events import Events

class Event_properties(QDialog, Ui_Dialog):
    close_by_code_initiated = Signal()
    def __init__(self, m_event: Events): # m_events = Modeling Events (Used because python conflicted event with it built in method)
        # The obj parameter is an object of the temp_objects singleton, not the original objects singleton. This object will be deleted if the event creation process is completed to save memory space
        # Temporal and incomplete objects and events are created because the user may not complete the event creation process, so if in case we began storing the data in the really singletons, it may cause a problem. So temporal and incompleted objects and singletons are created to hold the data and may be deleted at the end if the event creation process is completed. Which if not completed, they will still be deleted
        super().__init__()
        self.setupUi(self)
        self.resize(1400, 900)
        self.setMinimumSize(800, 600)
        self.m_event = m_event
        print("*")
        print(m_event.database)
        print("*")
        
        # self.label.clear()
        # listt = []
        # for i in m_event.database:
        #     text = "["
        #     for j in i:
        #         text += str(j) + ", "
        #     text += "]"
        #     listt.append(text)
        # #print(listt)
        # for i in range(len(listt)):
        #     self.label.setText(self.label.text() + "\n" + listt[i])
        # if not obj == None:
        #     self.label.setText(self.label.text().strip() + " " + obj.number_system + "\n")
        
    def closeEvent(self, event):
        self.close_by_code_initiated.emit()
        event.accept()