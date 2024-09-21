def ford_bellman(g: list[list[int]], n: int, start: int) -> list[str]:
    d = [1000000001 for _ in range(n)]
    d[start] = 0

    for _ in range(n):
        for uv in g:
            if d[uv[0]] != 1000000001:
                d[uv[1]] = min(d[uv[1]], d[uv[0]] + uv[2])

    for uv in g:
        if d[uv[1]] != '-' and (d[uv[0]] == '-' or d[uv[1]] > d[uv[0]] + uv[2]):
            d[uv[1]] = '-'

    for i in range(n):
        if d[i] == 1000000001:
            d[i] = '*'
        else:
            d[i] = str(d[i])

    return d


def parse_input(file_path: str) -> tuple:
    with open(file_path, 'r', encoding='utf-8') as file_input:
        n, m = map(int, file_input.readline().split())
        g = []
        for _ in range(m):
            u, v, d = map(int, file_input.readline().split())
            g.append([u - 1, v - 1, d])
        start = int(file_input.readline()) - 1
    return g, n, start


def write_output(file_path: str, output: list[str]):
    with open(file_path, 'w', encoding='utf-8') as file_output:
        file_output.write('\n'.join(output))


if __name__ == '__main__':
    g, n, start = parse_input('input10.txt')
    output = ford_bellman(g, n, start)
    write_output('output10.txt', output)