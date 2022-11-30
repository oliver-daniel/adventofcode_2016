N = [line.strip() for line in open('./in/7.txt').readlines()]
# N = [line.strip() for line in open('./in/7.test.txt').readlines()]
# N = [line.strip() for line in open('./in/7.p2.test.txt').readlines()]
import itertools as it


def contains_abba(s):
    for i in range(len(s) - 3):
        if s[i] == s[i + 3] and s[i + 1] == s[i + 2] and \
                s[i] != s[i + 1]:
            return s[i: i + 4]
    return None


def parse_row(row):
    out_of_brackets = []
    in_brackets = []
    last_i = 0
    for i, c in enumerate(row):
        if c == '[':
            s = row[last_i: i]
            out_of_brackets.append(s)
            last_i = i + 1
        elif c == ']':
            s = row[last_i: i]
            in_brackets.append(s)
            last_i = i + 1
    out_of_brackets.append(row[last_i:])
    return out_of_brackets, in_brackets


def part_1():
    t = 0
    for row in N:
        out_of_brackets, in_brackets = parse_row(row)

        if (not any(filter(contains_abba, in_brackets))) and \
                any(filter(contains_abba, out_of_brackets)):
            # print(row)
            t += 1
    return t

def aba_subsequences(s):
    for i in range(len(s) - 2):
        if s[i] != s[i + 1] and s[i] == s[i + 2]:
            yield s[i : i + 3]

def part_2():
    t = 0
    for row in N:
        in_ssqs = []
        out_ssqs = []
        out_of_brackets, in_brackets = parse_row(row)
        for group in in_brackets:
            in_ssqs.extend(aba_subsequences(group))
        for group in out_of_brackets:
            out_ssqs.extend(aba_subsequences(group))

        for x, y in it.product(in_ssqs, out_ssqs):
            if x[0] == y[1] and y[0] == x[1]:
                # print('Match!', x, y)
                t += 1
                break
    return t


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
