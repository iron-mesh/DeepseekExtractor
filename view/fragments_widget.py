import traceback

from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QWidget, QGridLayout, QPlainTextEdit, QLabel, QPushButton

from .chat_views import ChatViewBase
from . import langconsts as lc
from .datatypes import DeepSeekMessage


class FragmentsWidget(QWidget):

    def __init__(self, messages: list[DeepSeekMessage], fragment_length: int,
                 view: ChatViewBase, parent=None):
        super().__init__(parent)
        layout = QGridLayout(self)

        marker: int = 0
        row: int = 0
        is_working = True
        while is_working:
            if marker + fragment_length >= len(messages):
                slice_range = (marker, len(messages))
                is_working = False
            else:
                slice_range = (marker, marker + fragment_length)
                marker += fragment_length

            fr_info = QLabel(f"{row + 1}")

            fr_text = QPlainTextEdit()
            fr_text.setReadOnly(True)
            fr_text.setMinimumHeight(200)
            try:
                fr_text.setPlainText(view.chat_to_text(messages[slice_range[0]:slice_range[1]]))
            except Exception as e:
                fr_text.setPlainText(f"{lc.VIEW_USING_FAILED}:\n\n{traceback.format_exc()}")
                is_working = False

            fr_copy_btn = QPushButton(lc.COPY())
            fr_copy_btn.setProperty("text_source", fr_text)
            fr_copy_btn.clicked.connect(self._on_copy_btn_clicked)

            layout.addWidget(fr_info, row, 0)
            layout.addWidget(fr_text, row, 1)
            layout.addWidget(fr_copy_btn, row, 2)

            row += 1

    def _on_copy_btn_clicked(self):
        plain_text_edit: QPlainTextEdit = self.sender().property("text_source")
        if not plain_text_edit.styleSheet():
            plain_text_edit.setStyleSheet("background-color: rgb(0, 170, 0)")
            clipboard = QGuiApplication.clipboard()
            clipboard.setText(plain_text_edit.toPlainText())
        else:
            plain_text_edit.setStyleSheet("")