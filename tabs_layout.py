import PySimpleGUI as sg
import openpyxl

sg.theme('DarkGrey6')
book = openpyxl.open('Оценка ОПФ.xlsx', read_only=True)

sheets = book.sheetnames
names_sheet = []
tab_group_layout = []

for name_sheet in sheets:                                             # Расчехляем имена листов
    names_sheet.append(name_sheet)

for i in range(len(names_sheet)):                                     #
    tab_layout = [[sg.Text(names_sheet[i])]]
    tab_group_layout.append([sg.Tab(names_sheet[i], tab_layout, key=f'-TAB{i}-')])


layout = [[sg.TabGroup(tab_group_layout)]]

window = sg.Window('My window with tabs', layout, no_titlebar=False)

tab_keys = ('-TAB1-','-TAB2-','-TAB3-', '-TAB4-')         # map from an input value to a key
while True:
    event, values = window.read()       # type: str, dict
    print(event, values)
    if event is None:
        break
window.close()