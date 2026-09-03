
#  Copyright (c)
#  2026 Ivan Balakirev (www.ironmesh.ru)
# 
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
# 
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
# 
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

from PySide6.QtWidgets import QWidget

from PyUB.bases import Singleton
from . import langconsts as lc
from .datatypes import DataStats, ChatStats
from .forms.ui_main_widget import Ui_Form


class MainWidget(Singleton, QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.data_stats = DataStats()
        self.chat_stats = ChatStats()
        self.data_stats.set_attr_changed_handler(self._update_stats_view)
        self.chat_stats.set_attr_changed_handler(self._update_stats_view)
        self.ui.webEngineView.page().renderProcessTerminated.connect(self._on_render_process_terminated)
        self.ui.webEngineView.renderProcessTerminated.connect(self._on_render_process_terminated)

        self.ui.view_info_btn.setVisible(False)
        self.ui.tabWidget.setCurrentIndex(0)

    def _on_render_process_terminated(termination_status, exit_code):
        print(f"!!! Процесс рендеринга упал !!!")
        print(f"Статус: {termination_status}")  # Показывает причину (например, нехватка памяти)
        print(f"Код выхода: {exit_code}")

    def _update_stats_view(self):

        def int2text(i: int) -> str:
            return f"{i:_}".replace("_", " ")

        dt_format = '%d.%m.%Y %H:%M:%S'
        stats = self.chat_stats
        lines = []

        # chat stats
        lines.append(f"## {lc.DETAILS_OF_SELECTED_CHAT}")

        if stats.inserted_datetime:
            lines.append(f"**{lc.INSERTED_AT}**: {stats.inserted_datetime.strftime(dt_format)}")
        if stats.updated_datetime:
            lines.append(f"**{lc.UPDATED_AT}**: {stats.updated_datetime.strftime(dt_format)}")
        if stats.total_msg_count:
            lines.append(f"**{lc.TOTAL_MSG_IN_CHAT}**: {int2text(stats.total_msg_count)}")
        if stats.chain_msg_count:
            lines.append(f"### {lc.MESSAGE_THREAD}")
            lines.append(f"**{lc.MSGS_IN_THREAD}**: {int2text(stats.chain_msg_count)}")
        if any([stats.msg_thread_token_count_requests >= 0,
                stats.msg_thread_word_count_requests >= 0,
                stats.msg_thread_char_count_requests >= 0]):

            lines.append(f"\n**{lc.REQUESTS}**")
            if stats.msg_thread_token_count_requests == 0:
                lines.append(f">**{lc.TOKENS}**: *{lc.CALCULATING}...*")
            elif stats.msg_thread_token_count_requests > 0:
                lines.append(f">**{lc.TOKENS}**: {int2text(stats.msg_thread_token_count_requests)}")
            if stats.msg_thread_word_count_requests == 0:
                lines.append(f">**{lc.WORDS}**: *{lc.CALCULATING}...*")
            elif stats.msg_thread_word_count_requests > 0:
                lines.append(f">**{lc.WORDS}**: {int2text(stats.msg_thread_word_count_requests)}")
            if stats.msg_thread_char_count_requests == 0:
                lines.append(f">**{lc.CHARACTERS}**: *{lc.CALCULATING}...*")
            elif stats.msg_thread_char_count_requests > 0:
                lines.append(f">**{lc.CHARACTERS}**: {int2text(stats.msg_thread_char_count_requests)}")

            lines.append(f"\n**{lc.RESPONSES}**")
            if stats.msg_thread_token_count_responses == 0:
                lines.append(f">**{lc.TOKENS}**: *{lc.CALCULATING}...*")
            elif stats.msg_thread_token_count_responses > 0:
                lines.append(f">**{lc.TOKENS}**: {int2text(stats.msg_thread_token_count_responses)}")
            if stats.msg_thread_word_count_responses == 0:
                lines.append(f">**{lc.WORDS}**: *{lc.CALCULATING}...*")
            elif stats.msg_thread_word_count_responses > 0:
                lines.append(f">**{lc.WORDS}**: {int2text(stats.msg_thread_word_count_responses)}")
            if stats.msg_thread_char_count_responses == 0:
                lines.append(f">**{lc.CHARACTERS}**: *{lc.CALCULATING}...*")
            elif stats.msg_thread_char_count_responses > 0:
                lines.append(f">**{lc.CHARACTERS}**: {int2text(stats.msg_thread_char_count_responses)}")

            lines.append(f"\n**{lc.TOTAL}**")

            total_tokens = stats.msg_thread_token_count_requests + stats.msg_thread_token_count_responses
            total_words = stats.msg_thread_word_count_requests + stats.msg_thread_word_count_responses
            total_chars = stats.msg_thread_char_count_requests + stats.msg_thread_char_count_responses

            if total_tokens == 0:
                lines.append(f">**{lc.TOKENS}**: *{lc.CALCULATING}...*")
            elif total_tokens > 0:
                lines.append(f">**{lc.TOKENS}**: {int2text(total_tokens)}")
            if total_words == 0:
                lines.append(f">**{lc.WORDS}**: *{lc.CALCULATING}...*")
            elif total_words > 0:
                lines.append(f">**{lc.WORDS}**: {int2text(total_words)}")
            if total_chars == 0:
                lines.append(f">**{lc.CHARACTERS}**: *{lc.CALCULATING}...*")
            elif total_chars > 0:
                lines.append(f">**{lc.CHARACTERS}**: {int2text(total_chars)}")

        #data stats
        lines.append(f"## {lc.DETAILS_OF_IMPORTED_DATA}")
        if self.data_stats.file_path:
            lines.append(f"**{lc.FILE}**: {self.data_stats.file_path}")
        if self.data_stats.chat_count:
            lines.append(f"**{lc.TOTAL_CHATS}**: {self.data_stats.chat_count:_}".replace("_", " "))

        self.ui.stats_richtext.setMarkdown(
            '\n\n'.join(lines)
        )

    def retranslate(self):
        self.ui.retranslateUi(self)
        self._update_stats_view()