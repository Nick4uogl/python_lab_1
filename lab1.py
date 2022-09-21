import argparse
import operator


def task1():
    parser = argparse.ArgumentParser(description='Calculate different operations')
    parser.add_argument('x', type=int, help='first operand')
    parser.add_argument('operator', help='operator')
    parser.add_argument('y', type=int, help='second operand')
    args = parser.parse_args()

    match args.operator:
        case "/":
            print(args.x / args.y)
        case "-":
            print(args.x - args.y)
        case "*":
            print(args.x * args.y)
        case "+":
            print(args.x + args.y)


def task2():
    parser = argparse.ArgumentParser(description='performs the standard math functions on the data')
    parser.add_argument('math_func', help='math function')
    parser.add_argument('x', type=int, help='first operand')
    parser.add_argument('y', type=int, help='second operand')
    args = parser.parse_args()

    match args.math_func:
        case "truediv":
            print(operator.truediv(args.x, args.y))
        case "sub":
            print(operator.sub(args.x, args.y))
        case "mul":
            print(operator.mul(args.x, args.y))
        case "add":
            print(operator.add(args.x, args.y))


def task3():
    parser = argparse.ArgumentParser(description='performs the standard math functions on the data')
    parser.add_argument('input', help='entry for the formula according EBNF syntax', nargs='*')
    args = parser.parse_args()
    entry_formula = args.input

    def check_input(user_input):
        if not user_input[0].isdigit() or user_input == '' or not user_input[-1].isdigit():
            return False
        for i in range(len(user_input)):
            if not user_input[i].isdigit() and not user_input[i + 1].isdigit():
                return False

        return True

    def calculate(numbers, operators):
        result = numbers[0]
        for i in range(len(operators)):
            if operators[i] == '+':
                result += numbers[i + 1]
            else:
                result -= numbers[i + 1]

        return result

    def split_input(user_input):
        numbers = []
        operators = []
        num = ''

        for i in user_input:
            if i.isdigit():
                num += i
            elif i == '+':
                numbers.append(int(num))
                num = ''
                operators += i
            elif i == '-':
                numbers.append(int(num))
                num = ''
                operators += i

        numbers.append(int(num))

        return calculate(numbers, operators)

    if check_input(entry_formula):
        print("result = (True, " + str(split_input(entry_formula)) + ")")
    else:
        print("result = (False, None)")


def task4():
    parser = argparse.ArgumentParser(description='performs the standard math functions on the data')
    parser.add_argument('-W', '--capacity', type=int, help='capacity')
    parser.add_argument('-w', '--weights', help='weights', nargs='+')
    parser.add_argument('-n', '--bars_number', type=int, help='bars number')
    args = parser.parse_args()
    user_capacity = args.capacity
    user_weights = args.weights
    user_bars_number = args.bars_number

    def dynamic_bars(capacity, weights, bars_number):
        table = [[0 for x in range(capacity + 1)] for x in range(bars_number + 1)]
        for i in range(bars_number + 1):
            for j in range(capacity + 1):
                if i == 0 or j == 0:
                    table[i][j] = 0
                elif int(weights[i - 1]) <= j:
                    table[i][j] = max(int(weights[i - 1]) + table[i - 1][j - int(weights[i - 1])], table[i - 1][j])
                else:
                    table[i][j] = table[i - 1][j]

        return table[bars_number][capacity]

    print(dynamic_bars(user_capacity, user_weights, user_bars_number))
