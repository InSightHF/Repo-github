from time import sleep

"""Практическая работа по Теме 6 'ООП. Введение'"""

"""Задание 6.1."""

print('\n6.1.Создать класс TrafficLight (светофор).\n'
      '* определить у него один атрибут color (цвет) и метод running (запуск);\n'
      '* атрибут реализовать как приватный;\n'
      '* в рамках метода реализовать переключение светофора в режимы: красный,\n'
      '  жёлтый, зелёный;\n'
      '* продолжительность первого состояния (красный) составляет 7 секунд,\n'
      '  второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;\n'
      '* переключение между режимами должно осуществляться только в указанном\n'
      '  порядке (красный, жёлтый, зелёный);\n'
      '* проверить работу примера, создав экземпляр и вызвав описанный метод.\n'
      'Задачу можно усложнить, реализовав проверку порядка режимов. При его\n'
      'нарушении выводить соответствующее сообщение и завершать скрипт.')
print('-' * 75)

print('ПОЯСНЕНИЕ. Реальная работа светофора заклюяется в постоянном регулировании\n'
      'движения ТС, а именно в циклической смене основных цветов красного\n'
      '(запрещён проезд) на зелёный (разрешён проезд) и наоборот с зелёного на\n'
      'красный, причём каждая смена основных цветов происходит через вспомогательный\n'
      'жёлтый цвет (внимание, приготовиться).\n'
      'Поэтому программа данного светофора демонстрирует именно такой режим -\n'
      '16 секунд начального запуска (по условию задания - красный (7 с), жёлтый (2 с),\n'
      'зелёный (7 с)),и далее светофор может работать "постоянно", повторяющимися\n'
      'циклами по 18 секунд каждый (жёлтый, красный, жёлтый, зелёный).\n'
      'Для демонстрации количество циклов d = 2, но может быть любым...')
print('-' * 75)
print('Демонстрация работы реального светофора:')


