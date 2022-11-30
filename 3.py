N = [line.strip() for line in open('./in/3.txt').readlines()]
# N = [line.strip() for line in open('./in/3.test.txt').readlines()]

def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def part_1():
    t = 0
    for a, b, c in map(str.split, N):
        if is_triangle(int(a), int(b), int(c)):
            t += 1
    return t

def part_2():
    triangles = []
    lns = iter(N)
    try:
        while True:
            rows = [next(lns).split() for _ in range(3)]
            triangles.extend([[row[i] for row in rows] for i in range(3)])
    except StopIteration: pass

    t = 0
    for a, b, c in triangles:
        if is_triangle(int(a), int(b), int(c)):
            t += 1
    return t
    

if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())

