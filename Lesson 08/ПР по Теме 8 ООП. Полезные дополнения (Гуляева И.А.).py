
"""Практическая работа по Теме 8 'ООП. Полезные дополнения'"""

"""Задание 8.1."""

print('\n8.1.Реализовать класс «Дата», функция-конструктор которого должна принимать\n'
      'дату в виде строки формата «день-месяц-год». В рамках класса реализовать два\n'
      'метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц,\n'
      'год и преобразовывать их тип к типу «Число». Второй, с декоратором\n'
      '@staticmethod, должен проводить валидацию числа, месяца и года (например,\n'
      'месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.')
print('-' * 80)


class Date:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f'Имеем данные: {self.data} {type(self.data)}'

    @classmethod
    def test(cls, data):
        try:
            day, month, year = data.replace('-', ' ').replace('.', ' ').split()
            day, month, year = int(day), int(month), int(year)
            return f'Число: {day} - это день. {type(day)}\n' \
                   f'Число: {month} - это месяц. {type(month)}\n' \
                   f'Число: {year} - это год. {type(year)}'
        except ValueError:
            return 'Указана некорректная дата!'

    @staticmethod
    def valid(data):
        try:
            day, month, year = [int(i) for i in data.replace('-', ' ').replace('.', ' ').split()]
            if 1 <= day <= 31:
                if 1 <= month <= 12:
                    if 1 <= year <= 5000:
                        return 'Такая дата имеет место быть!'
                    else:
                        return f'Указан неправильный год.'
                else:
                    return f'Указан нереальный месяц.'
            else:
                return f'Указан нереальный день.'
        except ValueError:
            return 'Или в принципе не дата!?!?'


print('1-й пример исследования даты:')
d = '22-12-2018'
print(Date(d))
print(Date.test(d))
print(Date.valid(d))
print('\t', '.' * 30)
print('2-й пример исследования даты:')
d = '30.05.1970'
print(Date(d))
print(Date.test(d))
print(Date.valid(d))
print('\t', '.' * 30)
print('3-й пример исследования даты:')
d = '15-15-1588'
print(Date(d))
print(Date.test(d))
print(Date.valid(d))
print('\t', '.' * 30)
print('4-й пример исследования даты:')
d = 'ДД:ММ:ГГГГ'
print(Date(d))
print(Date.test(d))
print(Date.valid(d))

print('*' * 75)


"""Задание 8.2."""

print('\n8.2.Создать собственный класс-исключение, обрабатывающий ситуацию деления\n'
      'на ноль. Проверить его работу на данных, вводимых пользователем. При вводе\n'
      'нуля в качестве делителя программа должна корректно обработать эту ситуацию\n'
      'и не завершиться с ошибкой.')
print('-' * 75)


class DivisionByZero(Exception):
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    @staticmethod
    def requests():
        count = 0
        while True:
            count += 1
            n1 = input('Введите первое число (делимое):\n\tn1 = ')
            n2 = input('Введите второе число (делитель):\n\tn2 = ')
            if not (n1 or n2):
                print('Вы не ввели данные. Попробуйте новый ввод.')
                print('\t', '.' * 30)
                continue
            try:
                n1 = float(n1)
                n2 = float(n2)
                print('Вы ввели числа.')
            except Exception as err:
                print(f'Нужно ввести число! {err}')
                print('Осуществите корректный ввод.')
                print('\t', '.' * 30)
                continue
            try:
                g = n1 / n2
                return f'Замечательно! Ввод верных данных осуществлён с {count}-й попытки.\n' \
                       f'И результат деления введённых чисел (частное) равен: {g:.2f}'
            except Exception as err:
                print(f'Однако попытка деления на ноль не допустима! {err}')
                print('У Вас есть возможность ввести другие числа.')
                print('\t', '.' * 30)


print('Программа проверки ввода данных для деления:')
print('..^..' * 9)
print(DivisionByZero.requests())

print('*' * 80)


"""Задание 8.3."""

print('\n8.3.Создать собственный класс-исключение, который должен проверять содержимое\n'
      'списка на наличие только чисел. Проверить работу исключения на реальном примере.\n'
      'Запрашивать у пользователя данные и заполнять список необходимо только числами.\n'
      'Класс-исключение должен контролировать типы данных элементов списка.\n'
      'Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,\n'
      'пока пользователь сам не остановит работу скрипта, введя, например, команду\n'
      '«stop». При этом скрипт завершается, сформированный список с числами\n'
      'выводится на экран.\n'
      'Подсказка: для этого задания примем, что пользователь может вводить только числа\n'
      'и строки. Во время ввода пользователем очередного элемента необходимо реализовать\n'
      'проверку типа элемента. Вносить его в список, только если введено число.\n'
      'Класс-исключение должен не позволить пользователю ввести текст (не число) и\n'
      'отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться')
