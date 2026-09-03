import datetime
import hashlib
import importlib
import json
import os
import tempfile
import traceback
import urllib
from inspect import isclass
from typing import Literal

from PySide6.QtCore import QUrl
from PySide6.QtGui import QCursor, QGuiApplication
from PySide6.QtWidgets import QFileDialog, QMessageBox, QMenu

from PyUB.Types import Helper
from PyUB.utils import retranslate_nested_langconstants
from . import detail_calculator
from .. import customviews
from ..settings import Settings
from ..view import chat_views
from ..view import langconsts as lc
from ..view.chat_views import ChatViewBase
from ..view.datatypes import DeepSeekMessage
from ..view.fragments_widget import FragmentsWidget
from ..view.main_widget import MainWidget
from ..view.select_chats_dialog import SelectChatsDialog
from ..view.select_msg_dialog import SelectMsgDialog
from . import settings_manager as sm

data = None
main_widget = MainWidget.instance() if MainWidget.instance() is not None else MainWidget()
msg_indexes = []
selected_message_chain: list[DeepSeekMessage] = []
helper = Helper()
temp_webpages = {}
custom_view_modules = {}

def _on_load_data():
    global data, main_widget
    filename = QFileDialog.getOpenFileName(parent=main_widget,
                                           caption=lc.OPEN_DATA_CAPTION(),
                                           filter=lc.OPEN_DATA_FILTER())

    if not filename[0]:
        return

    try:
        data = json.load(open(filename[0], encoding="utf-8"))
        main_widget.ui.chat_list_comboBox.blockSignals(True)
        main_widget.ui.chat_list_comboBox.clear()
        for chat in data:
            main_widget.ui.chat_list_comboBox.addItem(chat["title"])
        main_widget.ui.chat_list_comboBox.blockSignals(False)
        if not main_widget.ui.select_last_msg_btn.isEnabled() \
                and main_widget.ui.chat_list_comboBox.count() > 0:
            main_widget.ui.select_last_msg_btn.setEnabled(True)

        main_widget.data_stats.chat_count = len(data)
        main_widget.data_stats.file_path = filename[0]
        _on_chat_changed()
    except Exception as e:
        QMessageBox.warning(main_widget, f"{lc.ERROR}!", f"{lc.CANNOT_LOAD_SOURCE_DATA}!")
        data = None



def _on_chat_changed():
    chat_index = main_widget.ui.chat_list_comboBox.currentIndex()

    global msg_indexes, selected_message_chain
    msg_indexes = [k for k in data[chat_index]["mapping"].keys() if k != "root"]

    main_widget.chat_stats.block_handler_exec(True)
    main_widget.chat_stats.total_msg_count = len(msg_indexes)
    main_widget.chat_stats.chain_msg_count = 0
    main_widget.chat_stats.msg_thread_token_count_requests = -1
    main_widget.chat_stats.msg_thread_token_count_responses = -1
    main_widget.chat_stats.msg_thread_word_count_requests = -1
    main_widget.chat_stats.msg_thread_word_count_responses = -1
    main_widget.chat_stats.msg_thread_char_count_requests = -1
    main_widget.chat_stats.msg_thread_char_count_responses = -1
    main_widget.chat_stats.inserted_datetime = datetime.datetime.fromisoformat(data[chat_index]["inserted_at"])
    main_widget.chat_stats.updated_datetime = datetime.datetime.fromisoformat(data[chat_index]["updated_at"])
    main_widget.chat_stats.block_handler_exec(False)
    main_widget.chat_stats.exec_attr_changed_handler()

    selected_message_chain.clear()
    main_widget.ui.chat_text_plain_text.clear()
    main_widget.ui.chat_text_rich_text.clear()
    main_widget.ui.webEngineView.setHtml("")


