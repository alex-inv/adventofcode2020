def compute_y(y, max, y_inc):
    res = y + y_inc
    if res >= max:
        res %= max
    return res


file_name = "../input/input3.txt"
my_file = open(file_name)

lines = my_file.readlines()

max_y = 0
trees = list()

for line in lines:
    max_y = len(line)
    tree_line = list()
    for chr in line:
        tree_line.append(True) if chr == '#' else tree_line.append(False)
    trees.append(tree_line)


def count_trees(x_inc, y_inc):
    count = 0
    next_y = 0
    for i in range(0, len(trees), x_inc):
        if trees[i][next_y]:
            count += 1
        next_y = compute_y(next_y, max_y, y_inc)
    return count


res = count_trees(1, 1) * count_trees(1, 3) * count_trees(1, 5) * count_trees(1, 7) * count_trees(2, 1)
print(res)