class TrafficLight:
    __color = ['Red', 'yellow', 'Green']

    def running(self):
        i = 0
        while i != 3:
            print('+', TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(7)
            i += 1
        d = 2
        count = 0
        while count < d:
            count += 1
            i = 2
            while i > 0:
                i -= 1
                print(TrafficLight.__color[i])
                if i == 1:
                    sleep(2)
                elif i == 0:
                    sleep(7)
            i = 0
            while i != 2:
                i += 1
                print(TrafficLight.__color[i])
                if i == 1:
                    sleep(2)
                elif i == 2:
                    sleep(7)


t = TrafficLight()
t.running()

print('*' * 75)


"""Задание 6.2."""

print('\n6.2.Реализовать класс Road (дорога).\n'
      '* определить атрибуты: length (длина), width (ширина);\n'
      '* значения атрибутов должны передаваться при создании экземпляра класса;\n'
      '* атрибуты сделать защищёнными;\n'
      '* определить метод расчёта массы асфальта, необходимого для покрытия всей\n'
      '  дороги;\n'
      '* использовать формулу: длина * ширина * масса асфальта для покрытия одного\n'
      '  кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;\n'
      '* проверить работу метода.\n'
      'Например: 20 м * 5000 м * 25 кг * 5 см = 12500 т.')
print('-' * 75)


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height / 1000
        print(f'Результат расчёта:\n'
              f'Для покрытия всего дорожного полотна неободимо {round(asphalt_mass)} тонн массы асфальта.')


r = Road(5000, 20)
r.asphalt_mass()

print('*' * 75)


"""Задание 6.3."""

print('\n6.3.Реализовать базовый класс Worker (работник).\n'
      '* определить атрибуты: name, surname, position (должность), income (доход);\n'
      '* последний атрибут должен быть защищённым и ссылаться на словарь, содержащий\n'
      '  элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};\n'
      '* создать класс Position (должность) на базе класса Worker;\n'
      '* в классе Position реализовать методы получения полного имени сотрудника\n'
      '  (get_full_name) и дохода с учётом премии (get_total_income);\n'
      '* проверить работу примера на реальных данных: создать экземпляры класса\n'
      '  Position, передать данные, проверить значения атрибутов, вызвать методы\n'
      '  экземпляров.')
print('-' * 80)


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


p = Position('Ganna', 'Panova', 'N', 120000.50, 25300.33)
print(f'Требуемая информация о сотруднике:\n'
      f'Работник {p.get_full_name()} занимает должность {p.position}, и '
      f'имеет общий доход: {p.get_total_income():.2f} руб.')

print('*' * 80)


"""Задание 6.4."""

print('\n6.4.Реализовать базовый класс Car.\n'
      '* у класса должны быть следующие атрибуты: speed, color, name, is_police\n'
      '  булево). А также методы: go, stop, turn(direction), которые должны\n'
      '  сообщать, что машина поехала, остановилась, повернула (куда);\n'
      '* описать несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;\n'
      '* добавить в базовый класс метод show_speed, который должен показывать текущую\n'
      '  скорость автомобиля;\n'
      '* для классов TownCar и WorkCar переопределить метод show_speed. При значении\n'
      '  скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о\n'
      '  превышении скорости.\n'
      'Создать экземпляры классов, передать значения атрибутов. Выполнить доступ к\n'
      'атрибутам, вывести результат. Вызвать методы и показать результат.')
print('-' * 80)


class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'* Автомобиль {self.name} начал движение.'

    def stop(self):
        return f'\n* Автомобиль {self.name} остановился.'

    def turn(self, direction):
        return f'\n* Автомобиль {self.name} повернул {direction}'

    def show_speed(self):
        return f'\n* Скорость {self.name} {self.speed} км/ч.'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Это превышение допустимого.'
        else:
            return f'Это в пределах допустимого.'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nЭто превышение допустимого.'
        else:
            return f'Это в пределах допустимого.'


class PoliceCar(Car):
    pass


print('Вывод информации по автомобилям:')
town = TownCar('Toyota', 83, 'blue', False)
print('Первый - TownCar:\n' + town.go(), Car.show_speed(self=town), town.show_speed(), town.turn('налево.'),
      town.turn('направо.'), town.stop())
print('\t', '.' * 30)
sport = SportCar('Honda', 135, 'red', False)
print('Второй - SportCar:\n' + sport.go(), sport.show_speed(), sport.turn('налево.'), sport.stop())
print('\t', '.' * 30)
work = WorkCar('YAZ', 38, 'grey', False)
print('Третий - WorkCar:\n' + work.go(), Car.show_speed(self=work), work.show_speed(), work.turn('направо.'),
      work.turn('налево.'), work.stop())
print('\t', '.' * 30)
police = PoliceCar('Subaru', 99, 'white', True)
print('Четвёртый - PoliceCar:\n' + police.go(), police.show_speed(), police.turn('направо.'), police.stop())

print('*' * 80)


"""Задание 6.5."""

print('\n6.5.Реализовать класс Stationery (канцелярская принадлежность).\n'
      '* определить в нём атрибут title (название) и метод draw (отрисовка).\n'
      '  Метод выводит сообщение «Запуск отрисовки»;\n'
      '* создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);\n'
      '* в каждом классе реализовать переопределение метода draw. Для каждого класса\n'
      '  метод должен выводить уникальное сообщение;\n'
      '* создать экземпляры классов и проверить, что выведет описанный метод для \n'
      '  каждого экземпляра.')
print('-' * 80)


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'{self.title} - неинформативно.'


class Pencil(Stationery):
    def draw(self):
        return f'{self.title} - прекрасно!'


class Handle(Stationery):
    def draw(self):
        return f'{self.title} - размазанно.'


print('Вывод информации по канцелярским принадлежностям:')
pen = Pen('ручкой')
print('1)', Stationery.draw(self=pen), pen.draw())
pencil = Pencil('карандашом')
print('2)', Stationery.draw(self=pencil), pencil.draw())
handle = Handle('маркером')
print('3)', Stationery.draw(self=handle), handle.draw())

print('*' * 80)
print('END')
