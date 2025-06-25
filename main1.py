name = 'Igor'
email = "aaa@bbb.ru"
age = 32
weight = 34.33
# способ
print('Имя: %s, E-mail: %s, Возраст: %d' % (name,email,age))
# 2 способ
#print('Имя: {}, E-mail: {}, Возраст: {}' .format(name,email.age))
# 3 способ
print(f'Имя: {name}, E-mail: {email},Возраст: {age} , weight{weight:6.3f}')