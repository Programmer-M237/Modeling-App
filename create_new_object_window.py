# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QDialog, QTreeWidgetItem, QMessageBox
from PySide6.QtCore import Qt
from create_object_ui import Ui_Dialog
from object_01 import Object_01


class Create_new_object(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.treeWidget.setHeaderHidden(True)
        self.setWindowTitle("Create new object")
        self.setWindowFlags(Qt.Window | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.resize(1400, 900)
        self.setMinimumSize(800, 600)

        self.page_1 = Object_01()
        self.stackedWidget.addWidget(self.page_1)
        self.stackedWidget.setCurrentWidget(self.page_1)
        self.page_1.cancel_clicked.connect(self.close)

        self.populate_tree()
        self.treeWidget.itemClicked.connect(self.handle_tree_selection)
        self.lineEdit.setPlaceholderText("Search object type (or use @ID/#ID)")
        self.lineEdit.textChanged.connect(self.update_search)

        # Search mappings
        self.objects_path = {
            "objects with same forms for each property with replacement": "Objects / Object with same forms for each property",
            "objects": "Objects / Object with same forms for each property",
            "same forms": "Objects / Object with same forms for each property",
            "replacement": "Objects / Object with same forms for each property",
        }

        self.objects_id = {
            "objects with same forms for each property with replacement": "01"
        }

    def handle_tree_selection(self):
        selected = self.treeWidget.currentItem()
        if not selected:
            return
        full_path = self.get_full_path(selected)
        if full_path == "Objects / Object with same forms for each property":
            self.stackedWidget.setCurrentWidget(self.page_1)

    def get_full_path(self, item):
        """Build the full path of a tree item."""
        path = []
        while item:
            path.insert(0, item.text(0))
            item = item.parent()
        return " / ".join(path)

    def populate_tree(self):
        """Populate the tree with default structure."""
        self.treeWidget.clear()
        parent1 = QTreeWidgetItem(["Objects"])
        parent1.setToolTip(0, "Objects")

        child1 = QTreeWidgetItem(["Object with same forms for each property"])
        child1.setToolTip(0, "Object with same forms for each property")
        parent1.addChild(child1)

        self.treeWidget.addTopLevelItem(parent1)
        parent1.setExpanded(True)

    def closeEvent(self, event):
        """Handle dialog close with confirmation."""
        confirmed = QMessageBox.question(
            self, 
            "Exit", 
            "Do you want to exit? (Your unsaved data will be lost)", 
            QMessageBox.Yes | QMessageBox.No
        )
        if confirmed == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def update_search(self):
        """Update tree based on search query."""
        search_text = self.lineEdit.text().strip()

        # If search is empty, restore default tree
        if not search_text:
            self.populate_tree()
            return

        # Check if searching by ID
        if search_text[0] in ("@", "#"):
            self._search_by_id(search_text)
        else:
            self._search_by_keyword(search_text)

    def _search_by_keyword(self, search_text):
        """Search for objects by keyword."""
        found_matches = []
        search_lower = search_text.lower()

        for keyword, path in self.objects_path.items():
            if search_lower in keyword.lower():
                found_matches.append(path)

        # Remove duplicates while preserving order
        found_matches = list(dict.fromkeys(found_matches))

        if found_matches:
            tree_structure = self.build_tree_structure(found_matches)
            self.search_populate_tree(tree_structure)
        else:
            self.treeWidget.clear()
            no_results = QTreeWidgetItem(["No results found"])
            no_results.setFlags(Qt.ItemIsEnabled)  # Make it non-selectable
            self.treeWidget.addTopLevelItem(no_results)

    def _search_by_id(self, search_text):
        """Search for objects by ID."""
        # Expected format: @01 or #01 (3 characters total)
        if len(search_text) != 3:
            return

        object_id = search_text[1:3]
        found_paths = []

        # Find all keywords matching this ID
        for keyword, stored_id in self.objects_id.items():
            if object_id == stored_id:
                # Get the path for this keyword
                if keyword in self.objects_path:
                    found_paths.append(self.objects_path[keyword])

        # Remove duplicates
        found_paths = list(dict.fromkeys(found_paths))

        if found_paths:
            tree_structure = self.build_tree_structure(found_paths)
            self.search_populate_tree(tree_structure)
        else:
            self.treeWidget.clear()
            no_results = QTreeWidgetItem([f"No object found with ID: {object_id}"])
            no_results.setFlags(Qt.ItemIsEnabled)
            self.treeWidget.addTopLevelItem(no_results)

    def build_tree_structure(self, paths):
        """Build nested dictionary structure from paths."""
        tree = {}
        for path in paths:
            parts = path.split(" / ")
            current = tree
            for part in parts:
                current = current.setdefault(part, {})
        return tree

    def search_populate_tree(self, tree_dict):
        """Populate tree widget with search results."""
        def add_items(parent, subtree):
            for key, children in subtree.items():
                item = QTreeWidgetItem([key])
                item.setToolTip(0, key)
                parent.addChild(item)
                add_items(item, children)
                # Auto-expand items with children
                if children:
                    item.setExpanded(True)

        self.treeWidget.clear()

        for top_key, children in tree_dict.items():
            top_item = QTreeWidgetItem([top_key])
            top_item.setToolTip(0, top_key)
            self.treeWidget.addTopLevelItem(top_item)
            add_items(top_item, children)
            top_item.setExpanded(True)
