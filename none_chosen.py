from none_chosen_ui import Ui_Dialog
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

class None_chosen_page(QWidget):
    cancel_clicked = Signal()
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.name = "none"
        
        self.ui.pushButton.clicked.connect(self.cancel_clicked.emit)