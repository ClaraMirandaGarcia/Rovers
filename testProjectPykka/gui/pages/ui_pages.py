# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesXFToyu.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_app_pages(object):
    def setupUi(self, app_pages):
        if not app_pages.objectName():
            app_pages.setObjectName(u"app_pages")
        app_pages.resize(696, 922)
        self.page_initial = QWidget()
        self.page_initial.setObjectName(u"page_initial")
        self.verticalLayout = QVBoxLayout(self.page_initial)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.page_initial)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 150))
        self.frame.setMaximumSize(QSize(500, 150))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_welcome = QLabel(self.frame)
        self.label_welcome.setObjectName(u"label_welcome")
        self.label_welcome.setStyleSheet(u"font: 700 30pt \"Segoe UI\";\n"
"color:rgb(255, 255, 255);")
        self.label_welcome.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_welcome)

        self.label_description_welcome = QLabel(self.frame)
        self.label_description_welcome.setObjectName(u"label_description_welcome")
        self.label_description_welcome.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color:rgb(255, 255, 255);")
        self.label_description_welcome.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_description_welcome)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter)

        app_pages.addWidget(self.page_initial)
        self.page_create_rover = QWidget()
        self.page_create_rover.setObjectName(u"page_create_rover")
        self.page_create_rover_layout = QVBoxLayout(self.page_create_rover)
        self.page_create_rover_layout.setObjectName(u"page_create_rover_layout")
        app_pages.addWidget(self.page_create_rover)
        self.page_rovers = QWidget()
        self.page_rovers.setObjectName(u"page_rovers")
        self.verticalLayout_3 = QVBoxLayout(self.page_rovers)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.central_frame = QFrame(self.page_rovers)
        self.central_frame.setObjectName(u"central_frame")
        self.central_frame.setStyleSheet(u"background-color: #282a36")
        self.central_frame.setFrameShape(QFrame.StyledPanel)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.central_frame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.background_frame = QFrame(self.central_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.background_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_lbl_rovers = QFrame(self.background_frame)
        self.frame_lbl_rovers.setObjectName(u"frame_lbl_rovers")
        self.frame_lbl_rovers.setMinimumSize(QSize(0, 40))
        self.frame_lbl_rovers.setMaximumSize(QSize(16777215, 40))
        self.frame_lbl_rovers.setFrameShape(QFrame.StyledPanel)
        self.frame_lbl_rovers.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_lbl_rovers)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_rover = QLabel(self.frame_lbl_rovers)
        self.label_rover.setObjectName(u"label_rover")
        self.label_rover.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color:rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.label_rover)


        self.verticalLayout_7.addWidget(self.frame_lbl_rovers)

        self.frame_actions_rover = QFrame(self.background_frame)
        self.frame_actions_rover.setObjectName(u"frame_actions_rover")
        self.frame_actions_rover.setMinimumSize(QSize(0, 50))
        self.frame_actions_rover.setMaximumSize(QSize(16777215, 50))
        self.frame_actions_rover.setFrameShape(QFrame.StyledPanel)
        self.frame_actions_rover.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_actions_rover)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, -1, 3)
        self.search_lineEdit = QLineEdit(self.frame_actions_rover)
        self.search_lineEdit.setObjectName(u"search_lineEdit")
        self.search_lineEdit.setMinimumSize(QSize(400, 45))
        self.search_lineEdit.setMaximumSize(QSize(600, 45))
        self.search_lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color:rgb(68,71,90);\n"
