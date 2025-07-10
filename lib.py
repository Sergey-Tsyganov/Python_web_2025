def summ(a, b):
    return a + b


def diff(a, b):
    return a - b


if __name__ == '__main__':
    print('Это бибилиотека')


class Car:
    counter = 0  # счетчик машин

    def __init__(self, brand='Noname', model='Nomodel', color='Nocolor'):
        self.brand = brand
        self.nodel = model
        self.color = color
        self.engine_on = False
        Car.counter += 1

    def start_engine(self):
        self.engine_on = True

    def drive_to(self, place):
        if self.engine_on:
            print(f'едем {place} yf {self.brand}')
        else:
            print('не едем')

    def set_brand(self, new_brand):
        if new_brand:
            self.brand = new_brand

    def set_model(self, new_model):
        if new_model:
            self.model = new_model

    def set_color(self, new_color):
        if new_color:
            self.color = new_color

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_color(self):
        return self.color

    @staticmethod
    def get_counter():
        return Car.counter


class Student:
    pass

    def __init__(self, name='Bill', age=1, univercity=None):
        self._name = name
        self._age = age
        self._univercity = univercity

    def person_info(self):
        print(f'Человек с именем {self._name} возраста {self._age} из университета {self._univercity}')

    # setter
    def set_name(self, new_name):
        if new_name:
            self._name = new_name

    def set_age(self, new_age):
        if 0 < new_age < 140:
            self._age = new_age
        else:
            print('Некорректный возраст - ', new_age)

    def set_univercity(self, new_univercity):
        if new_univercity:
            self._univercity = new_univercity

    # getter
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_univercity(self):
        return self._univercity


class Employee:
    def __init__(self, name='Bill', age=1, company=None):
        self._name = name
        self._age = age
        self._company = company

    def person_info(self):
        print(f'Человек с именем {self._name} возраста {self._age} из компании {self._company}')

    # setter
    def set_name(self, new_name):
        if new_name:
            self._name = new_name

    def set_age(self, new_age):
        if 0 < new_age < 140:
            self._age = new_age
        else:
            print('Некорректный возраст - ', new_age)

    def set_company(self, new_company):
        if new_company:
            self._company = new_company

    # getter
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_company(self):
        return self._company


class Person:
    # свойства/поля клвсса
    # Статично классный свойство

    def __init__(self, name='Bill', age=1):
        self._name = name
        self._age = age

    def person_info(self):
        print(f'Человек с именем {self._name} возраста {self._age}')

    # setter
    def set_name(self, new_name):
        if new_name:
            self._name = new_name

    def set_age(self, new_age):
        if 0 < new_age < 140:
            self._age = new_age
        else:
            print('Некорректный возраст - ', new_age)

    # getter
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age


class Clicker:
    def __init__(self):
        self.counter = 0

    def click(self):
        self.counter += 1

    def get_counter(self):
        return self.counter

    def reset(self):
        self.counter = 0


class Separator:
    def __init__(self):
        self.odd = []
        self.even = []

    def add_num(self, num):
        if num % 2 == 0:
            self.odd.append(num)
        else:
            self.even.append(num)

    def get_odd(self):
        return self.odd

    def get_even(self):
        return self.even


class Sorter:
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def result(self):
        return sorted(self.words, key=lambda x: len(x))


# Class Book:
#     def __init__(self, title, author):
#         self._title = title
#         self._autor = author
#
#
#     def get_title(self):
#         return self._title
#
#
#     def get_autor(self):
#         return self._autor

from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.name = "Круг"

    def perimetr(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2

    def get_name(self):
        return 'круг'


class Square:
    def __init__(self, width, height=0):
        self.width = width
        if height == 0:
            self.height = self.width
        else:
            self.height = height

    def perimetr(self):
        return (self.height + self.width) * 2

    def area(self):
        return self.height * self.width

    def get_name(self):
        return 'прямоугольник'


class Selector:
    def __init__(self, lst):
        self.lst = lst
        self.lst_odd = []
        self.lst_even = []

    def get_odd(self):
        for item in self.lst:
            if item % 2 != 0:
                self.lst_odd.append(item)
        return self.lst_odd

    def get_even(self):
        for item in self.lst:
            if item % 2 == 0:
                self.lst_even.append(item)
        return self.lst_even


class Stat:
    def __init__(self, vals):
        self.lst = vals[:]

    def get_min(self):
        if self.on_err():
            return min(self.lst)

    def get_max(self):
        if self.on_err():
            return max(self.lst)

    def on_err(self) -> bool:
        return all(isinstance(item, int) for item in self.lst)

# def shape_info(shape):
#     print(f'Площадь {shape.get_name()} {shape.area()}, периметр {shape.perimetr()} ')
