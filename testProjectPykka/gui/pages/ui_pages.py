# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesvTuJxh.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_app_pages(object):
    def setupUi(self, app_pages):
        if not app_pages.objectName():
            app_pages.setObjectName(u"app_pages")
        app_pages.resize(722, 922)
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
        self.verticalLayout_2 = QVBoxLayout(self.page_create_rover)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.page_create_rover)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 35))
        self.label_12.setMaximumSize(QSize(16777215, 35))
        self.label_12.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color:rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.label_12)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_10.addWidget(self.label_13, 0, 0, 1, 1)

        self.name_lineEdit = QLineEdit(self.frame_2)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color:rgb(68,71,90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout_10.addWidget(self.name_lineEdit, 0, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_10)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.trans_dis_lineEdit = QLineEdit(self.frame_2)
        self.trans_dis_lineEdit.setObjectName(u"trans_dis_lineEdit")
        self.trans_dis_lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color:rgb(68,71,90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout_13.addWidget(self.trans_dis_lineEdit, 0, 1, 1, 1)

        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_13.addWidget(self.label_16, 0, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_13)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_11.addWidget(self.label_14, 0, 0, 1, 1)

        self.exp_dis_lineEdit = QLineEdit(self.frame_2)
        self.exp_dis_lineEdit.setObjectName(u"exp_dis_lineEdit")
        self.exp_dis_lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color:rgb(68,71,90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout_11.addWidget(self.exp_dis_lineEdit, 0, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_11)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_14.addWidget(self.label_17, 0, 0, 1, 1)

        self.bat_lineEdit = QLineEdit(self.frame_2)
        self.bat_lineEdit.setObjectName(u"bat_lineEdit")
        self.bat_lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color:rgb(68,71,90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout_14.addWidget(self.bat_lineEdit, 0, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_14)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_9.addWidget(self.label_11, 0, 0, 1, 1)

        self.ch_time_lineEdit = QLineEdit(self.frame_2)
        self.ch_time_lineEdit.setObjectName(u"ch_time_lineEdit")
        self.ch_time_lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color:rgb(68,71,90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout_9.addWidget(self.ch_time_lineEdit, 0, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_9)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_12.addWidget(self.label_15, 0, 0, 1, 1)

        self.trans_sp_lineEdit = QLineEdit(self.frame_2)
        self.trans_sp_lineEdit.setObjectName(u"trans_sp_lineEdit")
        self.trans_sp_lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color:rgb(68,71,90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout_12.addWidget(self.trans_sp_lineEdit, 0, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_12)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.exp_sp_lineEdit = QLineEdit(self.frame_2)
        self.exp_sp_lineEdit.setObjectName(u"exp_sp_lineEdit")
        self.exp_sp_lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color:rgb(68,71,90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"")

        self.gridLayout_15.addWidget(self.exp_sp_lineEdit, 0, 1, 1, 1)

        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_15.addWidget(self.label_18, 0, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_15)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.createButton = QPushButton(self.frame_2)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setMinimumSize(QSize(60, 35))
        self.createButton.setMaximumSize(QSize(60, 35))
        self.createButton.setStyleSheet(u"QPushButton{\n"
"	background-color :rgb(67,133,200);\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(85,170,225);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255,0,127);\n"
"}")

        self.gridLayout_2.addWidget(self.createButton, 0, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_2)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignHCenter)

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
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.search_lineEdit)

        self.search_rover = QPushButton(self.frame_actions_rover)
        self.search_rover.setObjectName(u"search_rover")
        self.search_rover.setMinimumSize(QSize(60, 45))
        self.search_rover.setMaximumSize(QSize(60, 45))
        self.search_rover.setStyleSheet(u"QPushButton{\n"
"	background-color :rgb(67,133,200);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(85,170,225);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255,0,127);\n"
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
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(85,170,225);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255,0,127);\n"
"}")

        self.horizontalLayout.addWidget(self.create_rover_btn)


        self.verticalLayout_7.addWidget(self.frame_actions_rover)

        self.frame_table_rovers = QFrame(self.background_frame)
        self.frame_table_rovers.setObjectName(u"frame_table_rovers")
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
        self.table_rovers.setShowGrid(True)

        self.horizontalLayout_2.addWidget(self.table_rovers)


        self.verticalLayout_7.addWidget(self.frame_table_rovers)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout_3.addWidget(self.central_frame)

        app_pages.addWidget(self.page_rovers)
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

        app_pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(app_pages)
    # setupUi

    def retranslateUi(self, app_pages):
        app_pages.setWindowTitle(QCoreApplication.translate("app_pages", u"StackedWidget", None))
        self.label_welcome.setText(QCoreApplication.translate("app_pages", u"Welcome !", None))
        self.label_description_welcome.setText(QCoreApplication.translate("app_pages", u"<html><head/><body><p>This is the application created for the System for the </p><p>exploration of caves with exploring rovers </p><p>Final Degree Project</p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("app_pages", u"Create your own rover:", None))
        self.label_13.setText(QCoreApplication.translate("app_pages", u"Name:", None))
        self.label_16.setText(QCoreApplication.translate("app_pages", u"Translate battery discharge:", None))
        self.label_14.setText(QCoreApplication.translate("app_pages", u"Exploring battery discharge:", None))
        self.label_17.setText(QCoreApplication.translate("app_pages", u"Battery:", None))
        self.label_11.setText(QCoreApplication.translate("app_pages", u"Charging time:", None))
        self.label_15.setText(QCoreApplication.translate("app_pages", u"Translate speed:", None))
        self.label_18.setText(QCoreApplication.translate("app_pages", u"Exploration speed:", None))
        self.createButton.setText(QCoreApplication.translate("app_pages", u"Create", None))
        self.label_rover.setText(QCoreApplication.translate("app_pages", u"Rover", None))
        self.search_lineEdit.setPlaceholderText(QCoreApplication.translate("app_pages", u"Search by name", None))
        self.search_rover.setText(QCoreApplication.translate("app_pages", u"Search", None))
        self.create_rover_btn.setText(QCoreApplication.translate("app_pages", u"Create", None))
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

