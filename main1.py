# Запись данных в существующий файл
# from PIL.SpiderImagePlugin import iforms
# from openpyxl import load_workbook
import csv

import schedule

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

# import os  # модуль управления операционной системой
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
# import pickle
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
# import re

# pattern = r'\b\w{4}\b'# все слова из 4 символов
# pattern = r'\d'# все цифры
#
# test_string = ' 10 + 20 , ,eltn fghn fghn 30'
# #result = re.search(pattern, test_string) # если одно ищем
# result = re.findall(pattern, test_string)
# #result = set(result)
# print(result)
# # тернарный  if - ternary if
# print('Цифры есть') if result else print('Цифр нет')

# pattern = r'\((.+?)\)'# все цифры
#
# test_string = ' Поиск пообразцу (pattern)'
# result = re.findall(pattern, test_string)
# print(result)

# {m} - ровно m раз
# {m,} -m раз  и более
# {,n} -  не более n раз
# {m,n} -  от m до n раз
# ? от 0 до 1 аналог {0,1}
# * от 0 до бескон(32767 {1.}
# + от 1 до бескон {1,}


# pattern = r'стеклянн?ый'  # вторая  н может присутствовать , но не обязана
# test_string = 'стекляный, оловянный, стеклянный'
# result = re.findall(pattern, test_string)
# print(result)

# жадный квантификатор (greedy quantifier)
# pattern = r'<img.*'
# схватывает все после img
# ленивый квантификатор (lazy non greedy)
# pattern = r'<img.*?>'
# точный квантификатор - только путь к картинке
# pattern = r'<img[^>]+src="([^">]+)"'
#
# test_string = 'Картинка <img src="bg.jpg">  в тексте </p>'
# result = re.findall(pattern, test_string)
# print(result)
# Вытаскиваем содержимое абзаца HTML
# pattern = r'<p>(.*?)</p>'
# pattern = r'<p[^>]*>(.*?)</p>' # содержимое абзаца html с атрибутами
# test_string = '<b>Цынтрируем содержимое абзаца</b><palign="center">Содержимое</p>'
#
# result = re.findall(pattern, test_string)
# print(result)
# популярный ресурс https://regex101.com

# удаление пунктуации
# def remove_pynctuation(input_string: str) -> str:
#     """
#     методом sub() заменяем все совпадения пустой строкой и возвращаем  "очищенную"
#     :param input_string: строка со знаками препинания
#     :return:
#     """
#     return re.sub(r'[^\w\s]','', input_string )
#
# test_string = 'Язык Python, являясь интуити-вно понятным, легко выучить! Ну и PEP8.'
# result = remove_pynctuation(test_string)
# print(result)


# разделители разные
# pattern= r'[,.;:!?]'
# test_string = 'яблоко. груша, банан; слива! абрикос'
# test_string=test_string.replace(' ','')
# print(test_string)
# test_str =[]
# for item in test_string:
#     test_str += re.split(pattern,test_string)
# test_str= set(test_str)
# #result = re.split(pattern,test_str)
# print(test_str)
# import re
# import requests
# pattern = r'<img[^>]+src="([^">]+)"'
# html = requests.get('https://skillbox.ru').text
# #print (html)
# result = re.findall(pattern,html)
# print(result)

#######################
# Объектно-ориентированное программирование
########################
# encapsulation каждый объект условно в капсуле что внутри неизвестно

# класс -это прототип будущего объекта, который описывает его свойства и поведение
# данные и методы по их обработке
# экземпляр - объект порожденный классом
# объект всегда экземпляр класса
# атрибут - свойства и методы присущее объекту
# класс определяет атрибуты, по сути набор атрибутов
#
# создание класса - название Класса в большой буквы
# Свойства классов
# class Fruit:
#     pass
#
#
# a=Fruit()
# b=Fruit()
# print(a.__class__)
#
# a.name  = 'яблоко'
# a.weight = 120
#
# b.name  = 'груша'
# b.weight = 100
# print(a.name)
# print(a.weight)
# print(b.name)
# print(b.weight)


# методы классов
# class Greeter:
#     def hello(self, name='Noname'):
#         print('Привет мир',name)
#
#     def good_bye(self):
#         print('Пока, мир')
#
#
# g = Greeter()
# g.hello('Горшок')
# g.good_bye()

# self - в него передается объект, который его вызвал. Это ссылка на объект вызвавший класс


# методы классов  и анализ предыдущих вызовов
#

