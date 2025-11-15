# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_condition_for_event_trigger.ui'
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
    QDoubleSpinBox, QFrame, QHBoxLayout, QLabel,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(970, 615)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_9 = QFrame(Dialog)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_9)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_12.addWidget(self.label_6)

        self.comboBox_3 = QComboBox(self.frame_9)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_12.addWidget(self.comboBox_3)

        self.horizontalLayout_12.setStretch(1, 10)

        self.verticalLayout.addWidget(self.frame_9)

        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.stackedWidget.setFrameShadow(QFrame.Shadow.Sunken)
        self.stackedWidget.setMidLineWidth(-10)
        self.time_delay = QWidget()
        self.time_delay.setObjectName(u"time_delay")
        self.verticalLayout_2 = QVBoxLayout(self.time_delay)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.time_delay)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 932, 515))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.frame)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout.addWidget(self.radioButton)

        self.doubleSpinBox = QDoubleSpinBox(self.frame)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.horizontalLayout.addWidget(self.doubleSpinBox)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout.addWidget(self.label_11)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 6)

        self.verticalLayout_8.addWidget(self.frame)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButton_2 = QRadioButton(self.frame_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_2.addWidget(self.radioButton_2)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.frame_2)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_2)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_2.addWidget(self.label_12)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 6)

        self.verticalLayout_8.addWidget(self.frame_2)

        self.radioButton_3 = QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_8.addWidget(self.radioButton_3)

        self.frame_40 = QFrame(self.scrollAreaWidgetContents)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy)
        self.frame_40.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_40)
        self.label.setObjectName(u"label")

        self.horizontalLayout_55.addWidget(self.label)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.frame_40)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")

        self.horizontalLayout_55.addWidget(self.doubleSpinBox_3)

        self.label_13 = QLabel(self.frame_40)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_55.addWidget(self.label_13)

        self.horizontalLayout_55.setStretch(1, 10)

        self.verticalLayout_8.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.scrollAreaWidgetContents)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_41)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_56.addWidget(self.label_2)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.frame_41)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")

        self.horizontalLayout_56.addWidget(self.doubleSpinBox_4)

        self.label_14 = QLabel(self.frame_41)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_56.addWidget(self.label_14)

        self.horizontalLayout_56.setStretch(1, 10)

        self.verticalLayout_8.addWidget(self.frame_41)

        self.radioButton_4 = QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.verticalLayout_8.addWidget(self.radioButton_4)

        self.frame_43 = QFrame(self.scrollAreaWidgetContents)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_43)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_58.addWidget(self.label_10)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.frame_43)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")

        self.horizontalLayout_58.addWidget(self.doubleSpinBox_6)

        self.label_15 = QLabel(self.frame_43)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_58.addWidget(self.label_15)

        self.horizontalLayout_58.setStretch(1, 10)

        self.verticalLayout_8.addWidget(self.frame_43)

        self.frame_42 = QFrame(self.scrollAreaWidgetContents)
        self.frame_42.setObjectName(u"frame_42")
        sizePolicy.setHeightForWidth(self.frame_42.sizePolicy().hasHeightForWidth())
        self.frame_42.setSizePolicy(sizePolicy)
        self.frame_42.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_42)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_57.addWidget(self.label_3)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.frame_42)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")

        self.horizontalLayout_57.addWidget(self.doubleSpinBox_5)

        self.label_16 = QLabel(self.frame_42)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_57.addWidget(self.label_16)

        self.horizontalLayout_57.setStretch(1, 10)

        self.verticalLayout_8.addWidget(self.frame_42)

        self.verticalSpacer = QSpacerItem(20, 250, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.time_delay)
        self.event_state = QWidget()
        self.event_state.setObjectName(u"event_state")
        self.verticalLayout_3 = QVBoxLayout(self.event_state)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea_3 = QScrollArea(self.event_state)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 932, 515))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_4 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.checkBox_3 = QCheckBox(self.frame_4)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_4.addWidget(self.checkBox_3)

        self.horizontalLayout_4.setStretch(0, 20)

        self.verticalLayout_10.addWidget(self.frame_4)

        self.frame_10 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_13 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_13)

        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_13.addWidget(self.label_7)

        self.comboBox_4 = QComboBox(self.frame_10)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_13.addWidget(self.comboBox_4)

        self.horizontalLayout_13.setStretch(1, 1)
        self.horizontalLayout_13.setStretch(2, 10)

        self.verticalLayout_10.addWidget(self.frame_10)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.checkBox_7 = QCheckBox(self.frame_3)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.horizontalLayout_3.addWidget(self.checkBox_7)

        self.horizontalLayout_3.setStretch(0, 20)

        self.verticalLayout_10.addWidget(self.frame_3)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_15)

        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_14.addWidget(self.label_8)

        self.comboBox_5 = QComboBox(self.frame_11)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.horizontalLayout_14.addWidget(self.comboBox_5)

        self.horizontalLayout_14.setStretch(1, 1)
        self.horizontalLayout_14.setStretch(2, 10)

        self.verticalLayout_10.addWidget(self.frame_11)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.checkBox_8 = QCheckBox(self.frame_5)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.horizontalLayout_5.addWidget(self.checkBox_8)

        self.horizontalLayout_5.setStretch(0, 20)

        self.verticalLayout_10.addWidget(self.frame_5)

        self.frame_12 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_17 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_17)

        self.label_9 = QLabel(self.frame_12)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_15.addWidget(self.label_9)

        self.comboBox_6 = QComboBox(self.frame_12)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.horizontalLayout_15.addWidget(self.comboBox_6)

        self.horizontalLayout_15.setStretch(1, 1)
        self.horizontalLayout_15.setStretch(2, 10)

        self.verticalLayout_10.addWidget(self.frame_12)

        self.verticalSpacer_2 = QSpacerItem(20, 314, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_3.addWidget(self.scrollArea_3)

        self.stackedWidget.addWidget(self.event_state)
        self.another_event_state = QWidget()
        self.another_event_state.setObjectName(u"another_event_state")
        self.verticalLayout_4 = QVBoxLayout(self.another_event_state)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea_2 = QScrollArea(self.another_event_state)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 932, 515))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.checkBox_10 = QCheckBox(self.scrollAreaWidgetContents_4)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.verticalLayout_9.addWidget(self.checkBox_10)

        self.widget = QWidget(self.scrollAreaWidgetContents_4)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.verticalLayout_9.addWidget(self.widget)

        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_9.addWidget(self.pushButton_2, 0, Qt.AlignmentFlag.AlignRight)

        self.checkBox_11 = QCheckBox(self.scrollAreaWidgetContents_4)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.verticalLayout_9.addWidget(self.checkBox_11)

        self.widget_2 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_6 = QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.verticalLayout_9.addWidget(self.widget_2)

        self.pushButton_3 = QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_9.addWidget(self.pushButton_3, 0, Qt.AlignmentFlag.AlignRight)

        self.checkBox_9 = QCheckBox(self.scrollAreaWidgetContents_4)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.verticalLayout_9.addWidget(self.checkBox_9)

        self.widget_3 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_7 = QVBoxLayout(self.widget_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.verticalLayout_9.addWidget(self.widget_3)

        self.pushButton_4 = QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_9.addWidget(self.pushButton_4, 0, Qt.AlignmentFlag.AlignRight)

        self.verticalSpacer_3 = QSpacerItem(20, 39, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_4.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.another_event_state)
        self.event_occurring = QWidget()
        self.event_occurring.setObjectName(u"event_occurring")
        self.verticalLayout_11 = QVBoxLayout(self.event_occurring)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.scrollArea_4 = QScrollArea(self.event_occurring)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 932, 515))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_4 = QWidget(self.scrollAreaWidgetContents_6)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_13 = QVBoxLayout(self.widget_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")

        self.verticalLayout_12.addWidget(self.widget_4)

        self.pushButton_5 = QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_12.addWidget(self.pushButton_5, 0, Qt.AlignmentFlag.AlignRight)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_4)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_11.addWidget(self.scrollArea_4)

        self.stackedWidget.addWidget(self.event_occurring)
        self.event_state_comparing = QWidget()
        self.event_state_comparing.setObjectName(u"event_state_comparing")
        self.verticalLayout_14 = QVBoxLayout(self.event_state_comparing)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.scrollArea_5 = QScrollArea(self.event_state_comparing)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, -556, 920, 1071))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.checkBox_12 = QCheckBox(self.scrollAreaWidgetContents_7)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.verticalLayout_15.addWidget(self.checkBox_12)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_14 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_14)

        self.checkBox_4 = QCheckBox(self.frame_6)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout_6.addWidget(self.checkBox_4)


        self.verticalLayout_15.addWidget(self.frame_6)

        self.widget_5 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
        self.verticalLayout_16 = QVBoxLayout(self.widget_5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_15.addWidget(self.widget_5)

        self.pushButton_6 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_15.addWidget(self.pushButton_6, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_16 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_16)

        self.checkBox_5 = QCheckBox(self.frame_7)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.horizontalLayout_7.addWidget(self.checkBox_5)


        self.verticalLayout_15.addWidget(self.frame_7)

        self.widget_6 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.verticalLayout_17 = QVBoxLayout(self.widget_6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_15.addWidget(self.widget_6)

        self.pushButton_7 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_15.addWidget(self.pushButton_7, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_18 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_18)

        self.checkBox_13 = QCheckBox(self.frame_8)
        self.checkBox_13.setObjectName(u"checkBox_13")

        self.horizontalLayout_8.addWidget(self.checkBox_13)


        self.verticalLayout_15.addWidget(self.frame_8)

        self.widget_8 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy1.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy1)
        self.verticalLayout_19 = QVBoxLayout(self.widget_8)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_15.addWidget(self.widget_8)

        self.pushButton_9 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout_15.addWidget(self.pushButton_9, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_13 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_19 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_19)

        self.checkBox_14 = QCheckBox(self.frame_13)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.horizontalLayout_9.addWidget(self.checkBox_14)


        self.verticalLayout_15.addWidget(self.frame_13)

        self.widget_7 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy1.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy1)
        self.verticalLayout_18 = QVBoxLayout(self.widget_7)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_15.addWidget(self.widget_7)

        self.pushButton_8 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_15.addWidget(self.pushButton_8, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_14 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_20 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_20)

        self.checkBox_15 = QCheckBox(self.frame_14)
        self.checkBox_15.setObjectName(u"checkBox_15")

        self.horizontalLayout_16.addWidget(self.checkBox_15)


        self.verticalLayout_15.addWidget(self.frame_14)

        self.widget_9 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy1.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy1)
        self.verticalLayout_20 = QVBoxLayout(self.widget_9)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_15.addWidget(self.widget_9)

        self.pushButton_10 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.verticalLayout_15.addWidget(self.pushButton_10, 0, Qt.AlignmentFlag.AlignRight)

        self.checkBox_18 = QCheckBox(self.scrollAreaWidgetContents_7)
        self.checkBox_18.setObjectName(u"checkBox_18")

        self.verticalLayout_15.addWidget(self.checkBox_18)

        self.frame_15 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_26 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_26)

        self.checkBox_21 = QCheckBox(self.frame_15)
        self.checkBox_21.setObjectName(u"checkBox_21")

        self.horizontalLayout_22.addWidget(self.checkBox_21)


        self.verticalLayout_15.addWidget(self.frame_15)

        self.widget_10 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy1.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy1)
        self.verticalLayout_26 = QVBoxLayout(self.widget_10)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_15.addWidget(self.widget_10)

        self.pushButton_11 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.verticalLayout_15.addWidget(self.pushButton_11, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_16 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_27 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_27)

        self.checkBox_22 = QCheckBox(self.frame_16)
        self.checkBox_22.setObjectName(u"checkBox_22")

        self.horizontalLayout_23.addWidget(self.checkBox_22)


        self.verticalLayout_15.addWidget(self.frame_16)

        self.widget_11 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy1.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy1)
        self.verticalLayout_27 = QVBoxLayout(self.widget_11)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_15.addWidget(self.widget_11)

        self.pushButton_12 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.verticalLayout_15.addWidget(self.pushButton_12, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_17 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_28 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_28)

        self.checkBox_23 = QCheckBox(self.frame_17)
        self.checkBox_23.setObjectName(u"checkBox_23")

        self.horizontalLayout_24.addWidget(self.checkBox_23)


        self.verticalLayout_15.addWidget(self.frame_17)

        self.widget_12 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy1.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy1)
        self.verticalLayout_28 = QVBoxLayout(self.widget_12)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_15.addWidget(self.widget_12)

        self.pushButton_13 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.verticalLayout_15.addWidget(self.pushButton_13, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_18 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_32 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_32)

        self.checkBox_27 = QCheckBox(self.frame_18)
        self.checkBox_27.setObjectName(u"checkBox_27")

        self.horizontalLayout_28.addWidget(self.checkBox_27)


        self.verticalLayout_15.addWidget(self.frame_18)

        self.widget_13 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy1.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy1)
        self.verticalLayout_29 = QVBoxLayout(self.widget_13)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_15.addWidget(self.widget_13)

        self.pushButton_14 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.verticalLayout_15.addWidget(self.pushButton_14, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_19 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_33 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_33)

        self.checkBox_28 = QCheckBox(self.frame_19)
        self.checkBox_28.setObjectName(u"checkBox_28")

        self.horizontalLayout_29.addWidget(self.checkBox_28)


        self.verticalLayout_15.addWidget(self.frame_19)

        self.widget_14 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy1.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy1)
        self.verticalLayout_30 = QVBoxLayout(self.widget_14)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_15.addWidget(self.widget_14)

        self.pushButton_15 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.verticalLayout_15.addWidget(self.pushButton_15, 0, Qt.AlignmentFlag.AlignRight)

        self.checkBox_33 = QCheckBox(self.scrollAreaWidgetContents_7)
        self.checkBox_33.setObjectName(u"checkBox_33")

        self.verticalLayout_15.addWidget(self.checkBox_33)

        self.frame_20 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_39 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_39)

        self.checkBox_35 = QCheckBox(self.frame_20)
        self.checkBox_35.setObjectName(u"checkBox_35")

        self.horizontalLayout_35.addWidget(self.checkBox_35)


        self.verticalLayout_15.addWidget(self.frame_20)

        self.widget_15 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy1.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy1)
        self.verticalLayout_38 = QVBoxLayout(self.widget_15)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_15.addWidget(self.widget_15)

        self.pushButton_16 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.verticalLayout_15.addWidget(self.pushButton_16, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_21 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_40 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_40)

        self.checkBox_36 = QCheckBox(self.frame_21)
        self.checkBox_36.setObjectName(u"checkBox_36")

        self.horizontalLayout_36.addWidget(self.checkBox_36)


        self.verticalLayout_15.addWidget(self.frame_21)

        self.widget_16 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_16.setObjectName(u"widget_16")
        sizePolicy1.setHeightForWidth(self.widget_16.sizePolicy().hasHeightForWidth())
        self.widget_16.setSizePolicy(sizePolicy1)
        self.verticalLayout_39 = QVBoxLayout(self.widget_16)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_15.addWidget(self.widget_16)

        self.pushButton_17 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.verticalLayout_15.addWidget(self.pushButton_17, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_22 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_41 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_41)

        self.checkBox_37 = QCheckBox(self.frame_22)
        self.checkBox_37.setObjectName(u"checkBox_37")

        self.horizontalLayout_37.addWidget(self.checkBox_37)


        self.verticalLayout_15.addWidget(self.frame_22)

        self.widget_17 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_17.setObjectName(u"widget_17")
        sizePolicy1.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy1)
        self.verticalLayout_40 = QVBoxLayout(self.widget_17)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_15.addWidget(self.widget_17)

        self.pushButton_18 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.verticalLayout_15.addWidget(self.pushButton_18, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_23 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_42 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_42)

        self.checkBox_38 = QCheckBox(self.frame_23)
        self.checkBox_38.setObjectName(u"checkBox_38")

        self.horizontalLayout_38.addWidget(self.checkBox_38)


        self.verticalLayout_15.addWidget(self.frame_23)

        self.widget_18 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy1.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy1)
        self.verticalLayout_41 = QVBoxLayout(self.widget_18)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_15.addWidget(self.widget_18)

        self.pushButton_19 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.verticalLayout_15.addWidget(self.pushButton_19, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_24 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy)
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_43 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_43)

        self.checkBox_39 = QCheckBox(self.frame_24)
        self.checkBox_39.setObjectName(u"checkBox_39")

        self.horizontalLayout_39.addWidget(self.checkBox_39)


        self.verticalLayout_15.addWidget(self.frame_24)

        self.pushButton_20 = QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.verticalLayout_15.addWidget(self.pushButton_20, 0, Qt.AlignmentFlag.AlignRight)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_5)

        self.widget_19 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_19.setObjectName(u"widget_19")
        sizePolicy1.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy1)
        self.verticalLayout_42 = QVBoxLayout(self.widget_19)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_15.addWidget(self.widget_19)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_14.addWidget(self.scrollArea_5)

        self.stackedWidget.addWidget(self.event_state_comparing)
        self.another_event_state_comparing = QWidget()
        self.another_event_state_comparing.setObjectName(u"another_event_state_comparing")
        self.verticalLayout_59 = QVBoxLayout(self.another_event_state_comparing)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.scrollArea_6 = QScrollArea(self.another_event_state_comparing)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 920, 1071))
        self.verticalLayout_43 = QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.checkBox_40 = QCheckBox(self.scrollAreaWidgetContents_9)
        self.checkBox_40.setObjectName(u"checkBox_40")

        self.verticalLayout_43.addWidget(self.checkBox_40)

        self.frame_25 = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy)
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_44 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_44)

        self.checkBox_41 = QCheckBox(self.frame_25)
        self.checkBox_41.setObjectName(u"checkBox_41")

        self.horizontalLayout_40.addWidget(self.checkBox_41)


        self.verticalLayout_43.addWidget(self.frame_25)

        self.widget_20 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_20.setObjectName(u"widget_20")
        sizePolicy1.setHeightForWidth(self.widget_20.sizePolicy().hasHeightForWidth())
        self.widget_20.setSizePolicy(sizePolicy1)
        self.verticalLayout_44 = QVBoxLayout(self.widget_20)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_43.addWidget(self.widget_20)

        self.pushButton_21 = QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.verticalLayout_43.addWidget(self.pushButton_21, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_26 = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_45 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_45)

        self.checkBox_42 = QCheckBox(self.frame_26)
        self.checkBox_42.setObjectName(u"checkBox_42")

        self.horizontalLayout_41.addWidget(self.checkBox_42)


        self.verticalLayout_43.addWidget(self.frame_26)

        self.widget_21 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_21.setObjectName(u"widget_21")
        sizePolicy1.setHeightForWidth(self.widget_21.sizePolicy().hasHeightForWidth())
        self.widget_21.setSizePolicy(sizePolicy1)
        self.verticalLayout_45 = QVBoxLayout(self.widget_21)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_43.addWidget(self.widget_21)

        self.pushButton_22 = QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.verticalLayout_43.addWidget(self.pushButton_22, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_27 = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy)
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_46 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_46)

        self.checkBox_43 = QCheckBox(self.frame_27)
        self.checkBox_43.setObjectName(u"checkBox_43")

        self.horizontalLayout_42.addWidget(self.checkBox_43)


        self.verticalLayout_43.addWidget(self.frame_27)

        self.widget_22 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_22.setObjectName(u"widget_22")
        sizePolicy1.setHeightForWidth(self.widget_22.sizePolicy().hasHeightForWidth())
        self.widget_22.setSizePolicy(sizePolicy1)
        self.verticalLayout_46 = QVBoxLayout(self.widget_22)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_43.addWidget(self.widget_22)

        self.pushButton_23 = QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.verticalLayout_43.addWidget(self.pushButton_23, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_28 = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy)
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_47 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_47)

        self.checkBox_44 = QCheckBox(self.frame_28)
        self.checkBox_44.setObjectName(u"checkBox_44")

        self.horizontalLayout_43.addWidget(self.checkBox_44)


        self.verticalLayout_43.addWidget(self.frame_28)

        self.widget_23 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_23.setObjectName(u"widget_23")
        sizePolicy1.setHeightForWidth(self.widget_23.sizePolicy().hasHeightForWidth())
        self.widget_23.setSizePolicy(sizePolicy1)
        self.verticalLayout_47 = QVBoxLayout(self.widget_23)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_43.addWidget(self.widget_23)

        self.pushButton_24 = QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.verticalLayout_43.addWidget(self.pushButton_24, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_29 = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy)
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_48 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_48)

        self.checkBox_45 = QCheckBox(self.frame_29)
        self.checkBox_45.setObjectName(u"checkBox_45")

        self.horizontalLayout_44.addWidget(self.checkBox_45)


        self.verticalLayout_43.addWidget(self.frame_29)

        self.widget_24 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_24.setObjectName(u"widget_24")
        sizePolicy1.setHeightForWidth(self.widget_24.sizePolicy().hasHeightForWidth())
        self.widget_24.setSizePolicy(sizePolicy1)
        self.verticalLayout_48 = QVBoxLayout(self.widget_24)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_43.addWidget(self.widget_24)

        self.pushButton_25 = QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.verticalLayout_43.addWidget(self.pushButton_25, 0, Qt.AlignmentFlag.AlignRight)

        self.checkBox_46 = QCheckBox(self.scrollAreaWidgetContents_9)
        self.checkBox_46.setObjectName(u"checkBox_46")

        self.verticalLayout_43.addWidget(self.checkBox_46)

        self.frame_30 = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy)
        self.frame_30.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_49 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_49)

        self.checkBox_47 = QCheckBox(self.frame_30)
        self.checkBox_47.setObjectName(u"checkBox_47")

        self.horizontalLayout_45.addWidget(self.checkBox_47)


        self.verticalLayout_43.addWidget(self.frame_30)

        self.widget_25 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_25.setObjectName(u"widget_25")
        sizePolicy1.setHeightForWidth(self.widget_25.sizePolicy().hasHeightForWidth())
        self.widget_25.setSizePolicy(sizePolicy1)
        self.verticalLayout_49 = QVBoxLayout(self.widget_25)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_43.addWidget(self.widget_25)

        self.pushButton_26 = QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_26.setObjectName(u"pushButton_26")

        self.verticalLayout_43.addWidget(self.pushButton_26, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_31 = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_31.setObjectName(u"frame_31")
        sizePolicy.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy)
        self.frame_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_50 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_50)

        self.checkBox_48 = QCheckBox(self.frame_31)
        self.checkBox_48.setObjectName(u"checkBox_48")

        self.horizontalLayout_46.addWidget(self.checkBox_48)


        self.verticalLayout_43.addWidget(self.frame_31)

        self.widget_26 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_26.setObjectName(u"widget_26")
        sizePolicy1.setHeightForWidth(self.widget_26.sizePolicy().hasHeightForWidth())
        self.widget_26.setSizePolicy(sizePolicy1)
        self.verticalLayout_50 = QVBoxLayout(self.widget_26)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_43.addWidget(self.widget_26)

        self.pushButton_27 = QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_27.setObjectName(u"pushButton_27")

        self.verticalLayout_43.addWidget(self.pushButton_27, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_32 = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy)
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_51 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_51)

        self.checkBox_49 = QCheckBox(self.frame_32)
        self.checkBox_49.setObjectName(u"checkBox_49")

        self.horizontalLayout_47.addWidget(self.checkBox_49)


        self.verticalLayout_43.addWidget(self.frame_32)

        self.widget_27 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_27.setObjectName(u"widget_27")
        sizePolicy1.setHeightForWidth(self.widget_27.sizePolicy().hasHeightForWidth())
        self.widget_27.setSizePolicy(sizePolicy1)
        self.verticalLayout_51 = QVBoxLayout(self.widget_27)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_43.addWidget(self.widget_27)

        self.pushButton_28 = QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_28.setObjectName(u"pushButton_28")

        self.verticalLayout_43.addWidget(self.pushButton_28, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_33 = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_33.setObjectName(u"frame_33")
        sizePolicy.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy)
        self.frame_33.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_52 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_52)

        self.checkBox_50 = QCheckBox(self.frame_33)
        self.checkBox_50.setObjectName(u"checkBox_50")

        self.horizontalLayout_48.addWidget(self.checkBox_50)


        self.verticalLayout_43.addWidget(self.frame_33)

        self.widget_28 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_28.setObjectName(u"widget_28")
        sizePolicy1.setHeightForWidth(self.widget_28.sizePolicy().hasHeightForWidth())
        self.widget_28.setSizePolicy(sizePolicy1)
        self.verticalLayout_52 = QVBoxLayout(self.widget_28)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_43.addWidget(self.widget_28)

        self.pushButton_29 = QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_29.setObjectName(u"pushButton_29")

        self.verticalLayout_43.addWidget(self.pushButton_29, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_34 = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy)
        self.frame_34.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_53 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_49.addItem(self.horizontalSpacer_53)

        self.checkBox_51 = QCheckBox(self.frame_34)
        self.checkBox_51.setObjectName(u"checkBox_51")

        self.horizontalLayout_49.addWidget(self.checkBox_51)


        self.verticalLayout_43.addWidget(self.frame_34)

        self.widget_29 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_29.setObjectName(u"widget_29")
        sizePolicy1.setHeightForWidth(self.widget_29.sizePolicy().hasHeightForWidth())
        self.widget_29.setSizePolicy(sizePolicy1)
        self.verticalLayout_53 = QVBoxLayout(self.widget_29)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_43.addWidget(self.widget_29)

        self.pushButton_30 = QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_30.setObjectName(u"pushButton_30")

        self.verticalLayout_43.addWidget(self.pushButton_30, 0, Qt.AlignmentFlag.AlignRight)

        self.checkBox_52 = QCheckBox(self.scrollAreaWidgetContents_9)
        self.checkBox_52.setObjectName(u"checkBox_52")

        self.verticalLayout_43.addWidget(self.checkBox_52)

        self.frame_35 = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_35.setObjectName(u"frame_35")
        sizePolicy.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy)
        self.frame_35.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_54 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_50.addItem(self.horizontalSpacer_54)

        self.checkBox_53 = QCheckBox(self.frame_35)
        self.checkBox_53.setObjectName(u"checkBox_53")

        self.horizontalLayout_50.addWidget(self.checkBox_53)


        self.verticalLayout_43.addWidget(self.frame_35)

        self.widget_30 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_30.setObjectName(u"widget_30")
        sizePolicy1.setHeightForWidth(self.widget_30.sizePolicy().hasHeightForWidth())
        self.widget_30.setSizePolicy(sizePolicy1)
        self.verticalLayout_54 = QVBoxLayout(self.widget_30)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_43.addWidget(self.widget_30)

        self.pushButton_31 = QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_31.setObjectName(u"pushButton_31")

        self.verticalLayout_43.addWidget(self.pushButton_31, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_36 = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_36.setObjectName(u"frame_36")
        sizePolicy.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy)
        self.frame_36.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_55 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_55)

        self.checkBox_54 = QCheckBox(self.frame_36)
        self.checkBox_54.setObjectName(u"checkBox_54")

        self.horizontalLayout_51.addWidget(self.checkBox_54)


        self.verticalLayout_43.addWidget(self.frame_36)

        self.widget_31 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_31.setObjectName(u"widget_31")
        sizePolicy1.setHeightForWidth(self.widget_31.sizePolicy().hasHeightForWidth())
        self.widget_31.setSizePolicy(sizePolicy1)
        self.verticalLayout_55 = QVBoxLayout(self.widget_31)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_43.addWidget(self.widget_31)

        self.pushButton_32 = QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_32.setObjectName(u"pushButton_32")

        self.verticalLayout_43.addWidget(self.pushButton_32, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_37 = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_37.setObjectName(u"frame_37")
        sizePolicy.setHeightForWidth(self.frame_37.sizePolicy().hasHeightForWidth())
        self.frame_37.setSizePolicy(sizePolicy)
        self.frame_37.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_56 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_52.addItem(self.horizontalSpacer_56)

        self.checkBox_55 = QCheckBox(self.frame_37)
        self.checkBox_55.setObjectName(u"checkBox_55")

        self.horizontalLayout_52.addWidget(self.checkBox_55)


        self.verticalLayout_43.addWidget(self.frame_37)

        self.widget_32 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_32.setObjectName(u"widget_32")
        sizePolicy1.setHeightForWidth(self.widget_32.sizePolicy().hasHeightForWidth())
        self.widget_32.setSizePolicy(sizePolicy1)
        self.verticalLayout_56 = QVBoxLayout(self.widget_32)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_43.addWidget(self.widget_32)

        self.pushButton_33 = QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_33.setObjectName(u"pushButton_33")

        self.verticalLayout_43.addWidget(self.pushButton_33, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_38 = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy)
        self.frame_38.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_57 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_57)

        self.checkBox_56 = QCheckBox(self.frame_38)
        self.checkBox_56.setObjectName(u"checkBox_56")

        self.horizontalLayout_53.addWidget(self.checkBox_56)


        self.verticalLayout_43.addWidget(self.frame_38)

        self.widget_33 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_33.setObjectName(u"widget_33")
        sizePolicy1.setHeightForWidth(self.widget_33.sizePolicy().hasHeightForWidth())
        self.widget_33.setSizePolicy(sizePolicy1)
        self.verticalLayout_57 = QVBoxLayout(self.widget_33)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_43.addWidget(self.widget_33)

        self.pushButton_34 = QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_34.setObjectName(u"pushButton_34")

        self.verticalLayout_43.addWidget(self.pushButton_34, 0, Qt.AlignmentFlag.AlignRight)

        self.frame_39 = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_39.setObjectName(u"frame_39")
        sizePolicy.setHeightForWidth(self.frame_39.sizePolicy().hasHeightForWidth())
        self.frame_39.setSizePolicy(sizePolicy)
        self.frame_39.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_58 = QSpacerItem(17, 21, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_58)

        self.checkBox_57 = QCheckBox(self.frame_39)
        self.checkBox_57.setObjectName(u"checkBox_57")

        self.horizontalLayout_54.addWidget(self.checkBox_57)


        self.verticalLayout_43.addWidget(self.frame_39)

        self.pushButton_35 = QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_35.setObjectName(u"pushButton_35")

        self.verticalLayout_43.addWidget(self.pushButton_35, 0, Qt.AlignmentFlag.AlignRight)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_43.addItem(self.verticalSpacer_6)

        self.widget_34 = QWidget(self.scrollAreaWidgetContents_9)
        self.widget_34.setObjectName(u"widget_34")
        sizePolicy1.setHeightForWidth(self.widget_34.sizePolicy().hasHeightForWidth())
        self.widget_34.setSizePolicy(sizePolicy1)
        self.verticalLayout_58 = QVBoxLayout(self.widget_34)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_43.addWidget(self.widget_34)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_9)

        self.verticalLayout_59.addWidget(self.scrollArea_6)

        self.stackedWidget.addWidget(self.another_event_state_comparing)
        self.event_state_of_property = QWidget()
        self.event_state_of_property.setObjectName(u"event_state_of_property")
        self.verticalLayout_63 = QVBoxLayout(self.event_state_of_property)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.scrollArea_7 = QScrollArea(self.event_state_of_property)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 932, 515))
        self.verticalLayout_64 = QVBoxLayout(self.scrollAreaWidgetContents_10)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.checkBox_59 = QCheckBox(self.scrollAreaWidgetContents_10)
        self.checkBox_59.setObjectName(u"checkBox_59")

        self.verticalLayout_64.addWidget(self.checkBox_59)

        self.widget_37 = QWidget(self.scrollAreaWidgetContents_10)
        self.widget_37.setObjectName(u"widget_37")
        self.verticalLayout_62 = QVBoxLayout(self.widget_37)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")

        self.verticalLayout_64.addWidget(self.widget_37)

        self.pushButton_36 = QPushButton(self.scrollAreaWidgetContents_10)
        self.pushButton_36.setObjectName(u"pushButton_36")

        self.verticalLayout_64.addWidget(self.pushButton_36, 0, Qt.AlignmentFlag.AlignRight)

        self.checkBox_58 = QCheckBox(self.scrollAreaWidgetContents_10)
        self.checkBox_58.setObjectName(u"checkBox_58")

        self.verticalLayout_64.addWidget(self.checkBox_58)

        self.widget_36 = QWidget(self.scrollAreaWidgetContents_10)
        self.widget_36.setObjectName(u"widget_36")
        self.verticalLayout_61 = QVBoxLayout(self.widget_36)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")

        self.verticalLayout_64.addWidget(self.widget_36)

        self.pushButton_38 = QPushButton(self.scrollAreaWidgetContents_10)
        self.pushButton_38.setObjectName(u"pushButton_38")

        self.verticalLayout_64.addWidget(self.pushButton_38, 0, Qt.AlignmentFlag.AlignRight)

        self.checkBox_60 = QCheckBox(self.scrollAreaWidgetContents_10)
        self.checkBox_60.setObjectName(u"checkBox_60")

        self.verticalLayout_64.addWidget(self.checkBox_60)

        self.widget_35 = QWidget(self.scrollAreaWidgetContents_10)
        self.widget_35.setObjectName(u"widget_35")
        self.verticalLayout_60 = QVBoxLayout(self.widget_35)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")

        self.verticalLayout_64.addWidget(self.widget_35)

        self.pushButton_37 = QPushButton(self.scrollAreaWidgetContents_10)
        self.pushButton_37.setObjectName(u"pushButton_37")

        self.verticalLayout_64.addWidget(self.pushButton_37, 0, Qt.AlignmentFlag.AlignRight)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_64.addItem(self.verticalSpacer_7)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_10)

        self.verticalLayout_63.addWidget(self.scrollArea_7)

        self.stackedWidget.addWidget(self.event_state_of_property)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_69 = QVBoxLayout(self.page)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.scrollArea_8 = QScrollArea(self.page)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setObjectName(u"scrollAreaWidgetContents_11")
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 932, 515))
        self.verticalLayout_65 = QVBoxLayout(self.scrollAreaWidgetContents_11)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.checkBox_61 = QCheckBox(self.scrollAreaWidgetContents_11)
        self.checkBox_61.setObjectName(u"checkBox_61")

        self.verticalLayout_65.addWidget(self.checkBox_61)

        self.widget_38 = QWidget(self.scrollAreaWidgetContents_11)
        self.widget_38.setObjectName(u"widget_38")
        self.verticalLayout_66 = QVBoxLayout(self.widget_38)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")

        self.verticalLayout_65.addWidget(self.widget_38)

        self.pushButton_39 = QPushButton(self.scrollAreaWidgetContents_11)
        self.pushButton_39.setObjectName(u"pushButton_39")

        self.verticalLayout_65.addWidget(self.pushButton_39, 0, Qt.AlignmentFlag.AlignRight)

        self.checkBox_62 = QCheckBox(self.scrollAreaWidgetContents_11)
        self.checkBox_62.setObjectName(u"checkBox_62")

        self.verticalLayout_65.addWidget(self.checkBox_62)

        self.widget_39 = QWidget(self.scrollAreaWidgetContents_11)
        self.widget_39.setObjectName(u"widget_39")
        self.verticalLayout_67 = QVBoxLayout(self.widget_39)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")

        self.verticalLayout_65.addWidget(self.widget_39)

        self.pushButton_40 = QPushButton(self.scrollAreaWidgetContents_11)
        self.pushButton_40.setObjectName(u"pushButton_40")

        self.verticalLayout_65.addWidget(self.pushButton_40, 0, Qt.AlignmentFlag.AlignRight)

        self.checkBox_63 = QCheckBox(self.scrollAreaWidgetContents_11)
        self.checkBox_63.setObjectName(u"checkBox_63")

        self.verticalLayout_65.addWidget(self.checkBox_63)

        self.widget_40 = QWidget(self.scrollAreaWidgetContents_11)
        self.widget_40.setObjectName(u"widget_40")
        self.verticalLayout_68 = QVBoxLayout(self.widget_40)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")

        self.verticalLayout_65.addWidget(self.widget_40)

        self.pushButton_41 = QPushButton(self.scrollAreaWidgetContents_11)
        self.pushButton_41.setObjectName(u"pushButton_41")

        self.verticalLayout_65.addWidget(self.pushButton_41, 0, Qt.AlignmentFlag.AlignRight)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_65.addItem(self.verticalSpacer_8)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_11)

        self.verticalLayout_69.addWidget(self.scrollArea_8)

        self.stackedWidget.addWidget(self.page)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)


        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Trigger", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"Time delay from previous occurrance", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"seconds", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"Time delay from initial app launch", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"seconds", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Random time delay from previous occurrance", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Upper time limit", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"seconds", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Lower time limit", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"seconds", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"Random time delay from initial app launch", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Lower time limit", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"seconds", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Upper time limit", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"seconds", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Next state trigger", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Next state", None))
        self.checkBox_7.setText(QCoreApplication.translate("Dialog", u"Present state trigger", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Present state", None))
        self.checkBox_8.setText(QCoreApplication.translate("Dialog", u"Previous state trigger", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Previous state", None))
        self.checkBox_10.setText(QCoreApplication.translate("Dialog", u"Next state trigger", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Add next state trigger for another event", None))
        self.checkBox_11.setText(QCoreApplication.translate("Dialog", u"Present state trigger", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Add present state trigger for another event", None))
        self.checkBox_9.setText(QCoreApplication.translate("Dialog", u"Previous state trigger", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Add previous state trigger for another event", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Add event occurring trigger for another event", None))
        self.checkBox_12.setText(QCoreApplication.translate("Dialog", u"Next state comparing", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Next state greater than", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"Add next state greater than trigger  for another property", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"Next state greater than or equal to", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"Add next state greater than or equal to trigger for another property", None))
        self.checkBox_13.setText(QCoreApplication.translate("Dialog", u"Next state less than", None))
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"Add next state less than trigger for another property", None))
        self.checkBox_14.setText(QCoreApplication.translate("Dialog", u"Next state less than or equal to", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"Add next state less than or equal to trigger for another property", None))
        self.checkBox_15.setText(QCoreApplication.translate("Dialog", u"Next state equal to", None))
        self.pushButton_10.setText(QCoreApplication.translate("Dialog", u"Add next state equal to trigger for another property", None))
        self.checkBox_18.setText(QCoreApplication.translate("Dialog", u"Present state comparing", None))
        self.checkBox_21.setText(QCoreApplication.translate("Dialog", u"Present state greater than", None))
        self.pushButton_11.setText(QCoreApplication.translate("Dialog", u"Add present state greater than trigger for another property", None))
        self.checkBox_22.setText(QCoreApplication.translate("Dialog", u"Present state greater than or equal to", None))
        self.pushButton_12.setText(QCoreApplication.translate("Dialog", u"Add present state greater than or equal to trigger for another property", None))
        self.checkBox_23.setText(QCoreApplication.translate("Dialog", u"Present state less than", None))
        self.pushButton_13.setText(QCoreApplication.translate("Dialog", u"Add present state less than trigger for another property", None))
        self.checkBox_27.setText(QCoreApplication.translate("Dialog", u"Present state less than or equal to", None))
        self.pushButton_14.setText(QCoreApplication.translate("Dialog", u"Add present state less than or equal to trigger for another property", None))
        self.checkBox_28.setText(QCoreApplication.translate("Dialog", u"Present state equal to", None))
        self.pushButton_15.setText(QCoreApplication.translate("Dialog", u"Add present state equal to trigger for another property", None))
        self.checkBox_33.setText(QCoreApplication.translate("Dialog", u"Previous state comparing", None))
        self.checkBox_35.setText(QCoreApplication.translate("Dialog", u"Previous state greater than", None))
        self.pushButton_16.setText(QCoreApplication.translate("Dialog", u"Add previous state greater than trigger for another property", None))
        self.checkBox_36.setText(QCoreApplication.translate("Dialog", u"Previous state greater than or equal to", None))
        self.pushButton_17.setText(QCoreApplication.translate("Dialog", u"Add previous state greater than or equal to trigger for another property", None))
        self.checkBox_37.setText(QCoreApplication.translate("Dialog", u"Previous state less than", None))
        self.pushButton_18.setText(QCoreApplication.translate("Dialog", u"Add previous state less than trigger for another property", None))
        self.checkBox_38.setText(QCoreApplication.translate("Dialog", u"Previous state less than or equal to", None))
        self.pushButton_19.setText(QCoreApplication.translate("Dialog", u"Add previous state less than or equal to trigger for another property", None))
        self.checkBox_39.setText(QCoreApplication.translate("Dialog", u"Previous state equal to", None))
        self.pushButton_20.setText(QCoreApplication.translate("Dialog", u"Add previous state equal to trigger for another property", None))
        self.checkBox_40.setText(QCoreApplication.translate("Dialog", u"Next state comparing", None))
        self.checkBox_41.setText(QCoreApplication.translate("Dialog", u"Next state greater than", None))
        self.pushButton_21.setText(QCoreApplication.translate("Dialog", u"Add next state greater than trigger  for another property", None))
        self.checkBox_42.setText(QCoreApplication.translate("Dialog", u"Next state greater than or equal to", None))
        self.pushButton_22.setText(QCoreApplication.translate("Dialog", u"Add next state greater than or equal to trigger for another property", None))
        self.checkBox_43.setText(QCoreApplication.translate("Dialog", u"Next state less than", None))
        self.pushButton_23.setText(QCoreApplication.translate("Dialog", u"Add next state less than trigger for another property", None))
        self.checkBox_44.setText(QCoreApplication.translate("Dialog", u"Next state less than or equal to", None))
        self.pushButton_24.setText(QCoreApplication.translate("Dialog", u"Add next state less than or equal to trigger for another property", None))
        self.checkBox_45.setText(QCoreApplication.translate("Dialog", u"Next state equal to", None))
        self.pushButton_25.setText(QCoreApplication.translate("Dialog", u"Add next state equal to trigger for another property", None))
        self.checkBox_46.setText(QCoreApplication.translate("Dialog", u"Present state comparing", None))
        self.checkBox_47.setText(QCoreApplication.translate("Dialog", u"Present state greater than", None))
        self.pushButton_26.setText(QCoreApplication.translate("Dialog", u"Add present state greater than trigger for another property", None))
        self.checkBox_48.setText(QCoreApplication.translate("Dialog", u"Present state greater than or equal to", None))
        self.pushButton_27.setText(QCoreApplication.translate("Dialog", u"Add present state greater than or equal to trigger for another property", None))
        self.checkBox_49.setText(QCoreApplication.translate("Dialog", u"Present state less than", None))
        self.pushButton_28.setText(QCoreApplication.translate("Dialog", u"Add present state less than trigger for another property", None))
        self.checkBox_50.setText(QCoreApplication.translate("Dialog", u"Present state less than or equal to", None))
        self.pushButton_29.setText(QCoreApplication.translate("Dialog", u"Add present state less than or equal to trigger for another property", None))
        self.checkBox_51.setText(QCoreApplication.translate("Dialog", u"Present state equal to", None))
        self.pushButton_30.setText(QCoreApplication.translate("Dialog", u"Add present state equal to trigger for another property", None))
        self.checkBox_52.setText(QCoreApplication.translate("Dialog", u"Previous state comparing", None))
        self.checkBox_53.setText(QCoreApplication.translate("Dialog", u"Previous state greater than", None))
        self.pushButton_31.setText(QCoreApplication.translate("Dialog", u"Add previous state greater than trigger for another property", None))
        self.checkBox_54.setText(QCoreApplication.translate("Dialog", u"Previous state greater than or equal to", None))
        self.pushButton_32.setText(QCoreApplication.translate("Dialog", u"Add previous state greater than or equal to trigger for another property", None))
        self.checkBox_55.setText(QCoreApplication.translate("Dialog", u"Previous state less than", None))
        self.pushButton_33.setText(QCoreApplication.translate("Dialog", u"Add previous state less than trigger for another property", None))
        self.checkBox_56.setText(QCoreApplication.translate("Dialog", u"Previous state less than or equal to", None))
        self.pushButton_34.setText(QCoreApplication.translate("Dialog", u"Add previous state less than or equal to trigger for another property", None))
        self.checkBox_57.setText(QCoreApplication.translate("Dialog", u"Previous state equal to", None))
        self.pushButton_35.setText(QCoreApplication.translate("Dialog", u"Add previous state equal to trigger for another property", None))
        self.checkBox_59.setText(QCoreApplication.translate("Dialog", u"Next state of property", None))
        self.pushButton_36.setText(QCoreApplication.translate("Dialog", u"Add next state of property trigger for another event", None))
        self.checkBox_58.setText(QCoreApplication.translate("Dialog", u"Present state of property", None))
        self.pushButton_38.setText(QCoreApplication.translate("Dialog", u"Add present state of property trigger for another event", None))
        self.checkBox_60.setText(QCoreApplication.translate("Dialog", u"Previous state of property", None))
        self.pushButton_37.setText(QCoreApplication.translate("Dialog", u"Add previous state of property trigger for another event", None))
        self.checkBox_61.setText(QCoreApplication.translate("Dialog", u"Next state of property", None))
        self.pushButton_39.setText(QCoreApplication.translate("Dialog", u"Add next state of property trigger for another event", None))
        self.checkBox_62.setText(QCoreApplication.translate("Dialog", u"Present state of property", None))
        self.pushButton_40.setText(QCoreApplication.translate("Dialog", u"Add present state of property trigger for another event", None))
        self.checkBox_63.setText(QCoreApplication.translate("Dialog", u"Previous state of property", None))
        self.pushButton_41.setText(QCoreApplication.translate("Dialog", u"Add previous state of property trigger for another event", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Add Trigger", None))
    # retranslateUi

