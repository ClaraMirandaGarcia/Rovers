import os
from qt_core import *
from gui.windows.ui_pages import Ui_app_pages
from gui.components.components import CustomMenuButton, CustomToolBox, CustomPage


class UI_MainWindow(object):
    def __init__(self):
        self.home_tab_page = None

    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # Parámetros iniciales de la app, tamaño inicial, max y min
        parent.resize(1200, 720)
        parent.setMinimumSize(960, 540)

        # Define central widget
        self.central_frame = QFrame()

        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # LEFT MENU
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)

        # LEFT MENU LAYOUT
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)

        # TOP FRAME MENU
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")

        # TOP FRAME LAYOUT
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_layout.setSpacing(0)
        self.left_menu_top_layout.setAlignment(Qt.AlignTop)

        # BUTTONS LEFT MENU TOP
        self.toggle_button = CustomMenuButton(text="Hide menu",
                                              icon_path="icon_menu.svg")
        self.toggle_button.setToolTip("Open menu")
        self.button_home = CustomMenuButton(text="Home",
                                            is_active=True)
        self.button_rover_list = CustomMenuButton(text="Rover List")
        self.button_rover_creation = CustomMenuButton(text="Rover Creation")
        self.button_simulation = CustomMenuButton(text="Simulation Creation")
        self.button_simulation_list = CustomMenuButton(text="Simulation List")

        # Left Menu ToolBox
        self.sim_toolBox = CustomToolBox("sim_toolBox", self.left_menu_top_frame, self.left_menu, 24)
        self.sim_toolBox.setContentsMargins(10, 0, 0, 0)

        # page 0 -> Home
        home_tab_page = CustomPage("home_tab_page", 40, 40, self.left_menu)
        self.home_tab_page = home_tab_page.get_page()
        
        # layout
        self.home_tab_layout = QVBoxLayout(self.home_tab_page)
        self.home_tab_layout.setSpacing(0)
        self.home_tab_layout.setObjectName("home_tab_layout")
        self.home_tab_layout.setContentsMargins(0, 0, 0, 0)

        # frame of page_0
        self.frame_page_home_menu = QFrame(self.home_tab_page)
        self.frame_page_home_menu.setObjectName("frame_page_home_menu")
        self.frame_page_home_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_page_home_menu.setFrameShadow(QFrame.Raised)
        # layout of the frame
        self.frame_page_home_menu_layout = QVBoxLayout(self.frame_page_home_menu)
        self.frame_page_home_menu_layout.setSpacing(0)
        self.frame_page_home_menu_layout.setObjectName("frame_page_home_menu_layout")
        self.frame_page_home_menu_layout.setContentsMargins(0, 0, 0, 0)

        # adding a button to the frame
        self.frame_page_home_menu_layout.addWidget(self.button_home)
        # adding the frame to the page_0
        self.home_tab_layout.addWidget(self.frame_page_home_menu, 0, Qt.AlignTop)
        # adding the page_0 to the toolBox


        url = os.getcwd()
        folder = "\gui\images\icons\icon-home-2.svg"
        path = url + folder
        icono = self.aux_paint_icon(path)
        ret = self.sim_toolBox.addItem(self.home_tab_page, icono, u"    Home  ")

        # extra pages for the dropdown menu
        page_1 = CustomPage("rover_management_menu", 40, 40, self.left_menu)
        self.page_1 = page_1.get_page()

        # layout
        self.page_layout = QVBoxLayout(self.page_1)
        self.page_layout.setSpacing(0)
        self.page_layout.setObjectName("page_layout")
        self.page_layout.setContentsMargins(0, 0, 0, 0)

        # frame of page_1
        self.fr_page_menu = QFrame(self.page_1)
        self.fr_page_menu.setObjectName("frame_page_menu")
        self.fr_page_menu.setFrameShape(QFrame.StyledPanel)
        self.fr_page_menu.setFrameShadow(QFrame.Raised)

        # layout of the frame
        self.fr_page_menu_layout = QVBoxLayout(self.fr_page_menu)
        self.fr_page_menu_layout.setSpacing(0)
        self.fr_page_menu_layout.setObjectName("fr_page_menu_layout")
        self.fr_page_menu_layout.setContentsMargins(0, 0, 0, 0)

        # adding a button to the frame
        self.fr_page_menu_layout.addWidget(self.button_rover_list)
        self.fr_page_menu_layout.addWidget(self.button_rover_creation)

        # adding the frame to the page_1
        self.page_layout.addWidget(self.fr_page_menu, 0, Qt.AlignTop)

        # adding the page_1 to the toolBox
        url = os.getcwd()
        folder = "\gui\images\icons\icon_moon_rover.svg"
        path = url + folder
        icono = self.aux_paint_icon(path)
        self.sim_toolBox.addItem(self.page_1, icono, u"   Rover Management")

        page_2 = CustomPage("sim_management_menu", 40, 40, self.left_menu)
        self.page_2 = page_2.get_page()
        # layout
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(0)
        self.page_2_layout.setObjectName("page_2_layout")
        self.page_2_layout.setContentsMargins(0, 0, 0, 0)
        # frame of page_2
        self.fr_page_menu_2 = QFrame(self.page_2)
        self.fr_page_menu_2.setObjectName("frame_page_menu")
        self.fr_page_menu_2.setFrameShape(QFrame.StyledPanel)
        self.fr_page_menu_2.setFrameShadow(QFrame.Raised)
        # layout of the frame
        self.fr_page_menu_2_layout = QVBoxLayout(self.fr_page_menu_2)
        self.fr_page_menu_2_layout.setSpacing(0)
        self.fr_page_menu_2_layout.setObjectName("fr_page_menu_2_layout")
        self.fr_page_menu_2_layout.setContentsMargins(0, 0, 0, 0)

        # adding a button to the frame
        self.fr_page_menu_2_layout.addWidget(self.button_simulation_list)
        self.fr_page_menu_2_layout.addWidget(self.button_simulation)
        # adding the frame to the page_2
        self.page_2_layout.addWidget(self.fr_page_menu_2, 0, Qt.AlignTop)
        # adding the page_2 to the toolBox
        url = os.getcwd()
        folder = "\gui\images\icons\icon_settings.svg"
        path = url + folder
        icono = self.aux_paint_icon(path)
        self.sim_toolBox.addItem(self.page_2, icono, u"   Simulation Management")

        # Closing
        self.page_3 = QWidget()
        self.page_3.setObjectName("closing_tab")
        # layout
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setSpacing(0)
        self.page_3_layout.setObjectName("page_3_layout")
        self.page_3_layout.setContentsMargins(0, 0, 0, 0)
        # frame of page_3
        self.fr_closing_tab = QFrame(self.page_3)
        self.fr_closing_tab.setObjectName("frame_closing_tab")
        self.fr_closing_tab.setFrameShape(QFrame.StyledPanel)
        self.fr_closing_tab.setFrameShadow(QFrame.Raised)
        # layout of the frame
        self.fr_closing_tab_layout = QVBoxLayout(self.fr_closing_tab)
        self.fr_closing_tab_layout.setSpacing(0)
        self.fr_closing_tab_layout.setObjectName("fr_closing_tab_layout")
        self.fr_closing_tab_layout.setContentsMargins(0, 0, 0, 0)

        # adding the frame to the page_3
        self.page_3_layout.addWidget(self.fr_closing_tab, 0, Qt.AlignTop)
        # adding the page_3 to the toolBox
        url = os.getcwd()
        folder = "\gui\images\icons\icon_up_arrow.svg"
        path = url + folder
        icono = self.aux_paint_icon(path)
        self.sim_toolBox.addItem(self.page_3, icono, u"   ")
        self.sim_toolBox.setItemToolTip(3, "Close the menu")


        # ADDING BUTTONS TO LAYOUT
        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.sim_toolBox)
        self.sim_toolBox.setCurrentIndex(0)

        # SPACER
        self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # LEFT BOTTOM FRAME MENU
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(40)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")

        # BOTTOM FRAME LAYOUT
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bottom_layout.setSpacing(0)

        # ADDING TO LAYOUT
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)

        # CONTENT
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # App pages
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2;")
        self.ui_pages = Ui_app_pages()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.page_initial)

        # self bottom bar
        self.bottom_bar = QFrame()
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10, 0, 10, 0)

        self.bottom_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # bottom label right
        self.bottom_label_right = QLabel("2022")
        self.bottom_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

        # Add to layout
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_label_right)

        # adding to the content layout
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        # adding the widgets
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        parent.setCentralWidget(self.central_frame)

    def aux_paint_icon(self, path):
        iconn = QIcon()
        iconn.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
        color = QColor(195, 204, 223)
        pixmap = QPixmap(path)
        painter = QPainter(pixmap)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.setBrush(color)
        painter.setPen(color)
        painter.drawRect(pixmap.rect())
        painter.end()
        icono = QIcon(pixmap)

        return icono