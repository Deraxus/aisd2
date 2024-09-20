def ford_bellman(g: list[list[int]], n: int, start: int) -> list[str]:
    d = [1000000001 for i in range(n)]
    d[start] = 0
    for i in range(n):
        for uv in g:
            d[uv[1]] = min(d[uv[1]], d[uv[0]] + uv[2])
    for uv in g:
        if d[uv[1]] != '-':
            if d[uv[0]] == '-' or d[uv[1]] > d[uv[0]] + uv[2]:
                d[uv[1]] = '-'
    for i in range(n):
        if d[i] == 1000000001:
            d[i] = '*'
        else:
            d[i] = str(d[i])
    return d


with open('input10.txt', 'r', encoding='utf-8') as file_input:
    with open('output10.txt', 'w', encoding='utf-8') as file_output:
        n, m = map(int, file_input.readline().split())
        g = []
        for i in range(m):
            u, v, d = map(int,file_input.readline().split())
            g.append([u - 1, v - 1, d])
        file_output.write('\n'.join(ford_bellman(g, n, int(file_input.readline()) - 1)))