print('-' * 85)


class ExceptionsInput:
    def __init__(self, *args):
        self.args = args
        self.numeric_list = []

    def requests(self):
        while True:
            try:
                meaning = input('Введите любое число, и нажмите клавишу "Enter":\n\tmeaning = ')
                if meaning == 'stop':
                    if len(self.numeric_list) == 0:
                        print('Список пуст.')
                    else:
                        print(f'В завершённом списке количество чисел = {len(self.numeric_list)}:\n\t'
                              f'{self.numeric_list}.')
                    return f'Вы остановили программу вводом ключевого слова "stop".'
                    break
                else:
                    meaning = float(meaning)
                    self.numeric_list.append(meaning)
                    print(f'Текущий список чисел: {self.numeric_list}')
            except ValueError:
                print(f'Вы ввели слово, или - букву, или - набор символов, или - ничего не ввели,\n'
                      f'напоминаю - подобный ввод не заносится в список.')
                query = input(f'Внимание! Если Вы хотите завершить программу, введите слово "stop",\n'
                              f'если желаете продолжить заполнение списка, нажмите клавишу "Enter".\n\t'
                              f'Ваше решение: ')
                if query == 'stop':
                    if len(self.numeric_list) == 0:
                        print('Список пуст.')
                    else:
                        print(f'В завершённом списке количество чисел = {len(self.numeric_list)}:\n\t'
                              f'{self.numeric_list}.')
                    return f'Вы остановили программу вводом ключевого слова "stop".'
                    break
                else:
                    print('Программа продолжает работу:')


print('Программа формирования списка введённых чисел:')
print('..^..' * 9)
try_except = ExceptionsInput()
print(try_except.requests())

print('*' * 85)


"""Задание 8.4-5-6."""

print('\n8.4-5-6.Начать работу над проектом «Склад оргтехники». Создать класс,\n'
      'описывающий склад. А также класс «Оргтехника», который будет базовым для\n'
      'классов-наследников. Эти классы — конкретные типы оргтехники (принтер,\n'
      'сканер, ксерокс). В базовом классе определить параметры, общие для\n'
      'приведённых типов. В классах-наследниках реализовать параметры, уникальные\n'
      'для каждого типа оргтехники.\n'
      'Продолжить работу над первым заданием. Разработать методы, которые отвечают\n'
      'за приём оргтехники на склад и передачу в определённое подразделение компании.\n'
      'Для хранения данных о наименовании и количестве единиц оргтехники, а также\n'
      'других данных, можно использовать любую подходящую структуру (например, словарь).\n'
      'Продолжить работу над вторым заданием. Реализовать механизм валидации вводимых\n'
      'пользователем данных. Например, для указания количества принтеров, отправленных\n'
      'на склад, нельзя использовать строковый тип данных.\n'
      'Подсказка: постараться реализовать в проекте «Склад оргтехники» максимум\n'
      'возможностей, изученных на уроках по ООП...')
print('-' * 83)


class EquipmentWarehouse:
    """Класс, описывающий склад оргтехники"""
    print('Склад оргтехники:')


class OfficeEquipment:
    """Базовый класс оргтехники"""
    def __init__(self, producer, model, former, entrance, escape):
        self.producer = producer
        self.model = model
        self.former = former
        self.entrance = entrance
        self.escape = escape

    def balance(self):
        if self.entrance > 0 and self.escape > 0:
            rest = (self.former + self.entrance) - self.escape
            return f'остаток на складе: {rest} ед.'
        else:
            if self.entrance > 0:
                rest = self.former + self.entrance
                return f'остаток на складе: {rest} ед.'
            elif self.escape > 0:
                rest = self.former - self.escape
                return f'остаток на складе: {rest} ед.'
            else:
                return f'остаток на складе: {self.former} ед.'


class Printer(OfficeEquipment):
    """Класс принтер"""
    amount_p = 0

    def __init__(self, producer, model, p_type, former, entrance, escape):
        super().__init__(producer, model, former, entrance, escape)
        self.p_type = p_type
        Printer.amount_p += 1

    @staticmethod
    def name():
        return '<<Принтер>>'

    def __str__(self):
        return 'производитель: {} \tмодель: {} \tтип принтера: {} \tбыло: {} \tприбыло: {} \tубыло: {}'\
               .format(self.producer, self.model, self.p_type, self.former, self.entrance, self.escape)


