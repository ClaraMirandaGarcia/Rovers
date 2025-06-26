from gui.components.components import *
from qt_core import *


class DetailsRoverPageView(QWidget):
    def __init__(self, parent=None, ui=None):
        super().__init__(parent)
        self.ui = ui

        # check if create page_1 is created
        to_create = self.ui.page_details.findChild(QFrame, "central_frame_details")
        if to_create is None:
            self.initialize_gui()

    def initialize_gui(self):
        # Container frame
        self.ui.details_container_frame = QFrame(self.ui.page_details)
        self.ui.details_container_frame.setObjectName(u"details_container_frame")
        self.ui.details_container_frame.setFrameShape(QFrame.StyledPanel)
        self.ui.details_container_frame.setFrameShadow(QFrame.Raised)

        self.ui.details_container_layout = QHBoxLayout(self.ui.details_container_frame)
        self.ui.details_container_layout.setObjectName(u"details_container_layout")
        self.ui.details_container_layout.setAlignment(Qt.AlignTop)

        # Frame return button
        self.ui.frame_return_details = QFrame(self.ui.details_container_frame)
        self.ui.frame_return_details.setObjectName(u"frame_return_details")
        self.ui.frame_return_details.setFrameShape(QFrame.StyledPanel)
        self.ui.frame_return_details.setFrameShadow(QFrame.Raised)
        self.ui.frame_return_details.setContentsMargins(0, 0, 0, 0)
        self.ui.frame_return_details.setMinimumHeight(50)
        self.ui.frame_return_details.setMaximumHeight(50)
        self.ui.return_details_layout = QVBoxLayout(self.ui.frame_return_details)
        self.ui.return_details_layout.setObjectName(u"return_details_layout")

        # return button
        # Frame return button
        self.ui.return_button_details = CustomReturnButton(self.ui, self.ui.frame_return_details,
                                                           self.ui.page_rovers, "return_button_details")

        self.ui.return_details_layout.addWidget(self.ui.return_button_details)
        self.ui.details_container_layout.addWidget(self.ui.frame_return_details)
        self.ui.page_details_rover_layout.addWidget(self.ui.details_container_frame)

        # Central frame
        self.ui.central_frame_details = QFrame(self.ui.details_container_frame)
        self.ui.central_frame_details.setObjectName(u"central_frame_details")
        self.ui.central_frame_details.setFrameShape(QFrame.StyledPanel)
        self.ui.central_frame_details.setFrameShadow(QFrame.Raised)
        self.ui.central_frame_details.setMinimumSize(QSize(600, 600))
        self.ui.central_frame_details.setMaximumSize(QSize(600, 600))

        self.ui.central_layout_details = QVBoxLayout(self.ui.central_frame_details)
        self.ui.central_layout_details.setObjectName(u"central_layout_details")
        self.ui.central_layout_details.setAlignment(Qt.AlignTop)
        self.ui.central_layout_details.setSpacing(10)

        # Title labels
        self.ui.label_rover_details = QLabel(self.ui.central_frame_details)
        self.ui.label_rover_details.setObjectName(u"label_rover_details")
        self.ui.label_rover_details.setMinimumSize(QSize(0, 35))
        self.ui.label_rover_details.setMaximumSize(QSize(16777215, 35))
        self.ui.label_rover_details.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
                                                  "color:rgb(255, 255, 255);")
        # Adding label details rover
        self.ui.central_layout_details.addWidget(self.ui.label_rover_details)

        # Creating the form
        self.ui.frame_form_details = QFrame(self.ui.central_frame_details)
        self.ui.frame_form_details.setObjectName(u"frame_form_details")
        self.ui.frame_form_details.setMinimumSize(QSize(500, 500))
        self.ui.frame_form_details.setMaximumSize(QSize(500, 500))
        self.ui.frame_form_details.setStyleSheet(u"	border-radius: 5px;\n")
                                                 #"	border: 1px solid rgb(255, 255, 255);\n")
        self.ui.frame_form_details.setFrameShape(QFrame.StyledPanel)
        self.ui.frame_form_details.setFrameShadow(QFrame.Raised)

        self.ui.form_layout_details = QFormLayout(self.ui.frame_form_details)
        self.ui.form_layout_details.setObjectName(u"form_layout_details")
        self.ui.form_layout_details.setSpacing(30)

        self.ui.label_name = QLabel(self.ui.frame_form_details)
        self.ui.label_name.setObjectName(u"label_name")
        self.ui.label_name.setMinimumSize(QSize(225, 30))
        self.ui.label_name.setMaximumSize(QSize(225, 30))
        self.ui.label_name.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
                                         "border: 0px;")

        self.ui.form_layout_details.setWidget(0, QFormLayout.LabelRole, self.ui.label_name)

        self.ui.label_name_changing = QLabel(self.ui.frame_form_details)
        self.ui.label_name_changing.setMinimumSize(QSize(225, 30))
        self.ui.label_name_changing.setMaximumSize(QSize(225, 30))
        self.ui.label_name_changing.setObjectName(u"label_name_changing")
        self.ui.label_name_changing.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
                                                  "border: 0px;\n"
                                                  "background-color: rgb(27, 29, 35);")

        self.ui.form_layout_details.setWidget(0, QFormLayout.FieldRole, self.ui.label_name_changing)

        self.ui.label_battery = QLabel(self.ui.frame_form_details)
        self.ui.label_battery.setMinimumSize(QSize(225, 30))
        self.ui.label_battery.setMaximumSize(QSize(225, 30))
        self.ui.label_battery.setObjectName(u"label_battery")
        self.ui.label_battery.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
                                            "border: 0px;")

        self.ui.form_layout_details.setWidget(1, QFormLayout.LabelRole, self.ui.label_battery)

        self.ui.label_battery_changing = QLabel(self.ui.frame_form_details)
        self.ui.label_battery_changing.setMinimumSize(QSize(225, 30))
        self.ui.label_battery_changing.setMaximumSize(QSize(225, 30))
        self.ui.label_battery_changing.setObjectName(u"label_battery_changing")
        self.ui.label_battery_changing.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
                                                     "border: 0px;\n"
                                                     "background-color: rgb(27, 29, 35);")

        self.ui.form_layout_details.setWidget(1, QFormLayout.FieldRole, self.ui.label_battery_changing)

        self.ui.label_exp_speed = QLabel(self.ui.frame_form_details)
        self.ui.label_exp_speed.setMinimumSize(QSize(225, 30))
        self.ui.label_exp_speed.setMaximumSize(QSize(225, 30))
        self.ui.label_exp_speed.setObjectName(u"label_exp_speed")
        self.ui.label_exp_speed.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
                                              "border: 0px;")

        self.ui.form_layout_details.setWidget(2, QFormLayout.LabelRole, self.ui.label_exp_speed)

        self.ui.label_exp_speed_changing = QLabel(self.ui.frame_form_details)
        self.ui.label_exp_speed_changing.setMinimumSize(QSize(225, 30))
        self.ui.label_exp_speed_changing.setMaximumSize(QSize(225, 30))
        self.ui.label_exp_speed_changing.setObjectName(u"label_exp_speed_changing")
        self.ui.label_exp_speed_changing.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
                                                       "border: 0px;\n"
                                                       "background-color: rgb(27, 29, 35);")

        self.ui.form_layout_details.setWidget(2, QFormLayout.FieldRole, self.ui.label_exp_speed_changing)

        self.ui.label_exp_dis = QLabel(self.ui.frame_form_details)
        self.ui.label_exp_dis.setMinimumSize(QSize(225, 30))
        self.ui.label_exp_dis.setMaximumSize(QSize(225, 30))
        self.ui.label_exp_dis.setObjectName(u"label_exp_dis")
        self.ui.label_exp_dis.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
                                            "border: 0px;")

        self.ui.form_layout_details.setWidget(3, QFormLayout.LabelRole, self.ui.label_exp_dis)

        self.ui.label_exp_dis_changing = QLabel(self.ui.frame_form_details)
        self.ui.label_exp_dis_changing.setMinimumSize(QSize(225, 30))
        self.ui.label_exp_dis_changing.setMaximumSize(QSize(225, 30))
        self.ui.label_exp_dis_changing.setObjectName(u"label_exp_dis_changing")
        self.ui.label_exp_dis_changing.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
                                                     "border: 0px;\n"
                                                     "background-color: rgb(27, 29, 35);")

        self.ui.form_layout_details.setWidget(3, QFormLayout.FieldRole, self.ui.label_exp_dis_changing)

        self.ui.label_trans_sp = QLabel(self.ui.frame_form_details)
        self.ui.label_trans_sp.setMinimumSize(QSize(225, 30))
        self.ui.label_trans_sp.setMaximumSize(QSize(225, 30))
        self.ui.label_trans_sp.setObjectName(u"label_trans_sp")
        self.ui.label_trans_sp.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
                                             "border: 0px;")

        self.ui.form_layout_details.setWidget(4, QFormLayout.LabelRole, self.ui.label_trans_sp)

        self.ui.label_trans_sp_changing = QLabel(self.ui.frame_form_details)
        self.ui.label_trans_sp_changing.setMinimumSize(QSize(225, 30))
        self.ui.label_trans_sp_changing.setMaximumSize(QSize(225, 30))
        self.ui.label_trans_sp_changing.setObjectName(u"label_trans_sp_changing")
        self.ui.label_trans_sp_changing.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
                                                      "border: 0px;\n"
                                                      "background-color: rgb(27, 29, 35);")

        self.ui.form_layout_details.setWidget(4, QFormLayout.FieldRole, self.ui.label_trans_sp_changing)

        self.ui.label_trans_dis = QLabel(self.ui.frame_form_details)
        self.ui.label_trans_dis.setMinimumSize(QSize(225, 30))
        self.ui.label_trans_dis.setMaximumSize(QSize(225, 30))
        self.ui.label_trans_dis.setObjectName(u"label_trans_dis")
        self.ui.label_trans_dis.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
                                              "border: 0px;")

        self.ui.form_layout_details.setWidget(5, QFormLayout.LabelRole, self.ui.label_trans_dis)

        self.ui.label_trans_dis_changing = QLabel(self.ui.frame_form_details)
        self.ui.label_trans_dis_changing.setMinimumSize(QSize(225, 30))
        self.ui.label_trans_dis_changing.setMaximumSize(QSize(225, 30))
        self.ui.label_trans_dis_changing.setObjectName(u"label_trans_dis_changing")
        self.ui.label_trans_dis_changing.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
                                                       "border: 0px;\n"
                                                       "background-color: rgb(27, 29, 35);")

        self.ui.form_layout_details.setWidget(5, QFormLayout.FieldRole, self.ui.label_trans_dis_changing)

        self.ui.label_charging_time = QLabel(self.ui.frame_form_details)
        self.ui.label_charging_time.setMinimumSize(QSize(225, 30))
        self.ui.label_charging_time.setMaximumSize(QSize(225, 30))
        self.ui.label_charging_time.setObjectName(u"label_charging_time")
        self.ui.label_charging_time.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
                                                  "border: 0px;")

        self.ui.form_layout_details.setWidget(6, QFormLayout.LabelRole, self.ui.label_charging_time)

        self.ui.label_charging_time_changing = QLabel(self.ui.frame_form_details)
        self.ui.label_name_changing.setMinimumSize(QSize(225, 30))
        self.ui.label_name_changing.setMaximumSize(QSize(225, 30))
        self.ui.label_charging_time_changing.setObjectName(u"label_charging_time_changing")
        self.ui.label_charging_time_changing.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
                                                           "border: 0px;\n"
                                                           "background-color: rgb(27, 29, 35);")

        self.ui.form_layout_details.setWidget(6, QFormLayout.FieldRole, self.ui.label_charging_time_changing)

        self.ui.central_layout_details.addWidget(self.ui.frame_form_details)
        # Add vertical spacer for verticalLayout_frame_details
        self.ui.vertical_spacer_details = QSpacerItem(0, 190, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.ui.central_layout_details.addItem(self.ui.vertical_spacer_details)
        self.ui.page_details_rover_layout.addWidget(self.ui.central_frame_details, 0, Qt.AlignHCenter)

        self.retranslateUi()

    def retranslateUi(self):
        self.ui.label_rover_details.setText(QCoreApplication.translate("app_pages", u"Rover details:", None))
        self.ui.label_name.setText(QCoreApplication.translate("app_pages", u"Rover's name:", None))
        self.ui.label_name_changing.setText(QCoreApplication.translate("app_pages", u"None", None))
        self.ui.label_battery.setText(QCoreApplication.translate("app_pages", u"Battery capacity (Wh):", None))
        self.ui.label_battery_changing.setText(QCoreApplication.translate("app_pages", u"None", None))
        self.ui.label_exp_speed.setText(QCoreApplication.translate("app_pages", u"Exploration speed (m/min):", None))
        self.ui.label_exp_speed_changing.setText(QCoreApplication.translate("app_pages", u"None", None))
        self.ui.label_exp_dis.setText(
            QCoreApplication.translate("app_pages", u"Exploration battery discharge (W):", None))
        self.ui.label_exp_dis_changing.setText(QCoreApplication.translate("app_pages", u"None", None))
        self.ui.label_trans_sp.setText(QCoreApplication.translate("app_pages", u"Translate speed (m/min):", None))
        self.ui.label_trans_sp_changing.setText(QCoreApplication.translate("app_pages", u"None", None))
        self.ui.label_trans_dis.setText(
            QCoreApplication.translate("app_pages", u"Translate battery discharge (W):", None))
        self.ui.label_trans_dis_changing.setText(QCoreApplication.translate("app_pages", u"None", None))
        self.ui.label_charging_time.setText(
            QCoreApplication.translate("app_pages", u"Recharging time (minutes):", None))
        self.ui.label_charging_time_changing.setText(QCoreApplication.translate("app_pages", u"None", None))
    # retranslateUi
