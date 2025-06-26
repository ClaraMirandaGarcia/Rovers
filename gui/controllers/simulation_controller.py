import json
import shutil
import random

import matplotlib.patches as mpatches
import numpy as np
from PySide2extn.RoundProgressBar import roundProgressBar
from PySide6 import QtCore
from matplotlib import pyplot as plt

from gui.repositories.DBError import DBError
from scheduler_module.errors_simulation import SimError
from scheduler_module.rover import RoverModel
import gui.repositories.RoversRepository as rovers
import gui.repositories.SimulationsRepository as simulations
import gui.repositories.ParticipateRepository as rovers_sims
from gui.components.components import *


class CreateSimulateController(QWidget):

    def __init__(self, parent=None, ui=None):
        super().__init__(parent)
        self.progress_window = None
        self.ui = ui
        self.rovers_selected = False
        self.parent = parent

        # Populate page_1 simulation
        self.populate_num_rovers()
        self.populate_num_jobs()
        self.populate_cb_rovers()

        self.ui.radioButton_max_area.toggled.connect(self.show_rb_max_area)
        self.ui.radioButton_max_time.toggled.connect(self.show_rb_max_time)

        # Add button
        self.ui.add_rover_select_btn.clicked.connect(self.add_rovers_simulation)
        self.rovers_simulation_selected = {}
        self.rovers_simulate = []
        self.text_to_add = ""

        # Add functionality to button simulate
        self.ui.button_simulate.clicked.connect(self.simulate)

    def populate_cb_rovers(self):
        # Clearing selection
        self.ui.cb_rovers.clear()
        # Filling combobox rovers
        try:
            list_name_rovers = rovers.get_rovers_names()
        except DBError as e:
            dlg = CustomDialog(e.motive, e.message)
            dlg.exec_()
        list_names_str = []

        if list_name_rovers is not None:
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

    def hide_max_area(self):
        self.ui.cave_width_container.setHidden(True)

    def hide_max_time(self):
        self.ui.max_time_container.setHidden(True)

    def add_rovers_simulation(self):

        # getting the rover type (name)
        rover_name = self.ui.cb_rovers.currentText()
        try:
            rover = rovers.get_full_rover_by_name(rover_name)
        except DBError as e:
            dlg = CustomDialog(e.motive, e.message)
            dlg.exec_()

        # getting the number of rovers of that type (combobox numbers)
        rover_num = int(self.ui.cb_num_rovers.currentText())

        # changing the names to avoid repetition #roverExample -> roverExample1, roverExample2, ...
        aux = 0
        for i in range(rover_num):
            rover_aux = list(rover[0])
            if rover_num > 1:
                r_name = rover_aux[1] + "-" + str(aux)
                rover_aux[1] = r_name
                aux += 1

            self.rovers_simulate.append(rover_aux)
            self.rovers_selected = True

        self.rovers_simulation_selected[rover_name] = rover_num
        # setting the selection to the text line
        text_to_add = "The rovers selected for the simulation are: \n"
        for name_rover, num_rover in self.rovers_simulation_selected.items():
            text_to_add += str(num_rover) + " rovers of the type " + name_rover + "\n"

        self.ui.textEdit_rovers_selected.setText(text_to_add)
        pass

    def validate(self):
        error_mode = self.check_mode()
        error_num_jobs = self.check_num_jobs()
        error_rovers_selected = self.check_rovers_selected()
        error_height = self.ui.height_sim_line_edit.checking_text()
        error_radio = self.ui.radio_sim_line_edit.checking_text()
        error_max_time = self.ui.max_time_sim_line_edit.checking_text()
        error_cave_width = self.ui.cave_width_sim_line_edit.checking_text()

        if self.ui.radioButton_max_area.isChecked():
            if error_mode or error_num_jobs or error_rovers_selected or error_radio or error_height \
                    or error_cave_width:
                return False
        elif self.ui.radioButton_max_time.isChecked():
            if error_mode or error_num_jobs or error_rovers_selected or error_radio or error_height \
                    or error_max_time:
                return False
        elif error_mode:
            return False
        return True

    def check_rovers_selected(self):
        if not self.rovers_selected:
            self.ui.lbl_error_rovers_select.setText("Please, select at least one rover to perform the simulation")
            self.ui.lbl_error_rovers_select.setStyleSheet("color : red; ")
            return True
        return False

    def check_num_jobs(self):
        num_job = self.ui.cb_num_jobs.currentText()
        if num_job == "":
            self.ui.lbl_error_num_jobs.setText("Please, select at least one job in order to run the simulation")
            self.ui.lbl_error_num_jobs.setStyleSheet("color : red; ")
            return True
        return False

    def check_mode(self):
        # Check if covered
        mode_max_time = self.ui.radioButton_max_time.isChecked()
        mode_max_area = self.ui.radioButton_max_area.isChecked()
        if not (mode_max_area or mode_max_time):
            self.ui.lbl_error_mode.setText("Select a mode")
            self.ui.lbl_error_mode.setStyleSheet("color : red; ")
            return True
        return False

    def simulate(self):
        # checking of every mandatory field filled
        is_valid = self.validate()
        if not is_valid:
            self.ui.button_simulate.setEnabled(False)
            dlg = CustomDialog("Error", "Some of the fields are empty or do not have the correct type")
            dlg.exec_()
        elif not self.rovers_selected:
            self.ui.button_simulate.setEnabled(False)
            dlg = CustomDialog("Error", "There are no rovers selected")
            dlg.exec_()
        else:
            rovers_models = []
            rovers_simulate = self.rovers_simulate

            for i in range(len(rovers_simulate)):
                rover = rovers_simulate[i]
                name_rover_file = rover[1]
                name_rover = rover[1]
                name_rover = name_rover.split("-")
                name_rover = name_rover[0]
                battery = rover[2]
                translate_speed = rover[3]
                translate_bat = rover[4]
                exp_speed = rover[5]
                exp_bat = rover[6]
                charging_time = rover[7]

                r = RoverModel(battery=battery, state=ExploringState, translate_speed=translate_speed,
                               translate_bat=translate_bat, exp_speed=exp_speed, exp_bat=exp_bat,
                               charging_time=charging_time,
                               grid=None, max_time=None,
                               name_rover=name_rover, name_rover_file=name_rover_file)
                rovers_models.append(r)

            # get all data about grid
            height = float(self.ui.height_sim_line_edit.text())
            observ_rad = float(self.ui.radio_sim_line_edit.text())
            num_jobs = int(self.ui.cb_num_jobs.currentText())

            max_time = None
            if not self.ui.max_time_sim_line_edit.text().__eq__(""):
                max_time = float(self.ui.max_time_sim_line_edit.text())

            cave_wx = None
            if not self.ui.cave_width_sim_line_edit.text().__eq__(""):
                cave_wx = float(self.ui.cave_width_sim_line_edit.text())

            main = SimulationManager(self, observ_rad, height, cave_wx, num_jobs, len(rovers_models), rovers_models,
                                     max_time)

        # clear everything

    def save_simulation(self, resume, queue):
        # get all rovers in simulation

        # inserting the simulation
        try:
            simulations.get_insert_simulation_sql(resume.name, resume.total_time, resume.total_space, resume.num_rovers,
                                                  resume.log_file_name)
            simulation_id = simulations.get_simulation_by_name(resume.name)[0][0]
        except DBError as e:
            self.pop_up_error(e.motive, e.message)

        # inserting the corresponding data into the rovers_simulation data
        queue_id = []
        for r in queue:
            try:
                rover = rovers.get_rover_by_name(r._actor.name_rover)
                rover_id = rover[0][0]
                a = rovers_sims.get_insert_rovers_simulations_sql(rover_id, simulation_id)
            except DBError as e:
                dlg = CustomDialog(e.motive, e.message)
                dlg.exec_()

        self.parent.show_page_simulations()
        pass

    def pop_up(self):
        dlg = CustomDialog("Simulation dialog", "The simulation has finished")
        dlg.exec_()
        pass

    def pop_up_in(self):
        dlg = CustomDialog("Simulation dialog", "The simulation has been initialized")
        dlg.exec_()
        pass

    def pop_up_error(self, motive, message):
        dlg = CustomDialog(motive, message)
        dlg.exec_()
        pass

    def show_window_progress(self):
        self.progress_window = None
        if self.progress_window is None:
            self.progress_window = self.ProgressBarWindow()
        self.progress_window.show()

    def close_window_progress(self):
        self.progress_window.close()
        self.progress_window = None

    class ProgressBarWindow(QWidget):
        def __init__(self):
            # path to the folder
            super().__init__()
            self.setMinimumSize(QSize(600, 200))
            layout = QVBoxLayout()
            layout.setContentsMargins(50, 50, 50, 50)

            # Lets create a board -> frame with x frames width and y frames length.
            self.progressBarContainer = QFrame()
            self.progressBarContainer.setObjectName(u"progressBarContainer")
            self.progressBarContainer.setFrameShape(QFrame.StyledPanel)
            self.progressBarContainer.setFrameShadow(QFrame.Raised)
            self.verticalLayout_progressBarContainer = QVBoxLayout(self.progressBarContainer)
            self.verticalLayout_progressBarContainer.setObjectName(u"verticalLayout_2")
            self.progressBar = roundProgressBar(self.progressBarContainer)
            self.progressBar.setObjectName(u"progressBar")
            self.progressBar.setMinimumSize(QSize(200, 200))
            self.progressBar.setMaximumSize(QSize(200, 200))
            self.verticalLayout_progressBarContainer.addWidget(self.progressBar, 0, Qt.AlignHCenter | Qt.AlignVCenter)

            self.verticalLayout_progressBarContainer.addWidget(self.progressBarContainer)

            # SET PROGRESS BAR VALUE
            self.progressBar.rpb_setMaximum(420)
            self.progress_val = 0

            # SET PROGRESS BAR STYLE
            self.progressBar.rpb_setBarStyle('Donet')

            # SET PROGRESS BAR LINE COLOR
            self.progressBar.rpb_setLineColor((0, 170, 255))  # ARGUMENT RGB AS A TUPLE

            # CHANGING THE PATH COLOR
            self.progressBar.rpb_setPathColor((255, 30, 99))

            # SET PROGRESS BAR TEXT COLOR
            self.progressBar.rpb_setTextColor((233, 30, 99))  # ARGUMENT RGB AS A TUPLE

            # SET PROGRESS BAR STARTING POSITION
            # North, East, West, South
            self.progressBar.rpb_setInitialPos('West')  # WEST AS STARTING POSITION.

            # SET PROGRESS BAR TEXT TYPE : VALUE OR PERCENTAGE
            # Value, Percentage
            self.progressBar.rpb_setTextFormat('Percentage')

            # SET PROGRESS BAR FONT
            self.progressBar.rpb_setTextFont('Arial')

            # TEXT HIDDEN
            self.progressBar.rpb_enableText(False)

            # SET PROGRESS BAR LINE WIDTH
            self.progressBar.rpb_setLineWidth(10)

            # PATH WIDTH
            self.progressBar.rpb_setPathWidth(15)

            # SET PROGRESS BAR LINE CAP
            # RoundCap, SquareCap
            self.progressBar.rpb_setLineCap('RoundCap')

            layout.addWidget(self.progressBarContainer)
            self.setLayout(layout)
            self.show()
            # LINE STYLE
            # DotLine, DashLine
            self.progressBar.rpb_setLineStyle('DashLine')
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.progress)  # progress function
            self.timer.start(60)

            # Change all progresses to zero on start
            QtCore.QTimer.singleShot(0, lambda: self.progressBar.rpb_setValue(0))

        def progress(self):
            # Set progress values
            self.progressBar.rpb_setValue(self.progress_val)

            # Reset progresses if the maximum value is reached
            if self.progress_val > 420:
                self.progress_val = 0;

            # Increase value every 60 ms
            self.progress_val += 1

        def close_window(self):
            self.close()


