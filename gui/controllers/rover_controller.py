from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

# from gui... import ui_pages.page_details
from gui.components.components import CustomDialog, CustomButton
from gui.repositories.DBError import DBError
from gui.windows.ui_create_rover_page import CreateRoverPageView
from gui.windows.ui_details_rover_page import DetailsRoverPageView
from gui.windows.ui_edit_rover_page import EditRoverPageView
from gui.repositories import RoversRepository as rovers
from gui.repositories import ParticipateRepository as rovers_sim


class DetailPageController(QWidget):

    def __init__(self, parent=None, rover_id=None, ui=None):
        super().__init__(parent)
        self.rover_id = rover_id
        self.ui = ui
        self.parent = parent
        self.ui.return_button_details.clicked.connect(self.show_page_rovers)
        self.populate_details()

    def show_page_rovers(self):
        self.parent.show_page_rovers()

    def populate_details(self):
        try:
            rover = rovers.get_rover_by_id(self.rover_id)
        except DBError as e:
            dlg = CustomDialog(e.motive, e.message)
            dlg.exec_()
        self.ui.label_name_changing.setText(str(rover[0][1]))
        self.ui.label_battery_changing.setText(str(rover[0][2]))
        self.ui.label_exp_speed_changing.setText(str(rover[0][3]))
        self.ui.label_exp_dis_changing.setText(str(rover[0][4]))
        self.ui.label_trans_sp_changing.setText(str(rover[0][5]))
        self.ui.label_trans_dis_changing.setText(str(rover[0][6]))
        self.ui.label_charging_time_changing.setText(str(rover[0][7]))


class EditRoverController(QWidget):

    def __init__(self, parent=None, ui=None, rover_id=None):
        super().__init__(parent)
        self.parent = parent
        self.rover_id = rover_id
        try:
            self.rover = rovers.get_rover_by_id(rover_id)
        except DBError as e:
            dlg = CustomDialog(e.motive, e.message)
            dlg.exec_()
        self.ui = ui
        self.set_up_page()
        self.ui.editButton.clicked.connect(self.edit_rover)
        self.ui.return_button_edit.clicked.connect(self.show_page_rovers)

    def show_page_rovers(self):
        self.parent.show_page_rovers()

    def set_up_page(self):
        # Get all fields of rover_id
        try:
            rover = rovers.get_rover_by_id(self.rover_id)
        except DBError as e:
            dlg = CustomDialog(e.motive, e.message)
            dlg.exec_()
        # Set fields
        self.ui.name_edit_line_edit.setText(str(rover[0][1]))
        self.ui.bat_edit_line_edit.setText(str(rover[0][2]))
        self.ui.exp_sp_edit_line_edit.setText(str(rover[0][3]))
        self.ui.exp_bat_edit_line_edit.setText(str(rover[0][4]))
        self.ui.trans_sp_edit_line_edit.setText(str(rover[0][5]))
        self.ui.trans_bat_edit_line_edit.setText(str(rover[0][6]))
        self.ui.ch_time_edit_line_edit.setText(str(rover[0][7]))

    def validate(self):
        # Checking parameters
        error_name = self.ui.name_edit_line_edit.checking_text()
        error_exp_dis = self.ui.exp_bat_edit_line_edit.checking_text()
        error_exp_sp = self.ui.exp_sp_edit_line_edit.checking_text()
        error_trans_sp = self.ui.trans_sp_edit_line_edit.checking_text()
        error_trans_dis = self.ui.trans_bat_edit_line_edit.checking_text()
        error_bat = self.ui.bat_edit_line_edit.checking_text()
        error_ch_time = self.ui.ch_time_edit_line_edit.checking_text()

        if error_name or error_exp_dis or error_exp_sp or error_trans_sp or error_trans_dis or error_bat or \
                error_ch_time:
            return False
        return True

    def edit_rover(self):
        is_valid = self.validate()

        if not is_valid:
            # show dialog
            dlg = CustomDialog("Error", "Some of the fields are empty or do not have the correct type")
            dlg.exec_()
            pass
        # checking if the name field has changed
        elif self.rover[0][1] != self.ui.name_edit_line_edit.text():

            try:
                aux_rover_name = rovers.get_rover_by_name(self.ui.name_edit_line_edit.text())
            except DBError as e:
                dlg = CustomDialog(e.motive, e.message)
                dlg.exec_()

            if len(aux_rover_name) > 0:
                # Checking if there already exists a rover with that name
                # show dialog
                dlg = CustomDialog("Error",
                                   "The rover with name " + self.ui.name_edit_line_edit.text() + " already exists.")
                dlg.exec_()
            else:
                self.updating_rover()
        else:
            # Get fields
            self.updating_rover()

    def updating_rover(self):
        text_name = self.ui.name_edit_line_edit.text()
        text_exp_dis = self.ui.exp_bat_edit_line_edit.text()
        text_exp_sp = self.ui.exp_sp_edit_line_edit.text()
        text_trans_sp = self.ui.trans_sp_edit_line_edit.text()
        text_trans_dis = self.ui.trans_bat_edit_line_edit.text()
        text_bat = self.ui.bat_edit_line_edit.text()
        text_ch_time = self.ui.ch_time_edit_line_edit.text()
        # Update
        try:
            update = rovers.update_rover_sql(name_rover=text_name, exp_speed=text_exp_sp,
                                             exp_battery=text_exp_dis, translate_speed=text_trans_sp,
                                             translate_battery=text_trans_dis, battery_rover=text_bat,
                                             charging_time=text_ch_time, rover_id=self.rover_id)
        except DBError as e:
            dlg = CustomDialog(e.motive, e.message)
            dlg.exec_()
        if update:
            dlg = CustomDialog("Rover updated", "The rover has been successfully updated")
            dlg.exec_()
            self.parent.fill_table()
            self.parent.show_page_rovers()
        else:
            # recover
            self.recover()

    def recover(self):
        pass


