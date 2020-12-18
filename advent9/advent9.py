init_amount = 25


def main():
    file_name = "../input/input9.txt"
    my_file = open(file_name)

    vals = list(map(lambda s: int(s.strip()), my_file.readlines()))
    lookup = init_lookup(vals, init_amount)

    for i in range(init_amount, len(vals)):
        if not check_hit(vals[i], lookup):
            print(vals[i])
            break

        lookup.pop(vals[i - init_amount], None)
        lookup[vals[i - 1]] = set()
        for key in lookup.keys():
            lookup[key].add(key + vals[i])


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