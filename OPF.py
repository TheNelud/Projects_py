import PySimpleGUI as sg 
import openpyxl 

sg.theme('DarkGrey6')

#Выбор документа в форме PySimple
def open_file():
    sg.set_options(auto_size_buttons=True)
    openfile = sg.popup_get_file(
        "Открыть документ",
         title="ОПФ",
         file_types=(("XLSX Files", "*.xlsx"),("CSV Files", "*.csv")))
   
    if openfile == '':
        return


    book = openpyxl.open(openfile, read_only=True)             # подключаем выбранный файл
    # book = openpyxl.open('Оценка ОПФ.xlsx', read_only=True)
    # sheet_list = []                                           #создание списка листов
    opnfl = openfile.split("/")[-1]
    header_list_first = []                                      #создание списка заголовков для таблицы
    data_list_first = []                                        #создание списка данных для таблицы
    # for sheet in book:
    #     sheet_list.append(sheet.title)
    # print(sheet_list)

    sheet_first = book.worksheets[0]                            #Работаем с первым листом
    sheet_second = book.worksheets[1]                           #Работаем со вторым листом
    sheet_third = book.worksheets[2]                            #Работаем с третьим листом
    sheet_fourth = book.worksheets[3]                           #Работаем с четвертым листом
    sheet_fifth = book.worksheets[4]                            #Работаем с пятым листом

    for column in range(sheet_first.min_column-1,sheet_first.max_column):               #Расчехляем значения заголовков   
        header_list_first.append(sheet_first[1][column].value)
    # print(header_list_first)

    for row in sheet_first.iter_rows(sheet_first.min_row+1, sheet_first.max_row):       #Расчехляем значения данных
        for cell in row:    
            data_list_first.append(cell.value)
    # print(data_list_first)

    layout = [
        [sg.Table(
            values=data_list_first,
            headings=header_list_first,
            pad=(25,25),
            display_row_numbers=False,
            auto_size_columns=True,
            num_rows=(25, len(data_list_first))
        )]
    ]

    window = sg.Window(openfile,layout, grab_anywhere=False)
    event, values = window.read()
    window.close()

   


if __name__ == '__main__':
    open_file()

                            