def _on_select_last_msg():
    chat_index = main_widget.ui.chat_list_comboBox.currentIndex()
    dialog = SelectMsgDialog(main_widget)
    dialog.setWindowTitle(lc.SELECT_LAST_MSG_TITLE())

    dialog.set_minimum(1)
    dialog.set_maximum(len(msg_indexes))
    dialog.set_value(dialog.get_maximum())

    def output_msg(value: int):
        text = ""
        value -= 1
        for fragment in data[chat_index]["mapping"][msg_indexes[value]]["message"]["fragments"]:
            match fragment["type"]:
                case "REQUEST":
                    text += f"<{lc.REQUEST}>"
                case "SEARCH" | "TOOL_SEARCH":
                    text += f"<{lc.FRAGMENT_SEARCH}>"
                case "RESPONSE":
                    text += f"<{lc.RESPONSE}>"
                case "THINK":
                    text += f"<{lc.THINKING}>"
                case _:
                    continue

            text += "\n"
            if "content" in fragment:
                text += fragment["content"]
            text += 2 * "\n"
        dialog.set_plain_text(text)

    dialog.curr_msg_changed.connect(output_msg)
    output_msg(dialog.get_value())

    if sm.settings.contains("last_msg_dialog_sizes"):
        dialog.setGeometry(sm.settings.value("last_msg_dialog_sizes"))

    result = dialog.exec()

    sm.settings.setValue("last_msg_dialog_sizes", dialog.geometry())

    if result:
        ds_messages = []
        curr_message =  data[chat_index]["mapping"][msg_indexes[dialog.get_value() - 1]]
        while True:
            ds_message = DeepSeekMessage()
            ds_message.inserted_datetime = datetime.datetime.fromisoformat(curr_message["message"]["inserted_at"])

            match curr_message["message"]["model"]:
                case "deepseek-reasoner":
                    ds_message.model = DeepSeekMessage.Model.DEEPSEEK_REASONER
                case "deepseek-chat":
                    ds_message.model = DeepSeekMessage.Model.DEEPSEEK_CHAT
                case _:
                    ds_message.model = DeepSeekMessage.Model.UNKNOWN

            ds_message.fragments = []
            for fragment in curr_message["message"]["fragments"]:
                msg_fragment = DeepSeekMessage.Fragment()

                match fragment["type"]:
                    case "REQUEST":
                        msg_fragment.type = DeepSeekMessage.Fragment.Type.REQUEST
                        msg_fragment.content = fragment["content"]
                    case "RESPONSE":
                        msg_fragment.type = DeepSeekMessage.Fragment.Type.RESPONSE
                        msg_fragment.content = fragment["content"]
                    case "THINK":
                        msg_fragment.type = DeepSeekMessage.Fragment.Type.THINK
                        msg_fragment.content = fragment["content"]
                    case "TOOL_SEARCH":
                        msg_fragment.type = DeepSeekMessage.Fragment.Type.TOOL_SEARCH
                        msg_fragment.search_result = \
                            [DeepSeekMessage.Fragment.SearchResultItem(**i) for i in fragment["results"]]
                    case _:
                        continue

                ds_message.fragments.append(msg_fragment)

            ds_messages.append(ds_message)
            parent_id = curr_message["parent"]
            if parent_id and parent_id != "root":
                curr_message = data[chat_index]["mapping"][parent_id]
            else:
                break

        global selected_message_chain
        selected_message_chain = ds_messages
        ds_messages.reverse()
        main_widget.chat_stats.chain_msg_count = len(ds_messages)

        detail_calculator.calculate_details(msg_thread=selected_message_chain,
                                            calc_tokens=Settings.calculate_tokens.value,
                                            calc_words=Settings.calculate_words.value,
                                            calc_chars=Settings.calculate_chars.value)

        _on_output_selected_message_chain()
    dialog.deleteLater()

def _on_output_selected_message_chain():
    if main_widget.ui.view_options_comboBox.currentIndex() < 0 or not selected_message_chain:
        return

    view: chat_views.ChatViewBase = main_widget.ui.view_options_comboBox.currentData()

    def get_key(s: str) -> str:
        if len(s) <= 2_000:
            meta = s
        else:
            meta = f"{len(s)}_{s[:1000]}_{s[-1000:]}"
        return hashlib.md5(meta.encode("utf-8")).hexdigest()

    try:
        result_text = view.chat_to_text(selected_message_chain)
    except Exception as e:
        result_text = f"{lc.VIEW_USING_FAILED}:\n\n{traceback.format_exc()}"
        main_widget.ui.stackedWidget.setCurrentIndex(0)
        main_widget.ui.chat_text_plain_text.setPlainText(result_text)
        return

    if view.type == ChatViewBase.Type.PLAIN_TEXT:
        main_widget.ui.stackedWidget.setCurrentIndex(0)
        main_widget.ui.chat_text_plain_text.setPlainText(result_text)
    elif view.type in (ChatViewBase.Type.MARKDOWN, ChatViewBase.Type.HTML4):
        main_widget.ui.stackedWidget.setCurrentIndex(1)
        if view.type == ChatViewBase.Type.HTML4:
            main_widget.ui.chat_text_rich_text.setHtml(result_text)
        elif view.type == ChatViewBase.Type.MARKDOWN:
            main_widget.ui.chat_text_rich_text.setMarkdown(result_text)
    else:
        main_widget.ui.stackedWidget.setCurrentIndex(2)
        LIMIT_LENGTH = 2 * 1024 * 1024 - 50_000
        if len(urllib.parse.quote(result_text)) < LIMIT_LENGTH:
            main_widget.ui.webEngineView.setHtml(result_text)
        else:
            key = get_key(result_text)
            if key not in temp_webpages:
                with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w", encoding="utf-8") as f:
                    f.write(result_text)
                    temp_webpages[key] = f.name
            main_widget.ui.webEngineView.load(QUrl.fromLocalFile(temp_webpages[key]))

