from PySide6.QtWidgets import *
from components import *


class SimulatePageView(QWidget):

    def __init__(self, parent=None, ui=None):
        super().__init__(parent)
        self.ui = ui

        grid_layout_height = self.add_grid_layout(label_name="height_label", error_label_name="height_error_label",
                                                  text_label="Height (m):", line_edit_name="height")
        grid_layout_observation_rad = self.add_grid_layout(label_name="rad_label", error_label_name="rad_error_label",
                                                           text_label="Observation radio (m):",
                                                           line_edit_name="obv_rad")
        grid_layout_max_time = self.add_grid_layout(label_name="max_time_label",
                                                    error_label_name="max_time_error_label",
                                                    text_label="Maximum time (s):", line_edit_name="max_time")
        grid_layout_cave_width = self.add_grid_layout(label_name="cave_width_label",
                                                      error_label_name="cave_width_error_label",
                                                      text_label="Cave width (m):", line_edit_name="cave_width")

        self.ui.fr_sim_widgets_layout.addLayout(grid_layout_height)
        self.ui.fr_sim_widgets_layout.addLayout(grid_layout_observation_rad)
        self.ui.fr_sim_widgets_layout.addLayout(grid_layout_max_time)
        self.ui.fr_sim_widgets_layout.addLayout(grid_layout_cave_width)

        # Populate page simulation
        self.populate_num_rovers()
        self.populate_num_jobs()
        self.populate_cb_rovers()

        # Hide max_time
        self.hide_max_time()
        # Hide max_area
        self.hide_max_area()

        # self.ui.radioButton_max_area.toggled.connect(self.show_rb_max_area)
        # self.ui.radioButton_max_time.toggled.connect(self.show_rb_max_time)

        self.rovers_simulation_selected = {}
        self.rovers_simulate = []
        self.text_to_add = ""

    def add_grid_layout(self, label_name, text_label, error_label_name, line_edit_name):
        grid_layout_height = QGridLayout(parent=self.ui.frame_simulation_widgets)
        # Add label
        label_ex = CustomLabel(parent=self.ui.frame_simulation_widgets, name=label_name, text=text_label)
        label_error = CustomLabelError(parent=self.ui.frame_simulation_widgets, name=error_label_name, text="")
        # Add lineEdit
        widget_ex = CustomLineEdit(parent=self.ui.frame_simulation_widgets, lineEdit_name=line_edit_name,
                                   label_error=label_error)
        grid_layout_height.addWidget(label_ex, 0, 0)
        grid_layout_height.addWidget(widget_ex, 0, 1)
        grid_layout_height.addWidget(label_error, 1, 0)
        return grid_layout_height

    def hide_max_area(self):
        self.ui.label_cave_width.setHidden(True)
        self.ui.cave_width_lineEdit.setHidden(True)
        self.ui.lbl_error_cave_width.setHidden(True)

    def hide_max_time(self):
        lbl = self.ui.fr_sim_widgets_layout.findChild(QLabel, "max_time_label")
        lbl_error = self.ui.fr_sim_widgets_layout.findChild(QLabel, "max_time_error_label")
        line_edit = self.ui.fr_sim_widgets_layout.findChild(QLineEdit, "max_time_line_edit")

        lbl.setHidden(True)
        lbl_error.setHidden(True)
        line_edit.setHidden(True)

    def show_rb_max_area(self):
        self.ui.label_cave_width.setHidden(False)
        self.ui.cave_width_lineEdit.setHidden(False)
        self.ui.lbl_error_cave_width.setHidden(False)
        self.hide_max_time()
        pass

    def show_rb_max_time(self):
        self.ui.label_max_time.setHidden(False)
        self.ui.lineEdit_max_time.setHidden(False)
        self.ui.lbl_error_max_time.setHidden(False)
        self.hide_max_area()
        pass

    def get_fields_simulate(self):
        # TODO get all fields
        message = ""
        mode_max_time = self.ui.radioButton_max_time.isChecked()
        mode_max_area = self.ui.radioButton_max_area.isChecked()

        height = self.ui.height_lineEdit.text()
        radio = self.ui.observ_rad_lineEdit.text()

        max_time = self.ui.lineEdit_max_time.text()
        cave_width = self.ui.cave_width_lineEdit.text()

        num_job = self.ui.cb_num_jobs.currentText()
        rovers_selected = False

        # Check if covered
        if not (mode_max_area or mode_max_time):
            message = "Please, select one of the available modes for the simulation"
            return True, message

        if height == "":
            message = "Please, select the approximate height of the cave to explore"
            return True, message

        if radio == "":
            message = "Please, select the observation radio of the rover"
            return True, message

        if num_job == "":
            message = "Please, select at least one job in order to run the simulation"
            return True, message

        if not rovers_selected:
            message = "Please, select at least one rover to perform the simulation"
            return True, message

        pass

    def simulate(self):

        # TODO -> chek all fields are filled

        # Add checking of every mandatory field filled
        # If not -> call the MainWindow and write a message in the
        not_filled, message = self.get_fields_simulate()

        if not_filled:
            print("There is a problem ma love")
            print(message)


from main import Main
