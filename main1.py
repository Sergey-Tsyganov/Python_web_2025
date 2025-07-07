# # cnhjrb
# # startwith endwith
# from builtins import PythonFinalizationError
# from idlelib.colorizer import prog_group_name_to_tag
# from json.decoder import WHITESPACE_STR
#
# # s='Cмотреть'
# # if s.lower.startwith('смо')
# #     print('Да')
#
# # find
# # s='Смотреть,видеть,вертеть'
# # index=s.find('еть')
# # print(s)
# # есть ли есть в строке первое вхождение
# # 1.find('подстрока') - если есть от возвращает индекс
# # 2.find('подстрока',start) - если есть от возвращает индекс c мета страт
# # 2.find('подстрока',start, end) - если есть от возвращает индекс c мета страт до места end
# # index=s.find('еть',10,15)
# # s = 'синхрофазотрон'
# # ch = 'о'
# # if ch in s:
# #     numbers=''
# #     count=s.count('о')
# #     sdv = 0
# #     for i in range(count):
# #         k = s.find(ch,sdv)
# #         numbers += str(k)
# #         print(numbers)
# #         sdv=sdv+k+1
# #         print ('sdv',sdv)
# # else:
# #     pass
#
# # 1. replace('что','на что') полная замена
# # 1. replace('что','на что', сколько раз) полная замена
# # s='тиливизор'
# # print(s.replace('и','е',2))
# # s='+7-012-345-67-89'
#
# # sliсe срез может быть у строки и у других коллекций, за исключением множеств(set)
# # [начало:окончание(не включительно):шаг]
# # обращение по срезу не приводит к вылету за предел
# # работате быстрее
# # s='Добрый день'
# # print(s[7:11:1])
# # print(s[:6]) от начала до 6 симв
# # print(s[11:]) от 11 до конца
# # print(s[7:11]) от 7 до 11 символа(не включая)
# # s=input('введите слово').strip()
# # # s='потоп'
# # # if s.lower()==s[::-1].lower():
# # #     print('Да')
# # # else:
# # #     print('нет')
# # s='Дорог Рим город или Миргород' # + и *
# # # Миргород дорог... дорог...
# # index = s.find(' ')
# # print(s[20:35] +' '+ ((s[0:index]+'...')*2).lower())
#
# # s='Дорог Рим'
# #
# # print(s[:5][::-1].lower()+' '+ s[::-1].replace(' ','').lower().capitalize())
#
#
# # Списки
# # s={'3','4','5'}
# # lst=list(s) #  превращение множества в список типколлекции и форма преобразования в коллекцию
# # print(s)
# # lst=list(range(1,10))
# # print(l)
#
# # lst = []  # пустой список
#
#
# # или
# # lst = lst()
# # lst = [1,2,3]
# # print(lst)
# # lst2=list('Pethon')
# # print(lst2)
# # lst3 = [1,2,3]*3
# # print(lst3)
# # print(lst[:2])
# # # метод списка
# # #['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# # lst[1] ='o'
# # print(lst)
#
# # распечатать список квадратов от 0 до 9
# # lst=list(range(10))
# # slice=lst[:len(lst):2]
# # print(slice)
# #
# # for item in range(0,len(lst),2):
# #     print (lst[item]," - ",lst[item]**2)
# # lst=list(range(10))
# # del lst[2]
# # print(lst)
# # сортировка
# # lst = [1,2,3]*3
# # lst.sort()
# # print (lst)
# # lst.reverse()
# # print (lst)
# # lst.sort(reverse=True)
# # print (lst)
# # b=a[]
# #
# # задача на ввод списка и сорировку пересчет и вывод
# # s=list() или s=[]
# # while (item :=input('введите ингридиент')) !='':
# #     s.append(item)
# # s.sort()
# # убираем задвоения
# # temp = set(list)
# # lst=list(temp)
# # print(len(s))
# # for i in range(len(s)):
# #     print(f'{i+1}, ',s[i])
# #
# # имтация стека
# # s=list()
# # s1=list()
# #
# # while (item :=input('введите книжку ')) !='':
# #     s.append(item)
# #
# # while s:
# #     item = s.pop(0) # если нуля нет то первый выйдет последним
# #     print( item)
# # print(s)
# #
# # создание аббревиатур
# # s=list()
# #
# #
# # while (item :=input('введите слово ')) !='':
# #     s.append(item[0])
# #
# # print(*s,sep='')
# #
# # кортеж(Tuple)
# # такой же список , но неизменяемый
# # BLACK = (0,0,0)
# # empty = () # tuple
# # s='Python'
# # t = tuple(s)+('.',)
# # print(t)
# # # методы
# # # 'count', 'index']
# #
# # cards=[(7,'Червей'),('туз','пик')]
# # # список кортежей
# # # сравнение кортежей
# # print((1,2)==(1,2))
# #
# #  распаковка и запаковка
# # channels = ['red','green','blue']
# # r,g,b, = channels
# # print (r)
# # a,b,c = 1,2,3
# # statist =[]
# # for _ in range(3):
# #     fio, ball = input('Введите фио Студента:' ), float(input('Введите средний балл:' ))
# #     statist.append((fio,ball))
# # print (*statist, sep='\n')
# #
# # for st in statist:
# #     fio, ball = st
# #     print('Студент - ', fio, 'средний балл - ', ball)
# #
# # sorted сортировка - выдает на выходе сортированный список
# # функция сортировки
# # s= {'Иванов','Петров','Сидоров'}
# # lst = sorted(s)
# # print(*lst,sep=', ')
# #
# #
# # функция enumerate
# # fio= ['Иванов','Петров','Сидоров']
# # for item in enumerate(fio):
# #     print(item)
# # в цикле возвращает пару индекс и поле
# # fio= ['Иванов','Петров','Сидоров']
# # for i,v in enumerate(fio):
# #     print(f'{i+1}.{v}')
# #
# #
# # методы строки
# # split и join
# #
# # text = 'оди     два три четыре'
# # ip = '192.168.0.1'
# # lst = ip.split('.')
# # print(lst)
# # text2 = '-'.join(lst)
# # print(text2)
# # # ['192', '168', '0', '1']
# #
# # есть список стоп слов стоп лист с какими то словами которые запрещены
# # пользователь вводит - выводится список убирая слова из стоп списка
# #
# # создание отсортированного списка с исключениями
# # text1 = input('Введите текст')
# # slova = ['черт', 'хрен']
# # t2 = []
# # t3=[]
# # # убираем знаки препинания
# # text1=text1.replace('.', ' ')
# # text1=text1.replace(',', ' ')
# # text1=text1.replace('!', ' ')
# # text1=text1.replace('?', ' ')
# # text1=text1.replace(':', ' ')
# # text1=text1.replace(';', ' ')
# # text1=text1.strip().lower()
# # #print(text1)
# #
# # t2 = text1.split()
# #
# # t2 = tuple(t2)
# # #print(t2)
# # for item in t2:
# #     if item in slova:
# #         pass
# #     else:
# #         t3.append(item)
# # t3.sort()
# # for i, v in enumerate(t3):
# #     print(f'{i + 1}.{v}')
# #
# #
# # Списочные выражения (list comprehension)
# #
# # традиционно
# # squares =[]
# # for i in range(10):
# #     squares.append(i**2)
# # print(*squares,', ')
# #
# # # то же самое
# # squares = [i**2 for i in range(10)]
# # print(*squares,sep =', ')
# #
# # # квадраты четных чисел
# # squares = [i**2 for i in range(10) if i%2 ==0]
# # print(*squares,sep =', ')
# #
# # #произведение i j
# #
# # print([j*i for i in range(3) for j in range(3)])
# # for i in range(3):
# #     for j in range(3):
# #      print(i*j)
# #
# # n='500 600 700 800'
# # print([int(i) for i in n.split()])
# #
# # n='500 600 700 800'
# # approved = ['500','600']
# # print([int(i) for i in n.split() if i in approved])
# #
# # вырезание каждого 3 слова
# # text = 'Списочные выражения применяются для эффективности ввода и оперативности'
# # #temp = [ i  for  i in text.split() if (text.index(i)+1 ) % 3 ==0 ]
# # # более эффективно
# # temp = [ i  for  i in text.split()[2::3]]
# #
# # print (temp)
# #
# #
# # Вложенные списки
# #
# # matrix=[
# #     [1,2,3],
# #     [4,5,6],
# #     [7,8,9],
# # ]
# # for row in range(3):
# #     for col in range(3):
# #         print(matrix[row][col])
# # # обход двумерного списка
# # for row in range(len(matrix)):
# #     for col in range(len(matrix[row])):
# #         print(matrix[row][col])
# #
# # count =1
# # matrix=[[1]*3 for _ in range(3)]
# # for row in range(len(matrix)):
# #     for col in range(len(matrix[row])):
# #          (matrix[row][col])=count
# #          count+=1
# # print(matrix)
# # элегантное решение
# # N=3
# # matrix=[[i+j for j in range(N)] for i in range(1,8,3) ]
# # print(matrix)
# #
# #
# # словари
# # нет индекса есть ключ
# # пустой словарь
# # создание пустого
# # d ={}
# # второй способ
# # d=dict(d)
# # предзаполненный словарь
# # d = {
# #     'table':[ 'таблица','стол'],
# #     'well':['хорошо','колодец','скважина' ],
# #     'chair': 'стул',
# #     'apple': 'яблоко',
# #
# #
# # #добавление в словарь
# # d['toble']=['хз']
# # print(d)
# # # добавление  значения в список
# # d['toble'].append('хз2')
# # print(d)
# #
# # # удаление элемента
# #
# # del d['toble']
# # print(d) # Словарь целиком как есть
# # # перебор по циклу вывод значений по строкам
# # for key in d:
# #     print(key,d[key])
# #
# # методы
# # 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# # #удаляет элемент и возвращает его в переменну.
# # deleted_item = d.pop('apple')
# # print(deleted_item)
# # # поиск по ключу
# # print('есть ли стул')
#
# # d = {
# #     'table': ['таблица', 'стол'],
# #     'well': ['хорошо', 'колодец', 'скважина'],
# #     'chair': 'стул',
# #     'apple': 'яблоко',
# #     (55.6,30.2): 'Москва',
# # }
#
# # if 'chair' in d:
# #     print('да,есть')
# # for key in d:
# #     print(d.keys())
# #     print(d.values())
# # for value in d.items():
# #     print(value)
#
# # вывод ключ - значения
# # for k,v in d.items():
# #     print( k,'   ',v)
# # # проверка наличия значения
# # if 'стул' in d.values():
# #     print('да')
# #
# # if 'стул' in d.values():
# #     print('да')
# # Доступ к несуществующему ключу без исключений
# # pear = d.get('peat')
# # print('где груша','')
# # # или
# # pear = d.get('peat','Груши нет')
# # print('где груша',pear)
# # print(d[(55.6,30.2)])
#
# # Частотный анализ
# # text = """
# # Утром 1 июля глава Удмуртской Республики Александр Бречалов сообщил, что украинский беспилотник атаковал одно из предприятий в Ижевске. По его словам, в результате удара есть погибшие и тяжелораненые.
# # Ведомости собрали информацию о том, что известно на данный момент об ударе по предприятию в Ижевске.
# # В 08:50 мск пресс-секретарь Росавиации Артем Кореняко сообщил о введении временных ограничений на прием и выпуск самолетов в аэропорту Ижевска.
# # Глава республики побывал на месте происшествия, где работают все оперативные службы, и сообщил, что на объекте возникло возгорание. Тяжелораненые получают необходимую медицинскую помощь в больнице Ижевска. С пострадавшими работают психологи. Telegram-канал Shot сообщил, что сотрудники предприятия эвакуированы.
# # Три человека погибли, 35 госпитализированы, сообщил глава Удмуртии. Спасатели разбирают завалы на месте падения беспилотника около.
# # """
# # text=text.strip().lower()
# # d={}
# # commas = ('.',',',)
# # for i in commas:
# #           text= text.replace(i,'')
# #
# # text_split = sorted(text.strip().lower().split())
# # #print(text_split)
# #
# # res = {}
# # for item in text_split:
# #     if item in res.keys():
# #         res[item] +=1
# #     else:
# #         res[item] = 1
# # for k,v in res.items():
# #     print(k,v)
#
# # Функции (dry)
# # Scope (local or global) - области видимости переменной
# # начинается с def <имя функции>([параметры]):
# #   команды
# # def greet(name):
# #     print('Привет,',name)
# #     name = 'Петя'
# #
# #
# # greet('Вася')
#
# # count=0
# # def increment():
# #     print(count)
# #
# # increment()
# # count=0
# # def increment():
# #     global count
# #
# #     print(count)
# #     count += 1
# # increment()
# # print(count)
#
# # def print_list(array):
# #     for item in array:
# #         print(item)
# #
# # print_list([1,2,3])
#
# # def greet(name='noname'):
# #     print('Привет,', name)
# #     name = 'Петя'
# #     return 5
# # greet('Вася')
# # print (greet())
# # greet()
#
# # def square(n=0):
# #     return n**2
# #
# # # print(square(4))
# # # #Функция  нужно выводить число словами 56 - пятьдесят шесть макс трехзначное
# # def num_to_text(num):
# #     nums= {
# #         0:'ноль',
# #         1:'один',
# #         2:'два',
# #         3:'три',
# #         4:'четыре',
# #         5:'пять',
# #         6:'шесть',
# #         7:'семь',
# #         8:'восемь',
# #         9:'девять',
# #         10:'десять',
# #         11:'одиннадцать',
# #         12:'двенадцать',
# #         13:'тринадцать',
# #         14:'четырнадцать',
# #         15:'пятнадцать',
# #         16:'шестнадцать',
# #         17:'семнадцать',
# #         18:'восемнадцать',
# #         19:'девятнадцать',
# #         20:'двадцать',
# #         30:'тридцать',
# #         40:'сорок',
# #         50:'пятьдесят',
# #         60:'шестьдесят',
# #         70:'семьдесят',
# #         80:'восемьдесят',
# #         90:'девяносто',
# #     }
# #     if num>=100:
# #         print('число должно быть меньше 100')
# #     elif num<=20 or num%10==0:
# #         print(f'{num} - ',nums[num])
# #     else:
# #         print(f'{num} - {nums[num//10*10]}  {nums[num%10]}')
# #
# # number = int(input('Введите любое двухзначное число: '))
# # num_to_text(number)
# #
# #     #
# #     # if srt(num)>2:
# #     #     return
# #     # e=num%10
#
#
# # аннотирование  функций для удобства
# # def number_to_words(n: int) -> str:
# #     """
# #     Функция переводит число в число словами
# #     :param n: двухзначное число
# #     :return: число словами
# #     """
# #
# # print(number_to_words())
# #
#
#
# # Ав от так делать нельзя
# # функция меняет глобальную переменную
# # a=[1,2]
# #
# # def change_array():
# #     a[0]=0
# # change_array()
# # print (a)
#
# # def print_array(array: list)-> None:
# #     for item in array:
# #         print(item)
# #
# # words =['Привет','world']
# # print_array(words)
#
# # не надо использовать имена глобальных переменных в функциях
# # PI=3.14
# # square = 'Дворцовая'
# # def sq_area(length,width):
# #     square = length*width
# #     print(square)
# # sq_area(2,3)
# # print(square)
# #
# # def circle_rad(radius):
# #     per = 2*PI*radius
# #     print(f'{per:.2f}')
# #
# # circle_rad(3)
#
# # def greet(name):
# #     print('Привет ',name)
# #     name = 'Друг'
# #     print('Здравстуй ',name)
# #
# # greet('Петр')
#
# # # главнвя функция в конце
# # def main():
# # #вызываем все функции
#
# # return vs yield
# # def generate_list():
# #     for i in range(5):
# # #        return i - завершает работу
# #         yield i   - возвращает и продолжает работу
# # # если выводится несколько величин их надо превратить в список, и т.д.
# # array =list(generate_list())
# # print(array)
#
#
# # если парамтер у функции есть, то аргумент должен быть если не используется
# # def print_gb(arg):
# #     print('good bye', end=' ')
# #
# #
# # def print_cruel(arg):
# #     print('cruel', end=' ')
# #
# #
# # def print_world(arg):
# #     print('world', end=' ')
# #
# #
# # def main():
# #
# #     print_gb(1)
# #     print_cruel(1)
# #     print_world(1)
# #
# # main()
#
#
# # оператор a is b то True будет только тогда когда а и в один и тот же объект
# # a=[0]
# #
# # print(id(a))
# # a[0] +=1
# # print(id(a))
# # Списки словари и множеста - изменяемые , строка и кортеж, число не изменяемые
#
#
# #содержимое одинаковое но объекты разные
# # my_ref = ['колбаса','молоко']
# # # присвоение - указание на тот же холодильник
# # #his_ref = my_ref
# # his_ref = my_ref[:] # копирование теперь это разные объекты
# # # his_ref = my_ref.copy() - или такая запись
# # #his_ref = ['колбаса','молоко']
# # print(my_ref==his_ref)
# # print(id(my_ref)==id(his_ref))
#
#
# #функ выводит массив рименение is на практике
# # def print_array(array: list,start: int=None):
# #     if start is None:
# #         for i in array:
# #             print(i)
# #     else:
# #         for i in range(start,len(array)):
# #             print(array[i])
# #
# #
# # a=[1,2,3]
# # print_array(a,1)
# # print_array(a)
#
#
# #ВОзвращение нескольких значений из функции
# # def coordinates() -> tuple:
# #     return 5.4,3.2,'Вася'
# # #x,y = coordinates()
# # x,y, z = coordinates()
# #
# # print(coordinates())
# # print(x,y,z)
#
#
# # Функция с переменным числом аргументов
#
# # def multy(*arcs): #* означает что значений несколько
# #     # print (len(arcs)) # подсчет числа аргументов
# #     # print(arcs) # по индексу или перебором в цикле
# #     temp=1
# #     for  arg in arcs:
# #         temp*=arg
# #     return temp
# #
# # print(multy(1,2,3))
#
# # функция с позиционным аргументом
#
# # def multy(first, *arcs): #* означает что значений несколько
# #     # print (len(arcs)) # подсчет числа аргументов
# #     # print(arcs) # по индексу или перебором в цикле
# #     temp=1
# #     for  arg in arcs:
# #         temp*=arg
# #     return temp
# #
# # # именованые аргументы = положение любое
# # def fio(name,surname):
# #     return f'{name},{surname}'
# # print(fio(name ='Остап', surname='Бендер'))
# # print(multy(1,2,3))
#
# #sandwitch
# # def sandwitch(type_of_meat, with_onion=False,with_tomatoe=False):
# #     print('Булочка')
# #     if with_onion:
# #         print('Onion')
# #     print(type_of_meat)
# #     if with_tomatoe:
# #         print('Tomatoe')
# #     print('Булочка')
# #
# # sandwitch('котлета',1,1)
#
# # args kwargs переменное количество переменных и именованных аргументов
# # def print_any(*args,**kwargs):
# #     for i in args:
# #         print(i)
# #     for k,v in kwargs.items():
# #         print(k, '=', v)
# #
# #
# # print_any(1,2,name='Дмитрий', age=25)
# # print_any('Дмитрий','Колесов',city='Москва', age=25)
#
# # def profile(name, surname, city, *children,**add):
# #     print(name)
# #     print(surname)
# #     print(city)
# #     if len(children)>0:
# #         print('Дети',', '.join(children))
# #     print('Хобби')
# #     print(add)
# #
# #
# # profile('Дмитий','Колесов',"Далезадовск",'Мария','Петр', hobby='дача')
#
# # функция как объект передается в другие функции эти функции называются функциями высшего порядка
# # 2 функции высшего порядка
# # функция критеие отбора элементов списка
# # критерий длина строки
#
# # def is_longer_six(word):
# #     return len(word)>6
# #
# # words = ['В','этом','списке','останутся','длина','которых','Больше','шести']
# # for word in filter(is_longer_six,words):
# #     print(word)
#
# # def na_a(word):
# #     return word[0] == 'а'
# #
# # words = ['В','арбуз','списке','останутся','длина','которых','Больше','шести']
# # for word in filter(na_a,words):
# #      print(word)
#
# def square(num):
#     return num**2
#
# nums=(1,2,3,4,5)
# squares =map(square,nums)
# squares2=map(str,squares)
# rez=''.join(squares2)
# print(rez)
#
import time

