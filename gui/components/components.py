import os

import PySide6

from qt_core import *


class CustomPage(QWidget):
    def __init__(self, name, width, height, left_menu):
        super().__init__()
        self.setObjectName(name)
        self.setMinimumWidth(width)
        self.setMinimumHeight(height)
        self.left_menu = left_menu

    def get_page(self):
        return self

    def showEvent(self, event: PySide6.QtGui.QShowEvent) -> None:
        self.open_menu()

    def open_menu(self):
        # Checking the width
        menu_width = self.left_menu.width()
        #
        width_aux = 50

        if menu_width == 50:
            width_aux = 240
            self.animation = QPropertyAnimation(self.left_menu, b"minimumWidth")
            self.animation.setStartValue(menu_width)
            self.animation.setEndValue(width_aux)
            self.animation.setDuration(500)
            self.animation.setEasingCurve(QEasingCurve.InOutCirc)
            self.animation.start()


class CustomToolBox(QToolBox):
    def __init__(self,
                 object_name,
                 parent,
                 left_menu,
                 icon_size,
                 height=240):
        super().__init__()

        # Set default parameters
        self.setParent(parent)
        self.left_menu = left_menu
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)
        self.setObjectName(object_name)
        self.button_associated = None
        self.setStyleSheet(u"QToolBox{\n"
                           "    color: #c3ccdf;\n "
                           f"    icon-size: {icon_size}px;\n "
                           "}\n"
                           "QToolBox::tab {\n"
                           "    border-radius: 5px;	\n"
                           "	background-color: #44475a;\n"
                           "    font: 12pt \"Segoe UI\";\n"
                           "    color:rgb(255, 255, 255);\n"
                           "}\n"
                           "QToolBox::tab:hover {\n"
                           "	background-color: #4f5368;\n"
                           "}\n"
                           "QToolBox::tab:pressed {\n"
                           "	background-color: #282a36;\n"
                           "}")


class CustomToolWidget(QWidget):
    def __init__(self, button_top, page):
        self.button_top = button_top
        self.page = page
        pass


class CustomMenuButton(QPushButton):
    def __init__(
            self,
            text="",
            height=40,
            minimum_width=50,
            text_padding=55,
            text_color="#c3ccdf",
            icon_path="",
            icon_color="#c3ccdf",
            btn_color="#44475a",
            btn_hover="#4f5368",
            btn_pressed="#282a36",
            is_active=False
    ):
        super().__init__()

        # Set default parametros
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        # Custom parameters
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active

        # Set style
        self.set_style(
            text_padding=self.text_padding,
            text_color=self.text_color,
            btn_color=self.btn_color,
            btn_hover=self.btn_hover,
            btn_pressed=self.btn_pressed,
            is_active=self.is_active
        )

    def set_style(
            self,
            text_padding=55,
            text_color="#c3ccdf",
            btn_color="#44475a",
            btn_hover="#4f5368",
            btn_pressed="#282a36",
            is_active=False
    ):
        style = f"""
            QPushButton {{
                color: {text_color};
                background-color: {btn_color};
                padding-left: {text_padding}px;
                text-align: left;
                border: none;
            }}
            QPushButton:hover {{
                background-color: {btn_hover};
            }}
            QPushButton:pressed{{
                background-color: {btn_pressed};

            }}
            """

        active_style = f"""
                QPushButton {{
                    background-color: {btn_hover};
                    border-right: 5px solid #282a36;
                }}
                """
        if not is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)

    def paintEvent(self, event):
        # Return default style
        QPushButton.paintEvent(self, event)

        # Painter
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)

        rect = QRect(0, 0, self.minimum_width, self.height())
        self.draw_icon(qp, self.icon_path, rect, self.icon_color)
        # closing the painter
        qp.end()

    def draw_icon(self, qp, image, rect, color):
        # Format Path
        # root of app
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/icons"
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, image))

        # Drawing icon
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()

    def set_active(self, is_active_menu):
        self.set_style(
            text_padding=self.text_padding,
            text_color=self.text_color,
            btn_color=self.btn_color,
            btn_hover=self.btn_hover,
            btn_pressed=self.btn_pressed,
            is_active=is_active_menu
        )


