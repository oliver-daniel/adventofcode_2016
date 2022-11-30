N = [line.strip() for line in open('./in/8.txt').readlines()]
# N = [line.strip() for line in open('./in/8.test.txt').readlines()]


def print_grid(grid):
    for row in grid:
        print("".join(".#"[c] for c in row))


def transition(grid, command, *args):
    G = [row[:] for row in grid]

    if command == 'rect':
        cols, rows = args
        for row in range(rows):
            for col in range(cols):
                G[row][col] = True
    elif command == 'row':
        loc, val = args
        wt = len(grid[loc])
        for col in range(wt):
            G[loc][(col + val) % wt] = grid[loc][col]
    else:
        loc, val = args
        ht = len(grid)
        for row in range(ht):
            G[(row + val) % ht][loc] = grid[row][loc]
    return G


def part_1():
    W = 50
    H = 6
    grid = [[False for _ in range(W)] for _ in range(H)]

    for cmd in N:
        if cmd.startswith('rect'):
            _, etc = cmd.split()
            cols, rows = map(int, etc.split('x'))
            args = ('rect', cols, rows)
        elif cmd.startswith('rotate'):
            tokens = cmd.split()
            axis = tokens[1]
            loc = int(tokens[2][2:])
            val = int(tokens[4])

            args = (axis, loc, val)

        # print(args)
        grid = transition(grid, *args)
        # print_grid(grid)
        # print()

    return sum(
        sum(1 for col in row if col)
        for row in grid)


def part_2():
    return 'AFBUPZBJPS'


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
