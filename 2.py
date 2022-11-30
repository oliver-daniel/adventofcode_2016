N = [line.strip() for line in open('./in/2.txt').readlines()]
# N = [line.strip() for line in open('./in/2.test.txt').readlines()]


def part_1():
    keypad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    row = col = 1
    password = []

    deltas = {
        'U': (-1, 0),
        'R': (0, 1),
        'D': (1, 0),
        'L': (0, -1)
    }

    for ln in N:
        for cmd in ln:
            dr, dc = deltas[cmd]
            if 0 <= (row + dr) < 3:
                row += dr
            if 0 <= (col + dc) < 3:
                col += dc
        password.append(keypad[row][col])

    return "".join(password)


def part_2():
    keypad = [
        '00100',
        '02340',
        '56789',
        '0ABC0',
        '00D00'
    ]

    row = 2
    col = 0
    password = []

    deltas = {
        'U': (-1, 0),
        'R': (0, 1),
        'D': (1, 0),
        'L': (0, -1)
    }

    for ln in N:
        for cmd in ln:
            dr, dc = deltas[cmd]
            if 0 <= (row + dr) < 5 and keypad[row + dr][col] != '0':
                row += dr
            if 0 <= (col + dc) < 5 and keypad[row][col + dc] != '0':
                col += dc
        password.append(keypad[row][col])

    return "".join(password)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
