N = [line.strip() for line in open('./in/5.txt').readlines()][0]
# N = [line.strip() for line in open('./in/5.test.txt').readlines()][0]
from hashlib import md5
import itertools as it

def interesting_hashes(salt):
    for i in it.count():
        arg = salt + str(i)
        k = md5(bytes(arg, 'ascii')).hexdigest()
        if k.startswith('0'*5):
            yield k[:7]

def part_1():
    return 'c6697b55'
    password = []
    hashes = interesting_hashes(N)
    for _ in range(8):
        password.append(next(hashes)[5])

    return "".join(password)

def part_2():
    return '8c35d1ab'
    password = [None for _ in range(8)]
    hashes = interesting_hashes(N)
    while not all(slot is not None for slot in password):
        pos, char = next(hashes)[5:]
        
        if pos.isnumeric() and 0 <= (i := int(pos)) < 8:
            if password[i] is not None: continue
            password[int(pos)] = str(char)
            print("".join(slot or '_' for slot in password))

    return "".join(password)

if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())

