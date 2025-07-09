# Запись данных в существующий файл
# from PIL.SpiderImagePlugin import iforms
# from openpyxl import load_workbook

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

# wb.save('docs/employees.xlsx')

# чтение данных
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
# from . lib import summ  - из текущей директории
# from .. lib import summ  - из директории выще
# from .lib import summ  - относительный импорт

# import lib
# if __name__ == '__main__':
#     c = lib.summ(2,3)
#     d= lib.diff(4,2)
# print( c,d)

# print(__name__)

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
# ДЗ методичка модуль

# открытие с менеджером контекста
# with open('info.txt','rt', encoding='utf-8') as fo:
#     text = fo.read()
#     lst = text.splitlines()
#     print (lst)
# # Проследит чтобы файл закрылся

# fo.close()

import os  # модуль управления операционной системой
# #os.mkdir ('libs')
# # мягкое создание директории вместо пред вар. елси дир уже есть то не страшно
# os.makedirs ('libs', exist_ok='True')
# # удаление
# # проверка существования директории
# if (os.path.exists('libs')):
#     os.rmdir('libs')
# # рабочаяя директория
# path = os.getcwd()
# print(path)
# # поменять дир
# os.chdir(path+'/images')
# print(os.getcwd())
#
# # на уровень выше
# os.chdir('..')
# path = os.getcwd()
# os.chdir(path+'/images')
# all_files = [f for f in os.listdir('.') if f.startswith('sun')]
# print(all_files)

# чтение последовательностей из текстового файла их сортировка
# res= []
# with open('primer.txt','rt', encoding='utf-8') as f:
#     while temp :=f.readline().rstrip('\n'):
#         res +=temp.split(',')
# #res= list(map(lambda x:x.rstrip('\n'),res))
# #res = set(res)
#
# res = sorted(int(x) for x in set(res))
# print(res)

# сериализация и десериализация
# import pickle
# import pprint
# d ={
#     'стол': 'table',
#     'стул':'chair',
# }
# сериализация
# with open('dickfile.dat','wb') as p:
#     # дамп файл словаря d  в p
#     pickle.dump(d,p)

# десериализация
# with open('dickfile.dat','rb')  as p:
#     d= pickle.load(p)
#
# pprint.pprint(d,width=15)
# ссылка на файл с директориями
# from path_lib import *
#
# print(img_dir)

# Исключения
# try:
#   что собираемся делать
# exсept исключение - обрабатываем исключениЙ
# finally  выполняется в любом случае

# print(name)
# открытие несуществующего файла
# flag = False
# try:
#     fo = open('inform.txt', encoding= 'utf-8' )
#     print(fo.read())
#     fo.close()
# except FileNotFoundError:
#     fo = open('inform.txt','wt', encoding='utf-8')
#     flag = True
#     # print('такого файла нет и он создан с параметрами по умолчанию')
#     # with open('inform.txt','wt',encoding='utf-8') as f:
#     #    f.write('По умолчанию')
# else:
#
#
# finally:
#     if Flag:
#         fo.write('По умолчанию')
#         fo.close()
#         print('Продолжаем работать')


# А как сдлать если мы не знаем что возникнет

# print('остаток от деления')
# try:
#     value = int(input('а что делим 10'))
#     res = 10%value
#     print('Остаток', res)
# except ZeroDivisionError :
#     print('На ноль делить нельзя')
# except ValueError:
#     print(' Только число')
# except Exception as exp:
#     print('Произошло исключение', exp.__class__.__name__, exp)
# бросаемся исключениями throw( в питоне raise)
# max_val=10
# min_val=0
# try:
#     val = int(input(f'Значение от {min_val} до {max_val}: '))
#     if not min_val<val<max_val:
#         raise ValueError('введенное числ вне диапазона')
#     print(f'Введенное число {val} лежит в диапазоне')
# except ValueError as exp:
#     print


# Утверждения (assertions)
# try:
#     text = input ('введите текст')
#     assert len(text)>3
# except AssertionError:
#     print('Слишком короткий текст')

# s = ('Вася','Петя','Сидор','Евгений')
# try:
#     a =float((input('введите число по индексу')))
#     assert a%1 == 0
#     print(s[int(a)])
# except ValueError:
#     print('Ввели не число')
# except IndexError:
#     print('такого индекса нет')
# except AssertionError:
#     print('не целое')
# f = True
# while f:
#     a = input('Введите первое число')
#     b = input('Введите 2 число')
#     try:
#         print('a/b = ', float(a)/float(b) )
#         f=False
#     except ZeroDivisionError:
#         print('b не может быть равно 0')
#     except ValueError:
#         print('а и в должны быть числами')
#     except Exception:
#         print('Какая-то фигня')

# Практикум

