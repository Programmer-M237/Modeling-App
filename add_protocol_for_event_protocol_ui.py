# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_protocol_for_event_protocol.ui'
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
    QHBoxLayout, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(669, 521)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.horizontalLayout.setStretch(1, 10)

        self.verticalLayout.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.direct_protocol = QWidget()
        self.direct_protocol.setObjectName(u"direct_protocol")
        self.verticalLayout_2 = QVBoxLayout(self.direct_protocol)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.direct_protocol)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 631, 421))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboBox_2 = QComboBox(self.frame_2)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_2.addWidget(self.comboBox_2)

        self.horizontalLayout_2.setStretch(1, 10)

        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_40 = QFrame(self.scrollAreaWidgetContents)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy)
        self.frame_40.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_40)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_55.addWidget(self.label_3)

        self.spinBox = QSpinBox(self.frame_40)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout_55.addWidget(self.spinBox)

        self.horizontalLayout_55.setStretch(1, 10)

        self.verticalLayout_3.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.scrollAreaWidgetContents)
        self.frame_41.setObjectName(u"frame_41")
        sizePolicy.setHeightForWidth(self.frame_41.sizePolicy().hasHeightForWidth())
        self.frame_41.setSizePolicy(sizePolicy)
        self.frame_41.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_41)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_57.addWidget(self.label_5)

        self.spinBox_2 = QSpinBox(self.frame_41)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.horizontalLayout_57.addWidget(self.spinBox_2)

        self.horizontalLayout_57.setStretch(1, 10)

        self.verticalLayout_3.addWidget(self.frame_41)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.direct_protocol)
        self.incremental_or_decremental_protocol = QWidget()
        self.incremental_or_decremental_protocol.setObjectName(u"incremental_or_decremental_protocol")
        self.verticalLayout_4 = QVBoxLayout(self.incremental_or_decremental_protocol)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea_2 = QScrollArea(self.incremental_or_decremental_protocol)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 631, 421))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_3 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.comboBox_3 = QComboBox(self.frame_3)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_3.addWidget(self.comboBox_3)

        self.horizontalLayout_3.setStretch(1, 10)

        self.verticalLayout_5.addWidget(self.frame_3)

        self.stackedWidget_2 = QStackedWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.incremental = QWidget()
        self.incremental.setObjectName(u"incremental")
        self.verticalLayout_6 = QVBoxLayout(self.incremental)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_4 = QFrame(self.incremental)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.comboBox_4 = QComboBox(self.frame_4)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_4.addWidget(self.comboBox_4)

        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.spinBox_3 = QSpinBox(self.frame_4)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.horizontalLayout_4.addWidget(self.spinBox_3)

        self.horizontalLayout_4.setStretch(1, 5)
        self.horizontalLayout_4.setStretch(3, 5)

        self.verticalLayout_6.addWidget(self.frame_4)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.stackedWidget_2.addWidget(self.incremental)
        self.decremental = QWidget()
        self.decremental.setObjectName(u"decremental")
        self.verticalLayout_9 = QVBoxLayout(self.decremental)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_5 = QFrame(self.decremental)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)

        self.comboBox_5 = QComboBox(self.frame_5)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.horizontalLayout_5.addWidget(self.comboBox_5)

        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_5.addWidget(self.label_10)

        self.spinBox_4 = QSpinBox(self.frame_5)
        self.spinBox_4.setObjectName(u"spinBox_4")

        self.horizontalLayout_5.addWidget(self.spinBox_4)

        self.horizontalLayout_5.setStretch(1, 5)
        self.horizontalLayout_5.setStretch(3, 5)

        self.verticalLayout_9.addWidget(self.frame_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.stackedWidget_2.addWidget(self.decremental)

        self.verticalLayout_5.addWidget(self.stackedWidget_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_4.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.incremental_or_decremental_protocol)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Protocol", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Next state ==", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Upper limit index of state", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Lower limit index of state", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Protocol type", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Next state ==", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Next state ==", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Add protocol", None))
    # retranslateUi