from PIL.ImageFont import ImageFont

# анонимные функции, однострочники, безымянные или lambda функции
# #lambda <аргументы>: <выражение>
# word = ['В','арбан','списке','останутся','длина','которых','Больше','шести']
# #is_longer_six = lambda word: len(word)>6
#
# #is_first_letter= lambda word: word[0]=='а'
# #подставляем вместо фунукции
# #q = filter(lambda word: len(word)>6, word)
# q= filter(lambda x: 'ан' in x, word)
# #


# Вот здесь правильно
# Анонимные функции (однострочники, безымянные)
# lambda-функции
# lambda <аргументы>: <выражение>
# словарные выражения

# numbers = [1, 2, 3, 4, 5]  # list(range(1, 6)
# squares = {n: n ** 2 for n in numbers}
# print(squares)
#
# squares = {n: n ** 2 for n in range(1, 10) if n % 2 == 0}
# print(squares)
#
# source_dict = {
#     'x': 1,
#     'y': 2,
#     'z': 3,
# }
#
# dest_dict = {k: v * 2 for k, v in source_dict.items()}
# print(dest_dict)

# fruits = ['ананас', 'банан', 'ежевика', 'малина', 'арбуз']
#
# print(sorted(fruits, key=lambda ch: len(ch)))


# ENGLISH_ABC = [chr(ch) for ch in range(ord('a'), ord('z') + 1)]
# RUSSIAN_ABC = [chr(ch) for ch in range(ord('а'), ord('я') + 1)] + ['ё']
# ABC = (set(ENGLISH_ABC) ^ set(RUSSIAN_ABC) ^
#        set([x.upper() for x in ENGLISH_ABC]) ^
#        set([x.upper() for x in RUSSIAN_ABC]))
# # print(ABC)
# # print(ENGLISH_ABC)
# # print(RUSSIAN_ABC)
# txt = ('Я знаю, что я ничего не знаю. '
#        'Но другие не знают и этого. А значит, я знаю больше, чем они.')
#
# d = {}
#
#
# def remove_punctuation(text):
#     return ''.join(filter(lambda x: x in ABC ^ {' '}, text))
#
#
# def get_words(text: str) -> list:
#     return remove_punctuation(text).split()
#
#
# def long_words(text, length=4) -> filter:
#     return filter(lambda word: len(word) >= length, get_words(text))
#
#
# words = get_words(txt.lower())
#
# # Считаем частоту слов
# for word in words:
#     if word in d:
#         d[word] += 1
#     else:
#         d[word] = 1
#
# res = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
#
# for k, v in res.items():
#     print(k, v)


