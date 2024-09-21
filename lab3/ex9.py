def negative_cycles(g: list[list[int]], n: int) -> bool:
    for start in range(n):
        d = [float('inf') for _ in range(n)]
        d[start] = 0
        for i in range(n):
            for uv in g:
                if d[uv[0]] < float('inf'):
                    d[uv[1]] = min(d[uv[1]], d[uv[0]] + uv[2])
        for uv in g:
            if d[uv[1]] > d[uv[0]] + uv[2]:
                return True
    return False

def read_graph_from_file(filename: str) -> tuple[int, list[list[int]]]:
    with open(filename, 'r', encoding='utf-8') as file_input:
        n, m = map(int, file_input.readline().split())
        g = []
        for i in range(m):
            u, v, d = map(int, file_input.readline().split())
            g.append([u - 1, v - 1, d])
    return n, g

def write_result_to_file(filename: str, result: bool):
    with open(filename, 'w', encoding='utf-8') as file_output:
        file_output.write(str(int(result)))

if __name__ == '__main__':
    n, graph = read_graph_from_file('input9.txt')
    result = negative_cycles(graph, n)
    write_result_to_file('output9.txt', result)