def main():
    file_name = "../input/input6.txt"
    my_file = open(file_name)

    lines = list(map(lambda s: s.strip(), my_file.readlines()))

    answers = []

    group_answer = {}
    for line in lines:
        if line == "":
            answers.append(group_answer.copy())
            group_answer = {}
        for ch in line:
            group_answer[ch] = True

    answers.append(group_answer)
    print(sum(list(map(map_answer_to_sum, answers))))


def map_answer_to_sum(answer):
    acc = 0

    for ch in range(ord('a'), ord('z') + 1):
        if answer.get(chr(ch)):
            acc += 1

    return acc


if __name__ == '__main__':
    main()