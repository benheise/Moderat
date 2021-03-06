from PyQt4.QtGui import *
from PyQt4.QtCore import *
from text_ui import Ui_Dialog


class Text(QDialog, Ui_Dialog):
    def __init__(self, title, groupText, placeHolderText, okButton, cancelButton, value=''):
        QWidget.__init__(self)
        self.setupUi(self)
        self.anim = QPropertyAnimation(self, 'windowOpacity')
        self.anim.setDuration(500)
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.start()

        self.setWindowFlags(Qt.WindowSystemMenuHint | Qt.WindowTitleHint)

        self.okButton.clicked.connect(self.getText)
        self.cancelButton.clicked.connect(self.reject)

        self.setWindowTitle(title)
        self.textGroup.setTitle(groupText)
        self.textLine.setPlaceholderText(placeHolderText)
        self.textLine.setText(value)
        self.okButton.setText(okButton)
        self.cancelButton.setText(cancelButton)

    def getText(self):
        self.accept()
        return unicode(self.textLine.text())

    def closeEvent(self, QCloseEvent):
        pass


def get(title, groupText, placeHolderText='', okButton='Ok', cancelButton='Cancel', value=''):
    dialog = Text(title, groupText, placeHolderText, okButton, cancelButton, value)
    result = dialog.exec_()
    return result == QDialog.Accepted, dialog.getText()


def get_password(title, groupText, placeHolderText='', okButton='Ok', cancelButton='Cancel'):
    dialog = Text(title, groupText, placeHolderText, okButton, cancelButton)
    dialog.textLine.setEchoMode(QLineEdit.Password)
    result = dialog.exec_()
    return result == QDialog.Accepted, dialog.getText()