class Scanner(OfficeEquipment):
    """Класс сканер"""
    amount_sc = 0

    def __init__(self, producer, model, s_type, former, entrance, escape):
        super().__init__(producer, model, former, entrance, escape)
        self.s_type = s_type
        Scanner.amount_sc += 1

    @staticmethod
    def name():
        return'<<Сканер>>'

    def __str__(self):
        return 'производитель: {} \tмодель: {} \tтип сенсора: {} \tбыло: {} \tприбыло: {} \tубыло: {}'\
               .format(self.producer, self.model, self.s_type, self.former, self.entrance, self.escape)


class Xerox(OfficeEquipment):
    """Класс ксерокс"""
    amount_x = 0

    def __init__(self, producer, model, category, former, entrance, escape):
        super().__init__(producer, model, former, entrance, escape)
        self.category = category
        Xerox.amount_x += 1

    @staticmethod
    def name():
        return '<<Ксерокс>>'

    def __str__(self):
        return 'производитель: {} \tмодель: {} \tкатегория: {} \tбыло: {} \tприбыло: {} \tубыло: {}'\
               .format(self.producer, self.model, self.category, self.former, self.entrance, self.escape)


p = Printer
p1 = Printer('Canon', 'ESD-453-1T', 'струйный', 7, 2, 0)
p2 = Printer('Brother', 'WEG-567-A', 'струйный', 27, 0, 0)
p3 = Printer('Ricoh', 'B-322HU-J', 'лазерный', 30, 3, 18)
print('\t', '.' * 30)
print(p.name(), 'количество позиций:', p.amount_p)
print('1)', p1.__str__())
print('2)', p2.__str__())
print('3)', p3.__str__())
print('1)', p1.balance())
print('2)', p2.balance())
print('3)', p3.balance())

s = Scanner
s1 = Scanner('Epson', 'HJYNN-32IB', 'CIS', 6, 0, 4)
s2 = Scanner('Avision', 'XFDE-77AS', 'CCD', 16, 4, 10)
s3 = Scanner('Kodak', 'JHY-54CC', 'CMOS', 22, 3, 8)
print('\t', '.' * 30)
print(s.name(), 'количество позиций:', s.amount_sc)
print('1)', s1.__str__())
print('2)', s2.__str__())
print('3)', s3.__str__())
print('1)', s1.balance())
print('2)', s2.balance())
print('3)', s3.balance())

x = Xerox
x1 = Xerox('Phaser', 'Y7856-HG', 'бытовой', 20, 4, 9)
x2 = Xerox('Xerox', 'YYY7670', 'офисный', 25, 0, 5)
x3 = Xerox('Pantum', 'CVE-56-45', 'профи', 5, 0, 1)
print('\t', '.' * 30)
print(x.name(), 'количество позиций:', x.amount_x)
print('1)', x1.__str__())
print('2)', x2.__str__())
print('3)', x3.__str__())
print('1)', x1.balance())
print('2)', x2.balance())
print('3)', x3.balance())

print('*' * 110)


"""Задание 8.7."""

print('\n8.7.Реализовать проект «Операции с комплексными числами». Создать класс\n'
      '«Комплексное число». Реализовать перегрузку методов сложения и умножения\n'
      'комплексных чисел. Проверить работу проекта. Для этого создать экземпляры\n'
      'класса (комплексные числа), выполнить сложение и умножение созданных\n'
      'экземпляров. Проверить корректность полученного результата.')
print('-' * 75)


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'- Сумма двух комплексных чисел составляет:\n\t' \
               f'z1+z2 = {(self.a + other.a) + (self.b + other.b)}'

    def __mul__(self, other):
        return f'- Произведение двух комплексных чисел составляет:\n\t' \
               f'z1*z2 = {self.a * other.a + self.b * other.b + (self.a * other.b + self.b * other.a)}'


z1 = complex(1.1+9j)
z2 = complex(5+1.5j)
print(f'Имеем комплексные числа:\n\tz1 = {z1} {type(z1)}\n\tz2 = {z2} {type(z2)}')
print('\t', '.' * 30)
print('Результаты операций с комплесными числами с перегрузкой методов:')
z3 = ComplexNumber(1.1, 9j)
z4 = ComplexNumber(5, 1.5j)
print(z3+z4)
print(z3*z4)
print('\t', '.' * 30)
print('ПРОВЕРКА. Результаты операций с комплесными числами с функцией complex:')
print(f'- Сумма двух комплексных чисел составляет:\n\t'
      f'z1+z2 = {z1+z2}')
print(f'- Произведение двух комплексных чисел составляет:\n\t'
      f'z1*z2 = {z1*z2}')

print('*' * 75)
print('END')
