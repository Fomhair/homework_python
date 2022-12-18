# Задача 2
# Найдите сумму цифр трехзначного числа.

def sum_numbers(numbers):
    result = 0
    for n in numbers:
        result += int(n)
    return result


def format_output(value):
    i = 0
    for v in value:
        if i != len(value) - 1:
            print(v, '+', end=' ')
        else:
            print(v, '->', end=' ')
        i += 1
    return value


# Задача 4
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали
# S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала
# в два раза больше журавликов, чем Петя и Сережа вместе?

def cranes_dict(value, persons):
    p = persons[0:3]
    s = int(value)
    cranes = {}
    cranes[p[0]] = s - s // 3 - (s % 3 > 0)
    cranes[p[1]] = (s - cranes[p[0]]) // 2
    cranes[p[2]] = s - cranes[p[0]] - cranes[p[1]]
    return cranes


def show_cranes(cranes):
    for k, v in cranes.items():
        print(f"{k.title()} makes {v} cranes")


# Задача 6
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за
# проезд и получали билет с номером. Счастливым билетом называют такой билет
# с шестизначным номером, где сумма первых трех цифр равна сумме последних
# трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

def is_happy(value):
    str1 = value[0:(len(value) // 2)]
    str2 = value[(len(value) // 2):len(value)]
    if sum_numbers(str1) == sum_numbers(str2):
        return True
    return False


def check_value(value, bool, msg_true='Yes', msg_false='No'):
    if bool:
        print(f"{value} -> {msg_true}")
    else:
        print(f"{value} -> {msg_false}")


# Задача 8
# Требуется определить, можно ли от шоколадки размером n × m долек отломить
# k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

def check_choco_slice(values):
    m = values[0]
    n = values[1]
    k = values[2]
    if k % m == 0 or k % n == 0:
        return True
    return False


###############################################################################
# ------------------------------- Результаты -------------------------------- #
###############################################################################

while True:
    try:
        task = input('Input task number or "q" to stop: ')
        if task == 'q':
            break
        elif task == '2':
            value = input('Input number: ')
            sum = sum_numbers(format_output(value))
            print(sum)
        elif task == '4':
            value = input('Input number of cranes: ')
            persons = ['kate', 'peter', 'sergey', 'some lazy person']
            cranes = cranes_dict(value, persons)
            show_cranes(cranes)
        elif task == '6':
            value = input('Input ticket value: ')
            print('Is your ticket happy?')
            check_value(value, is_happy(value))
        elif task == '8':
            values = []
            values.append(int(input('Input chocolate size (m): ')))
            values.append(int(input('Input chocolate size (n): ')))
            values.append(int(input('Input size of piece: ')))
            check_value(values, check_choco_slice(values),
                        'Awesome chocolate piese!',
                        'You can\'t cut off a piece of chocolate '
                        'with one cut :(')
    except ValueError:
        print('Incorrect value')
