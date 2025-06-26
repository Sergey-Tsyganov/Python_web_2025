#
num = 3
vars=''
print('Угадай число')
flag = True
while flag:
    vars= int(input('ваше значение'))
    if vars==num:
        print('угадал')
        flag = not flag
    else:
        vars = int(input('введи снова'))
print('приходи еще')