# Ключ сортировки
# fruits = ['ананас', 'банан', 'ежевика', 'малина', 'арбуз']
# print(sorted(fruits)) # обычная сортировка без ключей
# print(sorted(fruits, key=lambda s: s[-1])) # с ключом
# print(sorted(fruits, key=lambda s: (s[1], s[-1]))) # сначала по первой букве потом по последней
# print(sorted(fruits, key=lambda s: (len(s), s[-1]))) # сначала по длине потомом по последней
#
# goods = [
#     ['Утюг',1500, 10],
#     ['Фен',1000,10],
#     ['Телевизор', 1000,5]
# ]
# print(sorted(goods, key=lambda s: (s[1], s[2],s[0])))
#
# # проверка коллекций all any
# # any - функцию применяем ко всем эл-ту коллекции и какой то вернул True
# # alll- функцию применяем ко всем эл-ту коллекции и все вернул True
#
# print(all([1,2,3])) #- True все ненулевые
# print(all([1,2,0])) #- False есть нулевые

# words = 'один два три'.split()
# # list_for_analyze = list(map(lambda x: len(x)- 3, words))
# # print(list_for_analyze)
# # print(all(list_for_analyze))
#
# # потоковый ввод sys.stdin
# import sys
# # for line in sys.stdin:
# #     print(line)
# data=sys.stdin.readlines()
# data = [d.strip('\n') for d in data]
# #print(data)
# count = 1000
# stroka =''
# for i in data:
#   #  print(i)
#
#     count1 = 0
#     for j in i:
#   #      print(j)
#
#         if j==' ':
#             count1 +=1
#  #           print('счетчик в линии',count1)
#     if count>count1:
#         count = count1
#  #       print (count)
#         stroka= i
#         print(i)
#
# #print('количество мин' ,count, ' строка' ,stroka)
# str_dib = stroka.split()
# str_sorted = sorted(str_dib)
# print(*str_sorted,  sep='-')

