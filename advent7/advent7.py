import re


def main():
    file_name = "../input/input7.txt"
    my_file = open(file_name)

    lines = list(map(lambda s: s.strip(), my_file.readlines()))

    graph = inv(build_graph(lines))

    visited = {}
    dfs(norm_bag('shiny gold bag'), graph, visited)
    print(len(visited))


def dfs(bag, graph, visited):
    if graph.get(bag):
        for _, child in graph.get(bag):
            visited[child] = True
            dfs(child, graph, visited)


def inv(graph):
    inv_graph = {v: [] for v in graph}

    for v_parent in graph:
        for val, v_child in graph.get(v_parent):
            inv_graph[v_child].append((val, v_parent))

    return inv_graph


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
