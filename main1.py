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




