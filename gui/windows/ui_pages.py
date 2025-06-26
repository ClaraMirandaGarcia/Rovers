from qt_core import *


class Ui_app_pages(object):
    def setupUi(self, app_pages):
        if not app_pages.objectName():
            app_pages.setObjectName(u"app_pages")
        app_pages.resize(696, 922)
        self.page_initial = QWidget()
        self.page_initial.setObjectName(u"page_initial")

        self.verticalLayout = QVBoxLayout(self.page_initial)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.page_initial)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 150))
        self.frame.setMaximumSize(QSize(500, 150))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_welcome = QLabel(self.frame)
        self.label_welcome.setObjectName(u"label_welcome")
        self.label_welcome.setStyleSheet(u"font: 700 30pt \"Segoe UI\";\n"
                                         "color:rgb(255, 255, 255);")
        self.label_welcome.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_welcome)

        self.label_description_welcome = QLabel(self.frame)
        self.label_description_welcome.setObjectName(u"label_description_welcome")
        self.label_description_welcome.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
                                                     "color:rgb(255, 255, 255);")
        self.label_description_welcome.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_description_welcome)

        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter)

        app_pages.addWidget(self.page_initial)

        # page_1 create rover
        self.page_create_rover = QWidget()
        self.page_create_rover.setObjectName(u"page_create_rover")
        self.page_create_rover_layout = QVBoxLayout(self.page_create_rover)
        self.page_create_rover_layout.setObjectName(u"page_create_rover_layout")
        self.page_create_rover_layout.setAlignment(Qt.AlignTop)
        app_pages.addWidget(self.page_create_rover)

        # page_1 details rover
        self.page_details = QWidget()
        self.page_details.setObjectName(u"page_details")
        self.page_details_rover_layout = QVBoxLayout(self.page_details)
        self.page_details_rover_layout.setObjectName(u"page_details_rover_layout")
        self.page_details_rover_layout.setAlignment(Qt.AlignTop)
        app_pages.addWidget(self.page_details)

        # page_1 edit rover
        self.page_edit_rover = QWidget()
        self.page_edit_rover.setObjectName(u"page_edit_rover")
        self.page_edit_rover_layout = QVBoxLayout(self.page_edit_rover)
        self.page_edit_rover_layout.setObjectName(u"page_edit_rover_layout")
        self.page_edit_rover_layout.setAlignment(Qt.AlignTop)
        app_pages.addWidget(self.page_edit_rover)

        # page_1 rovers
        self.page_rovers = QWidget()
        self.page_rovers.setObjectName(u"page_rovers")
        self.page_rovers.setStyleSheet(u"QScrollBar:vertical {\n"
                                       "border: none;\n"
                                       "background: rgb(52, 59, 72);\n"
                                       "width: 5px;\n"
                                       "}\n"
                                       "QScrollBar::handle:vertical {\n"
                                       "background: #44475a;\n"
                                       "border-radius: 4px\n"
                                       "}\n"
                                       "QScrollBar::handle:vertical:hover {\n"
                                       "    border: 3px solid rgb(85,170,225);\n"
                                       "}\n"
                                       "QScrollBar::handle:vertical:pressed {\n"
                                       "    border: 3px solid rgb(79, 198, 219)\n"
                                       "}\n"
                                       "QScrollBar::add-line:vertical {\n"
                                       "border: none;\n"
                                       "}\n"
                                       "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                       "     background: none;\n"
                                       " }\n"
                                       "\n"
                                       " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                       "     background: none;\n"
                                       " }\n")
        self.layout_page_rovers = QVBoxLayout(self.page_rovers)
        self.layout_page_rovers.setObjectName(u"layout_page_rovers")
        self.layout_page_rovers.setContentsMargins(35, 9, 9, 9)
        app_pages.addWidget(self.page_rovers)

        # Create simulation page_1
        self.page_create_simulation = QWidget()
        self.page_create_simulation.setObjectName(u"page_create_simulation")
        self.page_create_simulation.setLayoutDirection(Qt.LeftToRight)
        self.page_create_simulation.setStyleSheet(u"QScrollBar:vertical {\n"
                                                  "border: none;\n"
                                                  "background: rgb(52, 59, 72);\n"
                                                  "width: 5px;\n"
                                                  "}\n"
                                                  "QScrollBar::handle:vertical {\n"
                                                  "background: #44475a;\n"
                                                  "border-radius: 4px\n"
                                                  "}\n"
                                                  "QScrollBar::handle:vertical:hover {\n"
                                                  "    border: 3px solid rgb(85,170,225);\n"
                                                  "}\n"
                                                  "QScrollBar::handle:vertical:pressed {\n"
                                                  "    border: 3px solid rgb(79, 198, 219)\n"
                                                  "}\n"
                                                  "QScrollBar::add-line:vertical {\n"
                                                  "border: none;\n"
                                                  "}\n"
                                                  "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                                  "     background: none;\n"
                                                  " }\n"
                                                  "\n"
                                                  " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                                  "     background: none;\n"
                                                  " }\n")
        # Create sim layout
        self.page_create_simulation_layout = QVBoxLayout(self.page_create_simulation)
        self.page_create_simulation_layout.setSpacing(0)
        self.page_create_simulation_layout.setObjectName(u"page_create_simulation_layout")
        self.page_create_simulation_layout.setContentsMargins(35, 9, 9, 9)

        # Simulation list
        self.page_simulations = QWidget()
        self.page_simulations.setObjectName(u"page_simulations")
        self.page_simulations_layout = QVBoxLayout(self.page_simulations)
        self.page_simulations_layout.setObjectName(u"page_simulations_layout")
        self.page_simulations_layout.setContentsMargins(35, 9, 9, 9)
        app_pages.addWidget(self.page_simulations)

        # Main frame
        self.central_frame_simulation = QFrame(self.page_create_simulation)
        self.central_frame_simulation.setObjectName(u"central_frame_simulation")
        self.central_frame_simulation.setMinimumSize(QSize(700, 0))
        self.central_frame_simulation.setMaximumSize(QSize(700, 16777215))
        self.central_frame_simulation.setLayoutDirection(Qt.LeftToRight)
        self.central_frame_simulation.setFrameShape(QFrame.StyledPanel)
        self.central_frame_simulation.setFrameShadow(QFrame.Raised)

        # Main frame layout
        self.central_fr_sim_layout = QVBoxLayout(self.central_frame_simulation)
        self.central_fr_sim_layout.setObjectName(u"central_fr_sim_layout")

        # Title frame and label
        self.title_sim_frame = QFrame(self.central_frame_simulation)
        self.title_sim_frame.setObjectName(u"title_sim_frame")
        self.title_sim_frame.setMinimumSize(QSize(0, 40))
        self.title_sim_frame.setMaximumSize(QSize(16777215, 40))
        self.title_sim_frame.setFrameShape(QFrame.StyledPanel)
        self.title_sim_frame.setFrameShadow(QFrame.Raised)

        self.title_sim_frame_layout = QVBoxLayout(self.title_sim_frame)
        self.title_sim_frame_layout.setObjectName(u"title_sim_frame_layout")

        self.label_run_simulation = QLabel(self.title_sim_frame)
        self.label_run_simulation.setObjectName(u"label_run_simulation")
        self.label_run_simulation.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
                                                "color:rgb(255, 255, 255);")

        self.title_sim_frame_layout.addWidget(self.label_run_simulation)
        self.central_fr_sim_layout.addWidget(self.title_sim_frame)

        # Description frame and label
        self.des_sim_frame = QFrame(self.central_frame_simulation)
        self.des_sim_frame.setObjectName(u"des_sim_frame")
        self.des_sim_frame.setFrameShape(QFrame.StyledPanel)
        self.des_sim_frame.setFrameShadow(QFrame.Raised)
        self.des_sim_frame.setMinimumSize(QSize(0, 40))
        self.des_sim_frame.setMaximumSize(QSize(16777215, 40))

        self.des_sim_frame_layout = QVBoxLayout(self.des_sim_frame)
        self.des_sim_frame_layout.setObjectName(u"des_sim_frame_layout")

        self.label_descrip_simulation = QLabel(self.des_sim_frame)
        self.label_descrip_simulation.setObjectName(u"label_descrip_simulation")
        self.label_descrip_simulation.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
                                                    "color:rgb(255, 255, 255);")

        self.des_sim_frame_layout.addWidget(self.label_descrip_simulation)
        self.central_fr_sim_layout.addWidget(self.des_sim_frame)

        self.group_box_modes = QGroupBox(self.central_frame_simulation)
        self.group_box_modes.setObjectName(u"group_box_modes")
        self.group_box_modes.setMinimumSize(QSize(180, 115))
        self.group_box_modes.setMaximumSize(QSize(180, 115))
        self.group_box_modes.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.layout_group_box_sim = QVBoxLayout(self.group_box_modes)
        self.layout_group_box_sim.setObjectName(u"layout_group_box_sim")
        self.layout_group_box_sim.setContentsMargins(9, 9, 9, 9)
        self.radioButton_max_time = QRadioButton(self.group_box_modes)
        self.radioButton_max_time.setObjectName(u"radioButton_max_time")
        self.radioButton_max_time.setStyleSheet(u"QRadioButton::indicator {\n"
                                                "    border: 3px solid rgb(52, 59, 72);\n"
                                                "	width: 15px;\n"
                                                "	height: 15px;\n"
                                                "	border-radius: 10px;\n"
                                                "    background: rgb(44, 49, 60);\n"
                                                "}\n"
                                                "QRadioButton::indicator:hover {\n"
                                                "    border: 3px solid rgb(58, 66, 81);\n"
                                                "}\n"
                                                "QRadioButton::indicator:checked {\n"
                                                "    background: 3px solid rgb(94, 106, 130);\n"
                                                "	border: 3px solid rgb(52, 59, 72);	\n"
                                                "}\n"
                                                "font: 11pt \"Segoe UI\";")

        self.layout_group_box_sim.addWidget(self.radioButton_max_time)

        self.radioButton_max_area = QRadioButton(self.group_box_modes)
        self.radioButton_max_area.setObjectName(u"radioButton_max_area")
        self.radioButton_max_area.setStyleSheet(u"QRadioButton::indicator {\n"
                                                "    border: 3px solid rgb(52, 59, 72);\n"
                                                "	 width: 15px;\n"
                                                "	 height: 15px;\n"
                                                "	 border-radius: 10px;\n"
                                                "    background: rgb(44, 49, 60);\n"
                                                "}\n"
                                                "QRadioButton::indicator:hover {\n"
                                                "    border: 3px solid rgb(58, 66, 81);\n"
                                                "}\n"
                                                "QRadioButton::indicator:checked {\n"
                                                "    background: 3px solid rgb(94, 106, 130);\n"
                                                "	border: 3px solid rgb(52, 59, 72);	\n"
                                                "}\n"
                                                "font: 11pt \"Segoe UI\";")

        self.layout_group_box_sim.addWidget(self.radioButton_max_area)

        self.lbl_error_mode = QLabel(self.group_box_modes)
        self.lbl_error_mode.setObjectName(u"lbl_error_mode")

        self.layout_group_box_sim.addWidget(self.lbl_error_mode)
        self.lbl_error_mode.setHidden(True)
        self.central_fr_sim_layout.addWidget(self.group_box_modes)

        self.fr_container_aux1 = QFrame(self.central_frame_simulation)
        self.fr_container_aux1.setObjectName(u"fr_container_aux1")
        self.fr_container_aux1.setMinimumSize(QSize(690, 150))
        self.fr_container_aux1.setMaximumSize(QSize(690, 150))
        self.fr_container_aux1.setFrameShape(QFrame.StyledPanel)
        self.fr_container_aux1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fr_container_aux1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_simulation_widgets = QFrame(self.fr_container_aux1)
        self.frame_simulation_widgets.setObjectName(u"frame_simulation_widgets")
        self.frame_simulation_widgets.setMinimumSize(QSize(300, 250))
        self.frame_simulation_widgets.setMaximumSize(QSize(460, 250))
        self.frame_simulation_widgets.setStyleSheet(u"")
        self.frame_simulation_widgets.setFrameShape(QFrame.StyledPanel)
        self.frame_simulation_widgets.setFrameShadow(QFrame.Raised)
        self.fr_sim_widgets_layout = QVBoxLayout(self.frame_simulation_widgets)
        self.fr_sim_widgets_layout.setSpacing(0)
        self.fr_sim_widgets_layout.setObjectName(u"fr_sim_widgets_layout")
        self.fr_sim_widgets_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.frame_simulation_widgets, 0, Qt.AlignLeft | Qt.AlignTop)

        app_pages.addWidget(self.page_create_simulation)

        self.retranslateUi(app_pages)
        app_pages.setCurrentIndex(3)
        QMetaObject.connectSlotsByName(app_pages)

    # setupUi

    def retranslateUi(self, app_pages):
        app_pages.setWindowTitle(QCoreApplication.translate("app_pages", u"StackedWidget", None))
        self.label_welcome.setText(QCoreApplication.translate("app_pages", u"Welcome!", None))
        self.label_description_welcome.setText(QCoreApplication.translate("app_pages",
                                                                          u"<html><head/><body><p>This is an application"
                                                                          u" created for the Planning System for lunar cave"
                                                                          u" </p><p>explorations with cooperative rovers </p>"
                                                                          u"<p>Final Degree Project</p></body></html>",
                                                                          None))
        self.label_run_simulation.setText(QCoreApplication.translate("app_pages", u"Run your simulation", None))
        self.label_descrip_simulation.setText(
            QCoreApplication.translate("app_pages", u"Please, select the following values in order to run a simulation",
                                       None))
        self.group_box_modes.setTitle(QCoreApplication.translate("app_pages", u"Mode", None))
        self.radioButton_max_time.setText(QCoreApplication.translate("app_pages", u"Maximum Time", None))
        self.radioButton_max_area.setText(QCoreApplication.translate("app_pages", u"Maximum Area", None))
        self.lbl_error_mode.setText("")

    # retranslateUi
