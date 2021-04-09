from PyQt5.QtWidgets import *
# from PyQt5 import Qt
# from opf_main import MainWindow


class MyTabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        #Инициализируем и расчехляем книгу
        # self.book = MainWindow.action_clicked.book
        # self.sheet_first = self.book.worksheets[0]  # Работаем с первым листом
        # self.sheet_second = self.book.worksheets[1]  # Работаем со вторым листом
        # self.sheet_third = self.book.worksheets[2]  # Работаем с третьим листом
        # self.sheet_fourth = self.book.worksheets[3]  # Работаем с четвертым листом
        # self.sheet_fifth = self.book.worksheets[4]  # Работаем с пятым листом
        #
        # header_list_first = []
        # for column in range(self.sheet_first.min_column - 1, self.sheet_first.max_column):  # Расчехляем значения заголовков
        #     if self.sheet_first[1][column].value is not None:
        #         header_list_first.append(self.sheet_first[1][column].value)
        #
        # print(header_list_first)



        # Инициализируем разделы
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        # Добавляем разделы
        self.tabs.addTab(self.tab1, "Исходные данные")
        self.tabs.addTab(self.tab2, "Результаты оценки состояния")
        self.tabs.addTab(self.tab3, "Оценка показателей ")
        self.tabs.addTab(self.tab4, "Анализ расчетов оценки состояния ")
        self.tabs.addTab(self.tab5, "Расшифровка баллов ")

        # =================================================>
        # Создаем первую страницу
        self.tab1.grid_layout = QGridLayout(self)
        self.button_edit = QPushButton("Расчитать")  # Создаём кнопку для расчетов всего



        self.table_tab1 = QTableWidget(30,5)



        #self.tab1.grid_layout.addWidget(self.label_tab1_28)
        self.tab1.grid_layout.addWidget(self.table_tab1)
        self.tab1.grid_layout.addWidget(self.button_edit)
        self.tab1.setLayout(self.tab1.grid_layout)
        # =================================================>
        # Создаем вторую страницу
        self.tab2.grid_layout = QGridLayout(self)
        self.table_tab2 = QTableWidget(30, 6)
        self.tab2.grid_layout.addWidget(self.table_tab2)
        self.tab2.setLayout(self.tab2.grid_layout)
        # =================================================>
        # Создаем третью страницу
        self.tab3.grid_layout = QGridLayout(self)
        self.table_tab3 = QTableWidget(30, 6)
        self.tab3.grid_layout.addWidget(self.table_tab3)
        self.tab3.setLayout(self.tab3.grid_layout)
        # =================================================>
        # Создаем четвертую страницу
        self.tab4.grid_layout = QGridLayout(self)
        self.table_tab4 = QTableWidget(30, 6)
        self.tab4.grid_layout.addWidget(self.table_tab4)
        self.tab4.setLayout(self.tab4.grid_layout)
        # =================================================>
        # Создаем пятую страницу
        self.tab5.grid_layout = QGridLayout(self)
        self.table_tab5 = QTableWidget(30, 6)
        self.tab5.grid_layout.addWidget(self.table_tab5)
        self.tab5.setLayout(self.tab5.grid_layout)
        # =================================================>

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