class CreateRoverController(QWidget):

    def __init__(self, parent=None, ui=None):
        super().__init__(parent)
        self.parent = parent
        self.ui = ui
        self.ui.createButton.clicked.connect(self.create_rover)
        self.ui.return_button_create.clicked.connect(self.show_page_rovers)

    def show_page_rovers(self):
        self.parent.show_page_rovers()

    def clear_page(self):
        obj = self.ui.page_create_rover.findChild(QFrame, "central_frame_page_create_rover")
        if obj is not None:
            self.ui.name_create_line_edit.clear()
            self.ui.exp_bat_create_line_edit.clear()
            self.ui.exp_sp_create_line_edit.clear()
            self.ui.trans_sp_create_line_edit.clear()
            self.ui.trans_bat_create_line_edit.clear()
            self.ui.bat_create_line_edit.clear()
            self.ui.ch_time_create_line_edit.clear()

            self.ui.name_create_error_label.setText("")
            self.ui.bat_create_error_label.setText("")
            self.ui.trans_sp_create_error_label.setText("")
            self.ui.trans_bat_create_error_label.setText("")
            self.ui.exp_sp_create_error_label.setText("")
            self.ui.exp_bat_create_error_label.setText("")
            self.ui.ch_time_create_error_label.setText("")

    def validate(self):
        error_name = self.ui.name_create_line_edit.checking_text()
        error_exp_dis = self.ui.exp_bat_create_line_edit.checking_text()
        error_exp_sp = self.ui.exp_sp_create_line_edit.checking_text()
        error_trans_sp = self.ui.trans_sp_create_line_edit.checking_text()
        error_trans_dis = self.ui.trans_bat_create_line_edit.checking_text()
        error_bat = self.ui.bat_create_line_edit.checking_text()
        error_ch_time = self.ui.ch_time_create_line_edit.checking_text()

        if error_name or error_exp_dis or error_exp_sp or error_trans_sp or error_trans_dis or error_bat or \
                error_ch_time:
            # show dialog
            return False
        return True

    def create_rover(self):
        # Checking parameters
        is_valid = self.validate()
        try:
            aux_rover_created = rovers.get_rover_by_name(self.ui.name_create_line_edit.text())
        except DBError as e:
            dlg = CustomDialog(e.motive, e.message)
            dlg.exec_()

        if not is_valid:
            # show dialog
            dlg = CustomDialog("Error", "Some of the fields are empty or do not have the correct type")
            dlg.exec_()
            pass
        elif len(aux_rover_created) > 0:
            # Checking if there already exists a rover with that name
            # show dialog
            dlg = CustomDialog("Error",
                               "The rover with name " + self.ui.name_create_line_edit.text() + " already exists.")
            dlg.exec_()
        else:
            text_name = str(self.ui.name_create_line_edit.text())
            # exploration parameters
            text_exp_dis = float(self.ui.exp_bat_create_line_edit.text())
            text_exp_sp = float(self.ui.exp_sp_create_line_edit.text())
            # translate parameters
            text_trans_sp = float(self.ui.trans_sp_create_line_edit.text())
            text_trans_dis = float(self.ui.trans_bat_create_line_edit.text())
            # battery
            text_battery = float(self.ui.bat_create_line_edit.text())
            # charging time
            text_charging_time = float(self.ui.ch_time_create_line_edit.text())

            # Insert rover
            try:
                inserted = rovers.get_insert_rover_sql(name_rover=text_name, exp_speed=text_exp_sp,
                                                       exp_battery=text_exp_dis, translate_speed=text_trans_sp,
                                                       translate_battery=text_trans_dis, battery_rover=text_battery,
                                                       charging_time=text_charging_time)
                if inserted:
                    dlg = CustomDialog("Rover created", "The rover has been successfully created")
                    # en okay redirigir
                    dlg.exec_()
                    # Redirigir a otra vista
                    self.parent.fill_table()
                    self.parent.show_page_rovers()
                    self.clear_page()
            except DBError as e:
                dlg = CustomDialog(e.motive, e.message)
                dlg.exec_()


