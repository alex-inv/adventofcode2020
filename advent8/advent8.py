def main():
    file_name = "../input/input8.txt"
    my_file = open(file_name)

    lines = list(map(lambda s: s.strip(), my_file.readlines()))

    prog = parse_prog(lines)
    res = execute(prog)

    print(res)


def parse_prog(lines):
    res = []

    for line in lines:
        res.append((line[:3], int(line[3:])))

    return res


def execute(prog):
    idx, acc = 0, 0
    visited = [False for _ in prog]

    while True:
        if visited[idx]:
            break

        cmd = prog[idx][0]
        visited[idx] = True

        if cmd == 'acc':
            acc += prog[idx][1]
            idx += 1
        elif cmd == 'nop':
            idx += 1
        elif cmd == 'jmp':
            idx += prog[idx][1]

    return acc


if __name__ == '__main__':
    main()