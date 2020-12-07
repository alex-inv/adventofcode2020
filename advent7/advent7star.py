import re


def main():
    file_name = "../input/input7.txt"
    my_file = open(file_name)

    lines = list(map(lambda s: s.strip(), my_file.readlines()))

    graph = build_graph(lines)

    result = dfs(norm_bag('shiny gold bag'), graph)
    print(result)


def dfs(bag, graph):
    acc = 0

    for idx, child in graph.get(bag):
        acc += idx + idx * dfs(child, graph)

    return acc


def build_graph(lines):
    graph = {}

    for line in lines:
        contain = re.search('^(.+) contains? (.+)\.$', line, re.IGNORECASE)

        arr = []
        for bag in map(lambda s: s.strip(), contain.group(2).split(',')):
            if bag == 'no other bags':
                continue
            else:
                arr.append(((int(bag[:1])), norm_bag(bag[2:])))

        graph[norm_bag(contain.group(1))] = arr

    return graph


def norm_bag(bag):
    return bag + 's' if bag[-1:] != 's' else bag


if __name__ == '__main__':
    main()