class RoversPageController(QWidget):

    def __init__(self, parent=None, ui=None):
        super().__init__(parent)
        self.parent = parent
        self.ui = ui
        self.rover_id_aux = None
        self.config_table()
        self.fill_table()

        self.ui.ui_pages.search_lineEdit.returnPressed.connect(self.search_rover)
        self.ui.ui_pages.search_lineEdit.textChanged.connect(self.restore_table_data)
        self.ui.ui_pages.search_rover.clicked.connect(self.search_rover)
        self.ui.ui_pages.create_rover_btn.clicked.connect(self.show_page_create_rover)
        self.ui.ui_pages.create_ex_rover_btn.clicked.connect(self.create_upload_rover_examples)

    def config_table(self):
        column_labels = ("ID", "NAME", "BATTERY", "CHARGING TIME", "")
        self.ui.ui_pages.table_rovers.setColumnCount(len(column_labels))
        self.ui.ui_pages.table_rovers.setHorizontalHeaderLabels(column_labels)
        self.ui.ui_pages.table_rovers.setColumnWidth(2, 200)
        self.ui.ui_pages.table_rovers.setColumnWidth(3, 200)
        self.ui.ui_pages.table_rovers.setColumnWidth(4, 150)
        self.ui.ui_pages.table_rovers.setColumnWidth(5, 200)
        self.ui.ui_pages.table_rovers.verticalHeader().setDefaultSectionSize(50)
        self.ui.ui_pages.table_rovers.setColumnHidden(0, True)
        self.ui.ui_pages.table_rovers.setSelectionBehavior(QAbstractItemView.SelectRows)

    def search_rover(self):
        param = self.ui.ui_pages.search_lineEdit.text()
        data = None
        if param != "":
            try:
                data = rovers.get_rover_by_name(param)
            except DBError as e:
                dlg = CustomDialog(e.motive, e.message)
                dlg.exec_()
        self.populate_table(data)

    def search_rover_write(self):
        param = self.ui.ui_pages.search_lineEdit.text()
        data = None
        if param != "":
            pattern = param + '%'
            try:
                data = rovers.get_rover_starting_name(pattern)
            except DBError as e:
                dlg = CustomDialog(e.motive, e.message)
                dlg.exec_()

        self.populate_table(data)

    def populate_table(self, data):
        if data is not None:
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
        view_rover_button = CustomButton("View", "rgb(10, 120, 115)")
        self.ui.ui_pages.ref_view_rover_button = view_rover_button
        edit_rover_button = CustomButton("Edit", "rgb(0, 128, 255)")
        self.ui.ui_pages.ref_edit_rover_button = edit_rover_button
        delete_rover_button = CustomButton("Delete", "rgb(178, 34, 34)")
        self.ui.ui_pages.ref_delete_rover_button = delete_rover_button

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(view_rover_button)
        buttons_layout.addWidget(edit_rover_button)
        buttons_layout.addWidget(delete_rover_button)

        buttons_frame = QFrame()
        buttons_frame.setLayout(buttons_layout)

        view_rover_button.clicked.connect(self.view_rover)
        edit_rover_button.clicked.connect(self.show_page_edit_rover)
        delete_rover_button.clicked.connect(self.delete_rover)

        return buttons_frame

    def view_rover(self):
        button = self.sender()
        table = self.ui.ui_pages.table_rovers
        if button:
            rover_id = self.get_rover_id_table(table, button)
            self.parent.clear_all()
            self.show_page_details(rover_id)

    # Btn pase gettings
    def show_page_details(self, rover_id):
        self.reset_selection()

        page_details = DetailsRoverPageView(self, self.ui.ui_pages)
        controller_details = DetailPageController(self, rover_id, self.ui.ui_pages)
        self.parent.clear_all()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_details)

    # Btn page_1 rover
    def show_page_create_rover(self):
        if self.parent.page_create_rover is None:
            self.parent.page_create_rover = CreateRoverPageView(self, self.ui.ui_pages)
            self.parent.controller_create_rover = CreateRoverController(self, self.ui.ui_pages)
        self.parent.clear_all()
        self.parent.show_page_create_rover()

    def create_upload_rover_examples(self):
        # Data rover_test_1

        # name_create_line_edit
        name_aux = "rover_test1"
        # trans_sp_create_line_edit
        trans_sp_aux = "2.5"
        # trans_bat_create_line_edit
        trans_bat_aux = "1"
        # exp_bat_create_line_edit
        exp_bat_aux = "2.5"
        # exp_sp_create_line_edit
        exp_sp_aux = "5"
        # ch_time_create_line_edit
        ch_time_aux = "60"
        # bat_create_line_edit
        bat_aux = "100"

        # Insert rover
        inserted = rovers.get_insert_rover_sql(name_rover=name_aux, exp_speed=exp_sp_aux,
                                                   exp_battery=exp_bat_aux, translate_speed=trans_sp_aux,
                                                   translate_battery=trans_bat_aux, battery_rover=bat_aux,
                                                   charging_time=ch_time_aux)
        print(inserted)

        # Data rover_no_battery
        name_aux = "rover_no_battery"
        # trans_sp_create_line_edit
        trans_sp_aux = "2.5"
        # trans_bat_create_line_edit
        trans_bat_aux = "1"
        # exp_bat_create_line_edit
        exp_bat_aux = "5"
        # exp_sp_create_line_edit
        exp_sp_aux = "5"
        # ch_time_create_line_edit
        ch_time_aux = "60"
        # bat_create_line_edit
        bat_aux = "15"
        # Insert rover
        inserted = rovers.get_insert_rover_sql(name_rover=name_aux, exp_speed=exp_sp_aux,
                                               exp_battery=exp_bat_aux, translate_speed=trans_sp_aux,
                                               translate_battery=trans_bat_aux, battery_rover=bat_aux,
                                               charging_time=ch_time_aux)
        print(inserted)

        # rover_no_speed
        name_aux = "rover_no_speed"
        # trans_sp_create_line_edit
        trans_sp_aux = "0.3"
        # trans_bat_create_line_edit
        trans_bat_aux = "2.5"
        # exp_bat_create_line_edit
        exp_bat_aux = "5"
        # exp_sp_create_line_edit
        exp_sp_aux = "0.1"
        # ch_time_create_line_edit
        ch_time_aux = "60"
        # bat_create_line_edit
        bat_aux = "100"
        inserted = rovers.get_insert_rover_sql(name_rover=name_aux, exp_speed=exp_sp_aux,
                                               exp_battery=exp_bat_aux, translate_speed=trans_sp_aux,
                                               translate_battery=trans_bat_aux, battery_rover=bat_aux,
                                               charging_time=ch_time_aux)
        print(inserted)
        # recharge the page
        self.restore_table_data()


    # Btn page_1 edit
    def show_page_edit_rover(self):
        button = self.sender()
        table = self.ui.ui_pages.table_rovers
        if button:
            if self.parent.page_edit_rover is None:
                rover_id = self.get_rover_id_table(table, button)
                self.parent.page_edit_rover = EditRoverPageView(self, self.ui)
                self.parent.controller_edit_rover = EditRoverController(self, self.ui, rover_id)
            # fill the data
            else:
                self.parent.controller_edit_rover.set_up_page()
            # show || hide
            self.parent.clear_create_page()
            self.parent.clear_simulation_page()
            self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_edit_rover)

    def get_rover_id_table(self, table, button):
        row_index = table.indexAt(button.parent().pos()).row()
        cell_id_index = table.model().index(row_index, 0)
        rover_id = table.model().data(cell_id_index)
        return rover_id

    def delete_rover(self):
        button = self.sender()
        table = self.ui.ui_pages.table_rovers

        if button:
            rover_id = self.get_rover_id_table(table, button)
        # if rover is in a current sim ->  can not delete rover
        try:
            exist = rovers_sim.get_rovers_simulations_by_rover_id(rover_id)
        except DBError as e:
            dlg = CustomDialog(e.motive, e.message)
            dlg.exec_()

        if len(exist) <= 0:
            try:
                if rovers.delete_rover(rover_id):
                    self.fill_table()
            except DBError as e:
                dlg = CustomDialog(e.motive, e.message)
                dlg.exec_()
        else:
            dlg = CustomDialog("Error",
                               "The rover is participating in an existant simulation, please delete the simulation"
                               "to be able to delete the rover")
            dlg.exec_()

    def restore_table_data(self):
        param = self.ui.ui_pages.search_lineEdit.text()
        # If it is empty restore the table
        if param == "":
            self.fill_table()
        # If it is not empty search and fill the table
        else:
            self.search_rover_write()

    def fill_table(self):
        try:
            data = rovers.get_all_rovers_table()
            self.populate_table(data)
        except DBError as e:
            dlg = CustomDialog(e.motive, e.message)
            dlg.exec_()

    def show_page_rovers(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_rovers)
        self.ui.button_rover_list.set_active(True)

    # Reset BTN Selection
    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass