import os

from PySide6.QtCore import QSettings
from ..view.main_widget import MainWidget
from PyUB.Types import Helper


if  MainWidget.instance():
    _main_widget = MainWidget.instance()
else:
    _main_widget = MainWidget()

_helper = Helper()

_path = os.path.join(_helper.plugin_localstorage_dir_abspath(), "config")
settings = QSettings(str(_path), QSettings.Format.IniFormat)

def _save_settings():
    settings.setValue("splitter_sizes", _main_widget.ui.splitter.sizes())
    settings.setValue("msgs_per_fragment", _main_widget.ui.fragment_length_spinBox.value())
    settings.sync()

def _apply_settings():
    _main_widget.ui.splitter.setSizes(
        [int(i) for i in settings.value("splitter_sizes")]
    )
    _main_widget.ui.fragment_length_spinBox.setValue(settings.value("msgs_per_fragment", type=int))

_helper.app_closing.connect(_save_settings)
_helper.plugin_deactivating.connect(_save_settings)

if not settings.childKeys():
    _save_settings()
else:
    _apply_settings()