from PySide6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QTableWidget, QAbstractItemView, QMessageBox
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon, QColor
from object_07_group_info_view_ui import Ui_Dialog

class Group_data_info(QWidget, Ui_Dialog):
    def __init__(self, data, total, order_matters, repetitions_allowed, num_of_its):
        super().__init__()
        self.setupUi(self)
        self.data = data
        self.sum = sum
        self.total = total
        self.order_matters = order_matters
        self.repetitions_allowed = repetitions_allowed
        self.populate_table()
        self.setWindowTitle("Summary of groups information")
        self.setWindowIcon(QIcon())
        self.spinBox_2.setRange(1, 1000)
        self.resize(960, 300)
        
        #self.tableWidget.setSizeAdjustPolicy(self.tableWidget.AdjustToContents)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.resizeRowToContents(True)
        self.tableWidget.resizeColumnToContents(True)
        
        self.scrollArea.setWidgetResizable(True)
        
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        
        #header.setStretchLastSection(True)
        
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        
        #self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)
        
        self.pushButton_7.clicked.connect(self.go_to_row)
        
        self.label.setText(f"Total number of items: {total}\nNumber of items to select: {num_of_its}\nOrder matters:  {self.order_matters}\nRepetitions allowed: {self.repetitions_allowed}")
        
    def populate_table(self):
        headers = ["Property name", "Number of items", "Validity"]
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)
        rows = len(self.data)
        cols = len(self.data[0]) if rows > 0 else 0
        self.tableWidget.setRowCount(rows)
        self.tableWidget.setColumnCount(cols)
        
        for row in range(rows):
            for col in range(cols):
                item = QTableWidgetItem(str(self.data[row][col]))
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                item.setToolTip(item.text())
                self.tableWidget.setItem(row, col, item)
                
    def go_to_row(self):
        row = self.spinBox_2.value() - 1
        item = self.tableWidget.item(row, 0)
        if item:
            self.tableWidget.scrollToItem(item, QAbstractItemView.PositionAtCenter)
        else:
            QMessageBox.warning(self, "Navigation Error", "Row not found")
        self.highlight_temporarily(self.tableWidget, row, duration=2000)
        
    def highlight_temporarily(self, table_widget: QTableWidget, row_index, color="#FFFF99", duration: int = 2000):
        if row_index < 0 or row_index >= table_widget.rowCount():
            return
        
        items = [table_widget.item(row_index, col) for col in range(table_widget.columnCount())]
        
        original_brushes = [item.background() if item else None for item in items]
        
        for item in items:
            if item:
                item.setBackground(QColor(color))
                
        def restore():
            for item, brush in zip(items, original_brushes):
                if item:
                    if brush:
                        item.setBackground(brush)
                    else:
                        item.setBackground(QColor("transparent"))

        QTimer.singleShot(duration, restore)