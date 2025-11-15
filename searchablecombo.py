from PySide6.QtWidgets import QComboBox, QListView
from PySide6.QtCore import Qt

class SearchableCombo(QComboBox):
    def __init__(self, placeholder="Search...", parent=None):
        super().__init__()
        
        self.setEditable(True)
        
        self.lineEdit().setPlaceholderText(placeholder)
        self.setInsertPolicy(QComboBox.NoInsert)
        
        self._all_items = []
        
        self.lineEdit().textEdited.connect(self._filter_items)
        
        self.lineEdit().returnPressed.connect(self._validate_selection)
        
    def addItems(self, items):
        super().addItems(items)
        self._all_items = items[:]
        
    def _filter_items(self, text):
        self.clear()
        if not text:
            super().addItems(self._all_items)
        else:
            filtered = [i for i in self._all_items if text.lower() in i.lower()]
            if filtered:
                super().addItems(filtered)
            else:
                super().addItem("❌ No results found")
        self.showPopup()
        
    def _validate_selection(self):
        text = self.currentText()
        matches = [i for i in self._all_items if i.lower().startswith(text.lower())]
        if matches:
            idx = self._all_items.index(matches[0])
            self.setCurrentText(matches[0])
            self.setCurrentIndex(idx)
        else:
            self.lineEdit.clear()