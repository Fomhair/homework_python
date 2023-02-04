import math


def get_formula(line):
    try:
        print(line)
        line = line.split()
        line = ''.join(line)
        sym_list = list(line)
        ops = ('(', ')', '/', '*', '-', '+', '^', 'p', 'e', 's', 'c')
        formula = []
        num = ''
        for sym in sym_list:
            if sym not in ops:
                num += sym
            elif sym == 'p':
                num = math.pi
            elif sym == 'e':
                num = math.e
            else:
                if num != '':
                    formula.append(float(num))
                formula.append(sym)
                num = ''
        if num != '':
            formula.append(float(num))
        return formula
    except ValueError:
        return ['Incorrect input! \nPress /help for details.']

