import sys
import components
from components import CustomDialog
import repositories.RoversRepository as rovers
from database_manager.database_manager import *
from gui.windows.ui_create_rover_page import CreateRoverPageView
from gui.windows.ui_edit_rover_page import EditRoverPageView
from gui.windows.ui_main_window import *
# controllers
from controllers.rover_controller import DetailPageController, CreateRoverController, EditRoverController
from controllers.simulation_controller import SimulatePageController



class MainWindow(QMainWindow):
    def __init__(self):
        # TODO
        # DONE Delete de database management here
        # DONE Add the classes to the general program
        # Done add a controller for page -> rovers DETAILS DONE, EDIT, CREATE, DELETE

        # TODO Change style
        # TODO Change lateral menu for -> creating and managing rovers

        # TODO Error management: Simulation
        # TODO Fix errors simulation + use good practices of akka

        # TODO Create the .exe
        # TODO Delete and update the repository

        super().__init__()

        # set up main window
        self.setWindowTitle("Exploring Rovers")
        self.ui = UI_MainWindow()
        # call to the method with self -> parent
        self.ui.setup_ui(self)
        # call the rest of the gui pages

        self.rover_id_aux = None

        # toggle button animation
        self.ui.toggle_button.clicked.connect(self.toggle_button)
        # Btn home
        self.ui.btn_1.clicked.connect(self.show_page_initial)

        # Btn widgets
        self.ui.btn_2.clicked.connect(self.show_page_rovers)

        # Btn simulation
        self.ui.btn_simulation.clicked.connect(self.show_page_simulation)

        # Btn create rovers
        self.ui.ui_pages.create_rover_btn.clicked.connect(self.show_page_create_rover)

        # Table rovers
        self.config_table()
        self.fill_table()

        # TODO set disabled but the scroll bar must be enabled
        # self.ui.ui_pages.textEdit_rovers_selected.setDisabled(True)

        self.ui.ui_pages.search_lineEdit.returnPressed.connect(self.search_rover)
        self.ui.ui_pages.search_lineEdit.textChanged.connect(self.restore_table_data)
        self.ui.ui_pages.search_rover.clicked.connect(self.search_rover)


        # self.ui.ui_pages.button_simulate.clicked.connect(self.simulate)
        self.show()

    def pop_up(self):
        dlg = CustomDialog("Simulation dialog", "The simulation has finished")
        dlg.exec_()
        pass

    def restore_table_data(self):
        param = self.ui.ui_pages.search_lineEdit.text()
        if param == "":
            self.fill_table()

    def fill_table(self):
        data = rovers.get_all_rovers_table()
        self.populate_table(data)



    def revert_create_rover(self):
        self.ui.ui_pages.name_lineEdit.clear()
        self.ui.ui_pages.exp_dis_lineEdit.clear()
        self.ui.ui_pages.exp_sp_lineEdit.clear()
        self.ui.ui_pages.trans_sp_lineEdit.clear()
        self.ui.ui_pages.trans_dis_lineEdit.clear()
        self.ui.ui_pages.bat_lineEdit.clear()
        self.ui.ui_pages.ch_time_lineEdit.clear()
        self.ui.ui_pages.createButton.setText("Create")

    # Btn home function
    def show_page_initial(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_initial)
        self.ui.btn_1.set_active(True)

    def show_page_simulation(self):
        self.reset_selection()
        controller_simulation = SimulatePageController(self, self.ui.ui_pages)
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_simulation)
        self.ui.btn_simulation.set_active(True)

    # Btn widgets function
    def show_page_rovers(self):
        self.reset_selection()

        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_rovers)
        self.ui.btn_2.set_active(True)

    # Btn pase gettings
    def show_page_details(self, rover_id):
        self.reset_selection()
        controller_details = DetailPageController(self, rover_id, self.ui.ui_pages)
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_details)

        # self.populate_details(rover_id)
        # self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_details)
        self.ui.settings_btn.set_active(True)

    def populate_details(self, rover_id):
        rover = rovers.get_rover_by_id(rover_id)
        self.ui.ui_pages.label_name_changing.setText(str(rover[0][1]))
        self.ui.ui_pages.label_battery_changing.setText(str(rover[0][2]))
        self.ui.ui_pages.label_exp_speed_changing.setText(str(rover[0][3]))
        self.ui.ui_pages.label_exp_dis_changing.setText(str(rover[0][4]))
        self.ui.ui_pages.label_trans_sp_changing.setText(str(rover[0][5]))
        self.ui.ui_pages.label_trans_dis_changing.setText(str(rover[0][6]))
        self.ui.ui_pages.label_charging_time_changing.setText(str(rover[0][7]))

    def view_rover(self):
        button = self.sender()
        table = self.ui.ui_pages.table_rovers
        if button:
            rover_id = self.get_rover_id_table(table, button)
            self.show_page_details(rover_id)

    # Btn pase gettings
    def show_page_create_rover(self):

        # self.reset_selection()
        # self.revert_create_rover()

        view = CreateRoverPageView(self, self.ui.ui_pages)
        controller = CreateRoverController(self, self.ui.ui_pages)
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_create_rover)

    # Btn pase gettings
    def show_page_edit_rover(self):
        button = self.sender()
        table = self.ui.ui_pages.table_rovers
        if button:
            rover_id = self.get_rover_id_table(table, button)
            view = EditRoverPageView(self, self.ui.ui_pages)
            controller = EditRoverController(self, self.ui.ui_pages, rover_id)
            self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_create_rover)


    def edit_rover(self):
        text_name = str(self.ui.ui_pages.name_lineEdit.text())
        # exploration parameters
        var2 = self.ui.ui_pages.exp_dis_lineEdit.text()
        text_exp_dis = float(self.ui.ui_pages.exp_dis_lineEdit.text())
        text_exp_sp = float(self.ui.ui_pages.exp_sp_lineEdit.text())
        # translate parameters
        text_trans_sp = float(self.ui.ui_pages.trans_sp_lineEdit.text())
        text_trans_dis = float(self.ui.ui_pages.trans_dis_lineEdit.text())

        # battery
        text_battery = float(self.ui.ui_pages.bat_lineEdit.text())

        # charging time
        text_charging_time = float(self.ui.ui_pages.ch_time_lineEdit.text())
        rovers.update_rover_sql(name_rover=text_name, exp_speed=text_exp_sp,
                                exp_battery=text_exp_dis, translate_speed=text_trans_sp,
                                translate_battery=text_trans_dis, battery_rover=text_battery,
                                charging_time=text_charging_time, rover_id=self.rover_id_aux)
        self.fill_table()
        self.show_page_rovers()
        self.revert_create_rover()
        pass

    def toggle_button(self):
        # Get menu width
        menu_width = self.ui.left_menu.width()
        # Checking width
        width = 50

        if menu_width == 50:
            width = 240

        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()

    def config_table(self):
        column_labels = ("ID", "NAME", "BATTERY", "CHARGING TIME", "")
        self.ui.ui_pages.table_rovers.setColumnCount(len(column_labels))
        self.ui.ui_pages.table_rovers.setHorizontalHeaderLabels(column_labels)
        self.ui.ui_pages.table_rovers.setColumnWidth(2, 200)
        self.ui.ui_pages.table_rovers.setColumnWidth(3, 200)
        self.ui.ui_pages.table_rovers.setColumnWidth(4, 200)
        self.ui.ui_pages.table_rovers.setColumnWidth(5, 200)
        self.ui.ui_pages.table_rovers.verticalHeader().setDefaultSectionSize(50)
        self.ui.ui_pages.table_rovers.setColumnHidden(0, True)
        self.ui.ui_pages.table_rovers.setSelectionBehavior(QAbstractItemView.SelectRows)

    def search_rover(self):

        param = self.ui.ui_pages.search_lineEdit.text()
        if param != "":
            data = rovers.get_rover_by_name(param)
            self.populate_table(data)

    def populate_table(self, data):
        self.ui.ui_pages.table_rovers.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                var = str(cell)
                item_var = QTableWidgetItem(var)
                item_var.setFlags(Qt.ItemIsEditable)
                self.ui.ui_pages.table_rovers.setItem(
                    index_row, index_cell, item_var
                )

            self.ui.ui_pages.table_rovers.setCellWidget(
                index_row, 4, self.build_action_button()
            )

    def build_action_button(self):
        view_button = components.Button("view", "#17A2B8")
        edit_button = components.Button("edit", "#007BFF")
        delete_button = components.Button("delete", "#DC3545")

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(view_button)
        buttons_layout.addWidget(edit_button)
        buttons_layout.addWidget(delete_button)

        buttons_frame = QFrame()
        buttons_frame.setLayout(buttons_layout)

        view_button.clicked.connect(self.view_rover)
        edit_button.clicked.connect(self.show_page_edit_rover)
        delete_button.clicked.connect(self.delete_rover)

        return buttons_frame

    def delete_rover(self):
        button = self.sender()
        table = self.ui.ui_pages.table_rovers

        if button:
            rover_id = self.get_rover_id_table(table, button)
            if rovers.delete_rover(rover_id):
                self.fill_table()

    def get_rover_id_table(self, table, button):
        row_index = table.indexAt(button.parent().pos()).row()
        cell_id_index = table.model().index(row_index, 0)
        rover_id = table.model().data(cell_id_index)
        return rover_id

    # Reset BTN Selection
    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Connect to db
    cnn = DataBaseManager()
    db = cnn.connect(3306)
    # Create table
    rovers.get_create_table_sql()
    # Insert data into table when button create pressed
    window = MainWindow()
    sys.exit(app.exec())


