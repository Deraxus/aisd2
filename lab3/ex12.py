def labyrinth(n, m, edges, colors):
    g = {i: {} for i in range(1, n + 1)}

    for u, v, c in edges:
        g[u][c] = v
        g[v][c] = u

    node = 1
    for color in colors:
        if color in g[node]:
            node = g[node][color]
        else:
            return 'INCORRECT'
    return str(node)


def parse_input(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file_input:
        n, m = map(int, file_input.readline().split())
        edges = []
        for _ in range(m):
            u, v, c = map(int, file_input.readline().split())
            edges.append((u, v, c))
        file_input.readline()
        colors = list(map(int, file_input.readline().split()))
    return n, m, edges, colors


def write_output(file_path: str, output: str):
    with open(file_path, 'w', encoding='utf-8') as file_output:
        file_output.write(output)


if __name__ == '__main__':
    n, m, edges, colors = parse_input('input12.txt')
    output = labyrinth(n, m, edges, colors)
    write_output('output12.txt', output)