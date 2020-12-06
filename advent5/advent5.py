import functools


def main():
    file_name = "../input/input5.txt"
    my_file = open(file_name)

    lines = list(map(lambda s: s.strip(), my_file.readlines()))
    coords = list(map(map_to_coords, lines))
    result = functools.reduce(check, coords, 0)
    print(result)


def check(cur, pair):
    mul = pair[0] * 8 + pair[1]
    return mul if mul > cur else cur


def map_to_coords(str):
    res = ""
    for chr in str:
        if chr == 'B' or chr == 'R':
            res += '1'
        else:
            res += '0'

    return int(res[:-3], 2), int(res[-3:], 2)


if __name__ == '__main__':
    main()