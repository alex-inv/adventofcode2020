file_name = "../input/input1.txt"
my_file = open(file_name)

lines = my_file.readlines()
lookup = set()
for line in lines:
    lookup.add(2020 - int(line.strip()))

for value in lookup:
    if 2020 - value in lookup:
        print(value * (2020 - value))
        break
