def main():
    file_name = "../input/input8.txt"
    my_file = open(file_name)

    lines = list(map(lambda s: s.strip(), my_file.readlines()))

    prog = parse_prog(lines)
    progs = generate_progs(prog)
    progs.append(prog)

    res = execute_all(progs)

    print(res)


def parse_prog(lines):
    res = []

    for line in lines:
        res.append((line[:3], int(line[3:])))

    return res


def generate_progs(prog):
    progs = []

    for idx in range(0, len(prog)):
        if prog[idx][0] == 'nop':
            new_prog = prog.copy()
            new_prog[idx] = ('jmp', prog[idx][1])
            progs.append(new_prog)
        elif prog[idx][0] == 'jmp':
            new_prog = prog.copy()
            new_prog[idx] = ('nop', prog[idx][1])
            progs.append(new_prog)

    return progs


def execute_all(progs):
    for prog in progs:
        res = execute(prog)
        if res != -1:
            return res


def execute(prog):
    idx, acc = 0, 0
    visited = [False for _ in prog]

    while idx < len(prog):
        if visited[idx]:
            return -1

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