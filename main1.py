# match  - case
print('Возможные ходы: \n\tL - влево\n\tR -вправо\n\tF -вперед\n\tQ -выход')
#ch = input('Ваш выбор: ')
while True:
    ch = input('Ваш выбор: ')
    match ch:
        case 'Q' | 'q':
            print('Выход')
            break
        case 'L' | 'l':
            print('Свернули налево')
        case 'R' | 'r':
            print('Свернули направо')
        case 'F' | 'f':
            print('Свернули прямо')
        case _:
            print('Выбор неверно')
