N = [line.strip() for line in open('./in/9.txt').readlines()]
# N = [line.strip() for line in open('./in/9.test.txt').readlines()]
# N = [line.strip() for line in open('./in/9.p2.test.txt').readlines()]


def parse(row):
    L = len(row)
    tokens = []
    seek = 0
    last_seek = 0
    while seek < L:
        if row[seek] == '(':
            tokens.append(row[last_seek: seek])
            last_seek = seek
            end = row.index(')', seek)
            marker = row[seek + 1: end]
            next_n, times = map(int, marker.split('x'))
            subsequence = row[end + 1: end + 1 + next_n]
            tokens.append((subsequence, times))
            seek = end + next_n
            last_seek = seek + 1
        seek += 1
    tokens.append(row[last_seek:])
    return tokens


def part_1():
    for row in N:
        tokens = parse(row)

        t = 0
        for token in tokens:
            if isinstance(token, tuple):
                sequence, times = token
                t += len(sequence) * times
            else:
                t += len(token)
        # print(t)
        return t


def part_2():
    def token_to_length(token):
        if isinstance(token, str):
            return len(token)
        sequence, times = token
        length = sum(map(token_to_length, parse(sequence)))
        return length * times

    for row in N:
        tokens = parse(row)
        length = sum(
            map(token_to_length, tokens)
        )
        # print(row, length)
        return length


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
