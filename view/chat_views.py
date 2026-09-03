from abc import abstractmethod, ABC
from enum import  IntEnum
from typing import Iterable

from PyUB.Types import LangConstant
from . import langconsts as lc

from .datatypes import DeepSeekMessage


class ChatViewBase(ABC):
    class Type(IntEnum):
        PLAIN_TEXT = 0
        HTML4 = 1
        MARKDOWN = 2
        HTML5 = 3

    title: LangConstant | str = lc.UNTITLED
    type: Type = Type.PLAIN_TEXT

    @classmethod
    @abstractmethod
    def chat_to_text(cls, chat: Iterable[DeepSeekMessage]) -> str:
        pass

class ClearView(ChatViewBase):
    title = lc.PURE_TEXT

    @classmethod
    def message_to_text(cls, message: DeepSeekMessage) -> str:
        text = ""
        for fragment in message.fragments:
            if fragment.type not in [DeepSeekMessage.Fragment.Type.REQUEST, DeepSeekMessage.Fragment.Type.RESPONSE]:
                continue
            if fragment.content:
                text += fragment.content

        return text

    @classmethod
    def chat_to_text(cls, chat: Iterable[DeepSeekMessage]) -> str:
        lines = []
        for msg in chat:
            lines.append(cls.message_to_text(msg))
            lines.append("")

        return "\n".join(lines)

class SimpleView(ChatViewBase):
    title = lc.STANDARD

    @classmethod
    def message_to_text(cls, message: DeepSeekMessage) -> str:
        text = ""
        for fragment in message.fragments:
            match fragment.type:
                case DeepSeekMessage.Fragment.Type.REQUEST:
                    text += f"<{lc.REQUEST}>"
                case DeepSeekMessage.Fragment.Type.RESPONSE:
                    text += f"<{lc.RESPONSE}>"
                case _:
                    continue

            text += "\n\n"
            if fragment.content:
                text += fragment.content

        return text

    @classmethod
    def chat_to_text(cls, chat: Iterable[DeepSeekMessage]) -> str:
        lines = []
        for msg in chat:
            lines.append(cls.message_to_text(msg))
            lines.append("")

        return "\n".join(lines)


class SimpleView2(SimpleView):
    title = lc.STANDARD_NO_EMPTY_LINE

    @classmethod
    def message_to_text(cls, message: DeepSeekMessage) -> str:
        text = ""
        for fragment in message.fragments:
            match fragment.type:
                case DeepSeekMessage.Fragment.Type.REQUEST:
                    text += f"<{lc.REQUEST}>"
                case DeepSeekMessage.Fragment.Type.RESPONSE:
                    text += f"<{lc.RESPONSE}>"
                case _:
                    continue

            text += "\n"
            if fragment.content:
                text += fragment.content

        return text

class SimpleView3(SimpleView):
    title = lc.STANDARD_ADDITIONAL_TIME

    @classmethod
    def message_to_text(cls, message: DeepSeekMessage) -> str:
        text = ""
        dt_format = '%d.%m.%Y %H:%M:%S'
        for fragment in message.fragments:
            match fragment.type:
                case DeepSeekMessage.Fragment.Type.REQUEST:
                    text += f"<{lc.REQUEST} ({lc.INSERTED_AT}: {message.inserted_datetime.strftime(dt_format)})>"
                case DeepSeekMessage.Fragment.Type.RESPONSE:
                    text += f"<{lc.RESPONSE} ({lc.INSERTED_AT}: {message.inserted_datetime.strftime(dt_format)})>"
                case _:
                    continue

            text += "\n"
            if fragment.content:
                text += fragment.content

        return text

class SimpleHtmlView(ChatViewBase):
    title = lc.STANDARD_ADDITIONAL_TIME
    type = ChatViewBase.Type.HTML4

    @classmethod
    def message_to_text(cls, message: DeepSeekMessage) -> str:
        text = ""
        dt_format = '%d.%m.%Y %H:%M:%S'
        for fragment in message.fragments:
            match fragment.type:
                case DeepSeekMessage.Fragment.Type.REQUEST:
                    text += f"<p class ='meta'>{lc.REQUEST_FROM} {message.inserted_datetime.strftime(dt_format)}</p>"
                    text += f"<p>{fragment.content}</p>"
                case DeepSeekMessage.Fragment.Type.RESPONSE:
                    text += f"<p class ='meta'>{lc.RESPONSE_FROM} {message.inserted_datetime.strftime(dt_format)}</p>"
                    text += f"<p>{fragment.content}</p>"
                case _:
                    continue

        return text

    @classmethod
    def chat_to_text(cls, chat: Iterable[DeepSeekMessage]) -> str:
        result: list[str] = []
        result.append(
        """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8" />
            <style type="text/css">
                body { font-family: 'Segoe UI', sans-serif; font-size: 14pt; color: #000000; }
                p { margin: 0; padding: 0; white-space: pre-wrap; }
                .meta { font-style: italic; color: #828282; }
                .right { text-align: right; }
            </style>
        </head>
        <body>
        """
        )

        chat_length = len(chat)
        for n, msg in enumerate(chat):
            result.append(cls.message_to_text(msg))
            if n < chat_length - 1:
                result.append("<p><br/></p>")

        result.append("</body></html>")

        return "".join(result)


class SimpleMDView(ChatViewBase):
    title = lc.STANDARD
    type = ChatViewBase.Type.MARKDOWN

    @classmethod
    def message_to_text(cls, message: DeepSeekMessage) -> str:
        text = ""
        for fragment in message.fragments:
            match fragment.type:
                case DeepSeekMessage.Fragment.Type.REQUEST:
                    text += f"**{lc.REQUEST}**"
                case DeepSeekMessage.Fragment.Type.RESPONSE:
                    text += f"**{lc.RESPONSE}**"
                case _:
                    continue

            text += "\n\n"
            text += fragment.content
        return text

    @classmethod
    def chat_to_text(cls, chat: Iterable[DeepSeekMessage]) -> str:
        lines = []
        for msg in chat:
            lines.append(cls.message_to_text(msg))
            lines.append("")

        return "\n".join(lines)