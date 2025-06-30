# cnhjrb
#startwith endwith
from builtins import PythonFinalizationError

# s='Cмотреть'
# if s.lower.startwith('смо')
#     print('Да')

# find
# s='Смотреть,видеть,вертеть'
# index=s.find('еть')
# print(s)
# есть ли есть в строке первое вхождение
#1.find('подстрока') - если есть от возвращает индекс
#2.find('подстрока',start) - если есть от возвращает индекс c мета страт
#2.find('подстрока',start, end) - если есть от возвращает индекс c мета страт до места end
#index=s.find('еть',10,15)
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
#s='+7-012-345-67-89'

#sliсe срез может быть у строки и у других коллекций, за исключением множеств(set)
#[начало:окончание(не включительно):шаг]
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


#Списки
# s={'3','4','5'}
# lst=list(s) #  превращение множества в список типколлекции и форма преобразования в коллекцию
# print(s)
# lst=list(range(1,10))
# print(l)

lst = [] # пустой список
# или
#lst = lst()
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

#создание аббревиатур
# s=list()
#
#
# while (item :=input('введите слово ')) !='':
#     s.append(item[0])
#
# print(*s,sep='')

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

#  распаковка и запаковка
# channels = ['red','green','blue']
# r,g,b, = channels
# print (r)
# a,b,c = 1,2,3
statist =[]
for _ in range(3):
    fio, ball = input('Введите фио Студента:' ), float(input('Введите средний балл:' ))
    statist.append((fio,ball))
print (*statist, sep='\n')

for st in statist:
    fio, ball = st
    print('Студент - ', fio, 'средний балл - ', ball)