import random


'''
Задача 16:
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
Заполните массив случайными натуральными числами от 1 до N/2.
Выведите, сколько раз X встречается в массиве.
'''


def show_list(input_f):
    def output_f(*args):
        print('List: ')
        result = input_f(*args)
        print(f'{result} ->')
        return result
    return output_f


@show_list
def random_list(N, mod = 1):
    result = []
    for n in range(1, N):
        result.append(random.randint(1, N//mod))
    return result


def find_x_count(x, A):
    count = 0
    for n in A:
        if n == x:
            count += 1
    return count


'''
Задача 18:
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
Заполните массив случайными натуральными числами от 1 до N.
Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.
'''


def find_nearest_x(x, A):
    result = len(A)
    compare = abs(result - x)
    tmp = 0

    for n in A:
        if compare > 0:
            tmp = abs(n - x)
        if compare > tmp:
            compare = tmp
            result = n
    return result


'''
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.

А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.
'''


def scrabble(word):
    def cost_check(pack):
        cost = 0
        for c in word:
            if c in pack[0]:
                cost += 1
            elif c in pack[1]:
                cost += 2
            elif c in pack[2]:
                cost += 3
            elif c in pack[3]:
                cost += 4
            elif c in pack[4]:
                cost += 5
            elif c in pack[5]:
                cost += 8
            elif c in pack[6]:
                cost += 10
        return cost

    pack1 = ['AEIOULNSTR', 'DG', 'BCMP', 'FHVWY', 'K', 'JX', 'JX']
    pack2 = ['АВЕИНОРСТ', 'ДКЛМПУ', 'БГЁЬЯ', 'ЙЫ', 'ЖЗХЦЧ', 'ШЭЮ', 'ФЩЪ']
    return cost_check(pack1) + cost_check(pack2)





def main():
    task = input('Input task number:')
    if task == '16':
        N = int(input('Input list length: '))
        x = int(input('Input X: '))
        A = random_list(N, 2)
        print(f'Find {find_x_count(x, A)} of X')
    elif task == '18':
        N = int(input('Input list length: '))
        x = int(input('Input X: '))
        A = random_list(N)
        print(f'Nearest number is {find_nearest_x(x, A)}')
    elif task == '20':
        word = input('Input word: ').upper()
        print(f'Word cost is {scrabble(word)}')


while True:
   main()
   exit = 'q' == input('Enter q to exit: ')
   if exit: break