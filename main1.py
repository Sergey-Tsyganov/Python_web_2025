# Коллекции
# 1.множества set
# это набор данных любого типа, не сохраняет порядка при выводе, дубли удаляются итерируемый объект
# 2.списки
# 3.словари
# 4.карточки

# 1
# методы 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard',
# 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset',
# 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

# s = set()  # пустое множество
# s = {'3', '5', '7', '3'}  # непустое множество
# # print(dir(s))
# # print(help(s.add))
# # print(type(s))  # распечатать класс
# # print(s)
# # print('есть ли 3')
# # if '3' in s:
# #     print('да')
# # if str(3) in s:
# #     print('число да')
# # for item in s:
# #     print(item)
# # print(f'число элементов в s = {len(s)}')
# #
# # print(s)
# # добавить в множество
# s.add('9')
# print(s)
# # удалить из множества
# #s.remove('3') если нет то ошибка
# # s.discard('3')  удаляет и не дает ошибки
# # temp=s.pop() # удаляет произвольный элемент
# print(s)
# операции надо множествами
# a = {1, 2, 3}
# b = {1, 2, 4}
# # объединение множеств
# c = a.union(b)  # или a|b
# print(c)
# # пересечение
# c = a.intersection(b) # a&b
# print(c)
#
# #разность
# c= a.difference(b) # есть в первом но нет во стором c=b-a
# print(c)
# # симметричная разность есть непересекающиеся элементы
# c= a.symmetric_difference(b) # b^a
#print(c)
# s=set() # создание пустого множества других вариантов нет
# # строки
# s='Python'
# print(s[0])
# #s[3]='y' нельзя
# s='длинношеее'
# slovar = {'а','е','о','у','и'}
# d = 'аеиоёуюя'
# count =0
# for i  in s:
#     if i in d:
#         count +=1
# print(count)
# s='Python'
# for  index in range(len(s)):
#     print (s[index])
# исправить букву в слове
# s = 'сабака'
# s1=''
# for index in range(len(s)):
#     if index == 1:
#         s1+='о'
#     else:
#         s1+=s[index]
# print(s1)
# ord(символ) код симвода в Unicode
# chr(символ) код симвода в Unicode
# s='\xB0'
# u='\u2603'
#
# print(f'25{s}C')
# print(f'25{u}C')
# print(f'код снеговика {ord('☃')}')
# print(chr(9731))
# s=input('введите фразу')
# s1=set()
# for index in range(len(s)):
#     s1.add(chr(index))
#     print(s1)
# шифр цезаря
# word = ('Привет')
# word2=''
# for i in range(1,len(word)+1):
#     word2 += word[i-1]*i
# print (word2)
# шифр цезаря
print('Программа шифрации и дешифрации кириллического текста со знаками')
print('препинания и математическими символами. Без знака \'')
print('Используется шифр Цезаря')
# word = input('Введите слово или предложение')
# word = 'Привет'
koded = ''
dekoded = ''
alphabet = '0123456789АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя,.!?:;"()+-*/=<>^% '
choice = input('ЧТо будем делать /n шифруем - 1 /n дешифруем - остальное: ')
if choice == '1':
    print('Шифрование текста')
    sdvig = int(input('Введите количество знаков, на который будет сдвиг: '))
    word = input('Введите слово или предложение: ')
    for i in range(len(word)):
        for j in range(len(alphabet)):
            if alphabet[j] == word[i]:
                if j+sdvig>=len(alphabet):
                    newnum = j+sdvig-len(alphabet)
                else:
                    newnum=j+sdvig
                koded += alphabet[newnum]
    print(koded)
else:
    print('Дешифрование текста')
    sdvig = int(input('Введите количество знаков, на который был сдвиг: '))
    word = input('Введите зашифрованный текст: ')
    for i in range(len(word)):
        for j in range(len(alphabet)):
            if alphabet[j] == word[i]:
                if j - sdvig < 0:
                    newnum = j - sdvig + len(alphabet)
                else:
                    newnum = j - sdvig
                dekoded += alphabet[newnum]
    print(dekoded)
