import json

"""Практическая работа по Теме 5 'Работа с файлами'"""

"""Задание 5.1."""

print('\n5.1.Создать программный файл в текстовом формате, записать в него\n'
      'построчно данные, вводимые пользователем. Об окончании ввода данных\n'
      'будет свидетельствовать пустая строка.')
print('-' * 70)

"""Создание программного файла с использованием менеджера контекста,
и запись в новый текстовый файл введённых построчных данных"""
with open('new_file1.txt', 'a', encoding='utf-8') as line:
    count = 0
    while True:
        count += 1
        user_indite = input(f'Введите данные {count}-ой строки: ')
        line.write(user_indite + '\n')
        if not user_indite:
            break
print('Проверка закрытия файла после записи данных: ', line.closed)

print('\t', '.' * 30)

""""Вывод из нового текстового файла введённых ранее пользователем
построчных данных с использованием менеджера контекста"""
with open('new_file1.txt', 'r', encoding='utf-8') as line:
    for user_indite in line:
        print(user_indite, end='')
print('Проверка закрытия файла после вывода данных: ', line.closed)

print('*' * 70)


"""Задание 5.2."""

print('\n5.2.Создать текстовый файл (не программно), сохранить в нём несколько\n'
      'строк, выполнить подсчёт строк и слов в каждой строке.')
print('-' * 70)


def count_info():
    with open('new_file2.txt', 'r', encoding="utf-8") as file:
        my_l = file.read()
        print(f'Имеем текстовый файл с данными:\n{my_l}')
        file.seek(0)  # для повтора чтения файла, переводим курсор в начало первой строки
        print('\t', '.' * 30)
        my_l = file.readlines()
        print(f'Результат подсчёта:\nКоличество строк в файле: {len(my_l)}.')
        for i in range(len(my_l)):
            new_l = my_l[i].split()
            print(f'Количество слов в {i + 1}-ой строке: {len(new_l)}.')


count_info()

print('*' * 70)


"""Задание 5.3."""

print('\n5.3.Создать текстовый файл (не программно). Построчно записать фамилии\n'
      'сотрудников и величину их окладов (не менее 10 строк). Определить, кто из\n'
      'сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.\n'
      'Выполнить подсчёт средней величины дохода всех сотрудников.')
print('-' * 73)


def wages_record():
    with open('new_file3.txt', 'r', encoding="utf-8") as file:
        my_l = file.read()
        print(f'Имеем текстовый файл с окладами сотрудников:\n{my_l}')
        file.seek(0)
        print('\t', '.' * 30)
        my_l = file.readlines()
        little = []
        sm = 0
        for i in range(len(my_l)):
            salary = int((my_l[i].split())[1])
            sm += salary
            if salary < 20000:
                little.append((my_l[i].split())[0])
        print(f'Результат исследования:\nОклад менее 20 тысяч рублей имеют сотрудники: {" и ".join(little)}.')
        print(f'Средняя величина дохода всех сотрудников равна: {sm / len(my_l):.2f} рублей.')


wages_record()

print('*' * 70)


"""Задание 5.4."""

print('\n5.4.Создать (не программно) текстовый файл с английскими числительными:\n'
      'построчно. Написать программу, открывающую файл на чтение и считывающую\n'
      'построчно данные. При этом английские числительные должны заменяться на\n'
      'русские. Новый блок строк должен записываться в новый текстовый файл.')
print('-' * 70)


def rewrite_file():
    with open('new_file4.txt', 'r', encoding="utf-8") as file:
        my_l = file.read()
        print(f'Вывод данных файла с английскими числительными:\n{my_l}')
    print('\t', '.' * 30)

    num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    new_text = []
    with open('new_file4.txt', 'r', encoding="utf-8") as file:
        my_l = file.readlines()
        for i in my_l:
            i = i.split(' ', 1)
            new_text.append(num[i[0]] + ' ' + i[1])
        with open('new_file4.1.txt', 'w+', encoding="utf-8") as new_file:
            new_file.writelines(new_text)
            new_file.seek(0)
            my_l = new_file.read()
            print(f'Вывод данных нового файла c русскими числительными:\n{my_l}')


