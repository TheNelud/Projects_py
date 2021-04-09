from PyQt5.QtWidgets import *
import openpyxl
from PyQt5 import QtCore


class MenuBar(QMainWindow):
    def __init__(self, parent):
        # super(QMainWindow, self).__init__(parent)
        QMainWindow.__init__(self)

        self.menuBar = QMenuBar(self)
        #self.setMenuBar(self.menuBar)

        self.fileMenu = QMenu("&Файл", self)
        self.menuBar.addMenu(self.fileMenu)

        self.fileMenu.addAction("Открыть", self.action_clicked)
        self.fileMenu.addAction("Сохранить", self.action_clicked)

    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()
        if action.text() == "Открыть":  # Отработка нажатия кнопки Отркрыть
            open_file = QFileDialog.getOpenFileName(self)[0]  # Открытия меню выбора файла

            try:
                book = openpyxl.open(open_file, read_only=True)  # Подключаем openpyxl, выбираем файл xlsx

            except FileNotFoundError:  # Проверка на невыбраный файл
                print("No such file")

        elif action.text() == "Сохранить":  # Отработка нажатия кнопки Сохранить
            print("Save")
            # save_file = QFileDialog.getSaveFileName(self)[0]