file_name = "../input/input2.txt"
my_file = open(file_name)

lines = my_file.readlines()

count = 0
for line in lines:
    arr = list(map(lambda s: s.strip(), line.split(":")))
    pattern, password = arr[0].split(" "), arr[1]
    min, max, symbol = int(pattern[0].split("-")[0]), int(pattern[0].split("-")[1]), pattern[1]

    letter_cnt = 0
    for chr in password:
        if chr == symbol: letter_cnt += 1

    if min <= letter_cnt <= max:
        count += 1

print(count)
