
from PyUB.Types.Properties import PropertyContainer, BoolProperty
from .view import langconsts as lc

class Settings(PropertyContainer):
    calculate_tokens = BoolProperty(default_value=True, name=lc.CALCULATE_TOKENS_NAME, tooltip=lc.CALCULATE_TOKENS_TOOLTIP)
    calculate_words = BoolProperty(default_value=True, name=lc.CALCULATE_WORDS_NAME, tooltip=lc.CALCULATE_WORDS_TOOLTIP)
    calculate_chars = BoolProperty(default_value=True, name=lc.CALCULATE_CHARS_NAME, tooltip=lc.CALCULATE_CHARS_TOOLTIP)