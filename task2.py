import argparse
import operator
import math

parser = argparse.ArgumentParser(description='performs the standard math functions on the data')
parser.add_argument('math_func', help='math function')
parser.add_argument('operands', type=int, help='first operand', nargs="+")
args = parser.parse_args()


def std_func(operands, func, modules):
    for i in modules:
        if hasattr(i, func):
            math_func = getattr(i, func)
            if math_func == operator.truediv and args.operands[1] == 0:
                raise ZeroDivisionError("Can not divide by zero")
            return math_func(*operands)
    raise AttributeError("Your function is not found")


print(std_func(args.operands, args.math_func, (math, operator)))
