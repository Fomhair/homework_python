from my_math.op import *


def calc(formula):
    if len(formula) > 1:
        p_ids = par_ids(formula)
        tmp = [check_priority(parenthesis(formula))]
        formula = formula[:p_ids[0]] + tmp + formula[p_ids[1]:]
        return calc(formula)
    return formula[0]