def _on_update_slicing_fragments():
    if not selected_message_chain:
        QMessageBox.warning(main_widget,
                            f"{lc.ERROR}!", f"{lc.MSG_CHAIN_EMPTY_ERROR}!")
        return

    view: chat_views.ChatViewBase = main_widget.ui.view_options_comboBox.currentData()
    if view.type != ChatViewBase.Type.PLAIN_TEXT:
        QMessageBox.warning(main_widget, f"{lc.ERROR}!",
                            f"{lc.VIEW_TYPE_ERROR}!")
        return

    fw = FragmentsWidget(messages=selected_message_chain,
                         view=view,
                         fragment_length=main_widget.ui.fragment_length_spinBox.value(),
                         parent=main_widget.ui.fragments_scrollArea)
    main_widget.ui.fragments_scrollArea.setWidget(fw)

def _on_reload_views():
    importlib.reload(chat_views)

    import_report = customviews.import_modules()
    if not import_report.is_success:
        QMessageBox.warning(main_widget, f"{lc.WARNING}!",
                            lc.CANNOT_IMPORT_MODULES_WITH_VIEWS().format(", ".join(import_report.trouble_modules)))

    main_widget.ui.view_options_comboBox.clear()
    module_list = [chat_views]
    module_list.extend(customviews.view_modules)
    trouble_views = []
    for module in module_list:
        for name, attr in vars(module).items():
            if name.startswith("__"):
                continue
            if isclass(attr) and issubclass(attr, chat_views.ChatViewBase) and attr is not chat_views.ChatViewBase:
                try:
                    if attr.type == ChatViewBase.Type.PLAIN_TEXT:
                        view_type = lc.PLAIN_TEXT()
                    elif attr.type == ChatViewBase.Type.HTML4:
                        view_type = f"{lc.HTML}4"
                    elif attr.type == ChatViewBase.Type.HTML5:
                        view_type = f"{lc.HTML}5"
                    elif attr.type == ChatViewBase.Type.MARKDOWN:
                        view_type = lc.MARKDOWN()
                    else:
                        trouble_views.append(str(attr))
                        continue
                    main_widget.ui.view_options_comboBox.addItem(f"{attr.title} ({view_type})", attr)
                except Exception as e:
                    trouble_views.append(str(attr))
    if trouble_views:
        QMessageBox.warning(main_widget, f"{lc.WARNING}!",
                            f"{lc.CANNOT_USE_THESE_VIEWS}: {", ".join(trouble_views)}")


    _on_output_selected_message_chain()

