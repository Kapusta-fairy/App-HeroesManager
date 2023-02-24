import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFileDialog

from config import Config
from game_files import Mods
from retranslate import retranslate_ui


class UserInterface(QMainWindow):

    def __init__(self):
        super().__init__()
        self.central_widget = QtWidgets.QWidget(self)
        self.tab_bar = QtWidgets.QTabWidget(self.central_widget)

        self.tab_main = QtWidgets.QWidget()

        self.mods = Mods()
        self.tab_mods = QtWidgets.QWidget()
        self.mods_widget = QtWidgets.QWidget(self.tab_mods)
        self.vertical_Layout_widget = QtWidgets.QWidget(self.tab_mods)
        self.mods_layout = QtWidgets.QVBoxLayout(self.vertical_Layout_widget)

        self.tab_maps = QtWidgets.QWidget()

        self.tab_conf = QtWidgets.QWidget()
        self.label_currently_path = QtWidgets.QLabel(self.tab_conf)
        self.label_path_to = QtWidgets.QLabel(self.tab_conf)
        self.button_path = QtWidgets.QPushButton(self.tab_conf)

        self.config = Config()
        QtCore.QMetaObject.connectSlotsByName(self)

    def setup(self):
        self.setup_window()
        self.setup_central_widget()
        self.setup_tab_bar()
        retranslate_ui(self)

    def setup_window(self):
        self.setObjectName("MainWindow")
        self.setEnabled(True)
        self.resize(800, 800)
        self.setMinimumSize(QtCore.QSize(800, 800))
        self.setMaximumSize(QtCore.QSize(800, 800))
        self.setTabletTracking(False)

    def setup_central_widget(self):
        self.central_widget.setObjectName("central_widget")
        self.setCentralWidget(self.central_widget)

    def setup_tab_bar(self):
        self.tab_bar.setObjectName("tab_bar")
        self.tab_bar.setCurrentIndex(3)
        self.tab_bar.setGeometry(QtCore.QRect(0, 0, 801, 801))
        self.tab_bar.setAutoFillBackground(False)

        self.tab_bar.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab_bar.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_bar.setElideMode(QtCore.Qt.ElideNone)
        self.tab_bar.setDocumentMode(False)
        self.tab_bar.setMovable(False)

        self.setup_tab_main()
        self.setup_tab_mods()
        self.setup_tab_maps()
        self.setup_tab_config()

    def setup_tab_main(self):
        self.tab_main.setObjectName("tab_main")
        self.tab_bar.addTab(self.tab_main, "")

    def setup_tab_mods(self):
        self.tab_mods.setObjectName("tab_mods")
        self.tab_bar.addTab(self.tab_mods, "")

        # mods widget
        self.mods_widget.setGeometry(QtCore.QRect(520, 9, 261, 751))
        self.mods_widget.setObjectName("mods_widget")

        # vertical_Layout_widget
        self.vertical_Layout_widget.setGeometry(QtCore.QRect(520, 9, 261, 751))
        self.vertical_Layout_widget.setObjectName("vertical_Layout_widget")

        # mods layout
        self.mods_layout.setContentsMargins(10, 10, 10, 10)
        self.mods_layout.setObjectName("mods_layout")

        enabled_list = self.mods.get_enabled_list()
        disabled_list = self.mods.get_disabled_list()

        for mod in enabled_list:
            index = enabled_list.index(mod)
            self.create_check_box(index, mod)
            exec(f'self.check_box_{index}.setChecked(True)')

        for mod in disabled_list:
            index = enabled_list.index(mod)
            self.create_check_box(index, mod)

    def create_check_box(self, index, item):
        # func = exec(f"""def state_change_{index}(self, state):
        #              if state == Qt.Checked:
        #                  self.mods.enable({item})
        #              else:
        #                  self.mods.disable(mod)
        #              func = state_change_{index}"""
        #             )
        #
        # exec(f'self.state_change_{index} = state_change_{index}')
        exec(f'self.check_box_{index} = QtWidgets.QCheckBox(self.vertical_Layout_widget)')
        exec(f'self.check_box_{index}.setObjectName("check_box_{index}")')
        # exec(f'self.check_box_{index}.stateChanged.connect(self.state_change_{index})')
        exec(f'self.mods_layout.addWidget(self.check_box_{index})')

    def setup_tab_maps(self):
        self.tab_maps.setObjectName("tab_maps")
        self.tab_bar.addTab(self.tab_maps, "")

    def setup_tab_config(self):
        self.tab_conf.setObjectName("tab_conf")
        self.tab_bar.addTab(self.tab_conf, "")

        # label currently path
        self.label_currently_path.setGeometry(QtCore.QRect(100, 30, 691, 41))
        self.label_currently_path.setAlignment(QtCore.Qt.AlignCenter)
        self.label_currently_path.setObjectName("label_currently_path")
        self.label_currently_path.setText(
            self.config.get().get('settings', 'path')
        )

        # label path to
        self.label_path_to.setGeometry(QtCore.QRect(100, 0, 691, 21))
        self.label_path_to.setAlignment(QtCore.Qt.AlignCenter)
        self.label_path_to.setObjectName("label_path_to")

        # button path
        self.button_path.setObjectName("button_path")
        self.button_path.setGeometry(QtCore.QRect(0, 30, 101, 41))
        self.button_path.clicked.connect(self.set_heroes_directory)

    def set_heroes_directory(self):
        dirlist = QFileDialog.getExistingDirectory(
            self,
            "Выберите папку с heroes 5",
            "."
        )
        self.config.save(dirlist)
        self.label_currently_path.setText(dirlist)





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    with open("style.qss", "r") as qss:
        app.setStyleSheet(qss.read())

    ui = UserInterface()
    ui.setup()
    ui.show()

    sys.exit(app.exec_())
