from typing import Iterable

from PySide6.QtCore import Slot, Signal, Qt, QSortFilterProxyModel
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QDialog, QAbstractSpinBox
from . import langconsts as lc
from .forms.ui_select_chats_dialog import Ui_Dialog


class SelectChatsDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.show_checked_only_btn.setText(lc.SHOW_CHECKED_ONLY())
        self.ui.filter_lineEdit.setPlaceholderText(lc.SEARCH())
        self.ui.select_all_btn.setText(lc.SELECT_ALL())
        self.ui.deselect_all_btn.setText(lc.DESELECT_ALL())


        self._model = QStandardItemModel()
        self._proxy_model = QSortFilterProxyModel()
        self._proxy_model.setSourceModel(self._model)
        self._proxy_model.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.ui.listView.setModel(self._proxy_model)

        self.ui.filter_lineEdit.textChanged.connect(self._proxy_model.setFilterFixedString)
        self.ui.show_checked_only_btn.clicked.connect(self._on_show_checked_only)
        self.ui.select_all_btn.clicked.connect(lambda: self._set_state_all(True))
        self.ui.deselect_all_btn.clicked.connect(lambda: self._set_state_all(False))

    def set_items(self, items: Iterable[str])->None:
        self._model.clear()

        for item in items:
            element = QStandardItem(item)
            element.setCheckable(True)
            element.setCheckState(Qt.CheckState.Unchecked)
            self._model.appendRow(element)


    def selected_indexes(self)->list[int]:
        result = []
        for i in range(self._model.rowCount()):
            if self._model.item(i).checkState() == Qt.CheckState.Checked:
                result.append(i)
        return result

    def _on_show_checked_only(self):
        self.ui.filter_lineEdit.setReadOnly(self.ui.show_checked_only_btn.isChecked())

        if self.ui.show_checked_only_btn.isChecked():
            self._proxy_model.setFilterRole(Qt.ItemDataRole.CheckStateRole)
            self._proxy_model.setFilterFixedString(str(Qt.CheckState.Checked.value))
        else:
            self._proxy_model.setFilterRole(Qt.ItemDataRole.DisplayRole)
            self._proxy_model.setFilterFixedString(self.ui.filter_lineEdit.text())

    def _set_state_all(self, state: bool)->None:
        new_state = Qt.CheckState.Checked if state else Qt.CheckState.Unchecked
        for i in range(self._model.rowCount()):
            self._model.item(i).setCheckState(new_state)
