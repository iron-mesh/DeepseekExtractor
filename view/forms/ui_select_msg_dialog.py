# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select-msg-dialog - DeepSeekExtractorbmmMOy.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QDialogButtonBox,
                               QFrame, QHBoxLayout, QLabel, QPlainTextEdit,
                               QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
                               QVBoxLayout)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(723, 575)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plainTextEdit = QPlainTextEdit(Dialog)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 5, -1, 10)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.first_msg_btn = QPushButton(Dialog)
        self.first_msg_btn.setObjectName(u"first_msg_btn")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSkipBackward))
        self.first_msg_btn.setIcon(icon)
        self.first_msg_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.first_msg_btn)

        self.prev_msg_btn = QPushButton(Dialog)
        self.prev_msg_btn.setObjectName(u"prev_msg_btn")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSeekBackward))
        self.prev_msg_btn.setIcon(icon1)
        self.prev_msg_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.prev_msg_btn)

        self.curr_msg_spinBox = QSpinBox(Dialog)
        self.curr_msg_spinBox.setObjectName(u"curr_msg_spinBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.curr_msg_spinBox.sizePolicy().hasHeightForWidth())
        self.curr_msg_spinBox.setSizePolicy(sizePolicy)
        self.curr_msg_spinBox.setMaximum(100)

        self.horizontalLayout.addWidget(self.curr_msg_spinBox)

        self.page_count_label = QLabel(Dialog)
        self.page_count_label.setObjectName(u"page_count_label")

        self.horizontalLayout.addWidget(self.page_count_label)

        self.next_msg_btn = QPushButton(Dialog)
        self.next_msg_btn.setObjectName(u"next_msg_btn")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSeekForward))
        self.next_msg_btn.setIcon(icon2)
        self.next_msg_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.next_msg_btn)

        self.last_msg_btn = QPushButton(Dialog)
        self.last_msg_btn.setObjectName(u"last_msg_btn")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSkipForward))
        self.last_msg_btn.setIcon(icon3)
        self.last_msg_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.last_msg_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.first_msg_btn.setText("")
        self.prev_msg_btn.setText("")
        self.page_count_label.setText(QCoreApplication.translate("Dialog", u"/100", None))
        self.next_msg_btn.setText("")
        self.last_msg_btn.setText("")
    # retranslateUi