class SimulationsPageController(QWidget):

    def __init__(self, parent=None, ui=None):
        super().__init__(parent)
        self.resume_window = None
        self.parent = parent
        self.ui = ui
        self.simulation_id_aux = None
        self.config_table()
        self.fill_table()

        self.ui.ui_pages.search_simulation_lineEdit.returnPressed.connect(self.search_simulation)
        self.ui.ui_pages.search_simulation_lineEdit.textChanged.connect(self.restore_table_data)
        self.ui.ui_pages.search_simulation.clicked.connect(self.search_simulation)
        self.ui.ui_pages.create_simulation_btn.clicked.connect(parent.show_page_simulation)

    def pop_up_error(self, motive, message):
        dlg = CustomDialog(motive, message)
        dlg.exec_()
        pass

    def fill_table(self):
        try:
            data = simulations.get_all_simulations_table()
        except DBError as e:
            self.pop_up_error(e.motive, e.message)
        # if data is empty
        if data is not None:
            self.populate_table(data)
        else:
            pass

    def restore_table_data(self):
        param = self.ui.ui_pages.search_simulation_lineEdit.text()
        # If it is empty restore the table
        if param == "":
            self.fill_table()
        # If it is not empty search and fill the table
        else:
            self.search_simulation_write()

    def config_table(self):
        # 7
        column_labels = ("ID", "NAME", "TOTAL TIME (min)", "TOTAL SPACE (m2)", "NUMBER OF ROVERS", "LOG FILE NAME", "")
        self.ui.ui_pages.table_simulations.setColumnCount(len(column_labels))
        self.ui.ui_pages.table_simulations.setHorizontalHeaderLabels(column_labels)
        self.ui.ui_pages.table_simulations.setColumnWidth(1, 80)
        self.ui.ui_pages.table_simulations.setColumnWidth(2, 180)
        self.ui.ui_pages.table_simulations.setColumnWidth(3, 180)
        self.ui.ui_pages.table_simulations.setColumnWidth(4, 180)
        self.ui.ui_pages.table_simulations.setColumnWidth(5, 180)
        self.ui.ui_pages.table_simulations.setColumnWidth(6, 90)
        self.ui.ui_pages.table_simulations.verticalHeader().setDefaultSectionSize(50)
        self.ui.ui_pages.table_simulations.setColumnHidden(0, True)
        self.ui.ui_pages.table_simulations.setSelectionBehavior(QAbstractItemView.SelectRows)

    def search_simulation(self):
        param = self.ui.ui_pages.search_simulation_lineEdit.text()
        data = None
        if param != "":
            data = simulations.get_simulation_by_name(param)
        self.populate_table(data)

    def search_simulation_write(self):
        param = self.ui.ui_pages.search_simulation_lineEdit.text()
        data = None
        error = False
        if param != "":
            pattern = param + '%'
            try:
                data = simulations.get_simulation_starting_name(pattern)
            except DBError as e:
                error = True
                self.pop_up_error(e.motive, e.message)
        if not error: self.populate_table(data)

    def populate_table(self, data):
        if data is not None:
            self.ui.ui_pages.table_simulations.setRowCount(len(data))

            for (index_row, row) in enumerate(data):
                for (index_cell, cell) in enumerate(row):
                    var = str(cell)
                    if index_cell == 2 or index_cell == 3:
                        var = "{:.2f}".format(cell)
                    item_var = QTableWidgetItem(var)
                    item_var.setFlags(Qt.ItemIsEditable)
                    self.ui.ui_pages.table_simulations.setItem(
                        index_row, index_cell, item_var
                    )

                    self.ui.ui_pages.table_simulations.setCellWidget(
                        index_row, 6, self.build_action_button()
                    )

    def build_action_button(self):
        delete_button = CustomButton("Delete", "rgb(180, 55, 87)")
        self.ui.ref_delete_sim_button = delete_button
        view_button = CustomButton("Summary", "rgb(10, 120, 115)")
        self.ui.ref_view_sim_button = view_button
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(delete_button)
        buttons_layout.addWidget(view_button)

        buttons_frame = QFrame()
        buttons_frame.setLayout(buttons_layout)
        delete_button.clicked.connect(self.delete_simulation)
        view_button.clicked.connect(self.resume_sim)

        return buttons_frame

    def get_simulation_id_table(self, table, button):
        row_index = table.indexAt(button.parent().pos()).row()
        cell_id_index = table.model().index(row_index, 0)
        sim_id = table.model().data(cell_id_index)
        return sim_id

    def get_simulation_path_table(self, table, button):
        row_index = table.indexAt(button.parent().pos()).row()
        cell_path_index = table.model().index(row_index, 5)
        sim_path = table.model().data(cell_path_index)
        return sim_path

    def delete_simulation(self):
        button = self.sender()
        table = self.ui.ui_pages.table_simulations

        if button:
            simulation_id = self.get_simulation_id_table(table, button)
            simulation_path = self.get_simulation_path_table(table, button)
        try:
            exist = rovers_sims.get_rovers_simulations_by_sim_id(simulation_id)

            if len(exist) > 0:
                rovers_sims.delete_rovers_simulations_by_sim_id(simulation_id)
                access_rights = 0o777
                os.chmod(simulation_path, access_rights)
                try:
                    if not os.path.exists(simulation_path):
                        # error
                        message = "There is no folder matching the deleted simulation"
                        error = SimError("Directory deletion error", message)
                        self.pop_up_error(error.get_motive(), error.get_message())
                    else:
                        # delete
                        shutil.rmtree(simulation_path)
                except OSError:
                    message = "Deletion of the directory failed"
                    error = SimError("Directory deletion error", message)
                    self.pop_up_error(error.get_motive(), error.get_message())

            if simulations.delete_simulation(simulation_id):
                self.fill_table()
        except DBError as e:
            self.pop_up_error(e.motive, e.message)

    def resume_sim(self):
        button = self.sender()
        table = self.ui.ui_pages.table_simulations

        if button:
            simulation_id = self.get_simulation_id_table(table, button)
            simulation_path = self.get_simulation_path_table(table, button)

        try:
            exist = rovers_sims.get_rovers_simulations_by_sim_id(simulation_id)
            if len(exist) > 0:
                self.show_window_resume(simulation_path)

        except DBError as e:
            self.pop_up_error(e.motive, e.message)

    def show_window_resume(self, simulation_path):
        self.resume_window = None
        if self.resume_window is None:
            self.resume_window = self.ResumePageController(simulation_path)
        # self.resume_window.show()
        self.resume_window.read_file()

    class ResumePageController(QWidget):
        def __init__(self, simulation_path):
            # path to the folder
            super().__init__()
            self.setMinimumSize(QSize(600, 200))
            layout = QVBoxLayout()
            layout.setContentsMargins(50, 50, 50, 50)

            # Setting title label
            self.title_label = QLabel("Simulation graphic saved in: " + simulation_path)
            layout.addWidget(self.title_label)
            # Aux frame containing left axis and board
            frame_aux0 = QFrame(self)
            layout_aux0 = QHBoxLayout(frame_aux0)
            # Creating the frame and the axis
            frame_axis = QFrame(frame_aux0)
            layout_axis_x = QVBoxLayout(frame_axis)
            layout.addWidget(frame_aux0)
            self.setLayout(layout)
            self.sim_path = simulation_path

        def read_file(self):

            contents = self.get_contents_file()

            len_x = contents["len_x"]
            len_y = contents["len_y"]

            cells = []
            # Iterating through the json
            for i in contents['cells_data']:
                cells.append(i)

            matrix = np.random.randint(0, 1, size=(len_x + 1, len_y + 1))

            # getting coordinates and different rovers
            coor_dict, coordinates, rovers, size, non_explored_coordinates = self.get_data(cells)

            side = np.sqrt(size)
            matrix = np.random.randint(0, 1, size=(len_x, len_y))
            fig, ax = plt.subplots()

            # representing each coordinate explored
            self.plot_explored_coordinates(fig, ax, coor_dict, matrix, non_explored_coordinates)
            self.plot_axis(ax, len_x, len_y, side)

        def plot_explored_coordinates(self, fig, ax, coor_dict, matrix, non_explored_coordinates):
            rovers = coor_dict.keys()
            vals = np.linspace(0, 1, 256)
            np.random.shuffle(vals)
            cmap = plt.cm.colors.ListedColormap(plt.cm.jet(vals))
            num = 0
            hm = np.zeros_like(matrix)

            rovers_array = []
            for r in rovers:
                # plot each array of coordinates
                coordinates = coor_dict[r]
                highlight = np.array(coordinates)
                hm[highlight[:, 1], highlight[:, 0]] = num
                num = num + 1
                rovers_array.append(r)

            if len(non_explored_coordinates) > 0:
                rovers_array.append("Unexplored")
                highlight = np.array(non_explored_coordinates)
                hm[highlight[:, 1], highlight[:, 0]] = num
            # add to the hm matrix the unexplored cells ?
            values = np.unique(hm.ravel())
            im = ax.matshow(hm, origin='lower', alpha=1, vmin=0.5, vmax=len(rovers) + 1, cmap=cmap)
            colors = [im.cmap(im.norm(value)) for value in values]
            for i in range(len(values)):
                x = values[i]
                asdf = rovers_array[values[i]]
            patches = [mpatches.Patch(color=colors[i], label=("Rover: "+str(rovers_array[values[i]]))) for i in range(len(values))]
            plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

        def plot_non_explored(self, ax, non_explored_coordinates, matrix):
            hm = np.zeros_like(matrix)
            highlight = np.array(non_explored_coordinates)
            hm[highlight[:, 1], highlight[:, 0]] = 99
            ax.matshow(hm, origin='lower', alpha=0.7, vmin=0.5, vmax=1, cmap="Blues")

        def plot_axis(self, ax, len_x, len_y, side):
            ax.set_xticks([], minor=False)
            aux_x = np.arange(-.5, len_y, 1)
            ax.set_xticks(aux_x, minor=True)
            ax.set_yticks([], minor=False)
            aux_y = np.arange(-.5, len_x, 1)
            ax.set_yticks(aux_y, minor=True)
            ax.set_xticklabels([], minor=False)
            aux_xtick = np.arange(0, (len_y + 1) * side, side)
            new_aux_xtick = []
            for element in aux_xtick:
                new_aux_xtick.append(round(element, 2))
            ax.set_xticklabels(new_aux_xtick, minor=True)
            ax.set_yticklabels([], minor=False)
            aux_ytick = np.arange(0, (len_x + 1) * side, side)
            new_aux_ytick = []
            for element in aux_ytick:
                new_aux_ytick.append(round(element, 2))
            ax.set_yticklabels(new_aux_ytick, minor=True)
            ax.xaxis.set_ticks_position('bottom')
            ax.grid(which='minor', color='black', linestyle='-', linewidth=1)
            ax.set_title('Explored space')
            plt.ylabel("Length (m)",
                       size=14)
            plt.xlabel("Width (m)",
                       size=14)
            plt.show()

        def get_data(self, cells):
            rover = None
            coordinates_dict = {}
            coordinates = []
            non_explored_coordinates = []
            rovers = []
            size = None
            for cell in cells:
                # {"location": "Coordinate({'y': 0, 'x': 0})", "area": 3.9925140100115266, "explored": true}
                # dict {'y': 0, 'x': 0}
                is_explored = cell["explored"]
                # Pasa algo con el punto de carga

                if cell["rover"] is not None:
                    rover = cell["rover"]
                elif is_explored:
                    rover = "Charge Point"

                size = cell["size"]
                if rover not in rovers and rover is not None:
                    rovers.append(rover)
                    coordinates_dict[rover] = []

                if is_explored:
                    coor = cell["location"]
                    coordinates.append(coor)
                    coordinates_dict[rover].append(coor)
                else:
                    coor_n = cell["location"]
                    non_explored_coordinates.append(coor_n)
                rover = None
            return coordinates_dict, coordinates, rovers, size, non_explored_coordinates

        def get_contents_file(self):
            name_file = self.sim_path + "\\resume.txt.json"
            with open(name_file, 'r') as j:
                contents = json.loads(j.read())
            return contents

        @staticmethod
        def generate_colors(num_colors):
            colors = []
            num_selected = 0
            while num_selected < num_colors:
                # hexadecimal
                # rand_colors = ["#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                rand_colors = [r, g, b]
                if rand_colors not in colors:
                    colors.append(rand_colors)
                    num_selected = num_selected + 1
            return colors


from scheduler_module.simulation_manager import SimulationManager
from scheduler_module.state.exploringState import ExploringState