rewrite_file()

print('*' * 70)


"""Задание 5.5."""

print('\n5.5.Создать (программно) текстовый файл, записать в него программно набор\n'
      'чисел, разделённых пробелами. Программа должна подсчитывать сумму чисел в\n'
      'файле и выводить её на экран.')
print('-' * 75)


def summ():
    try:
        with open('new_file5.txt', 'w', encoding='utf-8') as file:
            x = input('Введите целые числа через пробел:\n\t')
            file.writelines(x)
            my_numb = x.split()
            print('Результат вычислений введённых чисел равен: ', sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле.')
    except ValueError:
        print('Вы осуществили некорректный ввод.')
    print('\t', '.' * 30)
    print('Проверка закрытия файла после вывода данных или исключения: ', file.closed)


summ()

print('*' * 75)


"""Задание 5.6."""

print('\n5.6.Сформировать (не программно) текстовый файл. В нём каждая строка\n'
      'должна описывать учебный предмет и наличие лекционных, практических и\n'
      'лабораторных занятий по предмету. Сюда должно входить и количество занятий.\n'
      'Необязательно, чтобы для каждого предмета были все типы занятий. Сформировать\n'
      'словарь, содержащий название предмета и общее количество занятий по нему.\n'
      'Вывести его на экран.')
print('-' * 80)


def presentive():
    my_dict = {}
    with open('new_file6.txt', 'r', encoding='utf-8') as file:
        print('Преобразования учебного предмета и состава занятий:')
        my_l = file.read().split('\n')
        for g in my_l:
            subject, roster = g.split(':')
            print(subject, roster)
            subject_sum = sum(int(k) for word in roster.split() for k in word.split('(') if k.isdigit())
            my_dict[subject] = subject_sum
        print('\t', '.' * 30)
        print(f'Результирующий словарь предметов и соответствующее им количество занятий:\n{my_dict}')


presentive()

print('*' * 88)


"""Задание 5.7."""

print('\n5.7.Создать вручную и заполнить несколькими строками текстовый файл,\n'
      'в котором каждая строка будет содержать данные о фирме: название, форма\n'
      'собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.\n'
      'Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а\n'
      'также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли\n'
      'её не включать. Далее реализовать список. Он должен содержать словарь с \n'
      'фирмами и их прибылями, а также словарь со средней прибылью. Если фирма\n'
      'получила убытки, также добавить её в словарь (со значением убытков).\n'
      'Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},\n'
      '{“average_profit”: 2000}]. Итоговый список сохранить в виде json-объекта\n'
      'в соответствующий файл. Пример json-объекта:\n'
      '[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]\n'
      'Подсказка: использовать менеджер контекста.')
print('-' * 80)


def fin_statistics():
    with open('new_file7.txt', 'r', encoding='utf-8') as file:
        my_l = file.read()
        print(f'Имеем файл с данными пяти фирм:\n{my_l}')
        print('\t', '.' * 30)
        file.seek(0)
        statistics = []
        profit = {}
        average_profit = {}
        prof = 0
        n = 5
        for j in file:
            name, firm, earning, damage = j.split()
            total = int(earning) - int(damage)
            if total >= 0:
                prof = prof + total
            else:
                n -= 1
            profit[name] = total
        statistics.append(profit)
        if n != 0:
            av = prof / n
            average_profit['average_profit'] = round(av)
            statistics.append(average_profit)
        else:
            print('Все компании работают в убыток')
        print('Реализованный список со словарём фирм и их прибылями, а также словарём средней прибыли:\n',
              statistics)
    with open('file.json', 'w+', encoding='utf-8') as json_file:
        json.dump(statistics, json_file)


fin_statistics()

print('*' * 115)
print('END')
