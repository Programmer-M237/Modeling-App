# -*- coding: utf-8 -*-

from encodings.punycode import T
from re import L
from PySide6.QtWidgets import QDialog, QTreeWidgetItem, QApplication, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from object_01 import Object_01
from object_02 import Object_02
from object_03 import Object_03
from object_04 import Object_04
from object_05 import Object_05
from object_06 import Object_06
from object_07 import Object_07
from object_08 import Object_08
from object_09 import Object_09
from object_10 import Object_10
from object_11 import Object_11
from object_12 import Object_12
from object_13 import Object_13
from object_14 import Object_14
from object_15 import Object_15
from object_16 import Object_16
from object_17 import Object_17
from object_18 import Object_18
from object_19 import Object_19
from object_20 import Object_20
from object_21 import Object_21
from object_22 import Object_22
from object_23 import Object_23
from object_24 import Object_24
from object_25 import Object_25
from object_26 import Object_26
# from object_26 import Object_26 # name of file changed to object_##.py. This will be added in an advance version
from none_chosen import None_chosen_page
from create_new_object_window_ui_ui import Ui_Dialog
import data_store

class Create_new_object(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.treeWidget.setHeaderHidden(True)
        self.setWindowTitle("Create new object")
        self.setWindowIcon(QIcon())
        self.setWindowFlags(Qt.Window | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.resize(1400, 900)
        self.setMinimumSize(800, 600)
        self.page_1 = Object_01()
        self.page_2 = Object_02()
        self.page_3 = Object_03(self.ui.stackedWidget, self)
        self.page_3.name = "page_3"
        self.page_4 = Object_04(self.ui.stackedWidget, self)
        self.page_4.name = "page_4"
        self.page_5 = Object_05(self.ui.stackedWidget, self)
        self.page_5.name = "page_5"
        self.page_6 = Object_06(self.ui.stackedWidget, self)
        self.page_6.name = "page_6"
        self.page_7 = Object_07(self.ui.stackedWidget, self)
        self.page_7.name = "page_7"
        self.page_8 = Object_08()
        self.page_9 = Object_09()
        self.page_10 = Object_10()
        self.page_11 = Object_11()
        self.page_12 = Object_12(self.ui.stackedWidget, self) # Special case because it opens a non modal window, and these arguments are needed for the closing of the non modal window
        self.page_12.name = "page_12" # for special case of object 12
        self.page_13 = Object_13(self.ui.stackedWidget, self)
        self.page_13.name = "page_13"
        self.page_14 = Object_14()
        self.page_15 = Object_15()
        self.page_16 = Object_16()
        self.page_17 = Object_17()
        self.page_18 = Object_18()
        self.page_19 = Object_19()
        self.page_20 = Object_20()
        self.page_21 = Object_21()
        self.page_22 = Object_22()
        self.page_23 = Object_23()
        self.page_24 = Object_24()
        self.page_25 = Object_25()
        # self.page_26 = Object_26() # Will be added in advance versions
        self.page_26 = Object_26()
        self.none = None_chosen_page()
        self.ui.stackedWidget.addWidget(self.page_1)
        self.ui.stackedWidget.addWidget(self.page_2)
        self.ui.stackedWidget.addWidget(self.page_3)
        self.ui.stackedWidget.addWidget(self.page_4)
        self.ui.stackedWidget.addWidget(self.page_5)
        self.ui.stackedWidget.addWidget(self.page_6)
        self.ui.stackedWidget.addWidget(self.page_7)
        self.ui.stackedWidget.addWidget(self.page_8)
        self.ui.stackedWidget.addWidget(self.page_9)
        self.ui.stackedWidget.addWidget(self.page_10)
        self.ui.stackedWidget.addWidget(self.page_11)
        self.ui.stackedWidget.addWidget(self.page_12)
        self.ui.stackedWidget.addWidget(self.page_13)
        self.ui.stackedWidget.addWidget(self.page_14)
        self.ui.stackedWidget.addWidget(self.page_15)
        self.ui.stackedWidget.addWidget(self.page_16)
        self.ui.stackedWidget.addWidget(self.page_17)
        self.ui.stackedWidget.addWidget(self.page_18)
        self.ui.stackedWidget.addWidget(self.page_19)
        self.ui.stackedWidget.addWidget(self.page_20)
        self.ui.stackedWidget.addWidget(self.page_21)
        self.ui.stackedWidget.addWidget(self.page_22)
        self.ui.stackedWidget.addWidget(self.page_23)
        self.ui.stackedWidget.addWidget(self.page_24)
        self.ui.stackedWidget.addWidget(self.page_25)
        # self.ui.stackedWidget.addWidget(self.page_26) # Will be added in advance versions
        self.ui.stackedWidget.addWidget(self.page_26)
        self.ui.stackedWidget.addWidget(self.none)
        
        self.populate_tree()
        self.ui.treeWidget.itemClicked.connect(self.handle_tree_selection)
        
        self.page_1.cancel_clicked.connect(self.close)
        self.page_2.cancel_clicked.connect(self.close)
        self.page_3.cancel_clicked.connect(self.close)
        self.page_4.cancel_clicked.connect(self.close)
        self.page_5.cancel_clicked.connect(self.close)
        self.page_6.cancel_clicked.connect(self.close)
        self.page_7.cancel_clicked.connect(self.close)
        self.page_8.cancel_clicked.connect(self.close)
        self.page_9.cancel_clicked.connect(self.close)
        self.page_10.cancel_clicked.connect(self.close)
        self.page_11.cancel_clicked.connect(self.close)
        self.page_12.cancel_clicked.connect(self.close)
        self.page_13.cancel_clicked.connect(self.close)
        self.page_14.cancel_clicked.connect(self.close)
        self.page_15.cancel_clicked.connect(self.close)
        self.page_16.cancel_clicked.connect(self.close)
        self.page_17.cancel_clicked.connect(self.close)
        self.page_18.cancel_clicked.connect(self.close)
        self.page_19.cancel_clicked.connect(self.close)
        self.page_20.cancel_clicked.connect(self.close)
        self.page_21.cancel_clicked.connect(self.close)
        self.page_22.cancel_clicked.connect(self.close)
        self.page_23.cancel_clicked.connect(self.close)
        self.page_24.cancel_clicked.connect(self.close)
        self.page_25.cancel_clicked.connect(self.close)
        # self.page_26.cancel_clicked.connect(self.close)
        self.page_26.cancel_clicked.connect(self.close)
        self.none.cancel_clicked.connect(self.close)
        self.ui.stackedWidget.setCurrentWidget(self.none)
        
        self.ui.lineEdit.textChanged.connect(self.update_search)
        
        self.objects_path = { # This is for the search system. The keys are the search words and the pairs are the tree structure of the result (such that the result will appear exactly as it will on normal bases)
            ### The principal functioning of this search system is that, the keys of this dictionary have all the key words related to the object type it points to. Now the searcher will look for the searched word (which is expected to be a key word) in the keys of this dictionary
            "objects with same forms for each property with replacement": "Objects / Object with same forms for each property / With replacement 💎",
            "objects with same forms for each property without replacement": "Objects / Object with same forms for each property / Without replacement 💎",
            "objects with different forms for different properties": "Objects / Objects with different forms for different properties 💎",
            "objects from selecting a items from b items, c items from d items, etc choosing separately from each group": "Objects / Objects from selecting a items from b items, c items from d items, etc. / Choosing separately from each group 💎",
            "objects from selecting a items from b items, c items from d items, etc choosing across groups (pooled)": "Objects / Objects from selecting a items from b items, c items from d items, etc. / Choosing across groups (pooled) 💎",
            "objects from selecting a items from b items, c items from d items, etc choosing n items across groups (pooled)": "Objects / Objects from selecting a items from b items, c items from d items, etc. / Choosing n items across groups (pooled) 💎",
            "permutations": "Permutation systems / Permutations 💎",
            "permutations of multisets or identical items": "Permutation systems / Permutations of multisets or identical items 💎",
            "symmetry constrained circular permutations": "Permutation systems / Circular permutations / Symmetry-constrained circular permutations 💎",
            "circular permutations of multisets or identical items": "Permutation systems / Circular permutations / Circular permutations of multisets 💎",
            "partial circular permutations": "Permutation systems / Circular permutations / Partial circular permutations 💎",
            "combination": "Combination systems / Combination 💎",
            "mixed radix system of numbers (permutations and combinations possible)": "Mixed Radix System / Mixed Radix system of numbers (permutations and combinations possible) 💎",
            "mixed radix system of objects": "Mixed Radix System / Mixed Radix system of objects 💎",
            "distribution, grouping and teaming of items into any number of unlabeled groups": "Distributions and grouping / Teaming/grouping / Unlabeled groups / Any number of groups 💎",
            "distribution, grouping and teaming of items into exactly k number of unlabeled groups": "Distributions and grouping / Teaming/grouping / Unlabeled groups / Exactly k groups 💎",
            "distribution, grouping and teaming of items into equally sized unlabeled groups": "Distributions and grouping / Teaming/grouping / Unlabeled groups / Equal-sized groups 💎",
            "distribution grouping and teaming of items into equal team sizes labeled groups": "Distributions and grouping / Teaming/grouping / Labeled groups (teams) / Equal team sizes 💎",
            "distribution grouping and teaming of items into unequal team sizes labeled groups": "Distributions and grouping / Teaming/grouping / Labeled groups (teams) / Unequal team sizes 💎",
            "distribution grouping and teaming of items into teams in roles (slots) of labeled groups": "Distributions and grouping / Teaming/grouping / Teams with roles (slots) 💎",
            "partitions of money partition (money change)": "Partitions / Money partition (money change) 💎",
            "partitions into general integer partitions": "Partitions / Integer partitions / General integer partitions 💎",
            "partitions into restricted integer partitions of distinct parts": "Partitions / Integer partitions / Restricted integer partitions / Partitions into distinct parts 💎",
            "partitions into restricted integer partitions of exactly k parts": "Partitions / Integer partitions / Restricted integer partitions / Partitions into exactly k parts 💎",
            "partitions into restricted integer partitions of parts ≤ (less than or equal to) m": "Partitions / Integer partitions / Restricted integer partitions / Partitions with parts ≤ m 💎",
            "partitions into restricted integer partitions of odd parts": "Partitions / Integer partitions / Restricted integer partitions / Partitions into odd parts 💎",
            "partitions into restricted integer partitions of even parts": "Partitions / Integer partitions / Restricted integer partitions / Partitions into even parts 💎"
        }
        self.objects_id = { # This is for the search system. This is for searching using the id of the object directly, this is possible using the @ or # symbol and writing the id number behind to indicate that you want to search by id
            ### This principal functioning of this search system is that, after the @ or # symbol is seen, the search will now be directed to the pairs of this dictionary. When the id is found is it then linked to it corresponding key, which is then linked to the path via the @objects_parts dictionary above
            ### The search will traverse this dictionary to the end. It is true that there is no repetition except for id 03, but this is of reason for future extensibility of the code
            "objects with same forms for each property with replacement": "01",
            "objects with same forms for each property without replacement": "02",
            "objects with different forms for different properties": "03",
            "objects from selecting a items from b items, c items from d items, etc choosing separately from each group": "05",
            "objects from selecting a items from b items, c items from d items, etc choosing across groups (pooled)": "06",
            "objects from selecting a items from b items, c items from d items, etc choosing n items across groups (pooled)": "07",
            "permutations": "21",
            "permutations of multisets or identical items": "22",
            "symmetry constrained circular permutations": "23",
            "circular permutations of multisets or identical items": "24",
            "partial circular permutations": "25",
            "combination": "26",
            "mixed radix system of numbers (permutations and combinations possible)": "04",
            "mixed radix system of objects": "03",
            "distribution, grouping and teaming of items into any number of unlabeled groups": "08",
            "distribution, grouping and teaming of items into exactly k number of unlabeled groups": "09",
            "distribution, grouping and teaming of items into equally sized unlabeled groups": "10",
            "distribution grouping and teaming of items into equal team sizes labeled groups": "11",
            "distribution grouping and teaming of items into unequal team sizes labeled groups": "12",
            "distribution grouping and teaming of items into teams in roles (slots) of labeled groups": "13",
            "partitions of money partition (money change)": "14",
            "partitions into general integer partitions": "15",
            "partitions into restricted integer partitions of distinct parts": "16",
            "partitions into restricted integer partitions of exactly k parts": "17",
            "partitions into restricted integer partitions of parts ≤ (less than or equal to) m": "18",
            "partitions into restricted integer partitions of odd parts": "19",
            "partitions into restricted integer partitions of even parts":  "20"
        }
        """
            Display the tree items of the found matches is complex because displaying the tree items of the found matches from the gotten paths is not easy
            # I made my own system: I will use a list to store whether the tree items will be display, and a dictionary to store the variables of the QTreeWidgetItem() (this is very important because the same objects must be used)
        """
        
    def populate_tree(self):
        self.ui.treeWidget.clear()
        parent5 = QTreeWidgetItem(["Objects"])
        print(parent5.text(0))
        parent5.setToolTip(0, "Objects")
        child1_p5 = QTreeWidgetItem(["Object with same forms for each property"])
        child1_p5.setToolTip(0, "Object with same forms for each property")
        child1_p5_1 = QTreeWidgetItem(["With replacement 💎"])
        child1_p5_1.setToolTip(0, "With replacement")
        child1_p5_2 = QTreeWidgetItem(["Without replacement 💎"])
        
        child1_p5_2.setToolTip(0, "Without replacement")
        child1_p5.addChild(child1_p5_1)
        child1_p5.addChild(child1_p5_2)
        parent5.addChild(child1_p5)
        child2_p5 = QTreeWidgetItem(["Objects with different forms for different properties 💎"])
        child2_p5.setToolTip(0, "Objects with different forms for different properties")
        parent5.addChild(child2_p5)
        child3_p5 = QTreeWidgetItem(["Objects from selecting a items from b items, c items from d items, etc."])
        child3_p5.setToolTip(0, "Objects from selecting a items from b items, c items from d items, etc.")
        parent5.addChild(child3_p5)
        child3_p5_1 = QTreeWidgetItem(["Choosing separately from each group 💎"])
        child3_p5_1.setToolTip(0, "Choosing separately from each group")
        child3_p5_2 = QTreeWidgetItem(["Choosing across groups (pooled) 💎"])
        child3_p5_2.setToolTip(0, "Choosing across groups (pooled)")
        child3_p5_3 = QTreeWidgetItem(["Choosing n items across groups (pooled) 💎"])
        child3_p5_3.setToolTip(0, "Choosing n items across groups (pooled)")
        child3_p5.addChild(child3_p5_1)
        child3_p5.addChild(child3_p5_2)
        child3_p5.addChild(child3_p5_3)
        self.ui.treeWidget.addTopLevelItem(parent5)
        parent1 = QTreeWidgetItem(["Permutation systems"])
        parent1.setToolTip(0, "Permutation systems")
        child1_p1 = QTreeWidgetItem(["Permutations 💎"])
        child1_p1.setToolTip(0, "Permutations with/without repetition")
        # child2_p1 = QTreeWidgetItem(["Permutations without repetition 💎"])
        # child2_p1.setToolTip(0, "Permutations without repetition")
        child3_p1 = QTreeWidgetItem(["Permutations of multisets or identical items 💎"])
        child3_p1.setToolTip(0, "Permutations of multisets or identical items")
        child4_p1 = QTreeWidgetItem(["Circular permutations"])
        child4_p1.setToolTip(0, "Circular permutations")
        child4_p1_1 = QTreeWidgetItem(["Symmetry-constrained circular permutations 💎"])
        child4_p1_1.setToolTip(0, "Symmetry-constrained circular permutations")
        child4_p1_2 = QTreeWidgetItem(["Circular permutations of multisets 💎"])
        child4_p1_2.setToolTip(0, "Circular permutations of multisets")
        child4_p1_3 = QTreeWidgetItem(["Partial circular permutations 💎"])
        child4_p1_3.setToolTip(0, "Partial circular permutations")
        child4_p1.addChild(child4_p1_1)
        child4_p1.addChild(child4_p1_2)
        child4_p1.addChild(child4_p1_3)
        # child5_p1 = QTreeWidgetItem(["Restricted permutations 💎"])
        # child5_p1.setToolTip(0, "Restricted permutations")
        parent1.addChild(child1_p1)
        #parent1.addChild(child2_p1)
        parent1.addChild(child3_p1)
        parent1.addChild(child4_p1)
        # parent1.addChild(child5_p1)
        self.ui.treeWidget.addTopLevelItem(parent1)
        parent2 = QTreeWidgetItem(["Combination systems"])
        parent2.setToolTip(0, "Combination systems")
        child1_p2 = QTreeWidgetItem(["Combination 💎"])
        child1_p2.setToolTip(0, "Combination")
        parent2.addChild(child1_p2)
        self.ui.treeWidget.addTopLevelItem(parent2)
        parent6 = QTreeWidgetItem(["Mixed Radix System"])
        parent6.setToolTip(0, "Mixed Radix System")
        child1_p6 = QTreeWidgetItem(["Mixed Radix system of numbers (permutations and combinations possible) 💎"])
        child1_p6.setToolTip(0, "Mixed Radix system of numbers (permutations and combinations possible)")
        child2_p6 = QTreeWidgetItem(["Mixed Radix system of objects 💎"])
        child2_p6.setToolTip(0, "Mixed Radix system of objects")
        parent6.addChild(child1_p6)
        parent6.addChild(child2_p6)
        self.ui.treeWidget.addTopLevelItem(parent6)
        parent3 = QTreeWidgetItem(["Distributions and grouping"])
        parent3.setToolTip(0, "Distributions and grouping")
        child2_p3 = QTreeWidgetItem(["Teaming/grouping"])
        child2_p3.setToolTip(0, "Teaming/grouping")
        child2_p3_1 = QTreeWidgetItem(["Unlabeled groups"])
        child2_p3_1.setToolTip(0, "Unlabeled groups")
        child2_p3_1_1 = QTreeWidgetItem(["Any number of groups 💎"])
        child2_p3_1_1.setToolTip(0, "Any number of groups")
        child2_p3_1_2 = QTreeWidgetItem(["Exactly k groups 💎"])
        child2_p3_1_2.setToolTip(0, "Exactly k groups")
        child2_p3_1_3 = QTreeWidgetItem(["Equal-sized groups 💎"])
        child2_p3_1_3.setToolTip(0, "Equal-sized groups")
        child2_p3_2 = QTreeWidgetItem(["Labeled groups (teams)"])
        child2_p3_2.setToolTip(0, "Labeled groups (teams)")
        child2_p3_2_1 = QTreeWidgetItem(["Equal team sizes 💎"])
        child2_p3_2_1.setToolTip(0, "Equal team sizes")
        child2_p3_2_2 = QTreeWidgetItem(["Unequal team sizes 💎"])
        child2_p3_2_2.setToolTip(0, "Unequal team sizes")
        child2_p3_3 = QTreeWidgetItem(["Teams with roles (slots) 💎"])
        child2_p3_3.setToolTip(0, "Teams with roles (slots)")
        # child2_p3_4 = QTreeWidgetItem(["Hierarchical grouping 💎"])
        # child2_p3_4.setToolTip(0, "Hierarchical grouping")
        # child3_p3 = QTreeWidgetItem(["Grid/lattice paths 💎"])
        # child3_p3.setToolTip(0, "Grid/lattice paths")
        # child4_p3 = QTreeWidgetItem(["Bounded distributions 💎"])
        # child4_p3.setToolTip(0, "Bounded distributions")
        child2_p3_1.addChild(child2_p3_1_1)
        child2_p3_1.addChild(child2_p3_1_2)
        child2_p3_1.addChild(child2_p3_1_3)
        child2_p3_2.addChild(child2_p3_2_1)
        child2_p3_2.addChild(child2_p3_2_2)
        child2_p3.addChild(child2_p3_1)
        child2_p3.addChild(child2_p3_2)
        child2_p3.addChild(child2_p3_3)
        #child2_p3.addChild(child2_p3_4)
        parent3.addChild(child2_p3)
        #parent3.addChild(child3_p3)
        #parent3.addChild(child4_p3)
        self.ui.treeWidget.addTopLevelItem(parent3)
        parent4 = QTreeWidgetItem(["Partitions"])
        parent4.setToolTip(0, "Partitions")
        child1_p4_2_5 = QTreeWidgetItem(["Partitions into even parts 💎"])
        child1_p4_2_5.setToolTip(0, "Partitions into even parts")
        child1_p4_2_4 = QTreeWidgetItem(["Partitions into odd parts 💎"])
        child1_p4_2_4.setToolTip(0, "Partitions into odd parts")
        child1_p4_2_3 = QTreeWidgetItem(["Partitions with parts ≤ m 💎"])
        child1_p4_2_3.setToolTip(0, "Partitions with parts ≤ m")
        child1_p4_2_2 = QTreeWidgetItem(["Partitions into exactly k parts 💎"])
        child1_p4_2_2.setToolTip(0, "Partitions into exactly k parts")
        child1_p4_2_1 = QTreeWidgetItem(["Partitions into distinct parts 💎"])
        child1_p4_2_1.setToolTip(0, "Partitions into distinct parts")
        child1_p4_1 = QTreeWidgetItem(["General integer partitions 💎"])
        child1_p4_1.setToolTip(0, "General integer partitions")
        child1_p4_2 = QTreeWidgetItem(["Restricted integer partitions"])
        child1_p4_2.setToolTip(0, "Restricted integer partitions")
        child1_p4 = QTreeWidgetItem(["Integer partitions"])
        child1_p4.setToolTip(0, "Integer partitions ")
        child2_p4 = QTreeWidgetItem(["Money partition (money change) 💎"])
        child2_p4.setToolTip(0, "Money partition (money change)")
        # child3_p4 = QTreeWidgetItem(["Partitions into bins 💎"]) # Remove because I never knew how to implement it. I need advise from an expert combinatorics person on this
        # child3_p4.setToolTip(0, "Partitions into bins")
        parent4.addChild(child1_p4)
        parent4.addChild(child2_p4)
        #parent4.addChild(child3_p4)
        child1_p4.addChild(child1_p4_1)
        child1_p4.addChild(child1_p4_2)
        child1_p4_2.addChild(child1_p4_2_1)
        child1_p4_2.addChild(child1_p4_2_2)
        child1_p4_2.addChild(child1_p4_2_3)
        child1_p4_2.addChild(child1_p4_2_4)
        child1_p4_2.addChild(child1_p4_2_5)
        self.ui.treeWidget.addTopLevelItem(parent4)
        
    def handle_tree_selection(self):
        selected = self.ui.treeWidget.currentItem()
        if not selected:
            return
        full_path = self.get_full_path(selected)
        if full_path == "Objects / Object with same forms for each property / With replacement 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_1)
        elif full_path == "Objects / Object with same forms for each property / Without replacement 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_2)
        elif full_path == "Objects / Objects with different forms for different properties 💎" or full_path == "Mixed Radix System / Mixed Radix system of objects 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_3)
        elif full_path == "Mixed Radix System / Mixed Radix system of numbers (permutations and combinations possible) 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_4)
        elif full_path == "Objects / Objects from selecting a items from b items, c items from d items, etc. / Choosing separately from each group 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_5)
        elif full_path == "Objects / Objects from selecting a items from b items, c items from d items, etc. / Choosing across groups (pooled) 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_6)
        elif full_path == "Objects / Objects from selecting a items from b items, c items from d items, etc. / Choosing n items across groups (pooled) 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_7)
        elif full_path == "Distributions and grouping / Teaming/grouping / Unlabeled groups / Any number of groups 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_8)
        elif full_path == "Distributions and grouping / Teaming/grouping / Unlabeled groups / Exactly k groups 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_9)
        elif full_path == "Distributions and grouping / Teaming/grouping / Unlabeled groups / Equal-sized groups 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_10)
        elif full_path == "Distributions and grouping / Teaming/grouping / Labeled groups (teams) / Equal team sizes 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_11)
        elif full_path == "Distributions and grouping / Teaming/grouping / Labeled groups (teams) / Unequal team sizes 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_12)
        elif full_path == "Distributions and grouping / Teaming/grouping / Teams with roles (slots) 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_13)
        elif full_path == "Partitions / Money partition (money change) 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_14)
        elif full_path == "Partitions / Integer partitions / General integer partitions 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_15)
        elif full_path == "Partitions / Integer partitions / Restricted integer partitions / Partitions into distinct parts 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_16)
        elif full_path == "Partitions / Integer partitions / Restricted integer partitions / Partitions into exactly k parts 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_17)
        elif full_path == "Partitions / Integer partitions / Restricted integer partitions / Partitions with parts ≤ m 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_18)
        elif full_path == "Partitions / Integer partitions / Restricted integer partitions / Partitions into odd parts 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_19)
        elif full_path == "Partitions / Integer partitions / Restricted integer partitions / Partitions into even parts 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_20)
        elif full_path == "Permutation systems / Permutations 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_21)
        elif full_path == "Permutation systems / Permutations of multisets or identical items 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_22)
        elif full_path == "Permutation systems / Circular permutations / Symmetry-constrained circular permutations 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_23)
        elif full_path == "Permutation systems / Circular permutations / Circular permutations of multisets 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_24)
        elif full_path == "Permutation systems / Circular permutations / Partial circular permutations 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_25)
        # elif full_path == "Permutation systems / Restricted permutations 💎":
        #     self.ui.stackedWidget.setCurrentWidget(self.page_26)
        elif full_path == "Combination systems / Combination 💎":
            self.ui.stackedWidget.setCurrentWidget(self.page_26)
        # else:
        #     self.ui.stackedWidget.setCurrentWidget(self.none)
    
    def get_full_path(self, item):
        path = []
        while item:
            path.insert(0, item.text(0))
            item = item.parent()
        return " / ".join(path)
        
    def closeEvent(self, event):
        confirmed = QMessageBox.question(self, "Exit", "Do you want to exit (Your unsaved data will be lost)", QMessageBox.Yes | QMessageBox.No)
        #print(self.ui.stackedWidget.currentWidget().name)
        if confirmed == QMessageBox.Yes:
            data_store.DataStore.data_store.clear()
            data_store.DataStore1.data_store.clear()
            data_store.DataStore2.data_store.clear()
            data_store.DataStore3.data_store.clear()
            data_store.DataStore4.data_store.clear()
            event.accept()
        else:
            event.ignore()
        if self.ui.stackedWidget.currentWidget().name == "page_12": # Special for object 12
            self.page_12.close_team_info_window()
        elif self.ui.stackedWidget.currentWidget().name == "page_3": # This new functionality was first implemented on object 12, but was noticed that it will increase the overall UX of the app if implemented in the multi-data objects since it summarises making the user aware of what he/she is doing appropriately
            self.page_3.close_object_info_window()
        elif self.ui.stackedWidget.currentWidget().name == "page_5":
            self.page_5.close_group_info_window()
        elif self.ui.stackedWidget.currentWidget().name == "page_6":
            self.page_6.close_group_info_window()
        elif self.ui.stackedWidget.currentWidget().name == "page_7":
            self.page_7.close_group_info_window()
        elif self.ui.stackedWidget.currentWidget().name == "page_4":
            self.page_4.close_object_info_window()
        elif self.ui.stackedWidget.currentWidget().name == "page_13":
            self.page_13.close_team_info_window()
            
    def update_search(self):
        if not self.ui.lineEdit.text().strip():
            self.ui.treeWidget.clear()
            self.populate_tree()
        else:
            found_matches = [] # Generally, this is will contain the paths of the different found matches
            if not (self.ui.lineEdit.text().strip()[0] == "@" or self.ui.lineEdit.text().strip()[0] == "#"):
                for found_match in list(self.objects_path):
                    if self.ui.lineEdit.text().strip().lower() in found_match:
                        found_matches.append(self.objects_path[found_match])
                tree_structure = self.build_tree_structure(found_matches)
                self.search_populate_tree(self.ui.treeWidget, tree_structure)
            else:
                if (len(self.ui.lineEdit.text().strip()) < 3) or (len(self.ui.lineEdit.text().strip()) > 3):
                    pass
                else:
                    id = ""
                    print(len(self.ui.lineEdit.text().strip()))
                    id += self.ui.lineEdit.text().strip()[1] + self.ui.lineEdit.text().strip()[2]
                    #print(id)
                    key_words = []
                    for i in list(self.objects_id.keys()):
                        if id == self.objects_id[i]:
                            key_words.append(i)
                    #print(key_words)
                    paths = []
                    for i in key_words:
                        if i in list(self.objects_path.keys()):
                            paths.append(self.objects_path[i])
                    tree_structure = self.build_tree_structure(paths)
                    self.search_populate_tree(self.ui.treeWidget, tree_structure)
                
    def build_tree_structure(self, paths):
        tree = {}
        for path in paths:
            parts = path.split(" / ")
            current = tree
            for part in parts:
                current = current.setdefault(part, {})
        return tree
    
    def search_populate_tree(self, tree_widget, tree_dict):
        def add_items(parent, subtree):
            for key, children in subtree.items():
                item = QTreeWidgetItem([key])
                parent.addChild(item)
                add_items(item, children)
                
        tree_widget.clear()
        for top_key, children in tree_dict.items():
            top_item = QTreeWidgetItem([top_key])
            tree_widget.addTopLevelItem(top_item)
            add_items(top_item, children)
    
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Create_new_object()
#     window.show()
#     app.exec()