file_name = "../input/input1.txt"
my_file = open(file_name)

lines = my_file.readlines()

values = list()
lookup = set()

for line in lines:
    values.append(int(line.strip()))
    lookup.add(int(line.strip()))

for i in values:
    for j in values:
        if 2020 - i - j in lookup:
            print(i * j * (2020 - i - j))
            exit()