# Обучаемый словарь - создаем сохраняем открываем
# dict dat отсутствует
import pickle
# минимальная версия, если файл dict.dat отсутствует
# voc = {
#     'стол': 'table',
#     'стул': 'chair',
# }
#
#
# # функция для распечатки словаря
# def print_voc():
#     print('Сейчас словарь содержит: ')
#     for k, v in voc.items():
#         print(k, '—', v)  # Alt + 0151

# загружаем словарь из файла
# try:
#     with open('dict.dat', 'rb') as dump_in:
#         voc = pickle.load(dump_in)
# except FileNotFoundError:
#     with open('dict.dat', 'wb') as dump_out:
#         pickle.dump(voc, dump_out)
#     print('Создан минимальный словарь: ')
#     print_voc()
#
# while True:
#     temp = input('\nВведите слово для перевода или "#" для завершения: ')
#     word = temp.strip().lower()
#     if word == '#' or word == '№':
#         break
#     if word in voc.keys():
#         translate = voc[word]
#         print(f'Слово "{word}" переводится как {translate}.\n')
#     else:
#         print(f'Значение слова {word} отсутствует в словаре.')
#         newkey = f'А как слово {word} переводится.\n'
#         newkey += 'Если ничего не вводите нажмите ENTER,\n '
#         newkey += 'или введите его здесь: '
#         new_word = input(newkey)
#
#         if new_word != '' or len(new_word) > 2:
#             voc[word] = new_word
#             print(f'Слово {word} с переводом {new_word} внесено в словарь')
#         else:
#             print('Ничего не введено или слишком короткое слово')
#             continue
#
# # Сохранить словарь
# with open('dict.dat', 'wb') as dump_out:
#     pickle.dump(voc, dump_out)
#
# print('До новых встреч!!!')


# библиотука pymorphy
# import pymorphy3
# from pymorphy3 import MorphAnalyzer
# form = MorphAnalyzer().parse('бутылка')[0]
# for btl in reversed(range(99)):
#     print(f'В холодильнике {btl+1}{form.make_agree_with_number(btl+1).word} пива')
#     print('Возьмем одну и выпьем')
#     if btl % 10 == 1 and btl !=11:
#         remain = 'Осталась'
#     else:
#         remain ='осталось'
# print(f'{remain} {btl}  {form.make_agree_with_number(btl).word} пива' )

# morph = pymorphy3.MorphAnalyzer()
# print(morph.parse('Дмитрий'))№


# Линтер - статический анализатор кода, контролироует следование хорошим практикам
# Flake8
# pip install flake8
# (flake8-bugbear - для нахождения распространнеых логических ошибок в коде)
# (pep8 - naming - проверяет имена переменных, функций на соответствие pep\)
# --max-complexity 10 $FileDir$/$FileName$ аргументы
# Advanced Options/OutputFilter: $FILE_PATH$:$LINES$

# регулярные выражения - поиск по паттернам
# regular expressions   re
# r- строка - сырая строка, игнорирует все управляющие последовательности
import re

#pattern = r'\b\w{4}\b'# все слова из 4 символов
# pattern = r'\d'# все цифры
#
# test_string = ' 10 + 20 , ,eltn fghn fghn 30'
# #result = re.search(pattern, test_string) # если одно ищем
# result = re.findall(pattern, test_string)
# #result = set(result)
# print(result)
# # тернарный  if - ternary if
#print('Цифры есть') if result else print('Цифр нет')

# pattern = r'\((.+?)\)'# все цифры
#
# test_string = ' Поиск пообразцу (pattern)'
# result = re.findall(pattern, test_string)
# print(result)

# {m} - ровно m раз
# {m,} -m раз  и более
#{,n} -  не более n раз
# {m,n} -  от m до n раз
# ? от 0 до 1 аналог {0,1}
# * от 0 до бескон(32767 {1.}
# + от 1 до бескон {1,}


#pattern = r'стеклянн?ый'  # вторая  н может присутствовать , но не обязана
#test_string = 'стекляный, оловянный, стеклянный'
#result = re.findall(pattern, test_string)
#print(result)

# жадный квантификатор (greedy quantifier)
#pattern = r'<img.*'
# схватывает все после img
# ленивый квантификатор (lazy non greedy)
#pattern = r'<img.*?>'
# точный квантификатор - только путь к картинке
# pattern = r'<img[^>]+src="([^">]+)"'
#
# test_string = 'Картинка <img src="bg.jpg">  в тексте </p>'
# result = re.findall(pattern, test_string)
# print(result)
#Вытаскиваем содержимое абзаца HTML
#pattern = r'<p>(.*?)</p>'
# pattern = r'<p[^>]*>(.*?)</p>' # содержимое абзаца html с атрибутами
# test_string = '<b>Цынтрируем содержимое абзаца</b><palign="center">Содержимое</p>'
#
# result = re.findall(pattern, test_string)
# print(result)
# популярный ресурс https://regex101.com
