import argparse

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
