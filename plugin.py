from typing import Optional

from PySide6.QtWidgets import QWidget

from PyUB.Types import Plugin
from PyUB.Types.Properties import PropertyContainer


class MyPlugin(Plugin):

    @classmethod
    def gui(cls) -> QWidget:
        """
        Returns widget of the plugin GUI

        Returns:
            QWidget: widget of the plugin GUI

        Raises:
            NotImplementedError: not implemented method
        """
        from .presenter import manager
        return manager.main_widget

    @classmethod
    def settings(cls) -> Optional[PropertyContainer]:
        """
        Returns reference to the plugin settings

        Returns PropertyContainer class with properties of plugin settings, if it is not specified returns None

        Returns:
            PropertyContainer: reference to the plugin settings
            None: reference to the plugin settings is not defined
        """
        from .settings import Settings
        return Settings