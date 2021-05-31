# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from CustomisedWidgets import QLabelWithPosition


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(46, 52, 64);\n"
"color: rgb(211, 215, 207);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_left = QWidget(self.widget)
        self.widget_left.setObjectName(u"widget_left")
        self.verticalLayout_3 = QVBoxLayout(self.widget_left)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.pushButton_brush = QPushButton(self.widget_left)
        self.buttonGroup_tool = QButtonGroup(MainWindow)
        self.buttonGroup_tool.setObjectName(u"buttonGroup_tool")
        self.buttonGroup_tool.addButton(self.pushButton_brush)
        self.pushButton_brush.setObjectName(u"pushButton_brush")
        self.pushButton_brush.setStyleSheet(u"font: 8pt \"Ubuntu\";")
        self.pushButton_brush.setCheckable(True)
        self.pushButton_brush.setChecked(True)
        self.pushButton_brush.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.pushButton_brush)

        self.pushButton_eraser = QPushButton(self.widget_left)
        self.buttonGroup_tool.addButton(self.pushButton_eraser)
        self.pushButton_eraser.setObjectName(u"pushButton_eraser")
        self.pushButton_eraser.setStyleSheet(u"font: 8pt \"Ubuntu\";")
        self.pushButton_eraser.setCheckable(True)
        self.pushButton_eraser.setChecked(False)
        self.pushButton_eraser.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.pushButton_eraser)

        self.checkBox_highlight_mouse = QCheckBox(self.widget_left)
        self.checkBox_highlight_mouse.setObjectName(u"checkBox_highlight_mouse")
        self.checkBox_highlight_mouse.setChecked(False)
        self.checkBox_highlight_mouse.setTristate(False)

        self.verticalLayout_3.addWidget(self.checkBox_highlight_mouse)

        self.checkBox_highlight_mask = QCheckBox(self.widget_left)
        self.checkBox_highlight_mask.setObjectName(u"checkBox_highlight_mask")
        self.checkBox_highlight_mask.setChecked(False)
        self.checkBox_highlight_mask.setTristate(False)

        self.verticalLayout_3.addWidget(self.checkBox_highlight_mask)

        self.checkBox_showmask = QCheckBox(self.widget_left)
        self.checkBox_showmask.setObjectName(u"checkBox_showmask")
        self.checkBox_showmask.setChecked(True)

        self.verticalLayout_3.addWidget(self.checkBox_showmask)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(6, 10)

        self.horizontalLayout.addWidget(self.widget_left)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(480, 480))
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_filename = QLabel(self.widget_3)
        self.label_filename.setObjectName(u"label_filename")
        self.label_filename.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_filename)

        self.label_image = QLabelWithPosition(self.widget_3)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setMinimumSize(QSize(480, 480))
        self.label_image.setMaximumSize(QSize(480, 480))
        self.label_image.setStyleSheet(u"background-color: rgb(25, 29, 38);\n"
"color: rgb(255, 255, 255);")
        self.label_image.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_4.addWidget(self.label_image)

        self.widget_bottom = QWidget(self.widget_3)
        self.widget_bottom.setObjectName(u"widget_bottom")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_bottom)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 9, -1, 9)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_brush_1 = QPushButton(self.widget_bottom)
        self.buttonGroup_brush_size = QButtonGroup(MainWindow)
        self.buttonGroup_brush_size.setObjectName(u"buttonGroup_brush_size")
        self.buttonGroup_brush_size.addButton(self.pushButton_brush_1)
        self.pushButton_brush_1.setObjectName(u"pushButton_brush_1")
        self.pushButton_brush_1.setMaximumSize(QSize(25, 16777215))
        self.pushButton_brush_1.setCheckable(True)
        self.pushButton_brush_1.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.pushButton_brush_1)

        self.pushButton_brush_2 = QPushButton(self.widget_bottom)
        self.buttonGroup_brush_size.addButton(self.pushButton_brush_2)
        self.pushButton_brush_2.setObjectName(u"pushButton_brush_2")
        self.pushButton_brush_2.setMaximumSize(QSize(25, 16777215))
        self.pushButton_brush_2.setCheckable(True)
        self.pushButton_brush_2.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.pushButton_brush_2)

        self.pushButton_brush_3 = QPushButton(self.widget_bottom)
        self.buttonGroup_brush_size.addButton(self.pushButton_brush_3)
        self.pushButton_brush_3.setObjectName(u"pushButton_brush_3")
        self.pushButton_brush_3.setMaximumSize(QSize(25, 16777215))
        self.pushButton_brush_3.setCheckable(True)
        self.pushButton_brush_3.setChecked(True)
        self.pushButton_brush_3.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.pushButton_brush_3)

        self.pushButton_brush_4 = QPushButton(self.widget_bottom)
        self.buttonGroup_brush_size.addButton(self.pushButton_brush_4)
        self.pushButton_brush_4.setObjectName(u"pushButton_brush_4")
        self.pushButton_brush_4.setMaximumSize(QSize(25, 16777215))
        self.pushButton_brush_4.setCheckable(True)
        self.pushButton_brush_4.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.pushButton_brush_4)

        self.pushButton_brush_5 = QPushButton(self.widget_bottom)
        self.buttonGroup_brush_size.addButton(self.pushButton_brush_5)
        self.pushButton_brush_5.setObjectName(u"pushButton_brush_5")
        self.pushButton_brush_5.setMaximumSize(QSize(25, 16777215))
        self.pushButton_brush_5.setCheckable(True)
        self.pushButton_brush_5.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.pushButton_brush_5)

        self.pushButton_brush_6 = QPushButton(self.widget_bottom)
        self.buttonGroup_brush_size.addButton(self.pushButton_brush_6)
        self.pushButton_brush_6.setObjectName(u"pushButton_brush_6")
        self.pushButton_brush_6.setMaximumSize(QSize(25, 16777215))
        self.pushButton_brush_6.setCheckable(True)
        self.pushButton_brush_6.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.pushButton_brush_6)

        self.pushButton_brush_7 = QPushButton(self.widget_bottom)
        self.buttonGroup_brush_size.addButton(self.pushButton_brush_7)
        self.pushButton_brush_7.setObjectName(u"pushButton_brush_7")
        self.pushButton_brush_7.setMaximumSize(QSize(25, 16777215))
        self.pushButton_brush_7.setCheckable(True)
        self.pushButton_brush_7.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.pushButton_brush_7)

        self.pushButton_brush_8 = QPushButton(self.widget_bottom)
        self.buttonGroup_brush_size.addButton(self.pushButton_brush_8)
        self.pushButton_brush_8.setObjectName(u"pushButton_brush_8")
        self.pushButton_brush_8.setMaximumSize(QSize(25, 16777215))
        self.pushButton_brush_8.setCheckable(True)
        self.pushButton_brush_8.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.pushButton_brush_8)

        self.horizontalSpacer = QSpacerItem(464, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(9, 4)

        self.verticalLayout_4.addWidget(self.widget_bottom)


        self.horizontalLayout.addWidget(self.widget_3)

        self.widget_right = QWidget(self.widget)
        self.widget_right.setObjectName(u"widget_right")
        self.verticalLayout_2 = QVBoxLayout(self.widget_right)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 10, 0, 10)
        self.pushButton_set_label = QPushButton(self.widget_right)
        self.pushButton_set_label.setObjectName(u"pushButton_set_label")

        self.verticalLayout_2.addWidget(self.pushButton_set_label)

        self.label_label_dir = QLabel(self.widget_right)
        self.label_label_dir.setObjectName(u"label_label_dir")
        self.label_label_dir.setAlignment(Qt.AlignCenter)
        self.label_label_dir.setWordWrap(True)
        self.label_label_dir.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_2.addWidget(self.label_label_dir, 0, Qt.AlignVCenter)

        self.pushButton_images = QPushButton(self.widget_right)
        self.pushButton_images.setObjectName(u"pushButton_images")

        self.verticalLayout_2.addWidget(self.pushButton_images)

        self.listWidget = QListWidget(self.widget_right)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_2.addWidget(self.listWidget)

        self.widget_2 = QWidget(self.widget_right)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.pushButton_back = QPushButton(self.widget_2)
        self.pushButton_back.setObjectName(u"pushButton_back")

        self.horizontalLayout_3.addWidget(self.pushButton_back)

        self.pushButton_next = QPushButton(self.widget_2)
        self.pushButton_next.setObjectName(u"pushButton_next")

        self.horizontalLayout_3.addWidget(self.pushButton_next)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.pushButton_save = QPushButton(self.widget_right)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.verticalLayout_2.addWidget(self.pushButton_save)


        self.horizontalLayout.addWidget(self.widget_right)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 3)

        self.verticalLayout.addWidget(self.widget)

        self.verticalLayout.setStretch(0, 8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ui_main", None))
        self.pushButton_brush.setText(QCoreApplication.translate("MainWindow", u"\uff1c\u03a3\u4e09\u4e09\u4e09\u2203", None))
#if QT_CONFIG(shortcut)
        self.pushButton_brush.setShortcut(QCoreApplication.translate("MainWindow", u"B", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_eraser.setText(QCoreApplication.translate("MainWindow", u"| \u0332\u0305| \u0332\u0305 \u0332\u0305 \u0332\u0305 \u0332\u0305 \u0332\u0305|", None))
#if QT_CONFIG(shortcut)
        self.pushButton_eraser.setShortcut(QCoreApplication.translate("MainWindow", u"E", None))
#endif // QT_CONFIG(shortcut)
        self.checkBox_highlight_mouse.setText(QCoreApplication.translate("MainWindow", u"HL Mouse", None))
        self.checkBox_highlight_mask.setText(QCoreApplication.translate("MainWindow", u"HL Mask", None))
        self.checkBox_showmask.setText(QCoreApplication.translate("MainWindow", u"ShowMask", None))
        self.label_filename.setText("")
        self.label_image.setText(QCoreApplication.translate("MainWindow", u"\u1555( \u141b )\u1557", None))
        self.pushButton_brush_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.pushButton_brush_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_brush_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.pushButton_brush_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_brush_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.pushButton_brush_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_brush_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.pushButton_brush_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_brush_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.pushButton_brush_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_brush_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.pushButton_brush_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_brush_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.pushButton_brush_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_brush_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.pushButton_brush_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_set_label.setText(QCoreApplication.translate("MainWindow", u"Set Label Dir", None))
        self.label_label_dir.setText("")
        self.pushButton_images.setText(QCoreApplication.translate("MainWindow", u"Images", None))
        self.pushButton_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.pushButton_next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

