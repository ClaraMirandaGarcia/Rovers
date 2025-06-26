from gui.components.components import *


class EditRoverPageView(QWidget):
    def __init__(self, parent=None, ui=None):
        super().__init__(parent)
        self.ui = ui

        to_create = self.ui.ui_pages.page_edit_rover.findChild(QFrame, "central_frame_page_edit_rover")
        if to_create is None:
            self.initialize_gui()
        else:
            to_create.setHidden(False)

    def initialize_gui(self):

        # Container frame
        self.ui.edit_container_frame = QFrame(self.ui.ui_pages.page_edit_rover)
        self.ui.edit_container_frame.setObjectName(u"edit_container_frame")
        self.ui.edit_container_frame.setFrameShape(QFrame.StyledPanel)
        self.ui.edit_container_frame.setFrameShadow(QFrame.Raised)

        self.ui.edit_container_layout = QHBoxLayout(self.ui.edit_container_frame)
        self.ui.edit_container_layout.setObjectName(u"edit_container_layout")
        self.ui.edit_container_layout.setAlignment(Qt.AlignTop)

        # Frame return button
        self.ui.frame_return_edit = QFrame(self.ui.edit_container_frame)
        self.ui.frame_return_edit.setObjectName(u"frame_return_edit")
        self.ui.frame_return_edit.setFrameShape(QFrame.StyledPanel)
        self.ui.frame_return_edit.setFrameShadow(QFrame.Raised)

        self.ui.return_edit_layout = QVBoxLayout(self.ui.frame_return_edit)
        self.ui.return_edit_layout.setObjectName(u"return_edit_layout")

        # return button
        # Frame return button
        self.ui.return_button_edit = CustomReturnButton(self.ui, self.ui.frame_return_edit,
                                                           self.ui.ui_pages.page_edit_rover, "return_button_edit")

        self.ui.return_edit_layout.addWidget(self.ui.return_button_edit)
        self.ui.edit_container_layout.addWidget(self.ui.frame_return_edit)
        self.ui.ui_pages.page_edit_rover_layout.addWidget(self.ui.edit_container_frame)

        # Central frame
        self.ui.central_frame_page_edit_rover = QFrame(self.ui.edit_container_frame)
        self.ui.central_frame_page_edit_rover.setObjectName(u"central_frame_page_edit_rover")
        self.ui.central_frame_page_edit_rover.setFrameShape(QFrame.StyledPanel)
        self.ui.central_frame_page_edit_rover.setFrameShadow(QFrame.Raised)
        self.ui.central_frame_page_edit_rover.setMinimumSize(QSize(600, 600))
        self.ui.central_frame_page_edit_rover.setMaximumSize(QSize(600, 600))
        # Central layout
        self.ui.central_layout_page_edit_rover = QVBoxLayout(self.ui.central_frame_page_edit_rover)
        self.ui.central_layout_page_edit_rover.setObjectName(u"central_layout_page_edit_rover")

        # Label edit rover title
        self.ui.edit_rover_label = QLabel(self.ui.central_frame_page_edit_rover)
        self.ui.edit_rover_label.setObjectName(u"edit_rover_label")
        self.ui.edit_rover_label.setText("Edit the rover")
        self.ui.edit_rover_label.setMinimumSize(QSize(0, 35))
        self.ui.edit_rover_label.setMaximumSize(QSize(16777215, 35))
        self.ui.edit_rover_label.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
                                               "color:rgb(255, 255, 255);")
        # Adding label edit rover
        self.ui.central_layout_page_edit_rover.addWidget(self.ui.edit_rover_label)
        # Creating the form
        self.ui.grid_layout_name_edit = self.add_name_grid_layout(grid_layout_name="grid_layout_name_edit",
                                                                  label_name="name_edit_label",
                                                                  error_label_name="name_edit_error_label",
                                                                  text_label="Rover's name:",
                                                                  line_edit_name="name_edit",
                                                                  line_edit_type="string", width_label=225)
        self.ui.grid_layout_bat_edit = self.add_bat_grid_layout(grid_layout_name="grid_layout_bat_edit",
                                                                label_name="bat_edit_label",
                                                                error_label_name="bat_edit_error_label",
                                                                text_label="Battery capacity (Wh):",
                                                                line_edit_name="bat_edit",
                                                                line_edit_type="float", width_label=225)
        self.ui.grid_layout_trans_sp_edit = self.add_trans_sp_grid_layout(
            grid_layout_name="grid_layout_trans_sp_edit",
            label_name="trans_sp_edit_label",
            error_label_name="trans_sp_edit_error_label",
            text_label="Translate speed (m/min):",
            line_edit_name="trans_sp_edit",
            line_edit_type="float", width_label=225)
        self.ui.grid_layout_trans_bat_edit = self.add_trans_bat_grid_layout(
            grid_layout_name="grid_layout_trans_bat_edit",
            label_name="trans_bat_edit_label",
            error_label_name="trans_bat_edit_error_label",
            text_label="Translate battery discharge (W):",
            line_edit_name="trans_bat_edit",
            line_edit_type="float", width_label=225)
        self.ui.grid_layout_exp_sp_edit = self.add_exp_sp_grid_layout(grid_layout_name="grid_layout_exp_sp_edit",
                                                                      label_name="exp_sp_edit_label",
                                                                      error_label_name="exp_sp_edit_error_label",
                                                                      text_label="Exploration speed (m/min):",
                                                                      line_edit_name="exp_sp_edit",
                                                                      line_edit_type="float", width_label=225)
        self.ui.grid_layout_exp_bat_edit = self.add_exp_bat_grid_layout(grid_layout_name="grid_layout_exp_bat_edit",
                                                                        label_name="exp_bat_edit_label",
                                                                        error_label_name="exp_bat_edit_error_label",
                                                                        text_label="Exploration battery discharge (W):",
                                                                        line_edit_name="exp_bat_edit",
                                                                        line_edit_type="float", width_label=225)
        self.ui.grid_layout_ch_time_edit = self.add_ch_time_grid_layout(grid_layout_name="grid_layout_ch_time_edit",
                                                                        label_name="ch_time_edit_label",
                                                                        error_label_name="ch_time_edit_error_label",
                                                                        text_label="Recharging time (minutes):",
                                                                        line_edit_name="ch_time_edit",
                                                                        line_edit_type="float", width_label=225)
        self.ui.central_layout_page_edit_rover.addLayout(self.ui.grid_layout_name_edit)
        self.ui.central_layout_page_edit_rover.addLayout(self.ui.grid_layout_bat_edit)
        self.ui.central_layout_page_edit_rover.addLayout(self.ui.grid_layout_trans_sp_edit)
        self.ui.central_layout_page_edit_rover.addLayout(self.ui.grid_layout_trans_bat_edit)
        self.ui.central_layout_page_edit_rover.addLayout(self.ui.grid_layout_exp_sp_edit)
        self.ui.central_layout_page_edit_rover.addLayout(self.ui.grid_layout_exp_bat_edit)
        self.ui.central_layout_page_edit_rover.addLayout(self.ui.grid_layout_ch_time_edit)
        self.ui.gridLayout_edit_button = QGridLayout()
        self.ui.gridLayout_edit_button.setObjectName(u"gridLayout_edit_button")
        self.ui.horizontalSpacer_edit = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.ui.gridLayout_edit_button.addItem(self.ui.horizontalSpacer_edit, 0, 0, 1, 1)
        self.ui.editButton = QPushButton(self.ui.central_frame_page_edit_rover)
        self.ui.editButton.setObjectName(u"editButton")
        self.ui.editButton.setMinimumSize(QSize(60, 35))
        self.ui.editButton.setMaximumSize(QSize(60, 35))
        self.ui.editButton.setText("Edit")
        self.ui.editButton.setStyleSheet(u"QPushButton{\n"
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
        self.ui.gridLayout_edit_button.addWidget(self.ui.editButton, 0, 1, 1, 1)
        self.ui.central_layout_page_edit_rover.addLayout(self.ui.gridLayout_edit_button)
        self.ui.ui_pages.page_edit_rover_layout.addWidget(self.ui.central_frame_page_edit_rover, 0, Qt.AlignHCenter)

    def add_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                        line_edit_type, width_label):

        grid_layout = self.edit_generic_layout(grid_layout_name)
        # Add label
        label_ex = CustomLabel(parent=self.ui.central_frame_page_edit_rover, name=label_name, text=text_label,
                               width_label=width_label)

        label_error = CustomLabelError(parent=self.ui.central_frame_page_edit_rover, name=error_label_name, text="")
        # Add lineEdit
        widget_ex = CustomLineEdit(parent=self.ui.central_frame_page_edit_rover, lineEdit_name=line_edit_name,
                                   label_error=label_error, line_edit_type=line_edit_type)
        grid_layout.addWidget(label_ex, 0, 0)
        grid_layout.addWidget(widget_ex, 0, 1)
        grid_layout.addWidget(label_error, 1, 0)
        return grid_layout

    def add_bat_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                            line_edit_type, width_label):
        grid_layout = self.edit_generic_layout(grid_layout_name)
        # Add label
        self.ui.bat_edit_label = CustomLabel(parent=self.ui.central_frame_page_edit_rover, name=label_name,
                                             text=text_label,
                                             width_label=width_label)
        # Add error label
        self.ui.bat_edit_error_label = CustomLabelError(parent=self.ui.central_frame_page_edit_rover,
                                                        name=error_label_name, text="")
        # Add lineEdit
        self.ui.bat_edit_line_edit = CustomLineEdit(parent=self.ui.central_frame_page_edit_rover,
                                                    lineEdit_name=line_edit_name,
                                                    label_error=self.ui.bat_edit_error_label,
                                                    line_edit_type=line_edit_type)

        grid_layout.addWidget(self.ui.bat_edit_label, 0, 0)
        grid_layout.addWidget(self.ui.bat_edit_line_edit, 0, 1)
        grid_layout.addWidget(self.ui.bat_edit_error_label, 1, 0)
        return grid_layout

    def add_ch_time_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                                line_edit_type, width_label):
        grid_layout = self.edit_generic_layout(grid_layout_name)
        # Add label
        self.ui.ch_time_edit_label = CustomLabel(parent=self.ui.central_frame_page_edit_rover, name=label_name,
                                                 text=text_label,
                                                 width_label=width_label)
        # Add error label
        self.ui.ch_time_edit_error_label = CustomLabelError(parent=self.ui.central_frame_page_edit_rover,
                                                            name=error_label_name, text="")
        # Add lineEdit
        self.ui.ch_time_edit_line_edit = CustomLineEdit(parent=self.ui.central_frame_page_edit_rover,
                                                        lineEdit_name=line_edit_name,
                                                        label_error=self.ui.ch_time_edit_error_label,
                                                        line_edit_type=line_edit_type)

        grid_layout.addWidget(self.ui.ch_time_edit_label, 0, 0)
        grid_layout.addWidget(self.ui.ch_time_edit_line_edit, 0, 1)
        grid_layout.addWidget(self.ui.ch_time_edit_error_label, 1, 0)
        return grid_layout

    def add_exp_sp_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                               line_edit_type, width_label):
        grid_layout = self.edit_generic_layout(grid_layout_name)
        # Add label
        self.ui.exp_sp_edit_label = CustomLabel(parent=self.ui.central_frame_page_edit_rover, name=label_name,
                                                text=text_label,
                                                width_label=width_label)
        # Add error label
        self.ui.exp_sp_edit_error_label = CustomLabelError(parent=self.ui.central_frame_page_edit_rover,
                                                           name=error_label_name, text="")
        # Add lineEdit
        self.ui.exp_sp_edit_line_edit = CustomLineEdit(parent=self.ui.central_frame_page_edit_rover,
                                                       lineEdit_name=line_edit_name,
                                                       label_error=self.ui.exp_sp_edit_error_label,
                                                       line_edit_type=line_edit_type)

        grid_layout.addWidget(self.ui.exp_sp_edit_label, 0, 0)
        grid_layout.addWidget(self.ui.exp_sp_edit_line_edit, 0, 1)
        grid_layout.addWidget(self.ui.exp_sp_edit_error_label, 1, 0)
        return grid_layout

    def add_exp_bat_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                                line_edit_type, width_label):

        grid_layout = self.edit_generic_layout(grid_layout_name)
        # Add label
        self.ui.exp_bat_edit_label = CustomLabel(parent=self.ui.central_frame_page_edit_rover, name=label_name,
                                                 text=text_label,
                                                 width_label=width_label)
        # Add error label
        self.ui.exp_bat_edit_error_label = CustomLabelError(parent=self.ui.central_frame_page_edit_rover,
                                                            name=error_label_name, text="")
        # Add lineEdit
        self.ui.exp_bat_edit_line_edit = CustomLineEdit(parent=self.ui.central_frame_page_edit_rover,
                                                        lineEdit_name=line_edit_name,
                                                        label_error=self.ui.exp_bat_edit_error_label,
                                                        line_edit_type=line_edit_type)

        grid_layout.addWidget(self.ui.exp_bat_edit_label, 0, 0)
        grid_layout.addWidget(self.ui.exp_bat_edit_line_edit, 0, 1)
        grid_layout.addWidget(self.ui.exp_bat_edit_error_label, 1, 0)
        return grid_layout

    def add_trans_sp_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                                 line_edit_type, width_label):
        grid_layout = self.edit_generic_layout(grid_layout_name)
        # Add label
        self.ui.trans_sp_edit_label = CustomLabel(parent=self.ui.central_frame_page_edit_rover, name=label_name,
                                                  text=text_label,
                                                  width_label=width_label)
        # Add error label
        self.ui.trans_sp_edit_error_label = CustomLabelError(parent=self.ui.central_frame_page_edit_rover,
                                                             name=error_label_name, text="")
        # Add lineEdit
        self.ui.trans_sp_edit_line_edit = CustomLineEdit(parent=self.ui.central_frame_page_edit_rover,
                                                         lineEdit_name=line_edit_name,
                                                         label_error=self.ui.trans_sp_edit_error_label,
                                                         line_edit_type=line_edit_type)

        grid_layout.addWidget(self.ui.trans_sp_edit_label, 0, 0)
        grid_layout.addWidget(self.ui.trans_sp_edit_line_edit, 0, 1)
        grid_layout.addWidget(self.ui.trans_sp_edit_error_label, 1, 0)
        return grid_layout

    def add_trans_bat_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                                  line_edit_type, width_label):

        grid_layout = self.edit_generic_layout(grid_layout_name)
        # Add label
        self.ui.trans_bat_edit_label = CustomLabel(parent=self.ui.central_frame_page_edit_rover, name=label_name,
                                                   text=text_label,
                                                   width_label=width_label)
        # Add error label
        self.ui.trans_bat_edit_error_label = CustomLabelError(parent=self.ui.central_frame_page_edit_rover,
                                                              name=error_label_name, text="")
        # Add lineEdit
        self.ui.trans_bat_edit_line_edit = CustomLineEdit(parent=self.ui.central_frame_page_edit_rover,
                                                          lineEdit_name=line_edit_name,
                                                          label_error=self.ui.trans_bat_edit_error_label,
                                                          line_edit_type=line_edit_type)

        grid_layout.addWidget(self.ui.trans_bat_edit_label, 0, 0)
        grid_layout.addWidget(self.ui.trans_bat_edit_line_edit, 0, 1)
        grid_layout.addWidget(self.ui.trans_bat_edit_error_label, 1, 0)
        return grid_layout

    def add_name_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                             line_edit_type, width_label):

        grid_layout = self.edit_generic_layout(grid_layout_name)
        # Add label
        self.ui.name_edit_label = CustomLabel(parent=self.ui.central_frame_page_edit_rover, name=label_name,
                                              text=text_label,
                                              width_label=width_label)
        # Add error label
        self.ui.name_edit_error_label = CustomLabelError(parent=self.ui.central_frame_page_edit_rover,
                                                         name=error_label_name, text="")
        # Add lineEdit
        self.ui.name_edit_line_edit = CustomLineEdit(parent=self.ui.central_frame_page_edit_rover,
                                                     lineEdit_name=line_edit_name,
                                                     label_error=self.ui.name_edit_error_label,
                                                     line_edit_type=line_edit_type)

        grid_layout.addWidget(self.ui.name_edit_label, 0, 0)
        grid_layout.addWidget(self.ui.name_edit_line_edit, 0, 1)
        grid_layout.addWidget(self.ui.name_edit_error_label, 1, 0)
        return grid_layout

    def edit_generic_layout(self, grid_layout_name):
        grid_layout = QGridLayout(parent=self.ui.central_frame_page_edit_rover)
        grid_layout.setObjectName(grid_layout_name)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setAlignment(Qt.AlignTop)
        return grid_layout
