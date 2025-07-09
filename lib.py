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
