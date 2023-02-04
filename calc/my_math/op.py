import math


def check_priority(formula):
    operands = [['s', 'c'], ['^'], ['*', '/'], ['+', '-']]
    for op in operands:
        for i in range(len(formula) - 1):
            if formula[i + 1] in op:
                tmp = [ops(x=formula[i], y=formula[i + 2], op=formula[i + 1])]
                return check_priority(formula[:i] + tmp + formula[(i+3):])
            elif formula[i + 1] not in op and formula[i] == '-':
                tmp = [ops(x=0, y=formula[i + 1], op=formula[i])]
                return check_priority(tmp + formula[(i + 2):])
            elif formula[i] in operands[0]:
                tmp = [trig(x=formula[i+1], op=formula[i])]
                print(tmp)
                return check_priority(formula[:i] + tmp + formula[(i+2):])

    return formula[0]


def ops(x, y, op):
    if op == '^':
        return x ** y
    elif op == '*':
        return x * y
    elif op == '/':
        if y == 0:
            return math.inf
        return x / y
    elif op == '+':
        return x + y
    elif op == '-':
        return x - y


def trig(x, op):
    if op == 's':
        return math.sin(x)
    elif op == 'c':
        return math.cos(x)


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
