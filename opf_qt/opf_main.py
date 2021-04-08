from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from opf_tabs import MyTabWidget
import openpyxl, os

# Наследуемся от QMainWindow
class MainWindow(QMainWindow):
    # Переопределяем конструктор класса
    def __init__(self):
        QMainWindow.__init__(self)                                  # Обязательно нужно вызвать метод супер класса

        self.setMinimumSize(QSize(800, 600))                        # Устанавливаем размеры
        self.setWindowTitle("Оценка ОПФ")                           # Устанавливаем заголовок окна

        self.central_widget = QWidget(self)                         # Создаём центральный виджет
        self.setCentralWidget(self.central_widget)                  # Устанавливаем центральный виджет

        self.tab_widget = MyTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        self.createMenuBar()

    def createMenuBar(self):                                        #создание менюбара

        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        fileMenu = QMenu("&Файл", self)
        self.menuBar.addMenu(fileMenu)

        fileMenu.addAction("Открыть", self.action_clicked)
        fileMenu.addAction("Сохранить", self.action_clicked)

    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()
        if action.text() == "Открыть":                              #Отработка нажатия кнопки Отркрыть
            open_file = QFileDialog.getOpenFileName(self)[0]        #Открытия меню выбора файла

            try:
                book = openpyxl.open(open_file, read_only=True)     #Подключаем openpyxl, выбираем файл xlsx
                header_list_first = []
                data_list_first = []

                sheet_first = book.worksheets[0]                    # Работаем с первым листом
                sheet_second = book.worksheets[1]                   # Работаем со вторым листом
                sheet_third = book.worksheets[2]                    # Работаем с третьим листом
                sheet_fourth = book.worksheets[3]                   # Работаем с четвертым листом
                sheet_fifth = book.worksheets[4]                    # Работаем с пятым листом

            except FileNotFoundError:                               #Проверка на невыбраный файл
                print("No such file")



        elif action.text() == "Сохранить":                          #Отработка нажатия кнопки Сохранить
            print("Save")
            # save_file = QFileDialog.getSaveFileName(self)[0]







if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())