"	padding: 8px;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 1px solid #c3ccdf;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.search_lineEdit)

        self.search_rover = QPushButton(self.frame_actions_rover)
        self.search_rover.setObjectName(u"search_rover")
        self.search_rover.setMinimumSize(QSize(62, 45))
        self.search_rover.setMaximumSize(QSize(62, 45))
        self.search_rover.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.search_rover)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.create_rover_btn = QPushButton(self.frame_actions_rover)
        self.create_rover_btn.setObjectName(u"create_rover_btn")
        self.create_rover_btn.setMinimumSize(QSize(60, 45))
        self.create_rover_btn.setMaximumSize(QSize(60, 45))
        self.create_rover_btn.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.create_rover_btn)


        self.verticalLayout_7.addWidget(self.frame_actions_rover)

        self.frame_table_rovers = QFrame(self.background_frame)
        self.frame_table_rovers.setObjectName(u"frame_table_rovers")
        self.frame_table_rovers.setStyleSheet(u"background-color: #282a36")
        self.frame_table_rovers.setFrameShape(QFrame.StyledPanel)
        self.frame_table_rovers.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_table_rovers)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.table_rovers = QTableWidget(self.frame_table_rovers)
        self.table_rovers.setObjectName(u"table_rovers")
        self.table_rovers.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.table_rovers.setLayoutDirection(Qt.LeftToRight)
        self.table_rovers.setStyleSheet(u"\n"
"QTableWidget{\n"
"background-color: transparent;\n"
"border : 1px  #282a36;\n"
"alternate-background-color:#525252;\n"
"gridline-color:rgb(44, 49, 58);\n"
"}\n"
"\n"
"QTableWidget::item{\n"
"border-color: rgb(44, 49, 60);\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"gridline-color: rgb(44, 49, 60);\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section{\n"
"background-color: rgb(33, 37, 43);\n"
"max-width: 30px;\n"
"border: 1px solid rgb(44, 49, 58);\n"
"border-style: none;\n"
"border-bottom: 1px solid rgb(44, 49, 60);\n"
"border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
" ")
        self.table_rovers.setShowGrid(False)
        self.table_rovers.setWordWrap(False)
        self.table_rovers.setCornerButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.table_rovers)


        self.verticalLayout_7.addWidget(self.frame_table_rovers)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout_3.addWidget(self.central_frame)

        app_pages.addWidget(self.page_rovers)
        self.page_simulation = QWidget()
        self.page_simulation.setObjectName(u"page_simulation")
        self.page_simulation.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_14 = QVBoxLayout(self.page_simulation)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.central_frame_simulation = QFrame(self.page_simulation)
        self.central_frame_simulation.setObjectName(u"central_frame_simulation")
        self.central_frame_simulation.setMinimumSize(QSize(490, 0))
        self.central_frame_simulation.setMaximumSize(QSize(490, 16777215))
        self.central_frame_simulation.setLayoutDirection(Qt.LeftToRight)
        self.central_frame_simulation.setFrameShape(QFrame.StyledPanel)
        self.central_frame_simulation.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.central_frame_simulation)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.top_frame = QFrame(self.central_frame_simulation)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.top_frame)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_run_simulation = QLabel(self.top_frame)
        self.label_run_simulation.setObjectName(u"label_run_simulation")
        self.label_run_simulation.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color:rgb(255, 255, 255);")

        self.verticalLayout_15.addWidget(self.label_run_simulation)

        self.label_descrip_simulation = QLabel(self.top_frame)
        self.label_descrip_simulation.setObjectName(u"label_descrip_simulation")
        self.label_descrip_simulation.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color:rgb(255, 255, 255);")

        self.verticalLayout_15.addWidget(self.label_descrip_simulation)


        self.verticalLayout_12.addWidget(self.top_frame)

        self.group_box_modes = QGroupBox(self.central_frame_simulation)
        self.group_box_modes.setObjectName(u"group_box_modes")
        self.group_box_modes.setMinimumSize(QSize(180, 115))
        self.group_box_modes.setMaximumSize(QSize(180, 115))
        self.group_box_modes.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.verticalLayout_16 = QVBoxLayout(self.group_box_modes)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(9, 9, -1, -1)
        self.radioButton_max_time = QRadioButton(self.group_box_modes)
        self.radioButton_max_time.setObjectName(u"radioButton_max_time")
        self.radioButton_max_time.setStyleSheet(u"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"font: 11pt \"Segoe UI\";")

        self.verticalLayout_16.addWidget(self.radioButton_max_time)

        self.radioButton_max_area = QRadioButton(self.group_box_modes)
        self.radioButton_max_area.setObjectName(u"radioButton_max_area")
        self.radioButton_max_area.setStyleSheet(u"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"font: 11pt \"Segoe UI\";")

        self.verticalLayout_16.addWidget(self.radioButton_max_area)

        self.lbl_error_mode = QLabel(self.group_box_modes)
        self.lbl_error_mode.setObjectName(u"lbl_error_mode")

        self.verticalLayout_16.addWidget(self.lbl_error_mode)


        self.verticalLayout_12.addWidget(self.group_box_modes)

        self.frame_simulation_widgets = QFrame(self.central_frame_simulation)
        self.frame_simulation_widgets.setObjectName(u"frame_simulation_widgets")
        self.frame_simulation_widgets.setMinimumSize(QSize(470, 230))
        self.frame_simulation_widgets.setMaximumSize(QSize(200, 230))
        self.frame_simulation_widgets.setStyleSheet(u"")
        self.frame_simulation_widgets.setFrameShape(QFrame.StyledPanel)
        self.frame_simulation_widgets.setFrameShadow(QFrame.Raised)
        self.fr_sim_widgets_layout = QVBoxLayout(self.frame_simulation_widgets)
        self.fr_sim_widgets_layout.setSpacing(0)
        self.fr_sim_widgets_layout.setObjectName(u"fr_sim_widgets_layout")
        self.fr_sim_widgets_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_12.addWidget(self.frame_simulation_widgets, 0, Qt.AlignLeft|Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.frame_jobs = QFrame(self.central_frame_simulation)
        self.frame_jobs.setObjectName(u"frame_jobs")
        self.frame_jobs.setMinimumSize(QSize(0, 50))
        self.frame_jobs.setFrameShape(QFrame.StyledPanel)
        self.frame_jobs.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_jobs)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_num_jobs = QLabel(self.frame_jobs)
        self.label_num_jobs.setObjectName(u"label_num_jobs")
        self.label_num_jobs.setMinimumSize(QSize(150, 0))
        self.label_num_jobs.setMaximumSize(QSize(150, 16777215))
        self.label_num_jobs.setStyleSheet(u"font: 11pt \"Segoe UI\";")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_num_jobs)

        self.cb_num_jobs = QComboBox(self.frame_jobs)
        self.cb_num_jobs.setObjectName(u"cb_num_jobs")
        self.cb_num_jobs.setMinimumSize(QSize(0, 30))
        self.cb_num_jobs.setMaximumSize(QSize(500, 30))
        self.cb_num_jobs.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.cb_num_jobs)

        self.lbl_error_num_jobs = QLabel(self.frame_jobs)
        self.lbl_error_num_jobs.setObjectName(u"lbl_error_num_jobs")
        self.lbl_error_num_jobs.setMinimumSize(QSize(0, 20))
        self.lbl_error_num_jobs.setMaximumSize(QSize(16777215, 20))

        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.lbl_error_num_jobs)


        self.horizontalLayout_4.addLayout(self.formLayout_2)


        self.verticalLayout_12.addWidget(self.frame_jobs)

        self.frame_rovers_select = QFrame(self.central_frame_simulation)
        self.frame_rovers_select.setObjectName(u"frame_rovers_select")
        self.frame_rovers_select.setMinimumSize(QSize(0, 50))
        self.frame_rovers_select.setFrameShape(QFrame.StyledPanel)
        self.frame_rovers_select.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_rovers_select)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.rover_select_gridLayout = QGridLayout()
        self.rover_select_gridLayout.setObjectName(u"rover_select_gridLayout")
        self.label_num_rovers = QLabel(self.frame_rovers_select)
        self.label_num_rovers.setObjectName(u"label_num_rovers")
        self.label_num_rovers.setStyleSheet(u"font: 11pt \"Segoe UI\";")

        self.rover_select_gridLayout.addWidget(self.label_num_rovers, 0, 2, 1, 1)

        self.add_rover_select_btn = QPushButton(self.frame_rovers_select)
        self.add_rover_select_btn.setObjectName(u"add_rover_select_btn")
        self.add_rover_select_btn.setMinimumSize(QSize(25, 0))
        self.add_rover_select_btn.setStyleSheet(u"QPushButton{\n"
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

        self.rover_select_gridLayout.addWidget(self.add_rover_select_btn, 0, 4, 1, 1)

        self.cb_rovers = QComboBox(self.frame_rovers_select)
        self.cb_rovers.setObjectName(u"cb_rovers")
        self.cb_rovers.setMinimumSize(QSize(0, 30))
        self.cb_rovers.setMaximumSize(QSize(16777215, 30))
        self.cb_rovers.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }")

        self.rover_select_gridLayout.addWidget(self.cb_rovers, 0, 1, 1, 1)

        self.label_rovers_select = QLabel(self.frame_rovers_select)
        self.label_rovers_select.setObjectName(u"label_rovers_select")
        self.label_rovers_select.setStyleSheet(u"font: 11pt \"Segoe UI\";")

        self.rover_select_gridLayout.addWidget(self.label_rovers_select, 0, 0, 1, 1)

        self.cb_num_rovers = QComboBox(self.frame_rovers_select)
        self.cb_num_rovers.setObjectName(u"cb_num_rovers")
        self.cb_num_rovers.setMinimumSize(QSize(0, 30))
        self.cb_num_rovers.setMaximumSize(QSize(16777215, 30))
        self.cb_num_rovers.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }")

        self.rover_select_gridLayout.addWidget(self.cb_num_rovers, 0, 3, 1, 1)

        self.lbl_error_rovers_select = QLabel(self.frame_rovers_select)
        self.lbl_error_rovers_select.setObjectName(u"lbl_error_rovers_select")
        self.lbl_error_rovers_select.setMinimumSize(QSize(0, 20))
        self.lbl_error_rovers_select.setMaximumSize(QSize(16777215, 20))

        self.rover_select_gridLayout.addWidget(self.lbl_error_rovers_select, 1, 0, 1, 5)


        self.horizontalLayout_3.addLayout(self.rover_select_gridLayout)


        self.verticalLayout_12.addWidget(self.frame_rovers_select)

        self.frame_rovers_selected = QFrame(self.central_frame_simulation)
        self.frame_rovers_selected.setObjectName(u"frame_rovers_selected")
        self.frame_rovers_selected.setFrameShape(QFrame.StyledPanel)
        self.frame_rovers_selected.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_rovers_selected)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_rovers_selected = QLabel(self.frame_rovers_selected)
        self.label_rovers_selected.setObjectName(u"label_rovers_selected")
        self.label_rovers_selected.setStyleSheet(u"font: 11pt \"Segoe UI\";")

        self.verticalLayout_18.addWidget(self.label_rovers_selected)

        self.textEdit_rovers_selected = QTextEdit(self.frame_rovers_selected)
        self.textEdit_rovers_selected.setObjectName(u"textEdit_rovers_selected")
        self.textEdit_rovers_selected.setMinimumSize(QSize(0, 70))
        self.textEdit_rovers_selected.setMaximumSize(QSize(16777215, 70))
        self.textEdit_rovers_selected.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.textEdit_rovers_selected.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textEdit_rovers_selected.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_18.addWidget(self.textEdit_rovers_selected)


        self.verticalLayout_12.addWidget(self.frame_rovers_selected)

        self.frame_simulate = QFrame(self.central_frame_simulation)
        self.frame_simulate.setObjectName(u"frame_simulate")
        self.frame_simulate.setMinimumSize(QSize(0, 50))
        self.frame_simulate.setMaximumSize(QSize(16777215, 50))
        self.frame_simulate.setFrameShape(QFrame.StyledPanel)
        self.frame_simulate.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_simulate)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.button_simulate = QPushButton(self.frame_simulate)
        self.button_simulate.setObjectName(u"button_simulate")
        self.button_simulate.setMinimumSize(QSize(70, 30))
        self.button_simulate.setMaximumSize(QSize(16777215, 30))
        self.button_simulate.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_5.addWidget(self.button_simulate)


        self.verticalLayout_12.addWidget(self.frame_simulate)


        self.verticalLayout_14.addWidget(self.central_frame_simulation, 0, Qt.AlignLeft|Qt.AlignTop)

        app_pages.addWidget(self.page_simulation)
        self.page_details = QWidget()
        self.page_details.setObjectName(u"page_details")
        self.verticalLayout_6 = QVBoxLayout(self.page_details)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.central_frame_details = QFrame(self.page_details)
        self.central_frame_details.setObjectName(u"central_frame_details")
        self.central_frame_details.setFrameShape(QFrame.StyledPanel)
        self.central_frame_details.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.central_frame_details)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.top_frame_details = QFrame(self.central_frame_details)
        self.top_frame_details.setObjectName(u"top_frame_details")
        self.top_frame_details.setFrameShape(QFrame.StyledPanel)
        self.top_frame_details.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.top_frame_details)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_rover_details = QLabel(self.top_frame_details)
        self.label_rover_details.setObjectName(u"label_rover_details")
        self.label_rover_details.setMinimumSize(QSize(500, 40))
        self.label_rover_details.setMaximumSize(QSize(500, 40))
        self.label_rover_details.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color:rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.label_rover_details)

        self.label_rover_det_description = QLabel(self.top_frame_details)
        self.label_rover_det_description.setObjectName(u"label_rover_det_description")
        self.label_rover_det_description.setMinimumSize(QSize(200, 30))
        self.label_rover_det_description.setMaximumSize(QSize(398, 30))
        self.label_rover_det_description.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.verticalLayout_10.addWidget(self.label_rover_det_description)

        self.frame_3 = QFrame(self.top_frame_details)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 800))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_name = QLabel(self.frame_3)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_name)

        self.label_name_changing = QLabel(self.frame_3)
        self.label_name_changing.setObjectName(u"label_name_changing")
        self.label_name_changing.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_name_changing)

        self.label_battery = QLabel(self.frame_3)
        self.label_battery.setObjectName(u"label_battery")
        self.label_battery.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_battery)

        self.label_battery_changing = QLabel(self.frame_3)
        self.label_battery_changing.setObjectName(u"label_battery_changing")
        self.label_battery_changing.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_battery_changing)

        self.label_exp_speed = QLabel(self.frame_3)
        self.label_exp_speed.setObjectName(u"label_exp_speed")
        self.label_exp_speed.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_exp_speed)

        self.label_exp_speed_changing = QLabel(self.frame_3)
        self.label_exp_speed_changing.setObjectName(u"label_exp_speed_changing")
        self.label_exp_speed_changing.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_exp_speed_changing)

        self.label_exp_dis = QLabel(self.frame_3)
        self.label_exp_dis.setObjectName(u"label_exp_dis")
        self.label_exp_dis.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_exp_dis)

        self.label_exp_dis_changing = QLabel(self.frame_3)
        self.label_exp_dis_changing.setObjectName(u"label_exp_dis_changing")
        self.label_exp_dis_changing.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_exp_dis_changing)

        self.label_trans_sp = QLabel(self.frame_3)
        self.label_trans_sp.setObjectName(u"label_trans_sp")
        self.label_trans_sp.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_trans_sp)

        self.label_trans_sp_changing = QLabel(self.frame_3)
        self.label_trans_sp_changing.setObjectName(u"label_trans_sp_changing")
        self.label_trans_sp_changing.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_trans_sp_changing)

        self.label_trans_dis = QLabel(self.frame_3)
        self.label_trans_dis.setObjectName(u"label_trans_dis")
        self.label_trans_dis.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_trans_dis)

        self.label_trans_dis_changing = QLabel(self.frame_3)
        self.label_trans_dis_changing.setObjectName(u"label_trans_dis_changing")
        self.label_trans_dis_changing.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.label_trans_dis_changing)

        self.label_charging_time = QLabel(self.frame_3)
        self.label_charging_time.setObjectName(u"label_charging_time")
        self.label_charging_time.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_charging_time)

        self.label_charging_time_changing = QLabel(self.frame_3)
        self.label_charging_time_changing.setObjectName(u"label_charging_time_changing")
        self.label_charging_time_changing.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.label_charging_time_changing)


        self.verticalLayout_11.addLayout(self.formLayout)


        self.verticalLayout_10.addWidget(self.frame_3)


        self.verticalLayout_9.addWidget(self.top_frame_details, 0, Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.central_frame_details)

        app_pages.addWidget(self.page_details)

        self.retranslateUi(app_pages)

        app_pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(app_pages)
    # setupUi

    def retranslateUi(self, app_pages):
        app_pages.setWindowTitle(QCoreApplication.translate("app_pages", u"StackedWidget", None))
        self.label_welcome.setText(QCoreApplication.translate("app_pages", u"Welcome !", None))
        self.label_description_welcome.setText(QCoreApplication.translate("app_pages", u"<html><head/><body><p>This is the application created for the System for the </p><p>exploration of caves with exploring rovers </p><p>Final Degree Project</p></body></html>", None))
        self.label_rover.setText(QCoreApplication.translate("app_pages", u"Rover", None))
        self.search_lineEdit.setPlaceholderText(QCoreApplication.translate("app_pages", u"Search by name", None))
        self.search_rover.setText(QCoreApplication.translate("app_pages", u"Search", None))
        self.create_rover_btn.setText(QCoreApplication.translate("app_pages", u"Create", None))
        self.label_run_simulation.setText(QCoreApplication.translate("app_pages", u"Run your simulation", None))
        self.label_descrip_simulation.setText(QCoreApplication.translate("app_pages", u"Please, select the following values in order to run a simulation", None))
        self.group_box_modes.setTitle(QCoreApplication.translate("app_pages", u"Mode", None))
        self.radioButton_max_time.setText(QCoreApplication.translate("app_pages", u"Maximum Time", None))
        self.radioButton_max_area.setText(QCoreApplication.translate("app_pages", u"Maximum Area", None))
        self.lbl_error_mode.setText("")
        self.label_num_jobs.setText(QCoreApplication.translate("app_pages", u"Select number of jobs:", None))
        self.lbl_error_num_jobs.setText("")
        self.label_num_rovers.setText(QCoreApplication.translate("app_pages", u"Number of rovers:", None))
        self.add_rover_select_btn.setText(QCoreApplication.translate("app_pages", u"+", None))
        self.label_rovers_select.setText(QCoreApplication.translate("app_pages", u"Select the rovers:", None))
        self.lbl_error_rovers_select.setText("")
        self.label_rovers_selected.setText(QCoreApplication.translate("app_pages", u"These are the rovers selected:", None))
        self.button_simulate.setText(QCoreApplication.translate("app_pages", u"Simulate", None))
        self.label_rover_details.setText(QCoreApplication.translate("app_pages", u"Rover details:", None))
        self.label_rover_det_description.setText(QCoreApplication.translate("app_pages", u"These are the properties of the rover chosen", None))
        self.label_name.setText(QCoreApplication.translate("app_pages", u"Name:", None))
        self.label_name_changing.setText(QCoreApplication.translate("app_pages", u"None", None))
        self.label_battery.setText(QCoreApplication.translate("app_pages", u"Battery:", None))
        self.label_battery_changing.setText(QCoreApplication.translate("app_pages", u"None", None))
        self.label_exp_speed.setText(QCoreApplication.translate("app_pages", u"Exploration speed:", None))
        self.label_exp_speed_changing.setText(QCoreApplication.translate("app_pages", u"None", None))
        self.label_exp_dis.setText(QCoreApplication.translate("app_pages", u"Exploration battery discharge:", None))
        self.label_exp_dis_changing.setText(QCoreApplication.translate("app_pages", u"None", None))
        self.label_trans_sp.setText(QCoreApplication.translate("app_pages", u"Translate speed:", None))
        self.label_trans_sp_changing.setText(QCoreApplication.translate("app_pages", u"None", None))
        self.label_trans_dis.setText(QCoreApplication.translate("app_pages", u"Translate battery discharge", None))
        self.label_trans_dis_changing.setText(QCoreApplication.translate("app_pages", u"None", None))
        self.label_charging_time.setText(QCoreApplication.translate("app_pages", u"Charging time", None))
        self.label_charging_time_changing.setText(QCoreApplication.translate("app_pages", u"None", None))
    # retranslateUi

