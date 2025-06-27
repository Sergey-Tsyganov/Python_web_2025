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
a = {1, 2, 3}
b = {1, 2, 4}
# объединение множеств
c = a.union(b)  # или a|b
print(c)
# пересечение
c = a.intersection(b) # a&b
print(c)

#разность
c= a.difference(b) # есть в первом но нет во стором c=b-a
print(c)
# симметричная разность есть непересекающиеся элементы
c= a.symmetric_difference(b) # b^a
print(c)
# s=set() # создание пустого множества других вариантов нет