# from lib import Car
#
# car = Car('Skoda','Octavie','Red')
# car.start_engine()
# car.drive_to('Город')
#
# car2 = Car()
# #car2.start_engine()
# car2.drive_to(('Город'))

# Геттеры и сеттеры

# from lib import Car
# p=Car()
# print(dir(p))
# print(p.color)
# p.set_color('red')
# print(p.color)
# a = p.get_color()
# print(a
#
# from lib import Clicker
# cl=Clicker()
# cl.click()
# cl.click()
# cl.click()
# cl.reset()
# print(cl.get_counter())


# from lib import Separator
#
# d=Separator()
# d.add_num(5)
# d.add_num(6)
# d.add_num(10)
# d.add_num(3)
# d.add_num(8)
#
# print(d.get_odd())
# #print(d.get_even())
#
# from lib import Sorter
# s=Sorter()
# s.add_word("Привет")
# s.add_word("Пока")
# s.add_word("Здорово")
# print(s.result())


# ДЗ
# class Balance:
#     self.rigth =0
#     self.left = 0
#     def add_left(self,weight):
#         pass
#     def add_right(self,weight):
#         pass
#     def result(self):
#          return - правая, левая,  # состояние весов


# Полиморфизм
# методы:
# method oveerride - переопределение методов
# operator overloading = оператор переопределения

# print(1+2)
# оператор + полиморфный  - работает с переменными разных типов
# интрпретатор проверяет типы данных и выводит результат в зависимости от их типа
# print([1,2]+[3,4])
# полиморфизм свойство кода работать с разными типами двнных
# def func

# c
# book=Book('Яхык С++', author='Бьярн Страупструп')
#
# print( f'{book.get_title()},{book.get_autor()}
# isinstance(объект,(тип1, тип2, тип3)
from lib import Circle, Square


# def shape_info(shape):
#
#     r, c = ('прямоугольник', 'круг')
#     if isinstance(shape, Square):
#         fig = r
#     if isinstance(shape, Circle):
#         fig = c
#     print(f'Площадь {fig}а {shape.area()}, периметр {shape.perimetr()} ')
#
# s = Circle(10)
#
# shape_info(s)
#
# r = Square(10)
# shape_info(r)


###
# from lib import Person,Student,Employee
# people = [
#     Person('Александр',27 ),
#     Student('Петр',22,'СПБГАСУ'),
#     Employee('Иван',30, 'Пупкин и сыновья'),
# ]
# for person in people:
#     if isinstance(person, Student):
#         print(person.get_univercity())
#     elif isinstance(person, Employee):
#         print(person.get_company())
#     else:
#         print(person.get_name())
# from lib import Stat
#
# lst = list(range(1, 15))
#
#
# lst += ['a']
#
#
#
# s = Stat(lst)
# print(s.get_min())
# print(s.get_max())
#
# print(lst)


# Специальные методы
# __init__

# class MyTime:
#     def __init__(self,minutes,seconds):
#         if 0<=minutes<60:
#             self.minutes =minutes
#         if 0<=seconds<60:
#             self.seconds = seconds
#
#     def __str__(self):
#         return f'<Time{self.minutes}:{self.seconds}>'
#
#     def __add__(self, others):
#         m=self.minutes+others.minutes
#         s=self.seconds+others.seconds
#         m +=m//60+s//60
#         s =s%60
#         print(m,s)
#         return MyTime(m,s)
#
# t1= MyTime(13,40)
# t2= MyTime(15,25)
# print (t1+t2)

# class SquareFunction:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b = b
#         self.c = c
#
#     def __call__(self, x):
#         return self.a*x**2 +self.b*x+self.c
# s=SquareFunction(1,2,3)
# print(s(2))


# наследование(расширение) inheritance
# класс от которого наследуется - базовый, родительский, суперкласс
# наследуемый класс - производный, дочерний
# from math import pi
#
# class Shape:
#     def info(self):
#         print(f'Класс: {self.__class__.__name__}')
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#         self.name = "Круг"
#
#     def perimetr(self):
#         return 2 * pi * self.radius
#
#     def area(self):
#         return pi * self.radius ** 2
#
#     def get_name(self):
#         return 'круг'
#
#
# class Square(Shape):
#     def __init__(self, width, height=0):
#         self.width = width
#         if height == 0:
#             self.height = self.width
#         else:
#             self.height = height
#
#     def perimetr(self):
#         return (self.height + self.width) * 2
#
#     def area(self):
#         return self.height * self.width
#
#     def get_name(self):
#         return 'прямоугольник'
#
#
# # class Kvadrat(Square,Shape) :
# #     super().__init__(self,self)
#
#
# s=Square(5)
# print(s.area())
# # print(s.info())
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.name = 'прямоугольник'
#
#     def perimetr(self):
#         return 2 * (self.width + self.height)
#
#     def area(self):
#         return self.width * self.height
#
#     def get_name(self):
#         return self.name
#
#
# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
#         self.name = 'квадрат'
#
#
# s = Square(5)
# print(s.area())
# print(s.perimetr())
# print(s.get_name())

