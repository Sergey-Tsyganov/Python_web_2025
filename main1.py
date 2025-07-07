# Запись данных в существующий файл
from PIL.SpiderImagePlugin import iforms
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
# from openpyxl import load_workbook
# wb = load_workbook('docs/employees.xlsx')
# ws=wb.active
# rows_count = ws.max_row
# for row in ws.iter_rows(values_only=True):
#     fio, pos, dept = row
#     print(f'Фамилия:{fio},Позиция:{pos}, Отдел: {dept}')
#     #print(row)
# ws['A1']=2
# ws['A2']=3
# #ws['A3']= "=A1+A2"
# ws['A3']= "=корень(A1+A2)"
# ws['A4']= "=Sum(A1+A2)"
# wb.save('docs/employees2.xlsx')


# Пишем свои модули
# lib

# Подключаем
#from . lib import summ  - из текущей директории
#from .. lib import summ  - из директории выще
#from .lib import summ  - относительный импорт

# import lib
# if __name__ == '__main__':
#     c = lib.summ(2,3)
#     d= lib.diff(4,2)
# print( c,d)

#print(__name__)

# Пакеты
# from new import greet
# from new import sum
# print (sum(2,3,4))
# print(greet('Вася!'))
# #print(new.module._hidden_function())
# print(new.__init__.py.__autor__)
#



# Файлы
# name.txt
# t - текстовые файлы( txt, xml, html)
# b - бинарные файлы(Jpg, avi mp3
# работа с текстовыми файлами
# w - на запись/создание(если файл был то стирается все
# a - если не существует создается, если существует то запись идет в конец
# r - читать - файл должен существовать по умолчанию
# fo = open('info.txt','wt', encoding='utf-8')
# print (fo.mode)
# print (fo.encoding)
# print (fo.name)
# # записываем в файл
# count = fo.write('Этот текст будет в файле')
# # или
# print('в файле хаписано', count, 'байт')
#
# fo.close()

# fo = open('info.txt','rt', encoding='utf-8')
# text = fo.read(11) # в скобках сколько байт читать, если нет то столько и считает
# text1 = fo.read(6)
# text += fo.read()
#
#
# print (text)
# #print (text1)
# #print (text2)
# #print (text3)

# fo = open('info.txt','at', encoding='utf-8')
# #fo.write(' Кукареку')
# print('\nА вот с новой строки', file =fo)
#
# fo.close()
#ДЗ методичка модуль
fo = open('info.txt','rt', encoding='utf-8')
#fo.write(' Кукареку')

# while text := fo.readline():
#     print(text.rstrip('\n'))

text = fo.read()
lst = text.splitlines()
print (lst)

fo.close()