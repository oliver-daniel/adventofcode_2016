N = [line.strip() for line in open('./in/6.txt').readlines()]
# N = [line.strip() for line in open('./in/6.test.txt').readlines()]
from collections import Counter, defaultdict

cols = defaultdict(Counter)
for row in N:
    for i, c in enumerate(row):
        cols[i].update(c)

def part_1():
    ret = []
    for col in cols.values():
        val, _ = col.most_common(1)[0]
        ret.append(val)

    return "".join(ret)

def part_2():
    ret = []
    for col in cols.values():
        val, _ = col.most_common()[-1]
        ret.append(val)

    return "".join(ret)

if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())

