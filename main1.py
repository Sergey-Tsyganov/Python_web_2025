# cnhjrb
# startwith endwith
from builtins import PythonFinalizationError

# s='Cмотреть'
# if s.lower.startwith('смо')
#     print('Да')

# find
# s='Смотреть,видеть,вертеть'
# index=s.find('еть')
# print(s)
# есть ли есть в строке первое вхождение
# 1.find('подстрока') - если есть от возвращает индекс
# 2.find('подстрока',start) - если есть от возвращает индекс c мета страт
# 2.find('подстрока',start, end) - если есть от возвращает индекс c мета страт до места end
# index=s.find('еть',10,15)
# s = 'синхрофазотрон'
# ch = 'о'
# if ch in s:
#     numbers=''
#     count=s.count('о')
#     sdv = 0
#     for i in range(count):
#         k = s.find(ch,sdv)
#         numbers += str(k)
#         print(numbers)
#         sdv=sdv+k+1
#         print ('sdv',sdv)
# else:
#     pass

# 1. replace('что','на что') полная замена
# 1. replace('что','на что', сколько раз) полная замена
# s='тиливизор'
# print(s.replace('и','е',2))
# s='+7-012-345-67-89'

# sliсe срез может быть у строки и у других коллекций, за исключением множеств(set)
# [начало:окончание(не включительно):шаг]
# обращение по срезу не приводит к вылету за предел
# работате быстрее
# s='Добрый день'
# print(s[7:11:1])
# print(s[:6]) от начала до 6 симв
# print(s[11:]) от 11 до конца
# print(s[7:11]) от 7 до 11 символа(не включая)
# s=input('введите слово').strip()
# # s='потоп'
# # if s.lower()==s[::-1].lower():
# #     print('Да')
# # else:
# #     print('нет')
# s='Дорог Рим город или Миргород' # + и *
# # Миргород дорог... дорог...
# index = s.find(' ')
# print(s[20:35] +' '+ ((s[0:index]+'...')*2).lower())

# s='Дорог Рим'
#
# print(s[:5][::-1].lower()+' '+ s[::-1].replace(' ','').lower().capitalize())


# Списки
# s={'3','4','5'}
# lst=list(s) #  превращение множества в список типколлекции и форма преобразования в коллекцию
# print(s)
# lst=list(range(1,10))
# print(l)

lst = []  # пустой список


# или
# lst = lst()
# lst = [1,2,3]
# print(lst)
# lst2=list('Pethon')
# print(lst2)
# lst3 = [1,2,3]*3
# print(lst3)
# print(lst[:2])
# # метод списка
# #['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# lst[1] ='o'
# print(lst)

