from typing import Iterable
from DeepSeekExtractor.view.datatypes import DeepSeekMessage
from DeepSeekExtractor.view.chat_views import ChatViewBase
from DeepSeekExtractor.view import langconsts as lc


class MyView(ChatViewBase):
    title = "My View"
    type = ChatViewBase.Type.HTML5

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
                case DeepSeekMessage.Fragment.Type.THINK:
                    text += f"<details>\
                     <summary>{lc.THINKING}</summary>\
                     <p>{fragment.content}</p>\
                     </details>"
                case DeepSeekMessage.Fragment.Type.TOOL_SEARCH:
                    if fragment.search_result:
                        text += f"<details>\
                                 <summary>{lc.SEARCH}</summary>\
                                <ul>"
                        for i in  fragment.search_result:
                            text += f"<li><a href=\"{i.url}\">{i.title}</a></li>"
                        text += "</ul></details>"
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
                </style>
            </head>
            <body>
            """
        )

        chat_length = len(chat)
        for n, msg in enumerate(chat):
            result.append(cls.message_to_text(msg))
            if n < chat_length - 1:
                result.append("<hr>")

        result.append("</body></html>")

        return "".join(result)