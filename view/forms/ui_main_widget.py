# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_widget - DeepSeekExtractorTjqqyq.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, QUrl, Qt)
from PySide6.QtGui import (QIcon)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QComboBox, QFrame, QGridLayout,
                               QHBoxLayout, QLabel, QPlainTextEdit, QPushButton,
                               QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
                               QSplitter, QStackedWidget, QTabWidget, QTextEdit,
                               QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1083, 827)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        self.source = QWidget()
        self.source.setObjectName(u"source")
        self.verticalLayout_3 = QVBoxLayout(self.source)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.source)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.splitter = QSplitter(self.widget_3)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(10)
        self.splitter.setChildrenCollapsible(True)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(300, 0))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.load_conversation_btn = QPushButton(self.widget)
        self.load_conversation_btn.setObjectName(u"load_conversation_btn")

        self.verticalLayout_7.addWidget(self.load_conversation_btn)

        self.chat_list_comboBox = QComboBox(self.widget)
        self.chat_list_comboBox.setObjectName(u"chat_list_comboBox")

        self.verticalLayout_7.addWidget(self.chat_list_comboBox)

        self.select_last_msg_btn = QPushButton(self.widget)
        self.select_last_msg_btn.setObjectName(u"select_last_msg_btn")
        self.select_last_msg_btn.setEnabled(False)

        self.verticalLayout_7.addWidget(self.select_last_msg_btn)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.view_options_comboBox = QComboBox(self.widget)
        self.view_options_comboBox.setObjectName(u"view_options_comboBox")

        self.horizontalLayout.addWidget(self.view_options_comboBox)

        self.view_info_btn = QPushButton(self.widget)
        self.view_info_btn.setObjectName(u"view_info_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.view_info_btn.sizePolicy().hasHeightForWidth())
        self.view_info_btn.setSizePolicy(sizePolicy1)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.InsertImage))
        self.view_info_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.view_info_btn)

        self.reload_views_btn = QPushButton(self.widget)
        self.reload_views_btn.setObjectName(u"reload_views_btn")
        sizePolicy1.setHeightForWidth(self.reload_views_btn.sizePolicy().hasHeightForWidth())
        self.reload_views_btn.setSizePolicy(sizePolicy1)
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.reload_views_btn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.reload_views_btn)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(0, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.stats_richtext = QTextEdit(self.widget)
        self.stats_richtext.setObjectName(u"stats_richtext")
        self.stats_richtext.setReadOnly(True)
        self.stats_richtext.setHtml(u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")

        self.verticalLayout_7.addWidget(self.stats_richtext)

        self.extra_actions_btn = QPushButton(self.widget)
        self.extra_actions_btn.setObjectName(u"extra_actions_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.extra_actions_btn.sizePolicy().hasHeightForWidth())
        self.extra_actions_btn.setSizePolicy(sizePolicy2)
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentProperties))
        self.extra_actions_btn.setIcon(icon2)
        self.extra_actions_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_7.addWidget(self.extra_actions_btn)

        self.splitter.addWidget(self.widget)
        self.stackedWidget = QStackedWidget(self.splitter)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.plaintext = QWidget()
        self.plaintext.setObjectName(u"plaintext")
        self.verticalLayout_2 = QVBoxLayout(self.plaintext)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.chat_text_plain_text = QPlainTextEdit(self.plaintext)
        self.chat_text_plain_text.setObjectName(u"chat_text_plain_text")
        self.chat_text_plain_text.setPlainText(u"")

        self.verticalLayout_2.addWidget(self.chat_text_plain_text)

        self.stackedWidget.addWidget(self.plaintext)
        self.richtext = QWidget()
        self.richtext.setObjectName(u"richtext")
        self.verticalLayout_5 = QVBoxLayout(self.richtext)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.chat_text_rich_text = QTextEdit(self.richtext)
        self.chat_text_rich_text.setObjectName(u"chat_text_rich_text")
        self.chat_text_rich_text.setOverwriteMode(False)

        self.verticalLayout_5.addWidget(self.chat_text_rich_text)

        self.stackedWidget.addWidget(self.richtext)
        self.webbrowser = QWidget()
        self.webbrowser.setObjectName(u"webbrowser")
        self.verticalLayout = QVBoxLayout(self.webbrowser)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.webEngineView = QWebEngineView(self.webbrowser)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.verticalLayout.addWidget(self.webEngineView)

        self.stackedWidget.addWidget(self.webbrowser)
        self.splitter.addWidget(self.stackedWidget)

        self.verticalLayout_4.addWidget(self.splitter)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.tabWidget.addTab(self.source, "")
        self.slicing = QWidget()
        self.slicing.setObjectName(u"slicing")
        self.verticalLayout_8 = QVBoxLayout(self.slicing)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.label_3 = QLabel(self.slicing)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.fragment_length_spinBox = QSpinBox(self.slicing)
        self.fragment_length_spinBox.setObjectName(u"fragment_length_spinBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.fragment_length_spinBox.sizePolicy().hasHeightForWidth())
        self.fragment_length_spinBox.setSizePolicy(sizePolicy3)
        self.fragment_length_spinBox.setMinimum(1)
        self.fragment_length_spinBox.setMaximum(999999999)
        self.fragment_length_spinBox.setValue(10)

        self.horizontalLayout_3.addWidget(self.fragment_length_spinBox)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.update_fragments_btn = QPushButton(self.slicing)
        self.update_fragments_btn.setObjectName(u"update_fragments_btn")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaylistRepeat))
        self.update_fragments_btn.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.update_fragments_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.fragments_scrollArea = QScrollArea(self.slicing)
        self.fragments_scrollArea.setObjectName(u"fragments_scrollArea")
        self.fragments_scrollArea.setFrameShape(QFrame.Shape.Box)
        self.fragments_scrollArea.setLineWidth(2)
        self.fragments_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1008, 742))
        self.fragments_scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_8.addWidget(self.fragments_scrollArea)

        self.tabWidget.addTab(self.slicing, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        self.load_conversation_btn.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Select file with source data (usually it's <span style=\" font-style:italic;\">conversations.json</span>)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.load_conversation_btn.setText(QCoreApplication.translate("Form", u"Load data", None))
#if QT_CONFIG(tooltip)
        self.chat_list_comboBox.setToolTip(QCoreApplication.translate("Form", u"Select a chat", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.select_last_msg_btn.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Select a message from the end of the thread of message from which the extraction will be performed</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.select_last_msg_btn.setText(QCoreApplication.translate("Form", u"Select last message", None))
#if QT_CONFIG(tooltip)
        self.view_options_comboBox.setToolTip(QCoreApplication.translate("Form", u"Select a view for thread of messages", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.view_info_btn.setToolTip(QCoreApplication.translate("Form", u"Show selected view's description", None))
#endif // QT_CONFIG(tooltip)
        self.view_info_btn.setText("")
#if QT_CONFIG(tooltip)
        self.reload_views_btn.setToolTip(QCoreApplication.translate("Form", u"Reload scriprt with views", None))
#endif // QT_CONFIG(tooltip)
        self.reload_views_btn.setText("")
        self.stats_richtext.setMarkdown("")
        self.stats_richtext.setPlaceholderText(QCoreApplication.translate("Form", u"Stats", None))
#if QT_CONFIG(tooltip)
        self.extra_actions_btn.setToolTip(QCoreApplication.translate("Form", u"Select extra actions", None))
#endif // QT_CONFIG(tooltip)
        self.extra_actions_btn.setText("")
        self.chat_text_plain_text.setPlaceholderText(QCoreApplication.translate("Form", u"Message thread text", None))
        self.chat_text_rich_text.setPlaceholderText(QCoreApplication.translate("Form", u"Message thread text", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.source), QCoreApplication.translate("Form", u"Source data", None))
#if QT_CONFIG(tooltip)
        self.slicing.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Form", u"Messages per fragment", None))
#if QT_CONFIG(tooltip)
        self.update_fragments_btn.setToolTip(QCoreApplication.translate("Form", u"Update fragments", None))
#endif // QT_CONFIG(tooltip)
        self.update_fragments_btn.setText(QCoreApplication.translate("Form", u"Update", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.slicing), QCoreApplication.translate("Form", u"Slicing", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.slicing), QCoreApplication.translate("Form", u"Splitting the selected thread of messages into fragments", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

