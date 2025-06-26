from PySide6 import QtCore
import gui.repositories.RoversRepository as rovers
import gui.repositories.SimulationsRepository as simulations
import gui.repositories.ParticipateRepository as rovers_sims

import app


# Test 1.1
def test_create_rover_1(qtbot):
    test_sim_app = app.MainWindow()
    qtbot.addWidget(test_sim_app)
    # DELETE ALL DATA
    rovers.truncate_table_sql()
    simulations.truncate_table_sql()
    rovers_sims.truncate_table_sql()

    # from initial page
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_initial"

    # rover list -> no elements in the table
    qtbot.mouseClick(test_sim_app.ui.button_rover_list, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_rovers"

    # rover list -> no elements in the table
    test_sim_app.controller_rovers.fill_table()
    test_sim_app.controller_simulations.fill_table()
    num_rovers = test_sim_app.ui.ui_pages.table_rovers.rowCount()
    assert num_rovers == 0

    # rover creation -> valid rover
    qtbot.mouseClick(test_sim_app.ui.button_rover_creation, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_create_rover"
    # fill form
    # name_create_line_edit
    name_aux = "rover_test1"
    test_sim_app.ui.ui_pages.name_create_line_edit.setText(name_aux)
    # trans_sp_create_line_edit
    trans_sp_aux = "2.5"
    test_sim_app.ui.ui_pages.trans_sp_create_line_edit.setText(trans_sp_aux)
    # trans_bat_create_line_edit
    trans_bat_aux = "1"
    test_sim_app.ui.ui_pages.trans_bat_create_line_edit.setText(trans_bat_aux)
    # exp_bat_create_line_edit
    exp_bat_aux = "2.5"
    test_sim_app.ui.ui_pages.exp_bat_create_line_edit.setText(exp_bat_aux)
    # exp_sp_create_line_edit
    exp_sp_aux = "5"
    test_sim_app.ui.ui_pages.exp_sp_create_line_edit.setText(exp_sp_aux)
    # ch_time_create_line_edit
    ch_time_aux = "60"
    test_sim_app.ui.ui_pages.ch_time_create_line_edit.setText(ch_time_aux)
    # bat_create_line_edit
    bat_aux = "100"
    test_sim_app.ui.ui_pages.bat_create_line_edit.setText(bat_aux)

    # button create rover
    qtbot.mouseClick(test_sim_app.ui.ui_pages.createButton, QtCore.Qt.LeftButton)

    # rover list automatic -> 1 element in the table
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_rovers"
    num_rovers = test_sim_app.ui.ui_pages.table_rovers.rowCount()
    assert num_rovers == 1


# Test 1.3
def test_create_rover_2(qtbot):
    test_sim_app = app.MainWindow()
    qtbot.addWidget(test_sim_app)
    # from initial page
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_initial"
    # rover list -> no elements in the table
    qtbot.mouseClick(test_sim_app.ui.button_rover_list, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_rovers"
    # rover list -> no elements in the table
    num_rovers = test_sim_app.ui.ui_pages.table_rovers.rowCount()
    assert num_rovers == 1
    # rover creation -> valid rover
    qtbot.mouseClick(test_sim_app.ui.button_rover_creation, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_create_rover"
    # fill form
    # name_create_line_edit
    name_aux = "rover_test3"
    test_sim_app.ui.ui_pages.name_create_line_edit.setText(name_aux)
    # trans_sp_create_line_edit
    trans_sp_aux = "2.5"
    test_sim_app.ui.ui_pages.trans_sp_create_line_edit.setText(trans_sp_aux)
    # trans_bat_create_line_edit
    trans_bat_aux = "a"
    test_sim_app.ui.ui_pages.trans_bat_create_line_edit.setText(trans_bat_aux)
    # exp_bat_create_line_edit
    exp_bat_aux = "2.5"
    test_sim_app.ui.ui_pages.exp_bat_create_line_edit.setText(exp_bat_aux)
    # exp_sp_create_line_edit
    exp_sp_aux = "5"
    test_sim_app.ui.ui_pages.exp_sp_create_line_edit.setText(exp_sp_aux)
    # ch_time_create_line_edit
    ch_time_aux = "60"
    test_sim_app.ui.ui_pages.ch_time_create_line_edit.setText(ch_time_aux)
    # bat_create_line_edit
    bat_aux = "100"
    test_sim_app.ui.ui_pages.bat_create_line_edit.setText(bat_aux)

    # button create rover
    qtbot.mouseClick(test_sim_app.ui.ui_pages.createButton, QtCore.Qt.LeftButton)

    # rover list automatic -> 1 element in the table
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_create_rover"
    num_rovers = test_sim_app.ui.ui_pages.table_rovers.rowCount()
    assert num_rovers == 1


# Test 1.2
def test_create_rover_3(qtbot):
    test_sim_app = app.MainWindow()
    qtbot.addWidget(test_sim_app)
    # from initial page
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_initial"
    # rover list -> no elements in the table
    qtbot.mouseClick(test_sim_app.ui.button_rover_list, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_rovers"
    # rover list -> no elements in the table
    num_rovers = test_sim_app.ui.ui_pages.table_rovers.rowCount()
    assert num_rovers == 1
    # rover creation -> valid rover
    qtbot.mouseClick(test_sim_app.ui.button_rover_creation, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_create_rover"
    # fill form
    # name_create_line_edit
    name_aux = "rover_test1"
    test_sim_app.ui.ui_pages.name_create_line_edit.setText(name_aux)
    # trans_sp_create_line_edit
    trans_sp_aux = "2.5"
    test_sim_app.ui.ui_pages.trans_sp_create_line_edit.setText(trans_sp_aux)
    # trans_bat_create_line_edit
    trans_bat_aux = "1"
    test_sim_app.ui.ui_pages.trans_bat_create_line_edit.setText(trans_bat_aux)
    # exp_bat_create_line_edit
    exp_bat_aux = "2.5"
    test_sim_app.ui.ui_pages.exp_bat_create_line_edit.setText(exp_bat_aux)
    # exp_sp_create_line_edit
    exp_sp_aux = "5"
    test_sim_app.ui.ui_pages.exp_sp_create_line_edit.setText(exp_sp_aux)
    # ch_time_create_line_edit
    ch_time_aux = "60"
    test_sim_app.ui.ui_pages.ch_time_create_line_edit.setText(ch_time_aux)
    # bat_create_line_edit
    bat_aux = "100"
    test_sim_app.ui.ui_pages.bat_create_line_edit.setText(bat_aux)

    # button create rover
    qtbot.mouseClick(test_sim_app.ui.ui_pages.createButton, QtCore.Qt.LeftButton)

    # rover list automatic -> 1 element in the table
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_create_rover"
    num_rovers = test_sim_app.ui.ui_pages.table_rovers.rowCount()
    assert num_rovers == 1


# Test 1.4
def test_create_rover_4(qtbot):
    test_sim_app = app.MainWindow()
    qtbot.addWidget(test_sim_app)
    # from initial page
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_initial"
    # rover list -> no elements in the table
    qtbot.mouseClick(test_sim_app.ui.button_rover_list, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_rovers"
    # rover list -> no elements in the table
    num_rovers = test_sim_app.ui.ui_pages.table_rovers.rowCount()
    assert num_rovers == 1
    # rover creation -> valid rover
    qtbot.mouseClick(test_sim_app.ui.button_rover_creation, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_create_rover"
    # fill form
    # name_create_line_edit
    name_aux = "rover_test3"
    test_sim_app.ui.ui_pages.name_create_line_edit.setText(name_aux)
    # trans_sp_create_line_edit
    trans_sp_aux = ""
    test_sim_app.ui.ui_pages.trans_sp_create_line_edit.setText(trans_sp_aux)
    # trans_bat_create_line_edit
    trans_bat_aux = "1"
    test_sim_app.ui.ui_pages.trans_bat_create_line_edit.setText(trans_bat_aux)
    # exp_bat_create_line_edit
    exp_bat_aux = "2.5"
    test_sim_app.ui.ui_pages.exp_bat_create_line_edit.setText(exp_bat_aux)
    # exp_sp_create_line_edit
    exp_sp_aux = "5"
    test_sim_app.ui.ui_pages.exp_sp_create_line_edit.setText(exp_sp_aux)
    # ch_time_create_line_edit
    ch_time_aux = "60"
    test_sim_app.ui.ui_pages.ch_time_create_line_edit.setText(ch_time_aux)
    # bat_create_line_edit
    bat_aux = "100"
    test_sim_app.ui.ui_pages.bat_create_line_edit.setText(bat_aux)

    # button create rover
    qtbot.mouseClick(test_sim_app.ui.ui_pages.createButton, QtCore.Qt.LeftButton)

    # rover list automatic -> 1 element in the table
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_create_rover"
    num_rovers = test_sim_app.ui.ui_pages.table_rovers.rowCount()
    assert num_rovers == 1


# Test 2.1
def test_delete_rover(qtbot):
    test_sim_app = app.MainWindow()
    qtbot.addWidget(test_sim_app)
    # from initial page
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_initial"
    # rover list -> no elements in the table
    qtbot.mouseClick(test_sim_app.ui.button_rover_list, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_rovers"
    # rover list -> no elements in the table
    num_rovers = test_sim_app.ui.ui_pages.table_rovers.rowCount()
    assert num_rovers == 1

    # button delete rover
    qtbot.mouseClick(test_sim_app.ui.ui_pages.ref_delete_rover_button, QtCore.Qt.LeftButton)
    # rover list automatic -> 0 element in the table
    num_rovers = test_sim_app.ui.ui_pages.table_rovers.rowCount()
    assert num_rovers == 0


def test_create_rover_5(qtbot):
    test_sim_app = app.MainWindow()
    qtbot.addWidget(test_sim_app)
    # from initial page
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_initial"
    # rover list -> no elements in the table
    qtbot.mouseClick(test_sim_app.ui.button_rover_list, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_rovers"
    # rover list -> no elements in the table
    num_rovers = test_sim_app.ui.ui_pages.table_rovers.rowCount()
    assert num_rovers == 0
    # rover creation -> valid rover
    qtbot.mouseClick(test_sim_app.ui.button_rover_creation, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_create_rover"
    # fill form
    # name_create_line_edit
    name_aux = "rover_test1"
    test_sim_app.ui.ui_pages.name_create_line_edit.setText(name_aux)
    # trans_sp_create_line_edit
    trans_sp_aux = "2.5"
    test_sim_app.ui.ui_pages.trans_sp_create_line_edit.setText(trans_sp_aux)
    # trans_bat_create_line_edit
    trans_bat_aux = "1"
    test_sim_app.ui.ui_pages.trans_bat_create_line_edit.setText(trans_bat_aux)
    # exp_bat_create_line_edit
    exp_bat_aux = "2.5"
    test_sim_app.ui.ui_pages.exp_bat_create_line_edit.setText(exp_bat_aux)
    # exp_sp_create_line_edit
    exp_sp_aux = "5"
    test_sim_app.ui.ui_pages.exp_sp_create_line_edit.setText(exp_sp_aux)
    # ch_time_create_line_edit
    ch_time_aux = "60"
    test_sim_app.ui.ui_pages.ch_time_create_line_edit.setText(ch_time_aux)
    # bat_create_line_edit
    bat_aux = "100"
    test_sim_app.ui.ui_pages.bat_create_line_edit.setText(bat_aux)

    # button create rover
    qtbot.mouseClick(test_sim_app.ui.ui_pages.createButton, QtCore.Qt.LeftButton)

    # rover list automatic -> 1 element in the table
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_rovers"
    num_rovers = test_sim_app.ui.ui_pages.table_rovers.rowCount()
    assert num_rovers == 1


def test_edit_rover(qtbot):
    test_sim_app = app.MainWindow()
    qtbot.addWidget(test_sim_app)
    # rover list -> 1 element in the table
    qtbot.mouseClick(test_sim_app.ui.button_rover_list, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_rovers"
    # rover list -> 1 elements in the table
    num_rovers = test_sim_app.ui.ui_pages.table_rovers.rowCount()
    assert num_rovers == 1

    qtbot.mouseClick(test_sim_app.ui.ui_pages.ref_edit_rover_button, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_edit_rover"

    # fill form
    # name_create_line_edit
    name_aux = "rover_test1"
    test_sim_app.ui.name_edit_line_edit.setText(name_aux)
    # trans_sp_create_line_edit
    trans_sp_aux = "2.5"
    test_sim_app.ui.trans_sp_edit_line_edit.setText(trans_sp_aux)
    # trans_bat_create_line_edit
    trans_bat_aux = "a"
    test_sim_app.ui.trans_bat_edit_line_edit.setText(trans_bat_aux)
    # exp_bat_create_line_edit
    exp_bat_aux = "a"
    test_sim_app.ui.exp_bat_edit_line_edit.setText(exp_bat_aux)
    # exp_sp_create_line_edit
    exp_sp_aux = "5"
    test_sim_app.ui.exp_sp_edit_line_edit.setText(exp_sp_aux)
    # ch_time_create_line_edit
    ch_time_aux = "60"
    test_sim_app.ui.ch_time_edit_line_edit.setText(ch_time_aux)
    # bat_create_line_edit
    bat_aux = "100"
    test_sim_app.ui.bat_edit_line_edit.setText(bat_aux)
    qtbot.mouseClick(test_sim_app.ui.editButton, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_edit_rover"

def test_sim52(qtbot):
    test_sim_app = app.MainWindow()
    qtbot.addWidget(test_sim_app)
    qtbot.mouseClick(test_sim_app.ui.button_simulation_list, QtCore.Qt.LeftButton)

    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_simulations"
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 0
    qtbot.mouseClick(test_sim_app.ui.button_simulation, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_create_simulation"

    # fill form
    # mode
    test_sim_app.ui.ui_pages.radioButton_max_area.setChecked(True)
    # height
    height_aux = "a"
    test_sim_app.ui.ui_pages.height_sim_line_edit.setText(height_aux)
    # width
    width_aux = "2"
    test_sim_app.ui.ui_pages.cave_width_sim_line_edit.setText(width_aux)
    # observation radio
    obs_rad_aux = "1"
    test_sim_app.ui.ui_pages.radio_sim_line_edit.setText(obs_rad_aux)
    # select rover type
    test_sim_app.ui.ui_pages.cb_rovers.setCurrentIndex(0)
    # select num rovers
    # add
    qtbot.mouseClick(test_sim_app.ui.ui_pages.add_rover_select_btn, QtCore.Qt.LeftButton)
    qtbot.mouseClick(test_sim_app.ui.ui_pages.button_simulate, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_create_simulation"
    # rover list -> 1 elements in the table
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 0

def test_sim71(qtbot):
    test_sim_app = app.MainWindow()
    qtbot.addWidget(test_sim_app)
    # rover list -> 1 element in the table
    qtbot.mouseClick(test_sim_app.ui.button_simulation_list, QtCore.Qt.LeftButton)

    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_simulations"
    # rover list -> 1 elements in the table
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 0
    qtbot.mouseClick(test_sim_app.ui.button_simulation, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_create_simulation"

    # fill form
    # mode
    test_sim_app.ui.ui_pages.radioButton_max_area.setChecked(True)
    # height
    height_aux = "5.5"
    test_sim_app.ui.ui_pages.height_sim_line_edit.setText(height_aux)
    # width
    width_aux = "2"
    test_sim_app.ui.ui_pages.cave_width_sim_line_edit.setText(width_aux)
    # observation radio
    obs_rad_aux = "1"
    test_sim_app.ui.ui_pages.radio_sim_line_edit.setText(obs_rad_aux)
    # select rover type
    test_sim_app.ui.ui_pages.cb_rovers.setCurrentIndex(0)
    # select num rovers
    # add
    qtbot.mouseClick(test_sim_app.ui.ui_pages.add_rover_select_btn, QtCore.Qt.LeftButton)
    qtbot.mouseClick(test_sim_app.ui.ui_pages.button_simulate, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_simulations"
    # rover list -> 1 elements in the table
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 1


def test_sim61(qtbot):
    test_sim_app = app.MainWindow()
    qtbot.addWidget(test_sim_app)
    qtbot.mouseClick(test_sim_app.ui.button_simulation_list, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_simulations"

    # sim list -> 1 elements in the table
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 1
    qtbot.mouseClick(test_sim_app.ui.button_simulation, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_create_simulation"

    # fill form
    # mode
    test_sim_app.ui.ui_pages.radioButton_max_area.setChecked(True)
    # height
    height_aux = "4.01"
    test_sim_app.ui.ui_pages.height_sim_line_edit.setText(height_aux)
    # width
    width_aux = "4.01"
    test_sim_app.ui.ui_pages.cave_width_sim_line_edit.setText(width_aux)
    # observation radio
    obs_rad_aux = "1.42"
    test_sim_app.ui.ui_pages.radio_sim_line_edit.setText(obs_rad_aux)
    # select rover type
    test_sim_app.ui.ui_pages.cb_rovers.setCurrentIndex(0)
    # select num rovers
    # add
    qtbot.mouseClick(test_sim_app.ui.ui_pages.add_rover_select_btn, QtCore.Qt.LeftButton)
    qtbot.mouseClick(test_sim_app.ui.ui_pages.button_simulate, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_simulations"
    # rover list -> 2 elements in the table
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 2


def test_sim62(qtbot):
    test_sim_app = app.MainWindow()
    qtbot.addWidget(test_sim_app)
    qtbot.mouseClick(test_sim_app.ui.button_simulation_list, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_simulations"

    # sim list -> 1 elements in the table
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 2
    qtbot.mouseClick(test_sim_app.ui.button_simulation, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_create_simulation"

    # fill form
    # mode
    test_sim_app.ui.ui_pages.radioButton_max_area.setChecked(True)
    # height
    height_aux = "6"
    test_sim_app.ui.ui_pages.height_sim_line_edit.setText(height_aux)
    # width
    width_aux = "2"
    test_sim_app.ui.ui_pages.cave_width_sim_line_edit.setText(width_aux)
    # observation radio
    obs_rad_aux = "1"
    test_sim_app.ui.ui_pages.radio_sim_line_edit.setText(obs_rad_aux)
    # select rover type
    test_sim_app.ui.ui_pages.cb_rovers.setCurrentIndex(0)
    # select num rovers
    # add
    qtbot.mouseClick(test_sim_app.ui.ui_pages.add_rover_select_btn, QtCore.Qt.LeftButton)
    qtbot.mouseClick(test_sim_app.ui.ui_pages.button_simulate, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_simulations"
    # rover list -> 1 elements in the table
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 3

def test_create_rover_no_battery(qtbot):
    test_sim_app = app.MainWindow()
    qtbot.addWidget(test_sim_app)
    # from initial page
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_initial"
    # rover list -> no elements in the table
    qtbot.mouseClick(test_sim_app.ui.button_rover_list, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_rovers"
    # rover list -> no elements in the table
    num_rovers = test_sim_app.ui.ui_pages.table_rovers.rowCount()
    assert num_rovers == 1
    # rover creation -> valid rover
    qtbot.mouseClick(test_sim_app.ui.button_rover_creation, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_create_rover"
    # fill form
    # name_create_line_edit
    name_aux = "rover_no_battery"
    test_sim_app.ui.ui_pages.name_create_line_edit.setText(name_aux)
    # trans_sp_create_line_edit
    trans_sp_aux = "2.5"
    test_sim_app.ui.ui_pages.trans_sp_create_line_edit.setText(trans_sp_aux)
    # trans_bat_create_line_edit
    trans_bat_aux = "1"
    test_sim_app.ui.ui_pages.trans_bat_create_line_edit.setText(trans_bat_aux)
    # exp_bat_create_line_edit
    exp_bat_aux = "5"
    test_sim_app.ui.ui_pages.exp_bat_create_line_edit.setText(exp_bat_aux)
    # exp_sp_create_line_edit
    exp_sp_aux = "5"
    test_sim_app.ui.ui_pages.exp_sp_create_line_edit.setText(exp_sp_aux)
    # ch_time_create_line_edit
    ch_time_aux = "60"
    test_sim_app.ui.ui_pages.ch_time_create_line_edit.setText(ch_time_aux)
    # bat_create_line_edit
    bat_aux = "15"
    test_sim_app.ui.ui_pages.bat_create_line_edit.setText(bat_aux)

    # button create rover
    qtbot.mouseClick(test_sim_app.ui.ui_pages.createButton, QtCore.Qt.LeftButton)

    # rover list automatic -> 1 element in the table
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_rovers"
    num_rovers = test_sim_app.ui.ui_pages.table_rovers.rowCount()
    assert num_rovers == 2

def test_sim72(qtbot):
    test_sim_app = app.MainWindow()
    qtbot.addWidget(test_sim_app)
    qtbot.mouseClick(test_sim_app.ui.button_simulation_list, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_simulations"

    # sim list -> 1 elements in the table
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 3
    qtbot.mouseClick(test_sim_app.ui.button_simulation, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_create_simulation"

    # fill form
    # mode
    test_sim_app.ui.ui_pages.radioButton_max_area.setChecked(True)
    # height
    height_aux = "20"
    test_sim_app.ui.ui_pages.height_sim_line_edit.setText(height_aux)
    # width
    width_aux = "2"
    test_sim_app.ui.ui_pages.cave_width_sim_line_edit.setText(width_aux)
    # observation radio
    obs_rad_aux = "1"
    test_sim_app.ui.ui_pages.radio_sim_line_edit.setText(obs_rad_aux)
    # select rover type
    test_sim_app.ui.ui_pages.cb_rovers.setCurrentIndex(1)
    # select num rovers
    # add
    qtbot.mouseClick(test_sim_app.ui.ui_pages.add_rover_select_btn, QtCore.Qt.LeftButton)
    qtbot.mouseClick(test_sim_app.ui.ui_pages.button_simulate, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_simulations"
    # rover list -> 1 elements in the table
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 4


def test_sim81(qtbot):
    test_sim_app = app.MainWindow()
    qtbot.addWidget(test_sim_app)
    qtbot.mouseClick(test_sim_app.ui.button_simulation_list, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_simulations"

    # sim list -> 1 elements in the table
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 4
    qtbot.mouseClick(test_sim_app.ui.button_simulation, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_create_simulation"

    # fill form
    # mode
    test_sim_app.ui.ui_pages.radioButton_max_time.setChecked(True)
    # height
    height_aux = "6"
    test_sim_app.ui.ui_pages.height_sim_line_edit.setText(height_aux)
    # time
    time = "6"
    test_sim_app.ui.ui_pages.max_time_sim_line_edit.setText(time)
    # observation radio
    obs_rad_aux = "1"
    test_sim_app.ui.ui_pages.radio_sim_line_edit.setText(obs_rad_aux)
    # select rover type
    test_sim_app.ui.ui_pages.cb_rovers.setCurrentIndex(0)
    # select num rovers
    # add
    qtbot.mouseClick(test_sim_app.ui.ui_pages.add_rover_select_btn, QtCore.Qt.LeftButton)
    qtbot.mouseClick(test_sim_app.ui.ui_pages.button_simulate, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_simulations"
    # rover list -> 1 elements in the table
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 5

def test_sim82(qtbot):
    test_sim_app = app.MainWindow()
    qtbot.addWidget(test_sim_app)
    qtbot.mouseClick(test_sim_app.ui.button_simulation_list, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_simulations"

    # sim list -> 1 elements in the table
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 5
    qtbot.mouseClick(test_sim_app.ui.button_simulation, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_create_simulation"

    # fill form
    # mode
    test_sim_app.ui.ui_pages.radioButton_max_time.setChecked(True)
    # height
    height_aux = "20"
    test_sim_app.ui.ui_pages.height_sim_line_edit.setText(height_aux)
    # time
    time = "4"
    test_sim_app.ui.ui_pages.max_time_sim_line_edit.setText(time)
    # observation radio
    obs_rad_aux = "1.42"
    test_sim_app.ui.ui_pages.radio_sim_line_edit.setText(obs_rad_aux)
    # select rover type
    test_sim_app.ui.ui_pages.cb_rovers.setCurrentIndex(0)
    # select num rovers
    # add
    qtbot.mouseClick(test_sim_app.ui.ui_pages.add_rover_select_btn, QtCore.Qt.LeftButton)
    qtbot.mouseClick(test_sim_app.ui.ui_pages.button_simulate, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_simulations"
    # rover list -> 1 elements in the table
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 6

def test_create_rover_no_speed(qtbot):
    test_sim_app = app.MainWindow()
    qtbot.addWidget(test_sim_app)
    # from initial page
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_initial"
    # rover list -> no elements in the table
    qtbot.mouseClick(test_sim_app.ui.button_rover_list, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_rovers"
    # rover list -> no elements in the table
    num_rovers = test_sim_app.ui.ui_pages.table_rovers.rowCount()
    assert num_rovers == 2
    # rover creation -> valid rover
    qtbot.mouseClick(test_sim_app.ui.button_rover_creation, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_create_rover"
    # fill form
    # name_create_line_edit
    name_aux = "rover_no_speed"
    test_sim_app.ui.ui_pages.name_create_line_edit.setText(name_aux)
    # trans_sp_create_line_edit
    trans_sp_aux = "0.3"
    test_sim_app.ui.ui_pages.trans_sp_create_line_edit.setText(trans_sp_aux)
    # trans_bat_create_line_edit
    trans_bat_aux = "2.5"
    test_sim_app.ui.ui_pages.trans_bat_create_line_edit.setText(trans_bat_aux)
    # exp_bat_create_line_edit
    exp_bat_aux = "5"
    test_sim_app.ui.ui_pages.exp_bat_create_line_edit.setText(exp_bat_aux)
    # exp_sp_create_line_edit
    exp_sp_aux = "0.1"
    test_sim_app.ui.ui_pages.exp_sp_create_line_edit.setText(exp_sp_aux)
    # ch_time_create_line_edit
    ch_time_aux = "60"
    test_sim_app.ui.ui_pages.ch_time_create_line_edit.setText(ch_time_aux)
    # bat_create_line_edit
    bat_aux = "100"
    test_sim_app.ui.ui_pages.bat_create_line_edit.setText(bat_aux)

    # button create rover
    qtbot.mouseClick(test_sim_app.ui.ui_pages.createButton, QtCore.Qt.LeftButton)

    # rover list automatic -> 1 element in the table
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_rovers"
    num_rovers = test_sim_app.ui.ui_pages.table_rovers.rowCount()
    assert num_rovers == 3

def test_sim83(qtbot):
    test_sim_app = app.MainWindow()
    qtbot.addWidget(test_sim_app)
    qtbot.mouseClick(test_sim_app.ui.button_simulation_list, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_simulations"

    # sim list -> 1 elements in the table
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 6
    qtbot.mouseClick(test_sim_app.ui.button_simulation, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_create_simulation"

    # fill form
    # mode
    test_sim_app.ui.ui_pages.radioButton_max_time.setChecked(True)
    # height
    height_aux = "16"
    test_sim_app.ui.ui_pages.height_sim_line_edit.setText(height_aux)
    # time
    time = "1"
    test_sim_app.ui.ui_pages.max_time_sim_line_edit.setText(time)
    # observation radio
    obs_rad_aux = "1.42"
    test_sim_app.ui.ui_pages.radio_sim_line_edit.setText(obs_rad_aux)
    # select rover type
    test_sim_app.ui.ui_pages.cb_rovers.setCurrentIndex(2)
    # select num rovers
    # add
    qtbot.mouseClick(test_sim_app.ui.ui_pages.add_rover_select_btn, QtCore.Qt.LeftButton)
    qtbot.mouseClick(test_sim_app.ui.ui_pages.button_simulate, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_simulations"
    # rover list -> 1 elements in the table
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 7

def test_sim91(qtbot):
    test_sim_app = app.MainWindow()
    qtbot.addWidget(test_sim_app)
    qtbot.mouseClick(test_sim_app.ui.button_simulation_list, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_simulations"

    # sim list -> 1 elements in the table
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 7
    qtbot.mouseClick(test_sim_app.ui.button_simulation, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_create_simulation"

    # fill form
    # mode
    test_sim_app.ui.ui_pages.radioButton_max_area.setChecked(True)
    # height
    height_aux = "20"
    test_sim_app.ui.ui_pages.height_sim_line_edit.setText(height_aux)
    # width
    width_aux = "2"
    test_sim_app.ui.ui_pages.cave_width_sim_line_edit.setText(width_aux)
    # observation radio
    obs_rad_aux = "1.42"
    test_sim_app.ui.ui_pages.radio_sim_line_edit.setText(obs_rad_aux)
    # select rover type
    test_sim_app.ui.ui_pages.cb_rovers.setCurrentIndex(0)
    # select num rovers
    test_sim_app.ui.ui_pages.cb_num_rovers.setCurrentIndex(1)
    # select num jobs
    test_sim_app.ui.ui_pages.cb_num_jobs.setCurrentIndex(3)

    # add
    qtbot.mouseClick(test_sim_app.ui.ui_pages.add_rover_select_btn, QtCore.Qt.LeftButton)
    qtbot.mouseClick(test_sim_app.ui.ui_pages.button_simulate, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_simulations"
    # rover list -> 1 elements in the table
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 8

def test_sim92(qtbot):
    test_sim_app = app.MainWindow()
    qtbot.addWidget(test_sim_app)
    qtbot.mouseClick(test_sim_app.ui.button_simulation_list, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_simulations"

    # sim list -> 1 elements in the table
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 8
    qtbot.mouseClick(test_sim_app.ui.button_simulation, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_create_simulation"

    # fill form
    # mode
    test_sim_app.ui.ui_pages.radioButton_max_area.setChecked(True)
    # height
    height_aux = "20"
    test_sim_app.ui.ui_pages.height_sim_line_edit.setText(height_aux)
    # width
    width_aux = "2"
    test_sim_app.ui.ui_pages.cave_width_sim_line_edit.setText(width_aux)
    # observation radio
    obs_rad_aux = "1.42"
    test_sim_app.ui.ui_pages.radio_sim_line_edit.setText(obs_rad_aux)

    # select rover type
    test_sim_app.ui.ui_pages.cb_rovers.setCurrentIndex(1)
    # select num rovers
    test_sim_app.ui.ui_pages.cb_num_rovers.setCurrentIndex(1)
    # 2 rovers type no battery
    # add
    qtbot.mouseClick(test_sim_app.ui.ui_pages.add_rover_select_btn, QtCore.Qt.LeftButton)

    # select rover type
    test_sim_app.ui.ui_pages.cb_rovers.setCurrentIndex(0)
    # select num rovers
    test_sim_app.ui.ui_pages.cb_num_rovers.setCurrentIndex(0)
    # 2 rovers type no battery
    # add
    qtbot.mouseClick(test_sim_app.ui.ui_pages.add_rover_select_btn, QtCore.Qt.LeftButton)
    # select num jobs
    test_sim_app.ui.ui_pages.cb_num_jobs.setCurrentIndex(3)


    qtbot.mouseClick(test_sim_app.ui.ui_pages.button_simulate, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_simulations"
    # rover list -> 1 elements in the table
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 9


def test_sim101(qtbot):
    test_sim_app = app.MainWindow()
    qtbot.addWidget(test_sim_app)
    qtbot.mouseClick(test_sim_app.ui.button_simulation_list, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_simulations"

    # sim list -> 1 elements in the table
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 9
    qtbot.mouseClick(test_sim_app.ui.button_simulation, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_create_simulation"

    # fill form
    # mode
    test_sim_app.ui.ui_pages.radioButton_max_time.setChecked(True)
    # height
    height_aux = "10"
    test_sim_app.ui.ui_pages.height_sim_line_edit.setText(height_aux)
    # time
    time = "15"
    test_sim_app.ui.ui_pages.max_time_sim_line_edit.setText(time)
    # observation radio
    obs_rad_aux = "1"
    test_sim_app.ui.ui_pages.radio_sim_line_edit.setText(obs_rad_aux)

    # select rover type
    test_sim_app.ui.ui_pages.cb_rovers.setCurrentIndex(0)
    # select num rovers
    test_sim_app.ui.ui_pages.cb_num_rovers.setCurrentIndex(1)
    # 2 rovers type test1
    # add
    qtbot.mouseClick(test_sim_app.ui.ui_pages.add_rover_select_btn, QtCore.Qt.LeftButton)
    # select num jobs
    test_sim_app.ui.ui_pages.cb_num_jobs.setCurrentIndex(1)

    qtbot.mouseClick(test_sim_app.ui.ui_pages.button_simulate, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_simulations"
    # rover list -> 1 elements in the table
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 10

def test_sim102(qtbot):
    test_sim_app = app.MainWindow()
    qtbot.addWidget(test_sim_app)
    qtbot.mouseClick(test_sim_app.ui.button_simulation_list, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_simulations"

    # sim list -> 1 elements in the table
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 10
    qtbot.mouseClick(test_sim_app.ui.button_simulation, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_create_simulation"

    # fill form
    # mode
    test_sim_app.ui.ui_pages.radioButton_max_time.setChecked(True)
    # height
    height_aux = "20"
    test_sim_app.ui.ui_pages.height_sim_line_edit.setText(height_aux)
    # time
    time = "15"
    test_sim_app.ui.ui_pages.max_time_sim_line_edit.setText(time)
    # observation radio
    obs_rad_aux = "1.42"
    test_sim_app.ui.ui_pages.radio_sim_line_edit.setText(obs_rad_aux)

    # select rover type
    test_sim_app.ui.ui_pages.cb_rovers.setCurrentIndex(1)
    # select num rovers
    test_sim_app.ui.ui_pages.cb_num_rovers.setCurrentIndex(1)
    # 2 rovers type no battery
    # add
    qtbot.mouseClick(test_sim_app.ui.ui_pages.add_rover_select_btn, QtCore.Qt.LeftButton)

    # select rover type
    test_sim_app.ui.ui_pages.cb_rovers.setCurrentIndex(0)
    # select num rovers
    test_sim_app.ui.ui_pages.cb_num_rovers.setCurrentIndex(0)
    # 2 rovers type no battery
    # add
    qtbot.mouseClick(test_sim_app.ui.ui_pages.add_rover_select_btn, QtCore.Qt.LeftButton)
    # select num jobs
    test_sim_app.ui.ui_pages.cb_num_jobs.setCurrentIndex(3)

    qtbot.mouseClick(test_sim_app.ui.ui_pages.button_simulate, QtCore.Qt.LeftButton)
    current_page = test_sim_app.ui.pages.currentWidget()
    name_page = current_page.objectName()
    assert name_page == "page_simulations"
    # rover list -> 1 elements in the table
    num_simulation = test_sim_app.ui.ui_pages.table_simulations.rowCount()
    assert num_simulation == 11