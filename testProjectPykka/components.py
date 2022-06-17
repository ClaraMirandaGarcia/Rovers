from qt_core import *
from gui.pages import ui_pages


class Button(QPushButton):

    def __init__(self, icon, color):
        super().__init__()

        self.setMinimumSize(30, 30)
        #self.set_cursor()
        self.setIcon(QIcon(f"gui/images/icons/{icon}.png"))
        self.setStyleSheet(f"border-radius: 15px; background-color: {color};")

    def set_cursor(self):
        pointer = QCursor(Qt.PointingHandCursor)
        self.setCursor(pointer)


class CustomDialog(QDialog):
    def __init__(self, title, message):
        super().__init__()

        self.setWindowTitle(title)
        self.setStyleSheet(f"font: 700 \"Segoe UI\"; background-color: #282a36;" \
                           "color:rgb(255, 255, 255);")
        self.buttonOk = QDialogButtonBox.Ok
        # self.buttonOk.setStyleSheet(f"border-radius: 15px; background-color: #282a36;")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel(message)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class CustomGridLayout(QGridLayout):
    def __init__(self, parent, lineEdit_name, label, label_error):
        super().__init__()
        self.setParent(parent)
        self.setObjectName(lineEdit_name + "_layout")

        self.label = label
        self.label_eror = label_error
        # Add lineEdit
        widget_ex = CustomLineEdit(parent, lineEdit_name)

        self.addWidget(label, 0, 0)
        # self.addWidget(widget_ex, 0, 1)
        # self.addWidget(label_error, 0, 2)


class CustomLabel(QLabel):
    def __init__(self, parent, name, text, width_label: 150):
        super().__init__()
        self.setParent(parent)
        self.setObjectName(name)
        self.setMinimumSize(QSize(width_label, 25))
        self.setMaximumSize(QSize(width_label, 25))
        self.setStyleSheet(u"font: 11pt \"Segoe UI\";")
        self.setText(text)


class CustomLabelError(QLabel):
    def __init__(self, parent, name, text):
        super().__init__()
        self.setParent(parent)
        self.setObjectName(name)
        self.setMinimumSize(QSize(150, 25))
        self.setMaximumSize(QSize(150, 25))
        self.setStyleSheet(u"font: 11pt \"Segoe UI\";")
        self.setText(text)


class CustomLineEdit(QLineEdit):
    def __init__(self, parent, lineEdit_name, label_error, line_edit_type):
        super().__init__()
        self.parent = parent
        self.lineEdit_name = lineEdit_name
        self.label_error = label_error
        self.line_edit_type = line_edit_type

        self.setParent(parent)
        self.setObjectName(lineEdit_name + "_line_edit")
        self.setMinimumSize(QSize(300, 30))
        self.setMaximumSize(QSize(300, 30))
        self.style_sheet = u"QLineEdit{\n" \
                           "	background-color: rgb(27, 29, 35);\n" \
                           "	border-radius: 5px;\n" \
                           "	border: 2px solid rgb(33, 37, 43);\n" \
                           "	padding: 5px;\n" \
                           "	padding-left: 10px;\n" \
                           "}\n" \
                           "\n" \
                           "QLineEdit:hover{\n" \
                           "	border: 1px solid #c3ccdf;\n" \
                           "}"

        self.setStyleSheet(self.style_sheet)

    def focusOutEvent(self, e):

        self.checkingText()
        # required to remove cursor on focusOut
        self.clearFocus()
        self.cursorForward(True, 1)

    def checkingText(self):
        # self.checkIfEmpty
        if self.checkEmpty(self.text()):
            text = "Fill the empty field"
            self.label_error.setText(text)
            return True
        # self.checkIfType
        elif not self.checkType(self.text()):
            text = "Wrong data type"
            self.label_error.setText(text)
            return True
        else:
            text = ""
        self.label_error.setText(text)
        return False

    @staticmethod
    def checkEmpty(text):
        if text == "":
            # Create a custom label error
            return True
        return False

    def checkType(self, text):
        if self.line_edit_type == "float":
            try:
                value = float(text)
                return True
            except ValueError:
                return False
        if self.line_edit_type == "int":
            try:
                value = int(text)
                return True
            except ValueError:
                return False
        return True
