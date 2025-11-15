# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Eobject_04.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(793, 678)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_14 = QLabel(Dialog)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout.addWidget(self.label_14)

        self.frame_21 = QFrame(Dialog)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(2, 0, 2, 0)
        self.label_19 = QLabel(self.frame_21)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_20.addWidget(self.label_19)

        self.lineEdit_6 = QLineEdit(self.frame_21)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_20.addWidget(self.lineEdit_6)


        self.verticalLayout.addWidget(self.frame_21)

        self.label_17 = QLabel(Dialog)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_17)

        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_17 = QFrame(self.groupBox_3)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_17)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_16.addWidget(self.label_15)

        self.spinBox_5 = QSpinBox(self.frame_17)
        self.spinBox_5.setObjectName(u"spinBox_5")

        self.horizontalLayout_16.addWidget(self.spinBox_5)

        self.horizontalLayout_16.setStretch(1, 5)

        self.verticalLayout_2.addWidget(self.frame_17)

        self.scrollArea_2 = QScrollArea(self.groupBox_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 753, 254))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea_2)

        self.frame_7 = QFrame(self.groupBox_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: red;")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.comboBox = QComboBox(self.frame_7)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_7.addWidget(self.comboBox)

        self.pushButton_8 = QPushButton(self.frame_7)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_7.addWidget(self.pushButton_8)

        self.horizontalLayout_7.setStretch(1, 6)

        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_14 = QFrame(self.groupBox_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_14)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_13.addWidget(self.label_10)

        self.spinBox_3 = QSpinBox(self.frame_14)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.horizontalLayout_13.addWidget(self.spinBox_3)

        self.pushButton_7 = QPushButton(self.frame_14)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_13.addWidget(self.pushButton_7)

        self.horizontalLayout_13.setStretch(1, 7)

        self.verticalLayout_2.addWidget(self.frame_14, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_7 = QGroupBox(Dialog)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_22 = QFrame(self.groupBox_7)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.radioButton_10 = QRadioButton(self.frame_22)
        self.radioButton_10.setObjectName(u"radioButton_10")

        self.horizontalLayout_21.addWidget(self.radioButton_10)


        self.verticalLayout_14.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.groupBox_7)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.radioButton_11 = QRadioButton(self.frame_23)
        self.radioButton_11.setObjectName(u"radioButton_11")

        self.horizontalLayout_22.addWidget(self.radioButton_11, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_14.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.groupBox_7)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.radioButton_12 = QRadioButton(self.frame_24)
        self.radioButton_12.setObjectName(u"radioButton_12")

        self.horizontalLayout_23.addWidget(self.radioButton_12)


        self.verticalLayout_14.addWidget(self.frame_24)


        self.verticalLayout.addWidget(self.groupBox_7)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_6 = QPushButton(self.frame_3)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_3.addWidget(self.pushButton_6)


        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.frame_2)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Selection ID: 04", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"Object Name", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"Check_name", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Properties", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"Number of properties", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Properties with same name", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"Go", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Go to property", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"Go", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Dialog", u"Permutations or Combinations table?", None))
        self.radioButton_10.setText(QCoreApplication.translate("Dialog", u"Normal table", None))
        self.radioButton_11.setText(QCoreApplication.translate("Dialog", u"Permutations table", None))
        self.radioButton_12.setText(QCoreApplication.translate("Dialog", u"Combinations table", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Save As", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"Load", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Next", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Status_bar", None))
    # retranslateUi

