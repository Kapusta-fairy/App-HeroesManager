from PyQt5 import QtCore


def retranslate_ui(window):
    _translate = QtCore.QCoreApplication.translate
    window.setWindowTitle(_translate("MainWindow", "Менеджер героев"))
    window.tab_bar.setTabText(window.tab_bar.indexOf(window.tab_main), _translate("MainWindow", "Главная"))
    window.tab_bar.setTabText(window.tab_bar.indexOf(window.tab_mods), _translate("MainWindow", "Моды"))
    window.tab_bar.setTabText(window.tab_bar.indexOf(window.tab_maps), _translate("MainWindow", "Карты"))
    window.label_path_to.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Путь к Heroes of Might and Magic 5 Tribes of the East</span></p></body></html>"))
    window.button_path.setText(_translate("MainWindow", "Указать путь"))
    window.tab_bar.setTabText(window.tab_bar.indexOf(window.tab_conf), _translate("MainWindow", "Настройки"))
