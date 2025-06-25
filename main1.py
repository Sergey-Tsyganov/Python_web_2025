#kghfkhkhg
text = """Витязь на распутье
Налево(L) пойдешь, вольну волю обретешь
Направо(R) пойдешь, коня потеряшь
Прямо(F) пойдешь, тоже хреново"""
print(text)
choice = input('Куда идем (RLF): ')
if choice == 'L' or choice == 'l':
    print('Воли захотел, фиг тебе')
elif choice == 'R' or choice == 'r':
    print('Гони коня')
elif choice == 'F' or choice == 'f':
    print('Уже хреново')
else:
    print('Фигню говоришь')
