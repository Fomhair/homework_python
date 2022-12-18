# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые –
# гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

def min_dublicates(list):
    tmp = list[0]
    i = 0
    for el in list:
        if el == tmp:
            i += 1
    if i < len(list) // 2:
        return i
    return len(list) - i


# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя
# помогает Кате по математике. Он задумывает два натуральных числа X и Y
# (X,Y ≤ 1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

def find_xy(s, p):
    result = []
    for i in range(1, s):
        if i * (s - i) == p and len(result) < 2:
            result.append(i)
            result.append(s - i)
    if result:
        return result
    return 'Incorrect S and P'


# Вычисление тестовых значений
# def set_sp(value1, value2):
#     x = int(value1)
#     y = int(value2)
#     return [x + y, x * y]


# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2 в степени k),
# не превосходящие числа N.

def pow_series(value):
    n = int(value)
    result = []
    for i in range(0, n):
        if 2 ** i <= n:
            result.append(2 ** i)
    return result


###############################################################################
# ------------------------------- Результаты -------------------------------- #
###############################################################################

while True:
    try:
        task = input('Input task number or "q" to stop: ')
        if task == 'q':
            break
        elif task == '10':
            coins = [1, 0, 1, 0, 1, 1]
            print(f'{coins} -> {min_dublicates(coins)}')
            tmp_list = list(input())
            coins = []
            for el in tmp_list:
                coins.append(int(el))
            print(f'{coins} -> {min_dublicates(coins)}')
        elif task == '12':
            s = int(input('Set S: '))
            p = int(input('Set P: '))
            xy = find_xy(s, p)
            print(f'S = {s}, P = {p} -> {xy}')
        elif task == '14':
            list = pow_series(input('Input N: '))
            print(list)
    except ValueError:
        print('Incorrect value')
