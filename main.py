from PySide6.QtWidgets import QMainWindow, QApplication
from main_ui import Ui_MainWindow # Main app UI
from create_object_window import Create_new_object
from create_event_window import Create_new_event
import sys

class Modeling_App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.statusbar.show()
        
        self.create_object_button.clicked.connect(self.create_object)
        
        self.create_event_button.clicked.connect(self.create_event)
        
    def create_object(self):
        create_object_win = Create_new_object()
        create_object_win.exec()
        
    def create_event(self):
        create_event_win = Create_new_event()
        create_event_win.exec()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Modeling_App()
    window.showMaximized()
    app.exec()