class CustomButton(QPushButton):

    def __init__(self, icon, color):
        super().__init__()

        self.setMinimumSize(30, 30)
        self.set_cursor()
        self.setToolTip(icon)
        path = f"gui/images/icons/{icon}.svg"
        icono = self.aux_paint_icon(path)
        self.setIcon(icono)

        self.setStyleSheet(u"QPushButton{\n"
                           "border-radius: 15px;\n"
                           "color: black;\n"
                           "background-color: " + color + ";\n"
                                                          "}\n"
                                                          "\n"
                                                          "QPushButton:hover{\n"
                                                          "	border: 1px solid #c3ccdf;\n"
                                                          "}\n"
                           "QToolTip{color: #44475a;}")

    def set_cursor(self):
        pointer = QCursor(Qt.PointingHandCursor)
        self.setCursor(pointer)

    def aux_paint_icon(self, path):
        iconn = QIcon()
        iconn.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
        color = QColor(195, 204, 223)
        pixmap = QPixmap(path)
        painter = QPainter(pixmap)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.setBrush(color)
        painter.setPen(color)
        painter.drawRect(pixmap.rect())
        painter.end()
        icono = QIcon(pixmap)

        return icono


class CustomReturnButton(QPushButton):

    def __init__(self, ui, parent_frame, page_goal, name_button):
        super().__init__()

        self.ui = ui
        self.page_goal = page_goal
        self.set_cursor()
        self.setParent(parent_frame)
        self.setObjectName(name_button)
        self.setMinimumSize(QSize(60, 35))
        self.setMaximumSize(QSize(60, 35))
        self.setText("Return")
        self.setStyleSheet(u"QPushButton{\n"
                           "	background-color :rgb(67,133,200);\n"
                           "	color: rgb(255, 255, 255);\n"
                           "	font: 11pt \"Segoe UI\";\n"
                           "	border-radius: 5px;\n"
                           "	border: 2px solid rgb(67,133,200);\n"
                           "	padding: 5px;\n"
                           "	padding-left: 10px;\n"
                           "}\n"
                           "\n"
                           "QPushButton:hover{\n"
                           "	background-color: rgb(85,170,225);\n"
                           "}\n"
                           "\n"
                           "QPushButton:pressed{\n"
                           "	background-color: rgb(79, 198, 219);\n"
                           "}")

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
        self.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.setText(text)


class CustomLabelError(QLabel):
    def __init__(self, parent, name, text):
        super().__init__()
        self.setParent(parent)
        self.setObjectName(name)
        self.setMinimumSize(QSize(150, 25))
        self.setMaximumSize(QSize(150, 25))
        self.setStyleSheet(u"font: 11pt \"Segoe UI\";\n"
                           "color: red;")
        self.setText(text)


class CustomLineEdit(QLineEdit):
    def __init__(self, parent, lineEdit_name, label_error, line_edit_type, line_edit_width=300):
        super().__init__()
        self.parent = parent
        self.lineEdit_name = lineEdit_name
        self.label_error = label_error
        self.line_edit_type = line_edit_type

        self.setParent(parent)
        self.setObjectName(lineEdit_name + "_line_edit")
        self.setMinimumSize(QSize(line_edit_width, 30))
        self.setMaximumSize(QSize(line_edit_width, 30))
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
        self.checking_text()
        # required to remove cursor on focusOut
        self.clearFocus()
        self.cursorForward(True, 1)

    def checking_text(self):
        if self.check_empty(self.text()):
            text = "Fill the empty field"
            self.label_error.setText(text)
            return True
        elif not self.check_type(self.text()):
            text = "Wrong data type"
            self.label_error.setText(text)
            return True
        else:
            text = ""
            self.label_error.setText(text)
            return False

    @staticmethod
    def check_empty(text):
        if text == "":
            # Create a custom label error
            return True
        return False

    def check_type(self, text):
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