# распечатать список квадратов от 0 до 9
# lst=list(range(10))
# slice=lst[:len(lst):2]
# print(slice)
#
# for item in range(0,len(lst),2):
#     print (lst[item]," - ",lst[item]**2)
# lst=list(range(10))
# del lst[2]
# print(lst)
# сортировка
# lst = [1,2,3]*3
# lst.sort()
# print (lst)
# lst.reverse()
# print (lst)
# lst.sort(reverse=True)
# print (lst)
# b=a[]
#
# задача на ввод списка и сорировку пересчет и вывод
# s=list() или s=[]
# while (item :=input('введите ингридиент')) !='':
#     s.append(item)
# s.sort()
# убираем задвоения
# temp = set(list)
# lst=list(temp)
# print(len(s))
# for i in range(len(s)):
#     print(f'{i+1}, ',s[i])
#
# имтация стека
# s=list()
# s1=list()
#
# while (item :=input('введите книжку ')) !='':
#     s.append(item)
#
# while s:
#     item = s.pop(0) # если нуля нет то первый выйдет последним
#     print( item)
# print(s)
#
# создание аббревиатур
# s=list()
#
#
# while (item :=input('введите слово ')) !='':
#     s.append(item[0])
#
# print(*s,sep='')
#
# кортеж(Tuple)
# такой же список , но неизменяемый
# BLACK = (0,0,0)
# empty = () # tuple
# s='Python'
# t = tuple(s)+('.',)
# print(t)
# # методы
# # 'count', 'index']
#
# cards=[(7,'Червей'),('туз','пик')]
# # список кортежей
# # сравнение кортежей
# print((1,2)==(1,2))
#
#  распаковка и запаковка
# channels = ['red','green','blue']
# r,g,b, = channels
# print (r)
# a,b,c = 1,2,3
# statist =[]
# for _ in range(3):
#     fio, ball = input('Введите фио Студента:' ), float(input('Введите средний балл:' ))
#     statist.append((fio,ball))
# print (*statist, sep='\n')
#
# for st in statist:
#     fio, ball = st
#     print('Студент - ', fio, 'средний балл - ', ball)
#
# sorted сортировка - выдает на выходе сортированный список
# функция сортировки
# s= {'Иванов','Петров','Сидоров'}
# lst = sorted(s)
# print(*lst,sep=', ')
#
#
# функция enumerate
# fio= ['Иванов','Петров','Сидоров']
# for item in enumerate(fio):
#     print(item)
# в цикле возвращает пару индекс и поле
# fio= ['Иванов','Петров','Сидоров']
# for i,v in enumerate(fio):
#     print(f'{i+1}.{v}')
#
#
# методы строки
# split и join
#
# text = 'оди     два три четыре'
# ip = '192.168.0.1'
# lst = ip.split('.')
# print(lst)
# text2 = '-'.join(lst)
# print(text2)
# # ['192', '168', '0', '1']
#
# есть список стоп слов стоп лист с какими то словами которые запрещены
# пользователь вводит - выводится список убирая слова из стоп списка
#
# создание отсортированного списка с исключениями
# text1 = input('Введите текст')
# slova = ['черт', 'хрен']
# t2 = []
# t3=[]
# # убираем знаки препинания
# text1=text1.replace('.', ' ')
# text1=text1.replace(',', ' ')
# text1=text1.replace('!', ' ')
# text1=text1.replace('?', ' ')
# text1=text1.replace(':', ' ')
# text1=text1.replace(';', ' ')
# text1=text1.strip().lower()
# #print(text1)
#
# t2 = text1.split()
#
# t2 = tuple(t2)
# #print(t2)
# for item in t2:
#     if item in slova:
#         pass
#     else:
#         t3.append(item)
# t3.sort()
# for i, v in enumerate(t3):
#     print(f'{i + 1}.{v}')
#
#
# Списочные выражения (list comprehension)
#
# традиционно
# squares =[]
# for i in range(10):
#     squares.append(i**2)
# print(*squares,', ')
#
# # то же самое
# squares = [i**2 for i in range(10)]
# print(*squares,sep =', ')
#
# # квадраты четных чисел
# squares = [i**2 for i in range(10) if i%2 ==0]
# print(*squares,sep =', ')
#
# #произведение i j
#
# print([j*i for i in range(3) for j in range(3)])
# for i in range(3):
#     for j in range(3):
#      print(i*j)
#
# n='500 600 700 800'
# print([int(i) for i in n.split()])
#
# n='500 600 700 800'
# approved = ['500','600']
# print([int(i) for i in n.split() if i in approved])
#
# вырезание каждого 3 слова
# text = 'Списочные выражения применяются для эффективности ввода и оперативности'
# #temp = [ i  for  i in text.split() if (text.index(i)+1 ) % 3 ==0 ]
# # более эффективно
# temp = [ i  for  i in text.split()[2::3]]
#
# print (temp)
#
#
# Вложенные списки
#
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]
# for row in range(3):
#     for col in range(3):
#         print(matrix[row][col])
# # обход двумерного списка
# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         print(matrix[row][col])
#
# count =1
# matrix=[[1]*3 for _ in range(3)]
# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#          (matrix[row][col])=count
#          count+=1
# print(matrix)
# элегантное решение
# N=3
# matrix=[[i+j for j in range(N)] for i in range(1,8,3) ]
# print(matrix)
#
#
# словари
# нет индекса есть ключ
# пустой словарь
# создание пустого
# d ={}
# второй способ
# d=dict(d)
# предзаполненный словарь
# d = {
#     'table':[ 'таблица','стол'],
#     'well':['хорошо','колодец','скважина' ],
#     'chair': 'стул',
#     'apple': 'яблоко',
#
#
# #добавление в словарь
# d['toble']=['хз']
# print(d)
# # добавление  значения в список
# d['toble'].append('хз2')
# print(d)
#
# # удаление элемента
#
# del d['toble']
# print(d) # Словарь целиком как есть
# # перебор по циклу вывод значений по строкам
# for key in d:
#     print(key,d[key])
#
# методы
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# #удаляет элемент и возвращает его в переменну.
# deleted_item = d.pop('apple')
# print(deleted_item)
# # поиск по ключу
# print('есть ли стул')

