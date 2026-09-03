from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QDialog, QAbstractSpinBox

from .forms.ui_select_msg_dialog import Ui_Dialog


class SelectMsgDialog(QDialog):
    curr_msg_changed = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

        self.ui.first_msg_btn.clicked.connect(self._on_btn_clicked)
        self.ui.prev_msg_btn.clicked.connect(self._on_btn_clicked)
        self.ui.next_msg_btn.clicked.connect(self._on_btn_clicked)
        self.ui.last_msg_btn.clicked.connect(self._on_btn_clicked)

        self.ui.curr_msg_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.ui.curr_msg_spinBox.valueChanged.connect(self._on_value_changed)
        self.ui.curr_msg_spinBox.valueChanged.connect(self.curr_msg_changed)

    @Slot()
    def _on_btn_clicked(self):
        sender = self.sender()
        match sender:
            case self.ui.first_msg_btn:
                self.ui.curr_msg_spinBox.setValue(self.ui.curr_msg_spinBox.minimum())
            case self.ui.prev_msg_btn:
                self.ui.curr_msg_spinBox.setValue(self.ui.curr_msg_spinBox.value() - 1)
            case self.ui.next_msg_btn:
                self.ui.curr_msg_spinBox.setValue(self.ui.curr_msg_spinBox.value() + 1)
            case self.ui.last_msg_btn:
                self.ui.curr_msg_spinBox.setValue(self.ui.curr_msg_spinBox.maximum())

    @Slot()
    def _on_value_changed(self, value: int):
        if value == self.ui.curr_msg_spinBox.minimum():
            self.ui.first_msg_btn.setEnabled(False)
            self.ui.prev_msg_btn.setEnabled(False)
        elif not self.ui.first_msg_btn.isEnabled():
            self.ui.first_msg_btn.setEnabled(True)
            self.ui.prev_msg_btn.setEnabled(True)

        if value == self.ui.curr_msg_spinBox.maximum():
            self.ui.last_msg_btn.setEnabled(False)
            self.ui.next_msg_btn.setEnabled(False)
        elif not self.ui.next_msg_btn.isEnabled():
            self.ui.last_msg_btn.setEnabled(True)
            self.ui.next_msg_btn.setEnabled(True)

    def set_minimum(self, val: int):
        self.ui.curr_msg_spinBox.setMinimum(val)

    def set_maximum(self, val: int):
        self.ui.curr_msg_spinBox.setMaximum(val)
        self.ui.page_count_label.setText(f"/{str(val)}")

    def get_minimum(self) -> int:
        return self.ui.curr_msg_spinBox.minimum()

    def get_maximum(self) -> int:
        return self.ui.curr_msg_spinBox.maximum()

    def get_value(self) -> int:
        return self.ui.curr_msg_spinBox.value()

    def set_value(self, val: int):
        self.ui.curr_msg_spinBox.setValue(val)

    def set_plain_text(self, val: str):
        self.ui.plainTextEdit.setPlainText(val)

    def get_plain_text(self) -> str:
        return self.ui.plainTextEdit.toPlainText()


