from gui.components.components import *


class CreateSimulatePageView(QWidget):

    def __init__(self, parent=None, ui=None):
        super().__init__(parent)
        self.ui = ui
        self.rovers_selected = False

        found = self.ui.fr_sim_widgets_layout.findChild(QGridLayout, "grid_layout_height")
        if found is None:
            self.create_widgets_sim_fields()

        # Hide max_time
        self.hide_max_time()
        # Hide max_area
        self.hide_max_area()

    def create_widgets_sim_fields(self):
        self.ui.grid_layout_height = self.add_height_grid_layout(grid_layout_name="grid_layout_height",
                                                                 label_name="height_label",
                                                                 error_label_name="height_error_label",
                                                                 text_label="Cave length (m):", line_edit_name="height",
                                                                 line_edit_type="float")

        self.add_num_jobs()
        self.ui.grid_layout_observation_rad = self.add_radio_grid_layout(grid_layout_name="grid_layout_observation_rad",
                                                                         label_name="rad_label",
                                                                         error_label_name="rad_error_label",
                                                                         text_label="Observation radio (m):  ",
                                                                         line_edit_name="obv_rad",
                                                                         line_edit_type="float")


        # Add a widget to contain each layout
        # Hide the widget corresponding to the mode chosen with the radio buttons
        self.ui.max_time_container = QWidget(parent=self.ui.frame_simulation_widgets)
        self.ui.grid_layout_max_time = self.add_max_time_grid_layout(grid_layout_name="grid_layout_max_time",
                                                                     label_name="max_time_label",
                                                                     error_label_name="max_time_error_label",
                                                                     text_label="Maximum time (min):",
                                                                     line_edit_name="max_time"
                                                                     , line_edit_type="float")
        self.ui.grid_layout_max_time.setSpacing(0)
        self.ui.max_time_container.setObjectName("max_time_container")
        self.ui.max_time_container.setLayout(self.ui.grid_layout_max_time)

        self.ui.cave_width_container = QWidget(parent=self.ui.frame_simulation_widgets)
        self.ui.grid_layout_cave_width = self.add_cave_width_grid_layout(grid_layout_name="grid_layout_cave_width",
                                                                         label_name="cave_width_label",
                                                                         error_label_name="cave_width_error_label",
                                                                         text_label="Cave width (m):",
                                                                         line_edit_name="cave_width",
                                                                         line_edit_type="float")
        self.ui.grid_layout_cave_width.setSpacing(0)
        self.ui.cave_width_container.setObjectName("max_area_container")

        self.ui.cave_width_container.setLayout(self.ui.grid_layout_cave_width)
        self.ui.fr_sim_widgets_layout.addLayout(self.ui.grid_layout_height)
        self.ui.verticalLayout_frame_num_jobs.addLayout(self.ui.grid_layout_observation_rad)
        self.ui.fr_sim_widgets_layout.addWidget(self.ui.max_time_container)
        self.ui.fr_sim_widgets_layout.addWidget(self.ui.cave_width_container)
        self.verticalSpacer_sim = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.ui.fr_sim_widgets_layout.addItem(self.verticalSpacer_sim)

        # Adding the frame for selecting the fleet of rovers
        self.add_select_rovers()

    def add_select_rovers(self):
        self.ui.frame_rovers_select = QFrame(self.ui.central_frame_simulation)
        self.ui.frame_rovers_select.setObjectName(u"frame_rovers_select")
        self.ui.frame_rovers_select.setMinimumSize(QSize(0, 50))
        self.ui.frame_rovers_select.setFrameShape(QFrame.StyledPanel)
        self.ui.frame_rovers_select.setFrameShadow(QFrame.Raised)
        self.ui.horizontalLayout_3 = QHBoxLayout(self.ui.frame_rovers_select)
        self.ui.horizontalLayout_3.setSpacing(0)
        self.ui.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ui.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ui.rover_select_gridLayout = QGridLayout()
        self.ui.rover_select_gridLayout.setObjectName(u"rover_select_gridLayout")
        self.ui.label_num_rovers = QLabel(self.ui.frame_rovers_select)
        self.ui.label_num_rovers.setObjectName(u"label_num_rovers")
        self.ui.label_num_rovers.setStyleSheet(u"font: 11pt \"Segoe UI\";")

        self.ui.rover_select_gridLayout.addWidget(self.ui.label_num_rovers, 0, 2, 1, 1)

        self.ui.add_rover_select_btn = QPushButton(self.ui.frame_rovers_select)
        self.ui.add_rover_select_btn.setObjectName(u"add_rover_select_btn")
        self.ui.add_rover_select_btn.setMinimumSize(QSize(25, 0))
        self.ui.add_rover_select_btn.setStyleSheet(u"QPushButton{\n"
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

        self.ui.rover_select_gridLayout.addWidget(self.ui.add_rover_select_btn, 0, 4, 1, 1)

        self.ui.cb_rovers = QComboBox(self.ui.frame_rovers_select)

        self.ui.cb_rovers.setObjectName(u"cb_rovers")
        self.ui.cb_rovers.setMinimumSize(QSize(0, 30))
        self.ui.cb_rovers.setMaximumSize(QSize(16777215, 30))

        self.ui.cb_rovers.setStyleSheet(u"QComboBox{\n"
                                        "	background-color: rgb(27, 29, 35);\n"
                                        "	border-radius: 5px;\n"
                                        "	border: 2px solid rgb(33, 37, 43);\n"
                                        "	padding: 5px;\n"
                                        "	padding-left: 10px;\n"
                                        "}\n"
                                        "QComboBox:hover{\n"
                                        "	border: 2px solid rgb(64, 71, 88);\n"
                                        "}\n")

        self.ui.rover_select_gridLayout.addWidget(self.ui.cb_rovers, 0, 1, 1, 1)

        self.ui.label_rovers_select = QLabel(self.ui.frame_rovers_select)
        self.ui.label_rovers_select.setObjectName(u"label_rovers_select")
        self.ui.label_rovers_select.setStyleSheet(u"font: 11pt \"Segoe UI\";")

        self.ui.rover_select_gridLayout.addWidget(self.ui.label_rovers_select, 0, 0, 1, 1)

        self.ui.cb_num_rovers = QComboBox(self.ui.frame_rovers_select)
        self.ui.cb_num_rovers.setObjectName(u"cb_num_rovers")
        self.ui.cb_num_rovers.setMinimumSize(QSize(0, 30))
        self.ui.cb_num_rovers.setMaximumSize(QSize(16777215, 30))
        self.ui.cb_num_rovers.setStyleSheet(u"QComboBox{\n"
                                            "	background-color: rgb(27, 29, 35);\n"
                                            "	border-radius: 5px;\n"
                                            "	border: 2px solid rgb(33, 37, 43);\n"
                                            "	padding: 5px;\n"
                                            "	padding-left: 10px;\n"
                                            "}\n"
                                            "QComboBox:hover{\n"
                                            "	border: 2px solid rgb(64, 71, 88);\n"
                                            "}\n")

        self.ui.rover_select_gridLayout.addWidget(self.ui.cb_num_rovers, 0, 3, 1, 1)

        self.ui.lbl_error_rovers_select = QLabel(self.ui.frame_rovers_select)
        self.ui.lbl_error_rovers_select.setObjectName(u"lbl_error_rovers_select")
        self.ui.lbl_error_rovers_select.setMinimumSize(QSize(0, 20))
        self.ui.lbl_error_rovers_select.setMaximumSize(QSize(16777215, 20))

        self.ui.rover_select_gridLayout.addWidget(self.ui.lbl_error_rovers_select, 1, 0, 1, 5)

        self.ui.horizontalLayout_3.addLayout(self.ui.rover_select_gridLayout)

        self.ui.central_fr_sim_layout.addWidget(self.ui.frame_rovers_select)

        self.ui.frame_rovers_selected = QFrame(self.ui.central_frame_simulation)
        self.ui.frame_rovers_selected.setObjectName(u"frame_rovers_selected")
        self.ui.frame_rovers_selected.setFrameShape(QFrame.StyledPanel)
        self.ui.frame_rovers_selected.setFrameShadow(QFrame.Raised)
        self.ui.verticalLayout_18 = QVBoxLayout(self.ui.frame_rovers_selected)
        self.ui.verticalLayout_18.setSpacing(0)
        self.ui.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.ui.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.ui.label_rovers_selected = QLabel(self.ui.frame_rovers_selected)
        self.ui.label_rovers_selected.setObjectName(u"label_rovers_selected")
        self.ui.label_rovers_selected.setStyleSheet(u"font: 11pt \"Segoe UI\";")

        self.ui.verticalLayout_18.addWidget(self.ui.label_rovers_selected)

        self.ui.textEdit_rovers_selected = QTextEdit(self.ui.frame_rovers_selected)
        self.ui.textEdit_rovers_selected.setObjectName(u"textEdit_rovers_selected")
        self.ui.textEdit_rovers_selected.setMinimumSize(QSize(0, 70))
        self.ui.textEdit_rovers_selected.setMaximumSize(QSize(16777215, 70))
        self.ui.textEdit_rovers_selected.setStyleSheet(u"QTextEdit{\n"
                                                       "	background-color: rgb(27, 29, 35);\n"
                                                       "	border-radius: 5px;\n"
                                                       "	border: 2px solid rgb(33, 37, 43);\n"
                                                       "	padding: 5px;\n"
                                                       "	padding-left: 10px;\n"
                                                       "}\n"
                                                       "QTextEdit:hover {\n"
                                                       "	border: 2px solid rgb(64, 71, 88);\n"
                                                       "}\n"
                                                       "QTextEdit:focus {\n"
                                                       "	border: 2px solid rgb(91, 101, 124);\n"
                                                       "}")
        self.ui.textEdit_rovers_selected.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ui.textEdit_rovers_selected.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.ui.verticalLayout_18.addWidget(self.ui.textEdit_rovers_selected)

        self.ui.central_fr_sim_layout.addWidget(self.ui.frame_rovers_selected)

        self.ui.frame_simulate = QFrame(self.ui.central_frame_simulation)
        self.ui.frame_simulate.setObjectName(u"frame_simulate")
        self.ui.frame_simulate.setMinimumSize(QSize(0, 50))
        self.ui.frame_simulate.setMaximumSize(QSize(16777215, 50))
        self.ui.frame_simulate.setFrameShape(QFrame.StyledPanel)
        self.ui.frame_simulate.setFrameShadow(QFrame.Raised)
        self.ui.horizontalLayout_5 = QHBoxLayout(self.ui.frame_simulate)
        self.ui.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ui.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ui.horizontalLayout_5.addItem(self.ui.horizontalSpacer_3)

        self.ui.button_simulate = QPushButton(self.ui.frame_simulate)
        self.ui.button_simulate.setObjectName(u"button_simulate")
        self.ui.button_simulate.setMinimumSize(QSize(70, 30))
        self.ui.button_simulate.setMaximumSize(QSize(16777215, 30))
        self.ui.button_simulate.setStyleSheet(u"QPushButton{\n"
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

        self.ui.horizontalLayout_5.addWidget(self.ui.button_simulate)

        self.ui.central_fr_sim_layout.addWidget(self.ui.frame_simulate)

        self.ui.page_create_simulation_layout.addWidget(self.ui.central_frame_simulation, 0, Qt.AlignLeft | Qt.AlignTop)
        # Adding text
        self.ui.label_num_rovers.setText(QCoreApplication.translate("app_pages", u"Number of rovers:", None))
        self.ui.add_rover_select_btn.setText(QCoreApplication.translate("app_pages", u"+", None))
        self.ui.label_rovers_select.setText(QCoreApplication.translate("app_pages", u"Select the rovers:", None))
        self.ui.lbl_error_rovers_select.setText("")
        self.ui.label_rovers_selected.setText(
            QCoreApplication.translate("app_pages", u"These are the rovers selected:", None))
        self.ui.button_simulate.setText(QCoreApplication.translate("app_pages", u"Simulate", None))

    def add_num_jobs(self):
        self.ui.frame_jobs = QFrame(self.ui.fr_container_aux1)
        self.ui.frame_jobs.setObjectName(u"frame_jobs")
        self.ui.frame_jobs.setMinimumSize(QSize(320, 100))
        self.ui.frame_jobs.setMaximumSize(QSize(320, 100))
        self.ui.frame_jobs.setFrameShape(QFrame.StyledPanel)
        self.ui.frame_jobs.setFrameShadow(QFrame.Raised)
        self.ui.verticalLayout_frame_num_jobs = QVBoxLayout(self.ui.frame_jobs)
        self.ui.verticalLayout_frame_num_jobs.setSpacing(0)
        self.ui.verticalLayout_frame_num_jobs.setObjectName(u"verticalLayout_frame_num_jobs")
        self.ui.verticalLayout_frame_num_jobs.setContentsMargins(0, 0, 0, 0)
        self.ui.gridLayout = QGridLayout()
        self.ui.gridLayout.setSpacing(0)
        self.ui.gridLayout.setObjectName(u"gridLayout")
        self.ui.label_num_jobs = QLabel(self.ui.frame_jobs)
        self.ui.label_num_jobs.setObjectName(u"label_num_jobs")
        self.ui.label_num_jobs.setMinimumSize(QSize(150, 25))
        self.ui.label_num_jobs.setMaximumSize(QSize(150, 25))
        self.ui.label_num_jobs.setStyleSheet(u"font: 11pt \"Segoe UI\";")

        self.ui.gridLayout.addWidget(self.ui.label_num_jobs, 0, 0, 1, 1)

        self.ui.lbl_error_num_jobs = QLabel(self.ui.frame_jobs)
        self.ui.lbl_error_num_jobs.setObjectName(u"lbl_error_num_jobs")
        self.ui.lbl_error_num_jobs.setMinimumSize(QSize(0, 25))
        self.ui.lbl_error_num_jobs.setMaximumSize(QSize(16777215, 25))

        self.ui.gridLayout.addWidget(self.ui.lbl_error_num_jobs, 2, 0, 1, 1)

        self.ui.cb_num_jobs = QComboBox(self.ui.frame_jobs)
        url1 = os.getcwd()
        folder = "\gui\images\icons\icon_down_arrow_2.svg"
        path = url1 + folder

        self.ui.cb_num_jobs.setObjectName(u"cb_num_jobs")
        self.ui.cb_num_jobs.setMinimumSize(QSize(160, 30))
        self.ui.cb_num_jobs.setMaximumSize(QSize(160, 30))

        self.ui.gridLayout.addWidget(self.ui.cb_num_jobs, 0, 1, 1, 1)
        self.ui.verticalLayout_frame_num_jobs.addLayout(self.ui.gridLayout)
        self.ui.horizontalLayout.addWidget(self.ui.frame_jobs, 0, Qt.AlignLeft | Qt.AlignTop)
        self.ui.central_fr_sim_layout.addWidget(self.ui.fr_container_aux1, 0, Qt.AlignLeft)
        self.ui.label_num_jobs.setText(QCoreApplication.translate("app_pages", u"Select number of jobs:", None))
        self.ui.lbl_error_num_jobs.setText("")
        self.ui.cb_num_jobs.setStyleSheet(u"QComboBox{\n"
                                          "background-color: rgb(27, 29, 35);\n"
                                          "border-radius: 5px; border: 2px solid rgb(33, 37, 43);\n"
                                          "padding: 5px; padding-left: 10px;}\n"
                                          "QComboBox:hover{\n"
                                          "border: 2px solid rgb(64, 71, 88);}\n")

    def add_cave_width_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                                   line_edit_type, width_label=150):

        grid_layout = self.create_generic_layout(grid_layout_name, parent_frame=self.ui.frame_simulation_widgets)
        # Add label
        self.ui.cave_width_sim_label = CustomLabel(parent=self.ui.frame_simulation_widgets, name=label_name,
                                                   text=text_label,
                                                   width_label=width_label)
        # Add error label
        self.ui.cave_width_sim_error_label = CustomLabelError(parent=self.ui.frame_simulation_widgets,
                                                              name=error_label_name, text="")
        # Add lineEdit
        self.ui.cave_width_sim_line_edit = CustomLineEdit(parent=self.ui.frame_simulation_widgets,
                                                          lineEdit_name=line_edit_name,
                                                          label_error=self.ui.cave_width_sim_error_label,
                                                          line_edit_type=line_edit_type,
                                                          line_edit_width=100)

        grid_layout.addWidget(self.ui.cave_width_sim_label, 0, 0)
        grid_layout.addWidget(self.ui.cave_width_sim_line_edit, 0, 1)
        grid_layout.addWidget(self.ui.cave_width_sim_error_label, 1, 0)
        return grid_layout

    def add_max_time_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                                 line_edit_type, width_label=150):

        grid_layout = self.create_generic_layout(grid_layout_name, parent_frame=self.ui.frame_simulation_widgets)
        # Add label
        self.ui.max_time_sim_label = CustomLabel(parent=self.ui.frame_simulation_widgets, name=label_name,
                                                 text=text_label,
                                                 width_label=width_label)
        # Add error label
        self.ui.max_time_sim_error_label = CustomLabelError(parent=self.ui.frame_simulation_widgets,
                                                            name=error_label_name, text="")
        # Add lineEdit
        self.ui.max_time_sim_line_edit = CustomLineEdit(parent=self.ui.frame_simulation_widgets,
                                                        lineEdit_name=line_edit_name,
                                                        label_error=self.ui.max_time_sim_error_label,
                                                        line_edit_type=line_edit_type,
                                                        line_edit_width=100)

        grid_layout.addWidget(self.ui.max_time_sim_label, 0, 0)
        grid_layout.addWidget(self.ui.max_time_sim_line_edit, 0, 1)
        grid_layout.addWidget(self.ui.max_time_sim_error_label, 1, 0)
        return grid_layout

    def add_radio_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                              line_edit_type, width_label=190):

        grid_layout = self.create_generic_layout(grid_layout_name, parent_frame=self.ui.frame_jobs)
        # Add label
        self.ui.radio_sim_label = CustomLabel(parent=self.ui.frame_jobs, name=label_name,
                                              text=text_label,
                                              width_label=width_label)
        # Add error label
        self.ui.radio_sim_error_label = CustomLabelError(parent=self.ui.frame_jobs,
                                                         name=error_label_name, text="")
        # Add lineEdit
        self.ui.radio_sim_line_edit = CustomLineEdit(parent=self.ui.frame_jobs,
                                                     lineEdit_name=line_edit_name,
                                                     label_error=self.ui.radio_sim_error_label,
                                                     line_edit_type=line_edit_type,
                                                     line_edit_width=160)

        grid_layout.addWidget(self.ui.radio_sim_label, 0, 0)
        grid_layout.addWidget(self.ui.radio_sim_line_edit, 0, 1)
        grid_layout.addWidget(self.ui.radio_sim_error_label, 1, 0)
        return grid_layout

    def add_height_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                               line_edit_type, width_label=150):

        grid_layout = self.create_generic_layout(grid_layout_name, parent_frame=self.ui.frame_simulation_widgets)
        # Add label
        self.ui.height_sim_label = CustomLabel(parent=self.ui.frame_simulation_widgets, name=label_name,
                                               text=text_label,
                                               width_label=width_label)

        # Add error label
        self.ui.height_sim_error_label = CustomLabelError(parent=self.ui.frame_simulation_widgets,
                                                          name=error_label_name, text="")
        # Add lineEdit
        self.ui.height_sim_line_edit = CustomLineEdit(parent=self.ui.frame_simulation_widgets,
                                                      lineEdit_name=line_edit_name,
                                                      label_error=self.ui.height_sim_error_label,
                                                      line_edit_type=line_edit_type,
                                                      line_edit_width=100)

        grid_layout.addWidget(self.ui.height_sim_label, 0, 0)
        grid_layout.addWidget(self.ui.height_sim_line_edit, 0, 1)
        grid_layout.addWidget(self.ui.height_sim_error_label, 1, 0)
        return grid_layout

    def create_generic_layout(self, grid_layout_name, parent_frame):
        grid_layout = QGridLayout(parent=parent_frame)
        grid_layout.setObjectName(grid_layout_name)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setAlignment(Qt.AlignTop)
        return grid_layout

    def hide_max_area(self):
        self.ui.cave_width_container.setHidden(True)

    def hide_max_time(self):
        self.ui.max_time_container.setHidden(True)