# рекурсия - функция вызывает сама себя

# def fact1(x):
#     if x==1:
#         return 1
#     return x*fact1(x-1)
#
#
# print(fact1(100))


# черепашья графика

# import turtle as t
# N=40
# t.penup()
# t.goto(0,-300)
# t.pendown()
# t.speed(N)
# for i in range(N):
#     t.forward(50)
#     t.left(360//N)
#
# t.mainloop()

# import turtle as t
# R=40
# N=40
# t.penup()
# t.goto(0,-300)
# t.pendown()
# t.speed(5)
# for i in range(N):
#     t.circle(100)
#     t.right(360//N)
#
# t.mainloop()

#
# import turtle as t
# N=5
#
# for _ in range(N):
#     for i in range(N):
#         t.forward(50)
#         t.left(360//N)
#     t.right(360/5)
# t.mainloop()

# import turtle as t
# def qv(b):
#
#     for _ in range(b):
#         t.circle(100)
#         t.right(360 /b)
#
# qv(10)
# t.mainloop()
# import turtle as t
# N=5
# colors =['red','green','blue','yellow','purple', 'orange']
# t.bgcolor('black')
# angle = 360/len( colors) -1
#
# # for x in range (200):
# #     t.pencolor(colors[x%len(colors)])
# #     t.width(x//100+1)
# #     t.forward(x)
# #     t.left(angle)
# #
# # t.mainloop()
#
# #фрактальное дерево
#
# import turtle as t
#
# def tree(length):
#     if length<10:
#         return
#     t.forward(length)
#     t.left(30)
#     tree(length*0.7)
#     t.right(60)
#     tree(length*0.7)
#     t.left(30)
#     t.backward(length)
#
#
# t.left(90)
# # tree(100)
# # t.mainloop()
#
#
# # модули
# # дз в виде картинки
# # Встроенные библиотеки подробно разобрать
#
# import sys
# from os import lstat
#
# strings = [d.strip('\n') for d in sys.stdin.readlines()]
# length = len(strings)  # сколько строк
# rem = length % 3
#
# if rem:
#     strings = strings[:length - rem]
#
# for x in range(0, length - rem, 3):
#     summ = sum(len(a) for a in strings[x:x + 3])
#     result = []
#     for s in strings[x:x + 3]:
#         temp = s.lower().split()
#         result += filter(lambda a: len(a) % 2 == summ % 2, temp)
#     result = sorted(set(map(lambda b: b.capitalize(), result)))[:5]
#     print(*result, sep='. ')
#
# #функция sum
sum([1,2,3]) # только итерируемый объект
# аналогично этому
# for x in lst:
#     res +=x
# то же самое in max

