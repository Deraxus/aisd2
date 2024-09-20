with open('input12.txt', 'r', encoding='utf-8') as file_input:
    with open('output12.txt', 'w', encoding='utf-8') as file_output:
        n, m = map(int, file_input.readline().split())
        g = {i: {} for i in range(1, n + 1)}
        for i in range(m):
            u, v, c = map(int, file_input.readline().split())
            g[u][c] = v
            g[v][c] = u
        file_input.readline()
        colors = [int(i) for i in file_input.readline().split()]
        def labyrinth() -> str:
            node = 1
            for color in colors:
                if color in g[node]:
                    node = g[node][color]
                else:
                    return 'INCORRECT'
            return str(node)
        file_output.write(labyrinth())