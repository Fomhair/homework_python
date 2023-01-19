'''
Задача 26:
Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.
'''


def pow_r(a, b):
    if b > 1:
        return a * pow_r(a, b-1)
    return a


'''
Задача 28:
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
неотрицательных чисел. Из всех арифметических операций допускаются только
+1 и -1. Также нельзя использовать циклы.
'''


def sum_r(a, b):
    if b > 0:
        a += 1
        return sum_r(a, b - 1)
    elif b < 0:
        a -= 1
        return sum_r(a, b + 1)
    return a


def main():
    task = input('Input task number:')
    if task == '26':
        a = int(input('Input a: '))
        b = int(input('Input b: '))
        print(f'Result: {pow_r(a, b)}')
    elif task == '28':
        a = int(input('Input a: '))
        b = int(input('Input b: '))
        print(f'Result: {sum_r(a, b)}')


while True:
   main()
   exit = 'q' == input('Enter q to exit: ')
   if exit: break