# встроенные билиотеки/модули

# math

# #PyPI - Python Package Index (pupi.org) # сторонние библиотеки огромный ассортимент
# import math as m
# from math import *
# # print('Пи',m.pi)
# # from math import pi, sqrt
# # print(pi, sqrt(pi))
# print(dir(m))
# print(help(m.acosh)

#модуль random  генерация случайных чисел
import random as r
# lst = [1,2,3,4,5,6,7,8,9]
#print(dir(random))
#print(random.random())
#for i in range(10): print(random.randint(1,10))
#for i in range(10): print(random.randrange(0,10,2))
# print(lst[random.randint(0,len(lst)-1)])
# print(random.choice(['орел','решка']))
# # кроме словаря и множества

# dicti = {
#     'a':1,
#     'b':2,
#     'c':3,
# }
# keys = list(dicti.keys())
# key = random.choice(keys)
# print(dicti[key])


# zara = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685',]
# for _ in range(10):
#     print (r.choice(zara),r.choice(zara))
#     help(print)

# lst = [1,2,3,4,5,6,7,8,9]
# raz= r.sample(lst,k=5)
# print(raz)
# res4=[]
# abc = 'qwerrtyyuiokjhgf'
# znaki = '@#$%^&*'
# cifry = '1234567890'
# lst = list(abc)
# res1 = ''.join(lst[:8])
# res2 = ''.join(znaki[:2])
# res3 = ''.join(cifry[:2])
# res4 =res1+res2+res3
# print(res4)
# res4 =list(res4)
# res5= list(r.shuffle((res4)))
# print(res5)


