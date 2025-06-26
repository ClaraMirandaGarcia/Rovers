from gui.components.components import *


class SimulationsPageView(QWidget):
    def __init__(self, parent=None, ui=None):
        super().__init__(parent)
        self.ui = ui

        # check if create page_1 is created
        to_create = self.ui.page_simulations.findChild(QFrame, "central_frame_simulations")
        if to_create is None:
            self.initialize_gui()

    def initialize_gui(self):
        # Central frame
        self.ui.central_frame_simulations = QFrame(self.ui.page_simulations)
        self.ui.central_frame_simulations.setObjectName(u"central_frame_simulations")
        self.ui.central_frame_simulations.setStyleSheet(u"background-color: #282a36")
        self.ui.central_frame_simulations.setFrameShape(QFrame.StyledPanel)
        self.ui.central_frame_simulations.setFrameShadow(QFrame.Raised)

        self.ui.central_frame_simulations_layout = QVBoxLayout(self.ui.central_frame_simulations)
        self.ui.central_frame_simulations_layout.setSpacing(0)
        self.ui.central_frame_simulations_layout.setObjectName(u"central_frame_simulations_layout")
        self.ui.central_frame_simulations_layout.setContentsMargins(0, 0, 0, 0)

        self.ui.background_frame_simulations = QFrame(self.ui.central_frame_simulations)
        self.ui.background_frame_simulations.setObjectName(u"background_frame_simulations")
        self.ui.background_frame_simulations.setStyleSheet(u"")
        self.ui.background_frame_simulations.setFrameShape(QFrame.StyledPanel)
        self.ui.background_frame_simulations.setFrameShadow(QFrame.Raised)
        self.ui.background_layout_simulations = QVBoxLayout(self.ui.background_frame_simulations)
        self.ui.background_layout_simulations.setObjectName(u"background_layout_simulations")

        self.ui.frame_lbl_simulations = QFrame(self.ui.background_frame_simulations)
        self.ui.frame_lbl_simulations.setObjectName(u"frame_lbl_simulations")
        self.ui.frame_lbl_simulations.setMinimumSize(QSize(0, 40))
        self.ui.frame_lbl_simulations.setMaximumSize(QSize(16777215, 40))
        self.ui.frame_lbl_simulations.setFrameShape(QFrame.StyledPanel)
        self.ui.frame_lbl_simulations.setFrameShadow(QFrame.Raised)


        self.ui.layout_lbl_simulations = QVBoxLayout(self.ui.frame_lbl_simulations)
        self.ui.layout_lbl_simulations.setObjectName(u"layout_lbl_simulations")
        self.ui.label_simulation = QLabel(self.ui.frame_lbl_simulations)
        self.ui.label_simulation.setObjectName(u"label_simulation")
        self.ui.label_simulation.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
                                          "color:rgb(255, 255, 255);")

        self.ui.layout_lbl_simulations.addWidget(self.ui.label_simulation)
        self.ui.background_layout_simulations.addWidget(self.ui.frame_lbl_simulations)

        # Adding explanatory text
        self.ui.frame_lbl_simulations_exp = QFrame(self.ui.background_frame_simulations)
        self.ui.frame_lbl_simulations_exp.setObjectName(u"frame_lbl_simulations")
        self.ui.frame_lbl_simulations_exp.setMinimumSize(QSize(0, 40))
        self.ui.frame_lbl_simulations_exp.setMaximumSize(QSize(16777215, 40))
        self.ui.frame_lbl_simulations_exp.setFrameShape(QFrame.StyledPanel)
        self.ui.frame_lbl_simulations_exp.setFrameShadow(QFrame.Raised)

        self.ui.layout_lbl_simulations_exp = QVBoxLayout(self.ui.frame_lbl_simulations_exp)
        self.ui.layout_lbl_simulations_exp.setObjectName(u"layout_lbl_simulations_exp")
        self.ui.label_simulation_exp = QLabel(self.ui.frame_lbl_simulations_exp)
        self.ui.label_simulation_exp.setObjectName(u"label_simulation_exp")
        self.ui.label_simulation_exp.setStyleSheet(u"font: 12pt \"Segoe UI\";\n "
                                              u"color:rgb(255, 255, 255);")
        self.ui.layout_lbl_simulations_exp.addWidget(self.ui.label_simulation_exp)
        self.ui.background_layout_simulations.addWidget(self.ui.frame_lbl_simulations_exp)

        self.ui.frame_actions_simulation = QFrame(self.ui.background_frame_simulations)
        self.ui.frame_actions_simulation.setObjectName(u"frame_actions_simulation")
        self.ui.frame_actions_simulation.setMinimumSize(QSize(0, 50))
        self.ui.frame_actions_simulation.setMaximumSize(QSize(16777215, 50))
        self.ui.frame_actions_simulation.setFrameShape(QFrame.StyledPanel)
        self.ui.frame_actions_simulation.setFrameShadow(QFrame.Raised)

        self.ui.horizontalLayout_actions_simulation = QHBoxLayout(self.ui.frame_actions_simulation)
        self.ui.horizontalLayout_actions_simulation.setObjectName(u"horizontalLayout_actions_simulation")
        self.ui.horizontalLayout_actions_simulation.setContentsMargins(3, 3, -1, 3)

        self.ui.search_simulation_lineEdit = QLineEdit(self.ui.frame_actions_simulation)
        self.ui.search_simulation_lineEdit.setObjectName(u"search_simulation_lineEdit")
        self.ui.search_simulation_lineEdit.setMinimumSize(QSize(400, 45))
        self.ui.search_simulation_lineEdit.setMaximumSize(QSize(600, 45))
        self.ui.search_simulation_lineEdit.setStyleSheet(u"QLineEdit{\n"
                                              "	background-color:rgb(68,71,90);\n"
                                              "	padding: 8px;\n"
                                              "	color: rgb(255, 255, 255);\n"
                                              "	border-radius: 10px;\n"
                                              "}\n"
                                              "\n"
                                              "QLineEdit:hover{\n"
                                              "	border: 1px solid #c3ccdf;\n"
                                              "}\n")

        self.ui.horizontalLayout_actions_simulation.addWidget(self.ui.search_simulation_lineEdit)

        self.ui.search_simulation = QPushButton(self.ui.frame_actions_simulation)
        self.ui.search_simulation.setObjectName(u"search_simulation")
        self.ui.search_simulation.setMinimumSize(QSize(62, 45))
        self.ui.search_simulation.setMaximumSize(QSize(62, 45))
        self.ui.search_simulation.setStyleSheet(u"QPushButton{\n"
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

        self.ui.horizontalLayout_actions_simulation.addWidget(self.ui.search_simulation)

        self.ui.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ui.horizontalLayout_actions_simulation.addItem(self.ui.horizontalSpacer_2)

        self.ui.create_simulation_btn = QPushButton(self.ui.frame_actions_simulation)
        self.ui.create_simulation_btn.setObjectName(u"create_simulation_btn")
        self.ui.create_simulation_btn.setMinimumSize(QSize(60, 45))
        self.ui.create_simulation_btn.setMaximumSize(QSize(60, 45))
        self.ui.create_simulation_btn.setStyleSheet(u"QPushButton{\n"
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

        self.ui.horizontalLayout_actions_simulation.addWidget(self.ui.create_simulation_btn)

        self.ui.background_layout_simulations.addWidget(self.ui.frame_actions_simulation)

        self.ui.frame_table_simulations = QFrame(self.ui.background_frame_simulations)
        self.ui.frame_table_simulations.setObjectName(u"frame_table_simulations")
        self.ui.frame_table_simulations.setStyleSheet(u"background-color: #282a36")
        self.ui.frame_table_simulations.setFrameShape(QFrame.StyledPanel)
        self.ui.frame_table_simulations.setFrameShadow(QFrame.Raised)
        self.ui.layout_table_simulations = QHBoxLayout(self.ui.frame_table_simulations)
        self.ui.layout_table_simulations.setSpacing(0)
        self.ui.layout_table_simulations.setObjectName(u"layout_table_simulations")
        self.ui.layout_table_simulations.setContentsMargins(0, 0, 0, 0)
        self.ui.table_simulations = QTableWidget(self.ui.frame_table_simulations)
        self.ui.table_simulations.setObjectName(u"table_simulations")
        self.ui.table_simulations.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ui.table_simulations.setLayoutDirection(Qt.LeftToRight)
        self.ui.table_simulations.setStyleSheet(u"\n"
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
                                           "\n"
                                           "}\n"
                                           "\n"
                                           "\n"
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
                                           "}\n"
                                           " ")
        self.ui.table_simulations.setShowGrid(False)
        self.ui.table_simulations.setWordWrap(False)
        self.ui.table_simulations.setCornerButtonEnabled(False)

        self.ui.layout_table_simulations.addWidget(self.ui.table_simulations)
        self.ui.background_layout_simulations.addWidget(self.ui.frame_table_simulations)
        self.ui.central_frame_simulations_layout.addWidget(self.ui.background_frame_simulations)
        self.ui.page_simulations_layout.addWidget(self.ui.central_frame_simulations)

        self.retranslateUi()

    def retranslateUi(self):
        self.ui.label_simulation.setText(QCoreApplication.translate("app_pages", u"Simulation", None))
        self.ui.label_simulation_exp.setText(QCoreApplication.translate("app_pages", u"These are the existent simulations", None))
        self.ui.search_simulation_lineEdit.setPlaceholderText(QCoreApplication.translate("app_pages", u"Search by name", None))
        self.ui.search_simulation.setText(QCoreApplication.translate("app_pages", u"Search", None))
        self.ui.create_simulation_btn.setText(QCoreApplication.translate("app_pages", u"Create", None))

    # retranslateUi
