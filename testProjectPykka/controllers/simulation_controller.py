from PySide6.QtCore import QSize
from PySide6.QtGui import QFocusEvent
from PySide6.QtWidgets import *
from rover1 import RoverModel, State1
import repositories.RoversRepository as rovers
from components import *


class SimulatePageController(QWidget):

    def __init__(self, parent=None, ui=None):
        super().__init__(parent)
        self.ui = ui
        self.rovers_selected = False

        found = self.ui.fr_sim_widgets_layout.findChild(QGridLayout, "grid_layout_height")
        if found is None:
            self.create_widgets_sim_fields()

        # Populate page simulation
        self.populate_num_rovers()
        self.populate_num_jobs()
        self.populate_cb_rovers()

        # Hide max_time
        self.hide_max_time()
        # Hide max_area
        self.hide_max_area()

        self.ui.radioButton_max_area.toggled.connect(self.show_rb_max_area)
        self.ui.radioButton_max_time.toggled.connect(self.show_rb_max_time)

        # Add button
        self.ui.add_rover_select_btn.clicked.connect(self.add_rovers_simulation)
        self.rovers_simulation_selected = {}
        self.rovers_simulate = []
        self.text_to_add = ""

        # Add functionality to button simulate
        self.ui.button_simulate.clicked.connect(self.simulate)

    def create_widgets_sim_fields(self):
        self.ui.grid_layout_height = self.add_height_grid_layout(grid_layout_name="grid_layout_height",
                                                          label_name="height_label",
                                                          error_label_name="height_error_label",
                                                          text_label="Height (m):", line_edit_name="height",
                                                          line_edit_type="float")
        self.ui.grid_layout_observation_rad = self.add_radio_grid_layout(grid_layout_name="grid_layout_observation_rad",
                                                                   label_name="rad_label",
                                                                   error_label_name="rad_error_label",
                                                                   text_label="Observation radio (m):",
                                                                   line_edit_name="obv_rad", line_edit_type="float")
        # Add a widget to contain each layout
        # Hide the widget corresponding to the mode chosen with the radio buttons
        self.ui.max_time_container = QWidget(parent=self.ui.frame_simulation_widgets)
        self.ui.grid_layout_max_time = self.add_max_time_grid_layout(grid_layout_name="grid_layout_max_time",
                                                            label_name="max_time_label",
                                                            error_label_name="max_time_error_label",
                                                            text_label="Maximum time (s):", line_edit_name="max_time"
                                                            , line_edit_type="int")
        self.ui.max_time_container.setObjectName("max_time_container")
        self.ui.max_time_container.setLayout(self.ui.grid_layout_max_time)
        self.ui.cave_width_container = QWidget(parent=self.ui.frame_simulation_widgets)
        self.ui.grid_layout_cave_width = self.add_cave_width_grid_layout(grid_layout_name="grid_layout_cave_width",
                                                              label_name="cave_width_label",
                                                              error_label_name="cave_width_error_label",
                                                              text_label="Cave width (m):", line_edit_name="cave_width",
                                                              line_edit_type="float")
        self.ui.max_time_container.setObjectName("max_area_container")
        self.ui.cave_width_container.setLayout(self.ui.grid_layout_cave_width)
        self.ui.fr_sim_widgets_layout.addLayout(self.ui.grid_layout_height)
        self.ui.fr_sim_widgets_layout.addLayout(self.ui.grid_layout_observation_rad)
        self.ui.fr_sim_widgets_layout.addWidget(self.ui.max_time_container)
        self.ui.fr_sim_widgets_layout.addWidget(self.ui.cave_width_container)
        self.verticalSpacer_sim = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.ui.fr_sim_widgets_layout.addItem(self.verticalSpacer_sim)

    def add_cave_width_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                        line_edit_type, width_label=150):

        grid_layout = self.create_generic_layout(grid_layout_name)
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
                                                     label_error=self.ui.radio_sim_error_label,
                                                     line_edit_type=line_edit_type)

        grid_layout.addWidget(self.ui.cave_width_sim_label, 0, 0)
        grid_layout.addWidget(self.ui.cave_width_sim_line_edit, 0, 1)
        grid_layout.addWidget(self.ui.cave_width_sim_error_label, 1, 0)
        return grid_layout

    def add_max_time_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                        line_edit_type, width_label=150):

        grid_layout = self.create_generic_layout(grid_layout_name)
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
                                                     label_error=self.ui.radio_sim_error_label,
                                                     line_edit_type=line_edit_type)

        grid_layout.addWidget(self.ui.max_time_sim_label, 0, 0)
        grid_layout.addWidget(self.ui.max_time_sim_line_edit, 0, 1)
        grid_layout.addWidget(self.ui.max_time_sim_error_label, 1, 0)
        return grid_layout

    def add_radio_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                        line_edit_type, width_label=150):

        grid_layout = self.create_generic_layout(grid_layout_name)
        # Add label
        self.ui.radio_sim_label = CustomLabel(parent=self.ui.frame_simulation_widgets, name=label_name,
                                              text=text_label,
                                              width_label=width_label)
        # Add error label
        self.ui.radio_sim_error_label = CustomLabelError(parent=self.ui.frame_simulation_widgets,
                                                         name=error_label_name, text="")
        # Add lineEdit
        self.ui.radio_sim_line_edit = CustomLineEdit(parent=self.ui.frame_simulation_widgets,
                                                     lineEdit_name=line_edit_name,
                                                     label_error=self.ui.radio_sim_error_label,
                                                     line_edit_type=line_edit_type)

        grid_layout.addWidget(self.ui.radio_sim_label, 0, 0)
        grid_layout.addWidget(self.ui.radio_sim_line_edit, 0, 1)
        grid_layout.addWidget(self.ui.radio_sim_error_label, 1, 0)
        return grid_layout

    def add_height_grid_layout(self, grid_layout_name, label_name, text_label, error_label_name, line_edit_name,
                        line_edit_type, width_label=150):

        grid_layout = self.create_generic_layout(grid_layout_name)
        # Add label
        self.ui.height_sim_label = CustomLabel(parent=self.ui.frame_simulation_widgets, name=label_name, text=text_label,
                               width_label=width_label)
        # Add error label
        self.ui.height_sim_error_label = CustomLabelError(parent=self.ui.frame_simulation_widgets, name=error_label_name, text="")
        # Add lineEdit
        self.ui.height_sim_line_edit = CustomLineEdit(parent=self.ui.frame_simulation_widgets, lineEdit_name=line_edit_name,
                                   label_error=self.ui.height_sim_error_label, line_edit_type=line_edit_type)

        grid_layout.addWidget(self.ui.height_sim_label, 0, 0)
        grid_layout.addWidget(self.ui.height_sim_line_edit, 0, 1)
        grid_layout.addWidget(self.ui.height_sim_error_label, 1, 0)
        return grid_layout

    def create_generic_layout(self, grid_layout_name):
        grid_layout = QGridLayout(parent=self.ui.frame_simulation_widgets)
        grid_layout.setObjectName(grid_layout_name)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setAlignment(Qt.AlignTop)
        return grid_layout

    def hide_max_area(self):
        self.ui.cave_width_container.setHidden(True)

    def hide_max_time(self):
        self.ui.max_time_container.setHidden(True)

    def populate_cb_rovers(self):
        # Clearing selection
        self.ui.cb_rovers.clear()
        # Filling combobox rovers
        list_name_rovers = rovers.get_rovers_names()
        list_names_str = []
        for name in list_name_rovers:
            list_names_str.append(name[0])
        self.ui.cb_rovers.addItems(
            list(map(str, list_names_str))
        )

    def populate_num_jobs(self):
        # Filling combobox num of jobs
        list_num = list(range(1, 11))
        self.ui.cb_num_jobs.addItems(
            list(map(str, list_num))
        )

    def populate_num_rovers(self):
        # Filling combobox num of rovers
        list_num = list(range(1, 11))
        self.ui.cb_num_rovers.addItems(
            list(map(str, list_num))
        )

    def show_rb_max_area(self):
        self.ui.cave_width_container.setHidden(False)
        self.hide_max_time()


    def show_rb_max_time(self):
        self.ui.max_time_container.setHidden(False)
        self.hide_max_area()


    def add_rovers_simulation(self):
        # TODO
        # getting the rover type (name)
        rover_name = self.ui.cb_rovers.currentText()
        rover = rovers.get_full_rover_by_name(rover_name)
        # getting the number of rovers of that type (combobox numbers)
        rover_num = int(self.ui.cb_num_rovers.currentText())

        for i in range(rover_num):
            self.rovers_simulate.append(rover)

        self.rovers_simulation_selected[rover_name] = rover_num
        # setting the selection to the text line
        text_to_add = "The rovers selected for the simulation are: \n"
        for name_rover, num_rover in self.rovers_simulation_selected.items():
            text_to_add += str(num_rover) + " rovers of the type " + name_rover + "\n"

        self.ui.textEdit_rovers_selected.setText(text_to_add)
        # adding to a list -> Create the rover models and store for simulation
        pass

    def get_fields_simulate(self):

        error_mode = self.check_mode()
        error_num_jobs = self.check_num_jobs()
        error_rovers_selected = self.check_rovers_selected()
        error_height = self.ui.height_sim_line_edit.checkingText()
        error_radio = self.ui.radio_sim_line_edit.checkingText()
        error_max_time = self.ui.max_time_sim_line_edit.checkingText()
        error_cave_width = self.ui.cave_width_sim_line_edit.checkingText()

        if error_mode or error_num_jobs or error_rovers_selected or error_radio or error_height \
                or error_max_time or error_cave_width:
            return True
        return False

    def check_cave_width(self):
        num_job = self.ui.cb_num_jobs.currentText()
        if num_job == "":
            self.ui.lbl_error_num_jobs.setText("Please, select at least one job in order to run the simulation")
            return True
        return False

    def check_max_time(self):
        num_job = self.ui.cb_num_jobs.currentText()
        if num_job == "":
            self.ui.lbl_error_num_jobs.setText("Please, select at least one job in order to run the simulation")
            return True
        return False

    def check_radio(self):
        num_job = self.ui.cb_num_jobs.currentText()
        if num_job == "":
            self.ui.lbl_error_num_jobs.setText("Please, select at least one job in order to run the simulation")
            return True
        return False

    def check_height(self):
        height = self.ui.fr_sim_widgets_layout.findChild(CustomLineEdit, "height_line_edit")
        if height is not None:
            if height.text() == "":
                self.ui.lbl_error_num_jobs.setText("Please, select at least one job in order to run the simulation")
            return True
        return False

    def check_rovers_selected(self):
        if not self.rovers_selected:
            self.ui.lbl_error_rovers_select.setText("Please, select at least one rover to perform the simulation")
            return True
        return False

    def check_num_jobs(self):
        num_job = self.ui.cb_num_jobs.currentText()
        if num_job == "":
            self.ui.lbl_error_num_jobs.setText("Please, select at least one job in order to run the simulation")
            return True
        return False

    def check_mode(self):
        # Check if covered
        mode_max_time = self.ui.radioButton_max_time.isChecked()
        mode_max_area = self.ui.radioButton_max_area.isChecked()
        if not (mode_max_area or mode_max_time):
            self.ui.lbl_error_mode.setText("Select a mode")
            return True
        return False

    def simulate(self):

        # TODO -> chek all fields are filled

        # Add checking of every mandatory field filled
        # If not -> call the MainWindow and write a message in the
        not_filled = self.get_fields_simulate()

        if not_filled:
            self.ui.button_simulate.setEnabled(False)
            dlg = CustomDialog("Error", "Some of the fields are empty or do not have the correct type")
            dlg.exec_()
        else:
            rovers_models = []
            rovers_simulate = self.rovers_simulate

            for i in range(len(rovers_simulate)):
                rover = rovers_simulate[i][i]
                print(rover)
                name_rover = rover[1]
                battery = rover[2]
                translate_speed = rover[3]
                translate_bat = rover[4]
                exp_speed = rover[5]
                exp_bat = rover[6]
                charging_time = rover[7]

                r = RoverModel(battery=battery, state=State1.EXPLORING_STATE, translate_speed=translate_speed,
                               translate_bat=translate_bat, exp_speed=exp_speed, exp_bat=exp_bat,
                               charging_time=charging_time,
                               grid=None, max_time=None,
                               name_rover=name_rover)
                rovers_models.append(r)

            # TODO Add functionality of simulate button self.ui.button_simulate
            # get all data about grid
            height = float(self.ui.height_lineEdit.text())
            observ_rad = float(self.ui.observ_rad_lineEdit.text())
            num_jobs = int(self.ui.cb_num_jobs.currentText())

            max_time = None
            if not self.ui.lineEdit_max_time.text().__eq__(""):
                max_time = float(self.ui.lineEdit_max_time.text())

            cave_wx = None
            if self.ui.cave_width_lineEdit.text() is not None:
                cave_wx = float(self.ui.cave_width_lineEdit.text())

            main = Main(self, observ_rad, height, cave_wx, num_jobs, len(rovers_models), rovers_models, max_time,
                        "name_file")


from main import Main
