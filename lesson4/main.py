import random


def main():
    while True:
        try:
            task = input('Input task number or "q" to stop: ')
            if task == 'q':
                break
            elif task == '22':
                n = int(input('Input N '))
                list1 = randint_list(n, -n, n)
                m = int(input('Input M '))
                list2 = randint_list(m, -m, m)
                sorted_list = sort_list(common_values(list1, list2))
                print(sorted_list)
            elif task == '24':
                bush = random.randint(6, 12)
                bushes = randint_list(bush, 0, bush * 2)
                print(f'Bushes: {bushes}')
                print('Max: ', max_per_run(bushes))
        except ValueError:
            print('Incorrect value')


def randint_list(n, start, end):
    result = []
    for i in range(0, n):
        result.append(random.randint(start, end))
    return result


'''
Задача 22:
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются 
в обоих наборах.
Пользователь вводит 2 числа.
n - кол-во элементов первого набора.
m - кол-во элементов второго набора.
Значения генерируются случайным образом.
'''


def common_values(list1, list2):
    result = []
    for el1 in list1:
        for el2 in list2:
            if el1 == el2 and el1 not in result:
                result.append(el1)
    return result


def sort_list(unsorted_list):
    def cycle(lst):
        tmp = 0
        i = 0
        while i < len(lst) - 1:
            tmp = lst[i + 1]
            if lst[i] > lst[i+1]:
                lst[i+1] = lst[i]
                lst[i] = tmp
            i += 1
        return lst
    j = 0
    sorted_list = []
    while j < len(unsorted_list):
        sorted_list = cycle(unsorted_list)
        j += 1
    return sorted_list


'''
Задача 24:
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой 
грядке, причем кусты высажены только по окружности. Таким образом, у каждого 
куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты 
обладают разной урожайностью, поэтому ко времени сбора на них выросло различное
число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым 
кустом, собирает ягоды с этого куста и с двух соседних с ним.

Напишите программу для нахождения максимального числа ягод, которое может 
собрать за один заход собирающий модуль, находясь перед некоторым кустом 
заданной во входном файле грядки.
'''


def max_per_run(bushes):
    i = 1
    maximum = bushes[i - 1] + bushes[i] + bushes[i + 1]
    while i < len(bushes) - 2:
        i += 1
        tmp = bushes[i - 1] + bushes[i] + bushes[i + 1]
        if tmp > maximum:
            maximum = tmp

    return maximum


main()