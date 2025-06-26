from gui.components.components import *


class RoversPageView(QWidget):
    def __init__(self, parent=None, ui=None):
        super().__init__(parent)
        self.ui = ui

        # check if create page_1 is created
        to_create = self.ui.page_rovers.findChild(QFrame, "central_frame_rovers")
        if to_create is None:
            self.initialize_gui()

    def initialize_gui(self):
        # Central frame
        self.ui.central_frame_rovers = QFrame(self.ui.page_rovers)
        self.ui.central_frame_rovers.setObjectName(u"central_frame_rovers")
        self.ui.central_frame_rovers.setStyleSheet(u"background-color: #282a36")
        self.ui.central_frame_rovers.setFrameShape(QFrame.StyledPanel)
        self.ui.central_frame_rovers.setFrameShadow(QFrame.Raised)
        self.ui.central_frame_rovers_layout = QVBoxLayout(self.ui.central_frame_rovers)
        self.ui.central_frame_rovers_layout.setSpacing(0)
        self.ui.central_frame_rovers_layout.setObjectName(u"central_frame_rovers_layout")
        self.ui.central_frame_rovers_layout.setContentsMargins(0, 0, 0, 0)

        self.ui.background_frame_rovers = QFrame(self.ui.central_frame_rovers)
        self.ui.background_frame_rovers.setObjectName(u"background_frame_rovers")
        self.ui.background_frame_rovers.setStyleSheet(u"")
        self.ui.background_frame_rovers.setFrameShape(QFrame.StyledPanel)
        self.ui.background_frame_rovers.setFrameShadow(QFrame.Raised)
        self.ui.background_layout_rovers = QVBoxLayout(self.ui.background_frame_rovers)
        self.ui.background_layout_rovers.setObjectName(u"background_layout_rovers")

        self.ui.frame_lbl_rovers = QFrame(self.ui.background_frame_rovers)
        self.ui.frame_lbl_rovers.setObjectName(u"frame_lbl_rovers")
        self.ui.frame_lbl_rovers.setMinimumSize(QSize(0, 40))
        self.ui.frame_lbl_rovers.setMaximumSize(QSize(16777215, 40))
        self.ui.frame_lbl_rovers.setFrameShape(QFrame.StyledPanel)
        self.ui.frame_lbl_rovers.setFrameShadow(QFrame.Raised)

        self.ui.layout_lbl_rovers = QVBoxLayout(self.ui.frame_lbl_rovers)
        self.ui.layout_lbl_rovers.setObjectName(u"layout_lbl_rovers")
        self.ui.label_rover = QLabel(self.ui.frame_lbl_rovers)
        self.ui.label_rover.setObjectName(u"label_rover")
        self.ui.label_rover.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
                                          "color:rgb(255, 255, 255);")

        self.ui.layout_lbl_rovers.addWidget(self.ui.label_rover)
        self.ui.background_layout_rovers.addWidget(self.ui.frame_lbl_rovers)

        # Adding explanatory text
        self.ui.frame_lbl_rovers_exp = QFrame(self.ui.background_frame_rovers)
        self.ui.frame_lbl_rovers_exp.setObjectName(u"frame_lbl_rovers")
        self.ui.frame_lbl_rovers_exp.setMinimumSize(QSize(0, 40))
        self.ui.frame_lbl_rovers_exp.setMaximumSize(QSize(16777215, 40))
        self.ui.frame_lbl_rovers_exp.setFrameShape(QFrame.StyledPanel)
        self.ui.frame_lbl_rovers_exp.setFrameShadow(QFrame.Raised)

        self.ui.layout_lbl_rovers_exp = QVBoxLayout(self.ui.frame_lbl_rovers_exp)
        self.ui.layout_lbl_rovers_exp.setObjectName(u"layout_lbl_rovers_exp")
        self.ui.label_rover_exp = QLabel(self.ui.frame_lbl_rovers_exp)
        self.ui.label_rover_exp.setObjectName(u"label_rover_exp")
        self.ui.label_rover_exp.setStyleSheet(u"font: 12pt \"Segoe UI\";\n "
                                              u"color:rgb(255, 255, 255);")
        self.ui.layout_lbl_rovers_exp.addWidget(self.ui.label_rover_exp)
        self.ui.background_layout_rovers.addWidget(self.ui.frame_lbl_rovers_exp)

        self.ui.frame_actions_rover = QFrame(self.ui.background_frame_rovers)
        self.ui.frame_actions_rover.setObjectName(u"frame_actions_rover")
        self.ui.frame_actions_rover.setMinimumSize(QSize(0, 50))
        self.ui.frame_actions_rover.setMaximumSize(QSize(16777215, 50))
        self.ui.frame_actions_rover.setFrameShape(QFrame.StyledPanel)
        self.ui.frame_actions_rover.setFrameShadow(QFrame.Raised)

        self.ui.horizontalLayout_actions_rover = QHBoxLayout(self.ui.frame_actions_rover)
        self.ui.horizontalLayout_actions_rover.setObjectName(u"horizontalLayout_actions_rover")
        self.ui.horizontalLayout_actions_rover.setContentsMargins(3, 3, -1, 3)

        self.ui.search_lineEdit = QLineEdit(self.ui.frame_actions_rover)
        self.ui.search_lineEdit.setObjectName(u"search_lineEdit")
        self.ui.search_lineEdit.setMinimumSize(QSize(400, 45))
        self.ui.search_lineEdit.setMaximumSize(QSize(600, 45))
        self.ui.search_lineEdit.setStyleSheet(u"QLineEdit{\n"
                                              "	background-color:rgb(68,71,90);\n"
                                              "	padding: 8px;\n"
                                              "	color: rgb(255, 255, 255);\n"
                                              "	border-radius: 10px;\n"
                                              "}\n"
                                              "\n"
                                              "QLineEdit:hover{\n"
                                              "	border: 1px solid #c3ccdf;\n"
                                              "}\n"
                                              "")

        self.ui.horizontalLayout_actions_rover.addWidget(self.ui.search_lineEdit)

        self.ui.search_rover = QPushButton(self.ui.frame_actions_rover)
        self.ui.search_rover.setObjectName(u"search_rover")
        self.ui.search_rover.setMinimumSize(QSize(62, 45))
        self.ui.search_rover.setMaximumSize(QSize(62, 45))
        self.ui.search_rover.setStyleSheet(u"QPushButton{\n"
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

        self.ui.horizontalLayout_actions_rover.addWidget(self.ui.search_rover)

        self.ui.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ui.horizontalLayout_actions_rover.addItem(self.ui.horizontalSpacer_2)

        self.ui.create_rover_btn = QPushButton(self.ui.frame_actions_rover)
        self.ui.create_rover_btn.setObjectName(u"create_rover_btn")
        self.ui.create_rover_btn.setMinimumSize(QSize(60, 45))
        self.ui.create_rover_btn.setMaximumSize(QSize(60, 45))
        self.ui.create_rover_btn.setStyleSheet(u"QPushButton{\n"
                                               "	background-color :rgb(67,133,200);\n"
                                               "	color: rgb(255, 255, 255);\n"
                                               "	font: 11pt \"Segoe UI\";\n"
                                               "	border-radius: 5px;\n"
                                               "	border: 2px solid rgb(67,133,200);\n"
                                               "	padding: 5px;\n"
                                               "	padding-left: 10px;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "	background-color: rgb(85,170,225);\n"
                                               "}\n"
                                               "QPushButton:pressed{\n"
                                               "	background-color: rgb(79, 198, 219);\n"
                                               "}")
        self.ui.create_ex_rover_btn = QPushButton(self.ui.frame_actions_rover)
        self.ui.create_ex_rover_btn.setObjectName(u"create_ex_rover_btn")
        self.ui.create_ex_rover_btn.setMinimumSize(QSize(90, 45))
        self.ui.create_ex_rover_btn.setMaximumSize(QSize(90, 45))
        self.ui.create_ex_rover_btn.setStyleSheet(u"QPushButton{\n"
                                               "	background-color :rgb(67,133,200);\n"
                                               "	color: rgb(255, 255, 255);\n"
                                               "	font: 11pt \"Segoe UI\";\n"
                                               "	border-radius: 5px;\n"
                                               "	border: 2px solid rgb(67,133,200);\n"
                                               "	padding: 5px;\n"
                                               "	padding-left: 10px;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "	background-color: rgb(85,170,225);\n"
                                               "}\n"
                                               "QPushButton:pressed{\n"
                                               "	background-color: rgb(79, 198, 219);\n"
                                               "}")

        self.ui.horizontalLayout_actions_rover.addWidget(self.ui.create_rover_btn)
        self.ui.horizontalLayout_actions_rover.addWidget(self.ui.create_ex_rover_btn)

        self.ui.background_layout_rovers.addWidget(self.ui.frame_actions_rover)

        self.ui.frame_table_rovers = QFrame(self.ui.background_frame_rovers)
        self.ui.frame_table_rovers.setObjectName(u"frame_table_rovers")
        self.ui.frame_table_rovers.setStyleSheet(u"background-color: #282a36")
        self.ui.frame_table_rovers.setFrameShape(QFrame.StyledPanel)
        self.ui.frame_table_rovers.setFrameShadow(QFrame.Raised)
        self.ui.layout_table_rovers = QHBoxLayout(self.ui.frame_table_rovers)
        self.ui.layout_table_rovers.setSpacing(0)
        self.ui.layout_table_rovers.setObjectName(u"layout_table_rovers")
        self.ui.layout_table_rovers.setContentsMargins(0, 0, 0, 0)
        self.ui.table_rovers = QTableWidget(self.ui.frame_table_rovers)
        self.ui.table_rovers.setObjectName(u"table_rovers")
        self.ui.table_rovers.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ui.table_rovers.setLayoutDirection(Qt.LeftToRight)
        self.ui.table_rovers.setStyleSheet(u"\n"
                                           "QTableWidget{\n"
                                           "background-color: transparent;\n"
                                           "border : 1px  #282a36;\n"
                                           "alternate-background-color:#525252;\n"
                                           "gridline-color:rgb(44, 49, 58);\n"
                                           "}\n"
                                           "\n"
                                           "QTableWidget::item{\n"
                                           "border-color: rgb(44, 49, 60);\n"
                                           "padding-left: 5px;\n"
                                           "padding-right: 5px;\n"
                                           "gridline-color: rgb(44, 49, 60);\n"
                                           "}\n"
                                           "QHeaderView::section{\n"
                                           "background-color: rgb(33, 37, 43);\n"
                                           "max-width: 30px;\n"
                                           "border: 1px solid rgb(44, 49, 58);\n"
                                           "border-style: none;\n"
                                           "border-bottom: 1px solid rgb(44, 49, 60);\n"
                                           "border-right: 1px solid rgb(44, 49, 60);\n"
                                           "}\n"
                                           "QTableCornerButton::section{\n"
                                           "background-color:  #232326;\n"
                                           "}\n")
        self.ui.table_rovers.setShowGrid(False)
        self.ui.table_rovers.setWordWrap(False)
        self.ui.table_rovers.setCornerButtonEnabled(False)
        self.ui.layout_table_rovers.addWidget(self.ui.table_rovers)
        self.ui.background_layout_rovers.addWidget(self.ui.frame_table_rovers)
        self.ui.central_frame_rovers_layout.addWidget(self.ui.background_frame_rovers)
        self.ui.layout_page_rovers.addWidget(self.ui.central_frame_rovers)
        self.retranslateUi()

    def retranslateUi(self):
        self.ui.label_rover.setText(QCoreApplication.translate("app_pages", u"Rover", None))
        self.ui.label_rover_exp.setText(QCoreApplication.translate("app_pages", u"These are the existent rovers", None))
        self.ui.search_lineEdit.setPlaceholderText(QCoreApplication.translate("app_pages", u"Search by name", None))
        self.ui.search_rover.setText(QCoreApplication.translate("app_pages", u"Search", None))
        self.ui.create_rover_btn.setText(QCoreApplication.translate("app_pages", u"Create", None))
        self.ui.create_ex_rover_btn.setText(QCoreApplication.translate("app_pages", u"Examples", None))

    # retranslateUi