# method override; operator overloading
# __call__ - экземпляр класса становится вызываемым
# (как функция)
# y = ax^2 + bx + c
# class SquareFunction:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __call__(self, x):
#         return self.a * x ** 2 + self.b * x + self.c
#
#
# s = SquareFunction(1, 2, 3)
# print(s(2))

# Банковскя систем
# Класс BankAccount owner, balanc
#методы депозит(>0), withdraw(amount(<balance). get_balance

# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.balance = balance
#     def amount(self,x):
#         if self.balance>=x:
#             self.balance = self.balance-x
#         else:
#              print(f'снять более {self.balance} нельзя!')
#     def deposit(self,x):
#         if x<0:
#             return F'Положить отрицательную сумму {self.balance} нельзя!'
#         else: self.balance +=x
#     def get_balance(self):
#         return f'Клиент {self.owner}, баланс {self.balance}'
#
# s= BankAccount('Иванов',100)
#
# s.amount(110)
# print(s.owner,s.balance)
# s.deposit(10)
# print(s.owner,s.balance)
# print(s.get_balance())


#ДЗ


# class Animal:
#     def make_sound(self):
#         print('Звуки животных')
#
# # дочерние
# class Dog(Animal):
#     def make_sound(self):
#         print('Гав!"')
#
# class Cat(Animal):
#     def make_sound(self):
#         print('Мяу!')
#
# class Elephant(Animal):
#     def make_sound(self):
#         print("Как то непонятно, но страшно!")
#
# class Piggy(Animal):
#     def make_sound(self):
#         print("Хрю-Хрю!")
#
#
# class Zoo:
#     def __init__(self):
#         self.animals = []  # список животных
#
#     def add_animal(self, animal):
#         self.animals.append(animal)
#
#     def make_all_sounds(self):
#         for animal in self.animals:
#             animal.make_sound()
#
#
#
# zoo = Zoo()
# zoo.add_animal(Piggy())
# zoo.add_animal(Dog())
# zoo.add_animal(Cat())
# zoo.add_animal(Elephant())
#
# zoo.make_all_sounds()

# import sys
# print('hello world', sys.argv[0],' и мой аргумент', sys.argv[1])
# if len(sys.argv)>=2:
#     match sys.argv[1]:
#         case 'p':
#             print('Привет')
# #         case 'g':
# #             print('Пока')
#
# # Cron и schedule
# # запуск по расписанию и периодические задачи
# # import schedule
# # import dat
# # import dat
# # i=1
# #
# # def job():
# #     global i
# #     print(f'скрипт запустился {i}')
# #     i +=1
# #     t = datetime.datetime.now()
# #     print('Время: ', t.strftime('%H:%M:%S'))
# #
# # schedule.every(3).seconds.do(job)
# # while True:
# #     schedule.run_pending()
# # плагин EMMET работает с HTML
#
#
# import csv
#
# data =  [
#     ['name','age','city'],
#     ['Борис',25,'Воронеж'],
#     ['Глеб',35, 'МОсква'],
#     ['етр',15,'Мухосранск']
#
# ]
# with open('people.csv','r',encoding ='utf-8') as f:
#     reader = csv.reader(f, delimiter=',', quotechar = '"')
#     for row in reader:
#         print(row)
#
# with open('employee.csv','w', newline = '',encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerows(data)
#
# with open('people.csv', 'r', encoding = 'utf-8') as f:
#     dict_reader=csv.DictReader(f)
#     print(dict_reader)
#     for row in dict_reader:
#         print(f'{row('name')} живет в городе {row('city')}')
#
# field_names = ['name','age','city']
# data = {
#     'name':'Борис';
#     'age': 27;
#     'city':'Москва'
# }
#
# with open('file.csv', 'w', newline='', encoding='utf-8') as f:
#

data = ['name', 25,'town']
with open('savefile.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f,quoting =csv.QUOTE_NONNUMERIC)
    writer.writerow(data)
