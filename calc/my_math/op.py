def check_priority(formula):
    operands = [['.'], ['^'], ['*', '/'], ['+', '-']]
    for op in operands:
        for i in range(len(formula) - 1):
            if formula[i + 1] in op:
                tmp = [ops(x=formula[i], y=formula[i + 2], op=formula[i + 1])]
                return check_priority(formula[:i] + tmp + formula[(i+3):])
    return formula[0]


def inv(y):
    while y >= 1:
        y /= 10
    return y


def ops(x, y, op):
    if op == '.':
        return x + inv(y)
    elif op == '^':
        return x ** y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y
    elif op == '+':
        return x + y
    elif op == '-':
        return x - y


def par_ids(formula):
    o_p_id = 0
    c_p_id = len(formula)
    for i in range(len(formula)):
        if formula[i] == '(':
            o_p_id = i
        elif formula[i] == ')':
            c_p_id = i + 1
            return o_p_id, c_p_id

    return o_p_id, c_p_id


def parenthesis(formula):
    for i in range(len(formula) - 1):
        if formula[i] == '(':
            return parenthesis(formula[(i + 1):])
        elif formula[i] == ')':
            return parenthesis(formula[:i])
    return formula