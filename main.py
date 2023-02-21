from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog

from config import ManagerConfig
from retranslate import retranslate_ui


class UserInterface(QMainWindow):

    def __init__(self):
        super().__init__()
        self.central_widget = QtWidgets.QWidget(self)
        self.tab_bar = QtWidgets.QTabWidget(self.central_widget)
        self.tab_main = QtWidgets.QWidget()
        self.tab_mods = QtWidgets.QWidget()
        self.tab_maps = QtWidgets.QWidget()
        self.tab_conf = QtWidgets.QWidget()
        self.label_currently_path = QtWidgets.QLabel(self.tab_conf)
        self.label_path_to = QtWidgets.QLabel(self.tab_conf)
        self.button_path = QtWidgets.QPushButton(self.tab_conf)

        config = ManagerConfig()

        QtCore.QMetaObject.connectSlotsByName(self)

    def setup(self):
        # configuration settings
        self.setObjectName("MainWindow")
        self.setEnabled(True)
        self.resize(800, 800)
        self.setMinimumSize(QtCore.QSize(800, 800))
        self.setMaximumSize(QtCore.QSize(800, 800))
        self.setTabletTracking(False)

        # central widget
        self.central_widget.setObjectName("central_widget")
        self.setCentralWidget(self.central_widget)

        # tab bar
        self.tab_bar.setObjectName("tab_bar")
        self.tab_bar.setCurrentIndex(3)
        self.tab_bar.setGeometry(QtCore.QRect(0, 0, 801, 801))
        self.tab_bar.setAutoFillBackground(False)
        self.tab_bar.setStyleSheet(
            'background-image: url("resources/main_back.jpg");'
        )
        self.tab_bar.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab_bar.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_bar.setElideMode(QtCore.Qt.ElideNone)
        self.tab_bar.setDocumentMode(False)
        self.tab_bar.setMovable(False)

        # tab main
        self.tab_main.setObjectName("tab_main")
        self.tab_bar.addTab(self.tab_main, "")

        # tab mods
        self.tab_mods.setObjectName("tab_mods")
        self.tab_bar.addTab(self.tab_mods, "")

        # tab maps
        self.tab_maps.setObjectName("tab_maps")
        self.tab_bar.addTab(self.tab_maps, "")

        # tab config
        self.tab_conf.setObjectName("tab_conf")
        self.tab_bar.addTab(self.tab_conf, "")

        # label currently path
        self.label_currently_path.setGeometry(QtCore.QRect(100, 30, 691, 41))
        self.label_currently_path.setAlignment(QtCore.Qt.AlignCenter)
        self.label_currently_path.setObjectName("label_currently_path")

        # label path to
        self.label_path_to.setGeometry(QtCore.QRect(100, 0, 691, 21))
        self.label_path_to.setAlignment(QtCore.Qt.AlignCenter)
        self.label_path_to.setObjectName("label_path_to")

        # button path
        self.button_path.setObjectName("button_path")
        self.button_path.setGeometry(QtCore.QRect(0, 30, 101, 41))
        self.button_path.clicked.connect(self.set_heroes_directory)

        # retranslate ui
        retranslate_ui(self)

    def set_heroes_directory(self):
        dirlist = QFileDialog.getExistingDirectory(
            self,
            "Выберите папку с heroes 5",
            "."
        )
        save_config(dirlist)
        self.label_currently_path.setText(dirlist)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.setup()
    ui.show()
    sys.exit(app.exec_())
