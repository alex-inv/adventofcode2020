def main():
    file_name = "../input/input6.txt"
    my_file = open(file_name)

    lines = list(map(lambda s: s.strip(), my_file.readlines()))

    answers = []

    group_size = 0
    group_answer = {chr(ch) : 0 for ch in range(ord('a'), ord('z') + 1)}
    for line in lines:
        if line == "":
            answers.append((group_size, group_answer.copy()))
            group_size = 0
            group_answer = {chr(ch) : 0 for ch in range(ord('a'), ord('z') + 1)}
        else:
            group_size += 1

        for ch in line:
            group_answer[ch] += 1

    answers.append((group_size, group_answer))
    print(sum(list(map(map_answer_to_sum, answers))))


def map_answer_to_sum(answer):
    acc = 0
    target = answer[0]

    for ch in range(ord('a'), ord('z') + 1):
        if answer[1].get(chr(ch)) == target:
            acc += 1

    return acc


if __name__ == '__main__':
    main()