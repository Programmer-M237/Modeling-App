# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'object_##.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(858, 829)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea_2 = QScrollArea(Dialog)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 838, 753))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label_2)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.lineEdit_3 = QLineEdit(self.frame_6)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_7.addWidget(self.lineEdit_3)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_5)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_10 = QFrame(self.groupBox_2)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_10)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)

        self.horizontalLayout_9.addWidget(self.label_9)

        self.spin_box_3 = QSpinBox(self.frame_10)
        self.spin_box_3.setObjectName(u"spin_box_3")

        self.horizontalLayout_9.addWidget(self.spin_box_3)


        self.verticalLayout_4.addWidget(self.frame_10)

        self.scrollArea = QScrollArea(self.groupBox_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 798, 111))
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea.setWidget(self.widget)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.frame_13 = QFrame(self.groupBox_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_13)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_12.addWidget(self.label_4)

        self.spinBox = QSpinBox(self.frame_13)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout_12.addWidget(self.spinBox)

        self.pushButton_3 = QPushButton(self.frame_13)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_12.addWidget(self.pushButton_3)

        self.horizontalLayout_12.setStretch(1, 7)

        self.verticalLayout_4.addWidget(self.frame_13)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_3.addWidget(self.checkBox)

        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_6.addWidget(self.label)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.comboBox = QComboBox(self.frame_7)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.pushButton = QPushButton(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalLayout.setStretch(1, 7)

        self.verticalLayout_6.addWidget(self.frame_7)


        self.verticalLayout_3.addWidget(self.frame)

        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_3.addWidget(self.checkBox_2)

        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_7.addWidget(self.label_7)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_2.addWidget(self.label_8)

        self.comboBox_2 = QComboBox(self.frame_8)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_2.addWidget(self.comboBox_2)

        self.pushButton_2 = QPushButton(self.frame_8)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.horizontalLayout_2.setStretch(1, 7)

        self.verticalLayout_7.addWidget(self.frame_8)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_3.addWidget(self.checkBox_3)

        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_8.addWidget(self.label_10)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_3.addWidget(self.label_11)

        self.comboBox_3 = QComboBox(self.frame_9)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_3.addWidget(self.comboBox_3)

        self.comboBox_4 = QComboBox(self.frame_9)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_3.addWidget(self.comboBox_4)

        self.pushButton_4 = QPushButton(self.frame_9)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.horizontalLayout_3.setStretch(1, 5)
        self.horizontalLayout_3.setStretch(2, 5)

        self.verticalLayout_8.addWidget(self.frame_9)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.checkBox_4 = QCheckBox(self.groupBox)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_3.addWidget(self.checkBox_4)

        self.frame_4 = QFrame(self.groupBox)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_9.addWidget(self.label_13)

        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_11)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_4.addWidget(self.label_12)

        self.comboBox_5 = QComboBox(self.frame_11)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.horizontalLayout_4.addWidget(self.comboBox_5)

        self.comboBox_6 = QComboBox(self.frame_11)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.horizontalLayout_4.addWidget(self.comboBox_6)

        self.pushButton_5 = QPushButton(self.frame_11)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_4.addWidget(self.pushButton_5)

        self.horizontalLayout_4.setStretch(1, 5)
        self.horizontalLayout_4.setStretch(2, 5)

        self.verticalLayout_9.addWidget(self.frame_11)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.checkBox_5 = QCheckBox(self.groupBox)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_3.addWidget(self.checkBox_5)

        self.frame_5 = QFrame(self.groupBox)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_10.addWidget(self.label_16)

        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_14)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_8.addWidget(self.label_15)

        self.comboBox_9 = QComboBox(self.frame_14)
        self.comboBox_9.setObjectName(u"comboBox_9")

        self.horizontalLayout_8.addWidget(self.comboBox_9)


        self.horizontalLayout_6.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_15)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_10.addWidget(self.label_17)

        self.comboBox_10 = QComboBox(self.frame_15)
        self.comboBox_10.setObjectName(u"comboBox_10")

        self.horizontalLayout_10.addWidget(self.comboBox_10)


        self.horizontalLayout_6.addWidget(self.frame_15)

        self.pushButton_7 = QPushButton(self.frame_12)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_6.addWidget(self.pushButton_7)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout_10.addWidget(self.frame_12)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea_2)

        self.frame_16 = QFrame(Dialog)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.frame_17)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_13.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame_17)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_13.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.frame_17)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_13.addWidget(self.pushButton_10)


        self.horizontalLayout_11.addWidget(self.frame_17, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.pushButton_11 = QPushButton(self.frame_18)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_14.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.frame_18)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_14.addWidget(self.pushButton_12)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 1)

        self.horizontalLayout_11.addWidget(self.frame_18, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.frame_16)

        self.label_18 = QLabel(Dialog)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_18)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Selection ID: 26", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Object Name", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Check_object_name", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Items", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Number of items", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Go to item", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Go", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Restrictions", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Inclusion", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"List of must included items", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Item", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Add item", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Exclusion", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"List of must excluded items", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Item", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Add item", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Togetherness", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"List of items to be always together", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Items", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Add item", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Separation", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"List of items to be always together", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Items", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Add item", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"Position based", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"List of items to be always together", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"Position", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"Item", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"Add item", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"Save As", None))
        self.pushButton_10.setText(QCoreApplication.translate("Dialog", u"Load", None))
        self.pushButton_11.setText(QCoreApplication.translate("Dialog", u"Create Object", None))
        self.pushButton_12.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"Status_bar", None))
    # retranslateUi

