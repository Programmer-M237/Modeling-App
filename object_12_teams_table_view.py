from PySide6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QTableWidget, QAbstractItemView, QMessageBox
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon, QColor
from object_12_teams_table_view_ui import Ui_Dialog

class Teams_data_info(QWidget, Ui_Dialog):
    def __init__(self, data, sum, nom, team_order, members_order):
        super().__init__()
        self.setupUi(self)
        self.data = data
        self.sum = sum
        self.number_of_members = nom
        self.populate_table()
        self.setWindowTitle("Summary of teams information")
        self.setWindowIcon(QIcon())
        self.spinBox_2.setRange(1, 1000)
        
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
        
        if self.sum != self.number_of_members:
            self.label.setStyleSheet("""
                                     QLabel {
                                         color: red
                                     }
                                     """)
        else:
            self.label.setStyleSheet("""
                                     QLabel {
                                         color: black
                                     }
                                     """)
        self.label.setText(f"Sum of number of members of teams: {self.sum}\nNumber of members: {self.number_of_members}\nTeam order matters: {team_order}\nMembers order matters: {members_order}")
        
        self.pushButton_7.clicked.connect(self.go_to_row)
        
    def populate_table(self):
        headers = ["Team name", "Number of members in the team"]
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
        # for row in range(self.tableWidget.rowCount()):
        #     for col in range(self.tableWidget.columnCount()):
        #         item = self.tableWidget.item(row, col)
        #         if item:
        #             item.setTextAlignment(Qt.AlignLeft | Qt.AlignTop)
        #     self.tableWidget.resizeRowsToContents()