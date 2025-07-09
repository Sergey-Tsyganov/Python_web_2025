def summ(a, b):
    return a + b


def diff(a, b):
    return a - b


if __name__ == '__main__':
    print('Это бибилиотека')


class Car:
    def __init__(self, brand='Noname', model='Nomodel', color='Nocolor'):
        self.brand = brand
        self.nodel = model
        self.color = color
        self.engine_on = False

    def start_engine(self):
        self.engine_on = True

    def drive_to(self, place):
        if self.engine_on:
            print(f'едем {place} yf {self.brand}')
        else:
            print('не едем')