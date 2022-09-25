import argparse

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
