from string import ascii_lowercase as alpha
from collections import Counter
N = [line.strip() for line in open('./in/4.txt').readlines()]
# N = [line.strip() for line in open('./in/4.test.txt').readlines()]


def is_real_room(room):
    *letters, etc = room.split('-')
    sector_id = etc[:-7]
    checksum = etc[-6:-1]

    ct = Counter()
    for group in letters:
        ct.update(group)

    expected_checksum = "".join(
        sorted(ct.keys(), key=lambda key: (ct[key], -(ord(key) - ord('a'))),
               reverse=True))[:5]

    if checksum == expected_checksum:
        return int(sector_id)
    return 0


def part_1():
    return sum(map(is_real_room, N))


def part_2():
    # room = 'qzmt-zixmtkozy-ivhz-343'
    # *tokens, sector_id = room.split('-')
    # sector_id = int(sector_id)

    def decrypt_char(sector_id): return lambda char: chr(
        (ord(char) - ord('a') + sector_id) % 26 + ord('a')
    )

    for room in filter(is_real_room, N):
        *tokens, sector_id = room[:-7].split('-')
        sector_id = int(sector_id)
        decrypted = " ".join(
            "".join(map(decrypt_char(sector_id), token)) for token in tokens)
        if "north" in decrypted:
            return sector_id


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