# d = {
#     'table': ['таблица', 'стол'],
#     'well': ['хорошо', 'колодец', 'скважина'],
#     'chair': 'стул',
#     'apple': 'яблоко',
#     (55.6,30.2): 'Москва',
# }

# if 'chair' in d:
#     print('да,есть')
# for key in d:
#     print(d.keys())
#     print(d.values())
# for value in d.items():
#     print(value)

# вывод ключ - значения
# for k,v in d.items():
#     print( k,'   ',v)
# # проверка наличия значения
# if 'стул' in d.values():
#     print('да')
#
# if 'стул' in d.values():
#     print('да')
# Доступ к несуществующему ключу без исключений
# pear = d.get('peat')
# print('где груша','')
# # или
# pear = d.get('peat','Груши нет')
# print('где груша',pear)
#print(d[(55.6,30.2)])

#Частотный анализ
# text = """
# Утром 1 июля глава Удмуртской Республики Александр Бречалов сообщил, что украинский беспилотник атаковал одно из предприятий в Ижевске. По его словам, в результате удара есть погибшие и тяжелораненые.
# Ведомости собрали информацию о том, что известно на данный момент об ударе по предприятию в Ижевске.
# В 08:50 мск пресс-секретарь Росавиации Артем Кореняко сообщил о введении временных ограничений на прием и выпуск самолетов в аэропорту Ижевска.
# Глава республики побывал на месте происшествия, где работают все оперативные службы, и сообщил, что на объекте возникло возгорание. Тяжелораненые получают необходимую медицинскую помощь в больнице Ижевска. С пострадавшими работают психологи. Telegram-канал Shot сообщил, что сотрудники предприятия эвакуированы.
# Три человека погибли, 35 госпитализированы, сообщил глава Удмуртии. Спасатели разбирают завалы на месте падения беспилотника около.
# """
# text=text.strip().lower()
# d={}
# commas = ('.',',',)
# for i in commas:
#           text= text.replace(i,'')
#
# text_split = sorted(text.strip().lower().split())
# #print(text_split)
#
# res = {}
# for item in text_split:
#     if item in res.keys():
#         res[item] +=1
#     else:
#         res[item] = 1
# for k,v in res.items():
#     print(k,v)

# Функции (dry)
# Scope (local or global) - области видимости переменной
# начинается с def <имя функции>([параметры]):
#   команды
# def greet(name):
#     print('Привет,',name)
#     name = 'Петя'
#
#
# greet('Вася')

# count=0
# def increment():
#     print(count)
#
# increment()
# count=0
# def increment():
#     global count
#
#     print(count)
#     count += 1
# increment()
# print(count)

# def print_list(array):
#     for item in array:
#         print(item)
#
# print_list([1,2,3])

def greet(name='noname'):
    print('Привет,', name)
    name = 'Петя'
    return 5
greet('Вася')
print (greet())
greet()
