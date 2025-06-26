print('алгоритм поиска решения квдратного уравнения ax^2+bx+c')
a=float(input('Введите a: '))
b=float(input('Введите b: '))
c=float(input('Введите  c: '))
if a!=0:
    discr = b**2 - 4 *a*c
    if discr<0:
        print('решения нет')
    elif discr==0:
        x=-b/(2*a)
        print(f'решение одно: x =  {x:.2f}')
    else:
        print('два решения : \n\t x1= ',-b+discr**0.5/(2*a),'\n\t x2= ',(-b+discr**0.5/(2*a)))
else:
    print('По условию а не равно нулю должно быть')