# библиотека времени и даты
import datetime as dt

# print(dt.datetime.now())
# print(dt.datetime.now().date())
#
# print(dt.datetime.now().time())
# print(dt.datetime.now().time())
# ftime= time.strftime('%d/%m/%y')
# print(ftime)
# my_time =dt.time(15,27)
# #print (my_time)
# my_date =dt.date(2025,6,15)
# # print (my_date)
# my_datetime = dt.datetime.combine(my_date,my_time)
# print(my_datetime)
#
# day1= dt.date(2052,7,6)
# day2= dt.date(2052,7,7)
# delta = day2 - day1
# print(delta)


#pprint  выводит данные в читабельном виде

# from pprint import pprint
# matrix=[
#     [1,2,3],
#     [4,4,5],
#     [6,7,8]
# ]
# pprint(matrix)

# внешние библиотеки
# правила хорошего тона - создание файла requrements - tools -Sync Pythob
# или работает лучше
# pip freeze > requirements.txt - создание файла зависимостей
# pip install -r requirements.txt -  установка списка библиотек

#графика
# PIL Python imagine library - подушка
# работает с растровыми изображениями
#RGB - модель три цвета от 0 до 255


#thumbnail - уменьшенная картинка с малой памятью
#from PIL import Image

# image = Image.open('images/vinny.jpg')
# print (image.size)
# x,y = image.size
# mode = image.mode
# #
# # pixels = image.load()
# print(f'x={x}, y={y}, режим {mode}')
# for i in range(x):
#     for j in range(y):
#        r,g,b = pixels[i,j]
#        pixels[i,j]= int((r+g+b)/3),int((r+g+b)/3),int((r+g+b)/3)
#image_rotate = image.rotate(45)
#image_flip=image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
#image_flip.save('images/vinny4.jpg')
# вырезание
#cropped = image.crop((200,0,700,300))
#cropped.save('images/vinny5.jpg')
# ресайзинг - соотношение сторон нужно контролировать
# #resized = image.resize((100,100))
# #resized.save('images/vinny6.jpg')
# from PIL import Image
# from PIL import ImageDraw
# #Создание риснков
#
# kvadrat = Image.new('RGB',(600,400),(0,0,255))
# draw = ImageDraw.Draw(kvadrat)
# draw.line((0,0,599,399), fill=(255,0,0), width=(5))
# draw.line((0,400,599,0), fill=(255,0,0), width=(5))
# kvadrat.save('images/kvadrat.jpg')
# draw.save('images/kvadrat2.jpg')

