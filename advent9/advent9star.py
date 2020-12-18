init_amount = 25


def main():
    file_name = "../input/input9.txt"
    my_file = open(file_name)

    vals = list(map(lambda s: int(s.strip()), my_file.readlines()))
    lookup = init_lookup(vals, init_amount)

    target = 0

    for i in range(init_amount, len(vals)):
        if not check_hit(vals[i], lookup):
            target = vals[i]
            break

        lookup.pop(vals[i - init_amount], None)
        lookup[vals[i - 1]] = set()
        for key in lookup.keys():
            lookup[key].add(key + vals[i])

    if target != 0:
        sum_arr = find_sum(vals, target)
        print(min(sum_arr) + max(sum_arr))


def find_sum(vals, target):
    sum = 0

    i, j = 0, 0
    while i <= j < len(vals):
        if sum == target:
            return vals[i:j]
        elif sum < target:
            sum += vals[j]
            j += 1
        else:
            sum -= vals[i]
            i += 1


def init_lookup(vals, amount):
    lookup = {}

    for i in range(0, amount):
        for j in range(i, amount):
            if not lookup.get(vals[i]):
                lookup[vals[i]] = set()
            lookup[vals[i]].add(vals[i] + vals[j])

    return lookup


def check_hit(val, lookup):
    for key in lookup.keys():
        if val in lookup.get(key):
            return True

    return False


if __name__ == '__main__':
    main()