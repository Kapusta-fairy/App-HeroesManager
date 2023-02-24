from PyQt5 import QtCore

from game_files import Mods


def retranslate_ui(window):
    _translate = QtCore.QCoreApplication.translate

    mods = Mods()
    enabled_list = mods.get_enabled_list()
    disabled_list = mods.get_disabled_list()

    for mod in enabled_list:
        index = enabled_list.index(mod)
        exec(f'window.check_box_{index}.setText(_translate("MainWindow", f"{mod[:-4]}"))')

    for mod in disabled_list:
        index = enabled_list.index(mod)
        exec(f'window.check_box_{index}.setText(_translate("MainWindow", f"{mod[:-4]}"))')

    window.setWindowTitle(_translate("MainWindow", "Менеджер героев"))
    window.tab_bar.setTabText(window.tab_bar.indexOf(window.tab_main), _translate("MainWindow", "Главная"))
    window.tab_bar.setTabText(window.tab_bar.indexOf(window.tab_mods), _translate("MainWindow", "Моды"))
    window.tab_bar.setTabText(window.tab_bar.indexOf(window.tab_maps), _translate("MainWindow", "Карты"))
    window.label_path_to.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Путь к Heroes of Might and Magic 5 Tribes of the East</span></p></body></html>"))
    window.button_path.setText(_translate("MainWindow", "Указать путь"))
    window.tab_bar.setTabText(window.tab_bar.indexOf(window.tab_conf), _translate("MainWindow", "Настройки"))

    # todo: сделать наименования для модов и карт
