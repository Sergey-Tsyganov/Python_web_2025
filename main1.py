# Запись данных в существующий файл
from openpyxl import load_workbook

# Открываем (загружаем) рабочую книгу
# wb = load_workbook('docs/report.xlsx')
#
# # Активный лист
# ws = wb.active
# # Можно и по имени
# # ws = wb['Отчёт']
#
# # Заголовки
# ws['A1'] = 'ФИО'
# ws['B1'] = 'Должность'
# ws['C1'] = 'Отдел'
#
# # Данные
# employees = [
#     ['Иванов И.И.', 'Менеджер', 'Продажи'],
#     ['Петров П.П.', 'Бухгалтер', 'Финансы'],
#     ['Сидорова С.С.', 'Аналитик', 'IT'],
# ]
#
# for row, data in enumerate(employees, start=2):
#     ws.cell(row=row, column=1, value=data[0])
#     ws.cell(row=row, column=2, value=data[1])
#     ws.cell(row=row, column=3, value=data[2])

#wb.save('docs/employees.xlsx')

#чтение данных
from openpyxl import load_workbook
wb = load_workbook('docs/employees.xlsx')
ws=wb.active
rows_count = ws.max_row
for row in ws.iter_rows(values_only=True):
    fio, pos, dept = row
    print(f'Фамилия:{fio},Позиция:{pos}, Отдел: {dept}')
    #print(row)
ws['A1']=2
ws['A2']=3
#ws['A3']= "=A1+A2"
ws['A3']= "=корень(A1+A2)"
ws['A4']= "=Sum(A1+A2)"
wb.save('docs/employees2.xlsx')
