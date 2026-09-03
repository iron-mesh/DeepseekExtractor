import re
from dataclasses import dataclass
from typing import Iterable
from deepseek_tokenizer import ds_token

from PySide6.QtCore import QThread, Slot
from ..view.main_widget import MainWidget
from ..view.datatypes import DeepSeekMessage

__all__ = ['calculate_details']

_main_widget = MainWidget.instance() if MainWidget.instance() is not None else MainWidget()

@dataclass
class CalculationResult:
    msg_thread_token_count_requests: int = -1
    msg_thread_token_count_responses: int = -1
    msg_thread_word_count_requests: int = -1
    msg_thread_word_count_responses: int = -1
    msg_thread_char_count_requests: int = -1
    msg_thread_char_count_responses: int = -1

class _WorkerThread(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._msg_thread = None
        self._result = None
        self._is_stopped = False
        self._calc_tokens = True
        self._calc_words = True
        self._calc_chars = True

        self.started.connect(self._on_started)
        self.finished.connect(self._on_finished)

    @Slot()
    def _on_started(self):
        global _main_widget
        _main_widget.chat_stats.block_handler_exec(True)
        if self._calc_tokens:
            _main_widget.chat_stats.msg_thread_token_count_requests = 0
            _main_widget.chat_stats.msg_thread_token_count_responses = 0
        if self._calc_words:
            _main_widget.chat_stats.msg_thread_word_count_requests = 0
            _main_widget.chat_stats.msg_thread_word_count_responses = 0
        if self._calc_chars:
            _main_widget.chat_stats.msg_thread_char_count_requests = 0
            _main_widget.chat_stats.msg_thread_char_count_responses = 0
        _main_widget.chat_stats.block_handler_exec(False)
        _main_widget.chat_stats.exec_attr_changed_handler()

    @Slot()
    def _on_finished(self):
        global _main_widget
        _main_widget.chat_stats.block_handler_exec(True)
        _main_widget.chat_stats.msg_thread_token_count_requests = self._result.msg_thread_token_count_requests
        _main_widget.chat_stats.msg_thread_token_count_responses = self._result.msg_thread_token_count_responses
        _main_widget.chat_stats.msg_thread_word_count_requests = self._result.msg_thread_word_count_requests
        _main_widget.chat_stats.msg_thread_word_count_responses = self._result.msg_thread_word_count_responses
        _main_widget.chat_stats.msg_thread_char_count_requests = self._result.msg_thread_char_count_requests
        _main_widget.chat_stats.msg_thread_char_count_responses = self._result.msg_thread_char_count_responses
        _main_widget.chat_stats.block_handler_exec(False)
        _main_widget.chat_stats.exec_attr_changed_handler()

    def set_calc_mode(self,
                      calc_tokens: bool,
                      calc_words: bool,
                      calc_chars: bool):
        self._calc_tokens = calc_tokens
        self._calc_words = calc_words
        self._calc_chars = calc_chars

    def set_message_thread(self, msg_thread: Iterable[DeepSeekMessage]):
        self._msg_thread = msg_thread

    def stop(self):
        self._is_stopped = True

    def run(self):
        self._result = CalculationResult()
        if not any([self._calc_tokens, self._calc_words, self._calc_chars]):
            return

        def word_count(text: str) -> int:
            text = re.sub(r'[^\w\s]', '', text.lower())
            return len([word for word in text.split() if word])

        self._is_stopped = False
        for msg in self._msg_thread:
            if self._is_stopped:
                break
            for fragment in msg.fragments:
                if not (fragment.type == DeepSeekMessage.Fragment.Type.REQUEST or
                        fragment.type == DeepSeekMessage.Fragment.Type.RESPONSE):
                    continue

                if self._calc_tokens:
                    if fragment.type == DeepSeekMessage.Fragment.Type.REQUEST:
                        self._result.msg_thread_token_count_requests += len(ds_token.encode(fragment.content))
                    elif fragment.type == DeepSeekMessage.Fragment.Type.RESPONSE:
                        self._result.msg_thread_token_count_responses += len(ds_token.encode(fragment.content))

                if self._calc_words:
                    if fragment.type == DeepSeekMessage.Fragment.Type.REQUEST:
                        self._result.msg_thread_word_count_requests += word_count(fragment.content)
                    elif fragment.type == DeepSeekMessage.Fragment.Type.RESPONSE:
                        self._result.msg_thread_word_count_responses += word_count(fragment.content)

                if self._calc_chars:
                    if fragment.type == DeepSeekMessage.Fragment.Type.REQUEST:
                        self._result.msg_thread_char_count_requests += len(fragment.content)
                    elif fragment.type == DeepSeekMessage.Fragment.Type.RESPONSE:
                        self._result.msg_thread_char_count_responses += len(fragment.content)


_worker = _WorkerThread()

def calculate_details(msg_thread: Iterable[DeepSeekMessage],
                      calc_tokens: bool = True,
                      calc_words: bool = True,
                      calc_chars: bool = True):
    global _worker, _main_widget
    if _worker.isRunning():
        _worker.stop()
        _worker.wait()

    _worker.set_calc_mode(calc_tokens, calc_words, calc_chars)
    _worker.set_message_thread(msg_thread)
    _worker.start()
