file_name = "../input/input2.txt"
my_file = open(file_name)

lines = my_file.readlines()

count = 0
for line in lines:
    arr = list(map(lambda s: s.strip(), line.split(":")))
    pattern, password = arr[0].split(" "), arr[1]
    first_pos, second_pos, symbol = int(pattern[0].split("-")[0]), int(pattern[0].split("-")[1]), pattern[1]

    if bool(password[first_pos - 1] == symbol) ^ bool(password[second_pos - 1] == symbol):
        count += 1

print(count)
