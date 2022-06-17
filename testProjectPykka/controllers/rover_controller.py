from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

# from gui... import ui_pages.page_details
from components import CustomDialog
from gui.pages.ui_pages import Ui_app_pages as Pages
from repositories import RoversRepository as rovers


class DetailPageController(QWidget):

    def __init__(self, parent=None, rover_id=None, ui=None):
        super().__init__(parent)

        self.rover_id = rover_id
        self.ui = ui
        self.populate_details()

    def populate_details(self):
        rover = rovers.get_rover_by_id(self.rover_id)
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
        self.ui = ui
        self.set_up_page()
        self.ui.editButton.clicked.connect(self.edit_rover)

    def set_up_page(self):
        # Get all fields of rover_id
        rover = rovers.get_rover_by_id(self.rover_id)
        # Set fields
        self.ui.name_edit_line_edit.setText(str(rover[0][1]))
        self.ui.bat_edit_line_edit.setText(str(rover[0][2]))
        self.ui.exp_sp_edit_line_edit.setText(str(rover[0][3]))
        self.ui.exp_bat_edit_line_edit.setText(str(rover[0][4]))
        self.ui.trans_sp_edit_line_edit.setText(str(rover[0][5]))
        self.ui.trans_bat_edit_line_edit.setText(str(rover[0][6]))
        self.ui.ch_time_edit_line_edit.setText(str(rover[0][7]))

    def edit_rover(self):
        # Checking parameters
        error_name = self.ui.name_edit_line_edit.checkingText()
        error_exp_dis = self.ui.exp_bat_edit_line_edit.checkingText()
        error_exp_sp = self.ui.exp_sp_edit_line_edit.checkingText()
        error_trans_sp = self.ui.trans_sp_edit_line_edit.checkingText()
        error_trans_dis = self.ui.trans_bat_edit_line_edit.checkingText()
        error_bat = self.ui.bat_edit_line_edit.checkingText()
        error_ch_time = self.ui.ch_time_edit_line_edit.checkingText()

        if error_name or error_exp_dis or error_exp_sp or error_trans_sp or error_trans_dis or error_bat or \
                error_ch_time:
            # show dialog
            dlg = CustomDialog("Error", "Some of the fields are empty or do not have the correct type")
            dlg.exec_()
            pass
        else:
            # Get fields
            text_name = self.ui.name_edit_line_edit.text()
            text_exp_dis = self.ui.exp_bat_edit_line_edit.text()
            text_exp_sp = self.ui.exp_sp_edit_line_edit.text()
            text_trans_sp = self.ui.trans_sp_edit_line_edit.text()
            text_trans_dis = self.ui.trans_bat_edit_line_edit.text()
            text_bat = self.ui.bat_edit_line_edit.text()
            text_ch_time = self.ui.ch_time_edit_line_edit.text()

            # Update
            update = rovers.update_rover_sql(name_rover=text_name, exp_speed=text_exp_sp,
                                    exp_battery=text_exp_dis, translate_speed=text_trans_sp,
                                    translate_battery=text_trans_dis, battery_rover=text_bat,
                                    charging_time=text_ch_time, rover_id=self.rover_id)
            if update:
                dlg = CustomDialog("Rover updated", "The rover has been successfully updated")
                dlg.exec_()
                self.parent.fill_table()
                self.parent.show_page_rovers()
        pass


class CreateRoverController(QWidget):

    def __init__(self, parent=None, ui=None):
        super().__init__(parent)
        self.parent = parent
        self.ui = ui
        self.ui.createButton.clicked.connect(self.add_rover)

    def add_rover(self):
        # TODO add value to cb rovers
        # repopulate cb rovers

        # Checking parameters
        error_name = self.ui.name_create_line_edit.checkingText()
        error_exp_dis = self.ui.exp_bat_create_line_edit.checkingText()
        error_exp_sp = self.ui.exp_sp_create_line_edit.checkingText()
        error_trans_sp = self.ui.trans_sp_create_line_edit.checkingText()
        error_trans_dis = self.ui.trans_bat_create_line_edit.checkingText()
        error_bat = self.ui.bat_create_line_edit.checkingText()
        error_ch_time = self.ui.ch_time_create_line_edit.checkingText()

        if error_name or error_exp_dis or error_exp_sp or error_trans_sp or error_trans_dis or error_bat or \
                error_ch_time:
            # show dialog
            dlg = CustomDialog("Error", "Some of the fields are empty or do not have the correct type")
            dlg.exec_()
            pass
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
            inserted = rovers.get_insert_rover_sql(name_rover=text_name, exp_speed=text_exp_sp,
                                                   exp_battery=text_exp_dis, translate_speed=text_trans_sp,
                                                   translate_battery=text_trans_dis, battery_rover=text_battery,
                                                   charging_time=text_charging_time)
            # Diálogo rover creado
            if inserted:
                dlg = CustomDialog("Rover created", "The rover has been successfully created")
                # en okay redirigir
                dlg.exec_()
                # Redirigir a otra vista
                self.parent.fill_table()
                self.parent.show_page_rovers()
                # self.parent.populate_cb_rovers()
                self.parent.revert_create_rover()
