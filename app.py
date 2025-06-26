import sys

from gui.components.components import CustomDialog
import gui.repositories.RoversRepository as rovers
import gui.repositories.SimulationsRepository as simulations
import gui.repositories.ParticipateRepository as rovers_sims
from gui.repositories.DBError import DBError
from gui.windows.ui_main_window import *
# controllers
from gui.controllers.rover_controller import RoversPageController
from gui.controllers.simulation_controller import CreateSimulateController, SimulationsPageController
from gui.windows.ui_rovers_page import RoversPageView
from gui.windows.ui_create_simulation_page import CreateSimulatePageView
from gui.windows.ui_simulations_page import SimulationsPageView


class MainWindow(QMainWindow):
    def __init__(self):

        super().__init__()

        # set up main window
        self.setWindowTitle("Exploring Rovers")
        self.ui = UI_MainWindow()

        # call to the method with self -> parent
        self.ui.setup_ui(self)
        # call the rest of the gui pages
        self.page_simulation = CreateSimulatePageView(self, self.ui.ui_pages)
        self.controller_simulation = CreateSimulateController(self, self.ui.ui_pages)

        self.page_rovers = RoversPageView(self, self.ui.ui_pages)
        self.controller_rovers = RoversPageController(self, self.ui)
        self.page_simulations = SimulationsPageView(self, self.ui.ui_pages)
        self.controller_simulations = SimulationsPageController(self, self.ui)
        self.page_edit_rover = None
        self.controller_edit_rover = None
        self.page_create_rover = None
        self.controller_create_rover = None

        self.closed_menu_width = 50
        self.open_menu_width = 240

        # toggle button animation
        self.ui.toggle_button.clicked.connect(self.toggle_button)
        # Btn home
        self.ui.button_home.clicked.connect(self.show_page_initial)
        # Btn widgets
        self.ui.button_rover_list.clicked.connect(self.show_page_rovers)
        self.ui.button_rover_creation.clicked.connect(self.show_page_create_rover)

        # Btn simulation
        self.ui.button_simulation.clicked.connect(self.show_page_simulation)
        # Btn list simulation
        self.ui.button_simulation_list.clicked.connect(self.show_page_simulations)
        self.show()

    def pop_up(self, title, message):
        dlg = CustomDialog(title, message)
        dlg.exec_()
        pass

    # Btn home function
    def show_page_initial(self):
        self.reset_selection()
        # self.clear_all()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_initial)
        self.ui.button_home.set_active(True)

    def show_page_simulation(self):
        self.reset_selection()
        self.controller_simulation.populate_cb_rovers()
        self.clear_all()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_create_simulation)
        self.ui.button_simulation.set_active(True)

    def show_page_simulations(self):
        self.reset_selection()
        self.clear_all()
        self.controller_simulations.fill_table()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_simulations)
        self.ui.button_simulation_list.set_active(True)

    # Btn widgets function
    def show_page_rovers(self):
        self.reset_selection()
        self.clear_all()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_rovers)
        # self.clear_all()
        self.ui.button_rover_list.set_active(True)

    def show_page_create_rover(self):
        self.reset_selection()
        self.clear_all()
        if self.controller_create_rover is None:
            self.controller_rovers.show_page_create_rover()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_create_rover)
        self.ui.button_rover_creation.set_active(True)
        pass

    def toggle_button(self):
        # Checking the width
        menu_width = self.ui.left_menu.width()
        #
        width_aux = self.closed_menu_width

        if menu_width == self.closed_menu_width:
            width_aux = self.open_menu_width
        else:
            self.vertical_close_menu()
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width_aux)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()

    def vertical_close_menu(self):
        self.ui.sim_toolBox.setCurrentIndex(3)

    # Reset BTN Selection
    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass

    def clear_all(self):
        self.clear_edit_page()
        self.clear_create_page()
        self.clear_simulation_page()

    def clear_edit_page(self):
        obj = self.ui.ui_pages.page_edit_rover.findChild(QFrame, "central_frame_page_edit_rover")
        if obj is not None:
            self.ui.name_edit_line_edit.clear()
            self.ui.exp_bat_edit_line_edit.clear()
            self.ui.exp_sp_edit_line_edit.clear()
            self.ui.trans_sp_edit_line_edit.clear()
            self.ui.trans_bat_edit_line_edit.clear()
            self.ui.bat_edit_line_edit.clear()
            self.ui.ch_time_edit_line_edit.clear()

    def clear_create_page(self):
        obj = self.ui.ui_pages.page_create_rover.findChild(QFrame, "central_frame_page_create_rover")
        if obj is not None:
            self.ui.ui_pages.name_create_line_edit.clear()
            self.ui.ui_pages.exp_bat_create_line_edit.clear()
            self.ui.ui_pages.exp_sp_create_line_edit.clear()
            self.ui.ui_pages.trans_sp_create_line_edit.clear()
            self.ui.ui_pages.trans_bat_create_line_edit.clear()
            self.ui.ui_pages.bat_create_line_edit.clear()
            self.ui.ui_pages.ch_time_create_line_edit.clear()

            self.ui.ui_pages.name_create_error_label.setText("")
            self.ui.ui_pages.bat_create_error_label.setText("")
            self.ui.ui_pages.trans_sp_create_error_label.setText("")
            self.ui.ui_pages.trans_bat_create_error_label.setText("")
            self.ui.ui_pages.exp_sp_create_error_label.setText("")
            self.ui.ui_pages.exp_bat_create_error_label.setText("")
            self.ui.ui_pages.ch_time_create_error_label.setText("")

    def clear_simulation_page(self):
        found = self.ui.ui_pages.fr_sim_widgets_layout.findChild(QGridLayout, "grid_layout_height")
        if found is not None:
            self.ui.ui_pages.height_sim_line_edit.clear()
            self.ui.ui_pages.radio_sim_line_edit.clear()
            self.ui.ui_pages.max_time_sim_line_edit.clear()
            self.ui.ui_pages.cave_width_sim_line_edit.clear()

            self.ui.ui_pages.height_sim_error_label.setText("")
            self.ui.ui_pages.radio_sim_error_label.setText("")
            self.ui.ui_pages.radio_sim_error_label.setText("")
            self.ui.ui_pages.max_time_sim_error_label.setText("")
            self.ui.ui_pages.cave_width_sim_error_label.setText("")

            self.ui.ui_pages.textEdit_rovers_selected.setText("")

            # Populate page_1 simulation
            self.controller_simulation.populate_num_rovers()
            self.controller_simulation.populate_num_jobs()
            self.controller_simulation.populate_cb_rovers()

            self.controller_simulation.rovers_simulation_selected = {}
            self.controller_simulation.rovers_simulate = []
            self.controller_simulation.text_to_add = ""

            # Hide max_time
            self.controller_simulation.hide_max_time()
            # Hide max_area
            self.controller_simulation.hide_max_area()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Create table
    errors = []
    try:
        rovers.get_create_table_sql()
        simulations.get_create_table_sql()
        rovers_sims.get_create_table_sql()
    except DBError as e:
        dlg = CustomDialog(e.motive, e.message)
        dlg.exec_()

    # Insert data into table when button create pressed
    window = MainWindow()
    sys.exit(app.exec())