def _handle_extra_action(operation:Literal["export_selected_chats", "save_as_md", "save_as_text", "save_as_html", "save_to_clipboard"]):
    view = main_widget.ui.view_options_comboBox.currentData()
    if operation == "save_to_clipboard":
        clipboard = QGuiApplication.clipboard()
        match view.type:
            case ChatViewBase.Type.PLAIN_TEXT:
                clipboard.setText(main_widget.ui.chat_text_plain_text.toPlainText())
            case ChatViewBase.Type.MARKDOWN:
                clipboard.setText(main_widget.ui.chat_text_rich_text.toMarkdown())
            case ChatViewBase.Type.HTML4 | ChatViewBase.Type.HTML5:
                try:
                    clipboard.setText(view.chat_to_text(selected_message_chain))
                except Exception as e:
                    clipboard.setText(f"{lc.VIEW_USING_FAILED}:\n\n{traceback.format_exc()}")
    elif operation == "export_selected_chats":
        dialog = SelectChatsDialog(main_widget)
        if sm.settings.contains("select_chats_dialog_sizes"):
            dialog.setGeometry(sm.settings.value("select_chats_dialog_sizes"))
        dialog.set_items([chat["title"] for chat in data])
        result = dialog.exec()
        sm.settings.setValue("select_chats_dialog_sizes", dialog.geometry())
        if result:
            selected_indexes = dialog.selected_indexes()
            if len(selected_indexes) > 0:
                filepath = QFileDialog.getSaveFileName(
                    main_widget,
                    lc.SAVE_SELECTED_CHATS(),
                    filter=lc.OPEN_DATA_FILTER())[0]
                if filepath:
                    with open(filepath, "w", encoding="utf-8") as f:
                        json.dump([data[i] for i in selected_indexes], f, ensure_ascii=False)

            else:
                QMessageBox.warning(main_widget, f"{lc.ERROR}!", lc.NO_CHATS_SELECTED())
        dialog.deleteLater()

    else:
        filepath = ""
        saving_text = ""
        match operation:
            case "save_as_md":
                filepath = QFileDialog.getSaveFileName(
                    main_widget,
                    f"{lc.SAVE_MSG_THREAD_AS} {lc.MARKDOWN}",
                    filter=f"{lc.MARKDOWN} (*.md)")[0]
                saving_text = main_widget.ui.chat_text_rich_text.toMarkdown()
            case "save_as_text":
                filepath = QFileDialog.getSaveFileName(
                    main_widget,
                    f"{lc.SAVE_MSG_THREAD_AS} {lc.PLAIN_TEXT}",
                    filter=f"{lc.PLAIN_TEXT} (*.txt)")[0]
                saving_text = main_widget.ui.chat_text_plain_text.toPlainText()
            case "save_as_html":
                filepath = QFileDialog.getSaveFileName(
                    main_widget,
                    f"{lc.SAVE_MSG_THREAD_AS} {lc.HTML}",
                    filter=f"{lc.HTML} (*.html)")[0]
                try:
                    saving_text = view.chat_to_text(selected_message_chain)
                except Exception as e:
                    saving_text = f"{lc.VIEW_USING_FAILED}:\n\n{traceback.format_exc()}"
        if filepath:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(saving_text)

def _on_extra_actions():
    menu = QMenu(main_widget)

    action = menu.addAction(lc.SAVE_MSG_THREAD_CLIPBOARD())
    action.triggered.connect(lambda: _handle_extra_action("save_to_clipboard"))
    action.setEnabled(len(selected_message_chain) > 0)

    action = menu.addAction(lc.SELECT_AND_EXPORT_CHATS())
    action.triggered.connect(lambda: _handle_extra_action("export_selected_chats"))
    action.setEnabled(data is not None)

    action = menu.addAction("")
    view: ChatViewBase = main_widget.ui.view_options_comboBox.currentData()
    action.setEnabled(len(selected_message_chain) > 0)
    match view.type:
        case ChatViewBase.Type.PLAIN_TEXT:
            action.setText(f"{lc.SAVE_MSG_THREAD_AS} {lc.PLAIN_TEXT}")
            action.triggered.connect(lambda: _handle_extra_action("save_as_text"))
        case ChatViewBase.Type.MARKDOWN:
            action.setText(f"{lc.SAVE_MSG_THREAD_AS} {lc.MARKDOWN}")
            action.triggered.connect(lambda: _handle_extra_action("save_as_md"))
        case ChatViewBase.Type.HTML4 | ChatViewBase.Type.HTML5:
            action.setText(f"{lc.SAVE_MSG_THREAD_AS} {lc.HTML}")
            action.triggered.connect(lambda: _handle_extra_action("save_as_html"))

    menu.aboutToHide.connect(menu.deleteLater)
    menu.popup(QCursor.pos())

def _on_retranslate():
    retranslate_nested_langconstants(lc)
    main_widget.retranslate()
    _on_reload_views()

def _on_cleanup():
    if temp_webpages:
        for page in temp_webpages.values():
            if not os.path.exists(page):
                continue
            try:
                os.remove(page)
            except Exception as e:
                pass


# init
helper.plugin_language_changing.connect(_on_retranslate)
helper.app_closing.connect(_on_cleanup)
helper.plugin_deactivating.connect(_on_cleanup)

main_widget.ui.view_options_comboBox.currentIndexChanged.connect(_on_output_selected_message_chain)
main_widget.ui.load_conversation_btn.clicked.connect(_on_load_data)
main_widget.ui.chat_list_comboBox.currentIndexChanged.connect(_on_chat_changed)
main_widget.ui.select_last_msg_btn.clicked.connect(_on_select_last_msg)
main_widget.ui.update_fragments_btn.clicked.connect(_on_update_slicing_fragments)
main_widget.ui.reload_views_btn.clicked.connect(_on_reload_views)
main_widget.ui.extra_actions_btn.clicked.connect(_on_extra_actions)