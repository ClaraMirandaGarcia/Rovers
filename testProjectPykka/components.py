from qt_core import *


class Button(QPushButton):

    def __init__(self, icon, color):
        super().__init__()

        self.setMinimumSize(30, 30)
        self.set_cursor()
        self.setIcon(QIcon(f"gui/images/icons/{icon}.png"))
        self.setStyleSheet(f"border-radius: 15px; background-color: {color};")

    def set_cursor(self):
        pointer = QCursor(Qt.PointingHandCursor)
        self.setCursor(pointer)
