from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from opf_tabs import MyTabWidget
from opf_menubar import MenuBar


# Наследуемся от QMainWindow
class MainWindow(QMainWindow):
    # Переопределяем конструктор класса
    def __init__(self):
        QMainWindow.__init__(self)                                  # Обязательно нужно вызвать метод супер класса

        self.setMinimumSize(QSize(800, 600))                        # Устанавливаем размеры
        self.setWindowTitle("Оценка ОПФ")                           # Устанавливаем заголовок окна

        self.central_widget = QWidget(self)                         # Создаём центральный виджет
        self.setCentralWidget(self.central_widget)                  # Устанавливаем центральный виджет

        self.menubar_widgets = MenuBar(self)
        self.setMenuBar(self.menubar_widgets.menuBar)

        self.tab_widget = MyTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        # self.menubar_widget = MenuBar(self)
        # self.setMenuBar(self.menubar_widget)
#


if __name__ == "__main__":

    import sys
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())