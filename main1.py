height = int(input('введите рост человека: '))
while 150 >= height <= 180:
    height = int(input('введите рост человека: '))
    print('Не подходит', height)
print(f'Рост: {height} - отлично')
