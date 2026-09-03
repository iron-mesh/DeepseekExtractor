import datetime
from dataclasses import dataclass, field
from enum import Enum
from typing import Callable

@dataclass
class BaseData:

    def __post_init__(self):
        self._is_handler_exec_blocked = False
        self._callback_func = None

    def set_attr_changed_handler(self, callback_func: Callable):
        if not isinstance(callback_func, Callable):
            raise TypeError("[callback_func] must be callable")
        self._callback_func = callback_func

    def exec_attr_changed_handler(self):
        if (hasattr(self, "_callback_func") and isinstance(self._callback_func, Callable)
                and not self._is_handler_exec_blocked):
            self._callback_func()

    def block_handler_exec(self, state:bool):
        self._is_handler_exec_blocked = state

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        self.exec_attr_changed_handler()


@dataclass
class DataStats(BaseData):
    file_path: str = None
    chat_count: int = 0

@dataclass
class ChatStats(BaseData):
    total_msg_count: int = 0
    chain_msg_count: int = 0
    inserted_datetime: datetime = None
    updated_datetime: datetime = None
    msg_thread_token_count_requests: int = -1
    msg_thread_token_count_responses: int = -1
    msg_thread_word_count_requests: int = -1
    msg_thread_word_count_responses: int = -1
    msg_thread_char_count_requests: int = -1
    msg_thread_char_count_responses: int = -1

@dataclass
class DeepSeekMessage:

    class Model(Enum):
        UNKNOWN = 0
        DEEPSEEK_CHAT = 1
        DEEPSEEK_REASONER = 2

    @dataclass
    class Fragment:

        class Type(Enum):
            REQUEST = 0
            RESPONSE = 1
            THINK = 2
            TOOL_SEARCH = 3

        @dataclass
        class SearchResultItem:
            url: str = None
            title: str = None

        type: Type = None
        content: str = None
        search_result: list[SearchResultItem] = field(default_factory=list)

    model: Model = Model.UNKNOWN
    inserted_datetime: datetime.datetime = field(default_factory=datetime.datetime.now)
    fragments: list[Fragment] = field(default_factory=list)