import pprint


# data = {
#     "name": "John",
#     "age": 30,
#     "city": "New York",
#     "hobbies": ["reading", "playing guitar", "travelling"],
# }
# pprint.pprint(data, width=50, indent=4)
# pprint.pprint(data)
# from PIL  import Image
# from PIL import ImageDraw
# from PIL import  ImageFont
# kvadrat2 = Image.new('RGB',(600,400),(0,0,255))
# draw = ImageDraw.Draw(kvadrat2)
# font = ImageFont.truetype(10)
# draw.textbbox(xy=(100,100),text='ДОБРОЕ УТРО',font_size=20,font=font)
# kvadrat2.save('images/kvadrat2.jpg')

# Внешние библиотеки
# Графика
# PIL - Python Imagine Library
# pip freeze > requirements.txt - создание файла зависимости
# pip install -r requirements.txt - установка списка библиотек
# from PIL import Image, ImageDraw, ImageFont
#
# # https://fontsforyou.com/ru/specific-fonts/ttf-fonts/languageru
# W = 600
# H = 400
#
# image = Image.new('RGB',
#                   (W, H),
#                   (0, 163, 232))
#
# draw = ImageDraw.Draw(image)
#
# text = 'Солнечный день'
# # draw.ellipse((470, -120, 800, 120), outline='yellow', fill='yellow')
# draw.circle((600, 0), 100, fill='yellow')
# font = ImageFont.truetype(
#     font='fonts/PfdintextcompproItalic.ttf',  # можно использовать любой установленный шрифт
#     size=50
# )
# # Получаем размеры текста
# _, _, w, h = draw.textbbox((0, 0), text, font=font)
#
# # Рассчитываем позицию для центрирования
# x = (W - w) // 2
# y = (H - h) // 2
#
# draw.text((x, y), text, fill=(255, 255, 0), font=font)
#
# image.save('images/sunny_day.jpg')
#
# #image.show()
#
#
# orig = Image.open('images/sunny_day.jpg').convert('RGB')
#
# up = orig.crop((0,0,600,200)) # отрезаем верх часть
# down = orig.crop((0,200,600,400))
# new = Image.new('RGB',(600,400))
# new.paste(down,(0,0))
# new.paste(up,(0,200))
# new.show()


# Фильтры
# from PIL import Image, ImageFilter, ImageEnhance
# orig = Image.open('images/vinny.jpg')
# # Размытие
# #blur_image = orig.filter(ImageFilter.BLUR)
# #blur_image = orig.filter(ImageFilter.GaussianBlur(radius=8))
# #Усиление резкости
# enchancer = ImageEnhance.Sharpness(orig)
# sharpened_image= enchancer.enhance(4)
#
# sharpened_image.show()
#


# Работа с документами
# DOCx - python-docx