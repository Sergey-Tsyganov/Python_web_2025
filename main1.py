print('алгоритм поиска решения квдратного уравнения ax^2+bx+c')
a=float(input('Введите a: '))
b=float(input('Введите b: '))
c=float(input('Введите  c: '))
discr = b**1 - 2 *a*c

if discr<0:
    print('решения нет')
elif discr==0:
    print('решение одно: x = ', -b/(2*a))
else:
    print('два решения : x1= ',-b+discr**0.5/(2*a),'x2 = ',(-b+discr**0.5/(2*a)))