# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select-chats-dialog - DeepSeekExtractoryQNEGN.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QMetaObject, Qt)
from PySide6.QtWidgets import (QDialogButtonBox,
                               QFrame, QHBoxLayout, QLineEdit, QListView,
                               QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(880, 728)
        Dialog.setWindowTitle(u"Dialog")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.filter_lineEdit = QLineEdit(Dialog)
        self.filter_lineEdit.setObjectName(u"filter_lineEdit")

        self.horizontalLayout_2.addWidget(self.filter_lineEdit)

        self.show_checked_only_btn = QPushButton(Dialog)
        self.show_checked_only_btn.setObjectName(u"show_checked_only_btn")
        self.show_checked_only_btn.setText(u"Show \u0421hecked \u041enly")
        self.show_checked_only_btn.setCheckable(True)
        self.show_checked_only_btn.setChecked(False)

        self.horizontalLayout_2.addWidget(self.show_checked_only_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.listView = QListView(Dialog)
        self.listView.setObjectName(u"listView")

        self.verticalLayout.addWidget(self.listView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.select_all_btn = QPushButton(Dialog)
        self.select_all_btn.setObjectName(u"select_all_btn")
        self.select_all_btn.setText(u"Select All")

        self.horizontalLayout.addWidget(self.select_all_btn)

        self.deselect_all_btn = QPushButton(Dialog)
        self.deselect_all_btn.setObjectName(u"deselect_all_btn")
        self.deselect_all_btn.setText(u"Deselect All")

        self.horizontalLayout.addWidget(self.deselect_all_btn)


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
        pass
    # retranslateUi

