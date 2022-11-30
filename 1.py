N = [line.strip() for line in open('./in/1.txt').readlines()]
# N = [line.strip() for line in open('./in/1.test.txt').readlines()]

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


def part_1():
    steps = N[0].split(', ')
    x = y = 0
    direction = NORTH

    for turn, *distance in steps:
        distance = int("".join(distance))
        if turn == 'R': direction = (direction + 1) % 4
        else: direction = (direction + 3) % 4
        
        deltas = {
            NORTH: (0, +distance),
            EAST:  (+distance, 0),
            SOUTH: (0, -distance),
            WEST:   (-distance, 0)
        }

        dx, dy = deltas[direction]
        x += dx
        y += dy

    return abs(x) + abs(y)

def part_2():
    steps = N[0].split(', ')
    x = y = 0
    direction = NORTH

    visited = set()

    for turn, *distance in steps:
        distance = int("".join(distance))
        if turn == 'R': direction = (direction + 1) % 4
        else: direction = (direction + 3) % 4
        
        deltas = {
            NORTH: (0, +distance),
            EAST:  (+distance, 0),
            SOUTH: (0, -distance),
            WEST:   (-distance, 0)
        }

        dx, dy = deltas[direction]
        # x += dx
        # y += dy

        for ddx in range(abs(dx)):
            x += dx // abs(dx)

            if (x, y) in visited:
                return abs(x) + abs(y)
            visited.add((x, y))

        for ddy in range(abs(dy)):
            y += dy // abs(dy)

            if (x, y) in visited:
                return abs(x) + abs(y)
            visited.add((x, y))

if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())

