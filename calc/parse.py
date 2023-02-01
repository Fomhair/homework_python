def get_formula(line):
    line = line.split()
    line.remove(line[0])
    line = ''.join(line)
    sym_list = list(line)
    ops = ('(', ')', '/', '*', '-', '+', '.', '^')
    formula = []
    num = ''
    for sym in sym_list:
        if sym not in ops:
            num += sym
        else:
            if num != '':
                formula.append(int(num))
            formula.append(sym)
            num = ''
    if num != '':
        formula.append(int(num))
    return formula
