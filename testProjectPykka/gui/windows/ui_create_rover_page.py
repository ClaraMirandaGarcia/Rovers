from PySide6.QtWidgets import *

from components import *


class CreateRoverPageView(QWidget):
    def __init__(self, parent=None, ui=None):
        super().__init__(parent)
        self.ui = ui

        # check if create page view is created
        page_view_edit = self.ui.page_create_rover.findChild(QFrame, "central_frame_page_edit_rover")
        if page_view_edit is not None:
            page_view_edit.setHidden(True)
        obj = self.ui.page_create_rover.findChild(QFrame, "central_frame_page_create_rover")
        if obj is None:
            self.initialize_gui()


    def initialize_gui(self):
        # Central frame
        self.ui.central_frame_page_create_rover = QFrame(self.ui.page_create_rover)
        self.ui.central_frame_page_create_rover.setObjectName(u"central_frame_page_create_rover")
        self.ui.central_frame_page_create_rover.setFrameShape(QFrame.StyledPanel)
        self.ui.central_frame_page_create_rover.setFrameShadow(QFrame.Raised)
        self.ui.central_frame_page_create_rover.setMinimumSize(QSize(600, 600))
        self.ui.central_frame_page_create_rover.setMaximumSize(QSize(600, 600))
        # Central layout
        self.ui.central_layout_page_create_rover = QVBoxLayout(self.ui.central_frame_page_create_rover)
        self.ui.central_layout_page_create_rover.setObjectName(u"central_layout_page_create_rover")
        # Label create rover title
        self.ui.create_rover_label = QLabel(self.ui.central_frame_page_create_rover)
        self.ui.create_rover_label.setObjectName(u"create_rover_label")
        self.ui.create_rover_label.setText("Create your own rover")
        self.ui.create_rover_label.setMinimumSize(QSize(0, 35))
        self.ui.create_rover_label.setMaximumSize(QSize(16777215, 35))
        self.ui.create_rover_label.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
                                                 "color:rgb(255, 255, 255);")
        # Adding label create rover
        self.ui.central_layout_page_create_rover.addWidget(self.ui.create_rover_label)
        # Creating the form
        self.ui.grid_layout_name_create = self.add_name_grid_layout(grid_layout_name="grid_layout_name_create",
                                                                    label_name="name_create_label",
                                                                    error_label_name="name_create_error_label",
                                                                    text_label="Rover's name:",
                                                                    line_edit_name="name_create",
                                                                    line_edit_type="string", width_label=225)
        self.ui.grid_layout_bat_create = self.add_bat_grid_layout(grid_layout_name="grid_layout_bat_create",
                                                                  label_name="bat_create_label",
                                                                  error_label_name="bat_create_error_label",
                                                                  text_label="Battery capacity (Wh):",
                                                                  line_edit_name="bat_create",
                                                                  line_edit_type="float", width_label=225)
        self.ui.grid_layout_trans_sp_create = self.add_trans_sp_grid_layout(
            grid_layout_name="grid_layout_trans_sp_create",
            label_name="trans_sp_create_label",
            error_label_name="trans_sp_create_error_label",
            text_label="Translate speed (m/min):",
            line_edit_name="trans_sp_create",
            line_edit_type="float", width_label=225)
        self.ui.grid_layout_trans_bat_create = self.add_trans_bat_grid_layout(
            grid_layout_name="grid_layout_trans_bat_create",
            label_name="trans_bat_create_label",
            error_label_name="trans_bat_create_error_label",
            text_label="Translate battery discharge (W):",
            line_edit_name="trans_bat_create",
            line_edit_type="float", width_label=225)
        self.ui.grid_layout_exp_sp_create = self.add_exp_sp_grid_layout(grid_layout_name="grid_layout_exp_sp_create",
                                                                        label_name="exp_sp_create_label",
                                                                        error_label_name="exp_sp_create_error_label",
                                                                        text_label="Exploration speed (m/min):",
                                                                        line_edit_name="exp_sp_create",
                                                                        line_edit_type="float", width_label=225)
        self.ui.grid_layout_exp_bat_create = self.add_exp_bat_grid_layout(grid_layout_name="grid_layout_exp_bat_create",
                                                                          label_name="exp_bat_create_label",
                                                                          error_label_name="exp_bat_create_error_label",
                                                                          text_label="Exploration battery discharge (W):",
                                                                          line_edit_name="exp_bat_create",
                                                                          line_edit_type="float", width_label=225)
        self.ui.grid_layout_ch_time_create = self.add_ch_time_grid_layout(grid_layout_name="grid_layout_ch_time_create",
                                                                          label_name="ch_time_create_label",
                                                                          error_label_name="ch_time_create_error_label",
                                                                          text_label="Recharging time (minutes):",
                                                                          line_edit_name="ch_time_create",
                                                                          line_edit_type="float", width_label=225)
        self.ui.central_layout_page_create_rover.addLayout(self.ui.grid_layout_name_create)
        self.ui.central_layout_page_create_rover.addLayout(self.ui.grid_layout_bat_create)
        self.ui.central_layout_page_create_rover.addLayout(self.ui.grid_layout_trans_sp_create)
        self.ui.central_layout_page_create_rover.addLayout(self.ui.grid_layout_trans_bat_create)
        self.ui.central_layout_page_create_rover.addLayout(self.ui.grid_layout_exp_sp_create)
        self.ui.central_layout_page_create_rover.addLayout(self.ui.grid_layout_exp_bat_create)
        self.ui.central_layout_page_create_rover.addLayout(self.ui.grid_layout_ch_time_create)
        self.ui.gridLayout_create_button = QGridLayout()
        self.ui.gridLayout_create_button.setObjectName(u"gridLayout_create_button")
        self.ui.horizontalSpacer_create = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.ui.gridLayout_create_button.addItem(self.ui.horizontalSpacer_create, 0, 0, 1, 1)
        self.ui.createButton = QPushButton(self.ui.central_frame_page_create_rover)
        self.ui.createButton.setObjectName(u"createButton")
        self.ui.createButton.setMinimumSize(QSize(60, 35))
        self.ui.createButton.setMaximumSize(QSize(60, 35))
        self.ui.createButton.setText("Create")
        self.ui.createButton.setStyleSheet(u"QPushButton{\n"
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
        self.ui.gridLayout_create_button.addWidget(self.ui.createButton, 0, 1, 1, 1)
        self.ui.central_layout_page_create_rover.addLayout(self.ui.gridLayout_create_button)
        self.ui.page_create_rover_layout.addWidget(self.ui.central_frame_page_create_rover, 0, Qt.AlignHCenter)

    def add_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                        line_edit_type, width_label):

        grid_layout = self.create_generic_layout(grid_layout_name)
        # Add label
        label_ex = CustomLabel(parent=self.ui.central_frame_page_create_rover, name=label_name, text=text_label,
                               width_label=width_label)

        label_error = CustomLabelError(parent=self.ui.central_frame_page_create_rover, name=error_label_name, text="")
        # Add lineEdit
        widget_ex = CustomLineEdit(parent=self.ui.central_frame_page_create_rover, lineEdit_name=line_edit_name,
                                   label_error=label_error, line_edit_type=line_edit_type)
        grid_layout.addWidget(label_ex, 0, 0)
        grid_layout.addWidget(widget_ex, 0, 1)
        grid_layout.addWidget(label_error, 1, 0)
        return grid_layout

    def add_bat_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                                 line_edit_type, width_label):
        grid_layout = self.create_generic_layout(grid_layout_name)
        # Add label
        self.ui.bat_create_label = CustomLabel(parent=self.ui.central_frame_page_create_rover, name=label_name,
                                                    text=text_label,
                                                    width_label=width_label)
        # Add error label
        self.ui.bat_create_error_label = CustomLabelError(parent=self.ui.central_frame_page_create_rover,
                                                               name=error_label_name, text="")
        # Add lineEdit
        self.ui.bat_create_line_edit = CustomLineEdit(parent=self.ui.central_frame_page_create_rover,
                                                           lineEdit_name=line_edit_name,
                                                           label_error=self.ui.bat_create_error_label,
                                                           line_edit_type=line_edit_type)

        grid_layout.addWidget(self.ui.bat_create_label, 0, 0)
        grid_layout.addWidget(self.ui.bat_create_line_edit, 0, 1)
        grid_layout.addWidget(self.ui.bat_create_error_label, 1, 0)
        return grid_layout

    def add_ch_time_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                                line_edit_type, width_label):
        grid_layout = self.create_generic_layout(grid_layout_name)
        # Add label
        self.ui.ch_time_create_label = CustomLabel(parent=self.ui.central_frame_page_create_rover, name=label_name,
                                                   text=text_label,
                                                   width_label=width_label)
        # Add error label
        self.ui.ch_time_create_error_label = CustomLabelError(parent=self.ui.central_frame_page_create_rover,
                                                              name=error_label_name, text="")
        # Add lineEdit
        self.ui.ch_time_create_line_edit = CustomLineEdit(parent=self.ui.central_frame_page_create_rover,
                                                          lineEdit_name=line_edit_name,
                                                          label_error=self.ui.ch_time_create_error_label,
                                                          line_edit_type=line_edit_type)

        grid_layout.addWidget(self.ui.ch_time_create_label, 0, 0)
        grid_layout.addWidget(self.ui.ch_time_create_line_edit, 0, 1)
        grid_layout.addWidget(self.ui.ch_time_create_error_label, 1, 0)
        return grid_layout

    def add_exp_sp_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                                 line_edit_type, width_label):
        grid_layout = self.create_generic_layout(grid_layout_name)
        # Add label
        self.ui.exp_sp_create_label = CustomLabel(parent=self.ui.central_frame_page_create_rover, name=label_name,
                                                    text=text_label,
                                                    width_label=width_label)
        # Add error label
        self.ui.exp_sp_create_error_label = CustomLabelError(parent=self.ui.central_frame_page_create_rover,
                                                               name=error_label_name, text="")
        # Add lineEdit
        self.ui.exp_sp_create_line_edit = CustomLineEdit(parent=self.ui.central_frame_page_create_rover,
                                                           lineEdit_name=line_edit_name,
                                                           label_error=self.ui.exp_sp_create_error_label,
                                                           line_edit_type=line_edit_type)

        grid_layout.addWidget(self.ui.exp_sp_create_label, 0, 0)
        grid_layout.addWidget(self.ui.exp_sp_create_line_edit, 0, 1)
        grid_layout.addWidget(self.ui.exp_sp_create_error_label, 1, 0)
        return grid_layout

    def add_exp_bat_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                        line_edit_type, width_label):

        grid_layout = self.create_generic_layout(grid_layout_name)
        # Add label
        self.ui.exp_bat_create_label = CustomLabel(parent=self.ui.central_frame_page_create_rover, name=label_name, text=text_label,
                               width_label=width_label)
        # Add error label
        self.ui.exp_bat_create_error_label = CustomLabelError(parent=self.ui.central_frame_page_create_rover, name=error_label_name, text="")
        # Add lineEdit
        self.ui.exp_bat_create_line_edit = CustomLineEdit(parent=self.ui.central_frame_page_create_rover, lineEdit_name=line_edit_name,
                                   label_error=self.ui.exp_bat_create_error_label, line_edit_type=line_edit_type)

        grid_layout.addWidget(self.ui.exp_bat_create_label, 0, 0)
        grid_layout.addWidget(self.ui.exp_bat_create_line_edit, 0, 1)
        grid_layout.addWidget(self.ui.exp_bat_create_error_label, 1, 0)
        return grid_layout

    def add_trans_sp_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                                 line_edit_type, width_label):
        grid_layout = self.create_generic_layout(grid_layout_name)
        # Add label
        self.ui.trans_sp_create_label = CustomLabel(parent=self.ui.central_frame_page_create_rover, name=label_name,
                                                    text=text_label,
                                                    width_label=width_label)
        # Add error label
        self.ui.trans_sp_create_error_label = CustomLabelError(parent=self.ui.central_frame_page_create_rover,
                                                               name=error_label_name, text="")
        # Add lineEdit
        self.ui.trans_sp_create_line_edit = CustomLineEdit(parent=self.ui.central_frame_page_create_rover,
                                                           lineEdit_name=line_edit_name,
                                                           label_error=self.ui.trans_sp_create_error_label,
                                                           line_edit_type=line_edit_type)

        grid_layout.addWidget(self.ui.trans_sp_create_label, 0, 0)
        grid_layout.addWidget(self.ui.trans_sp_create_line_edit, 0, 1)
        grid_layout.addWidget(self.ui.trans_sp_create_error_label, 1, 0)
        return grid_layout

    def add_trans_bat_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                        line_edit_type, width_label):

        grid_layout = self.create_generic_layout(grid_layout_name)
        # Add label
        self.ui.trans_bat_create_label = CustomLabel(parent=self.ui.central_frame_page_create_rover, name=label_name, text=text_label,
                               width_label=width_label)
        # Add error label
        self.ui.trans_bat_create_error_label = CustomLabelError(parent=self.ui.central_frame_page_create_rover, name=error_label_name, text="")
        # Add lineEdit
        self.ui.trans_bat_create_line_edit = CustomLineEdit(parent=self.ui.central_frame_page_create_rover, lineEdit_name=line_edit_name,
                                   label_error=self.ui.trans_bat_create_error_label, line_edit_type=line_edit_type)

        grid_layout.addWidget(self.ui.trans_bat_create_label, 0, 0)
        grid_layout.addWidget(self.ui.trans_bat_create_line_edit, 0, 1)
        grid_layout.addWidget(self.ui.trans_bat_create_error_label, 1, 0)
        return grid_layout

    def add_name_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                        line_edit_type, width_label):

        grid_layout = self.create_generic_layout(grid_layout_name)
        # Add label
        self.ui.name_create_label = CustomLabel(parent=self.ui.central_frame_page_create_rover, name=label_name, text=text_label,
                               width_label=width_label)
        # Add error label
        self.ui.name_create_error_label = CustomLabelError(parent=self.ui.central_frame_page_create_rover, name=error_label_name, text="")
        # Add lineEdit
        self.ui.name_create_line_edit = CustomLineEdit(parent=self.ui.central_frame_page_create_rover, lineEdit_name=line_edit_name,
                                   label_error=self.ui.name_create_error_label, line_edit_type=line_edit_type)

        grid_layout.addWidget(self.ui.name_create_label, 0, 0)
        grid_layout.addWidget(self.ui.name_create_line_edit, 0, 1)
        grid_layout.addWidget(self.ui.name_create_error_label, 1, 0)
        return grid_layout

    def create_generic_layout(self, grid_layout_name):
        grid_layout = QGridLayout(parent=self.ui.central_frame_page_create_rover)
        grid_layout.setObjectName(grid_layout_name)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setAlignment(Qt.AlignTop)
        return grid_layout
