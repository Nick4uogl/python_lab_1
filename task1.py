import argparse

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
    case _:
        raise ValueError('Not supported operand')
    