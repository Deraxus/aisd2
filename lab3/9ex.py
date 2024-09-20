def negative_cycles(g: list[list[int]], n: int) -> bool:
    for start in range(n):
        d = [1 for i in range(n)]
        d[start] = 0
        for i in range(n):
            for uv in g:
                d[uv[1]] = min(d[uv[1]], d[uv[0]] + uv[2])
        for uv in g:
            if d[uv[1]] > d[uv[0]] + uv[2]:
                return True
    return False

with open('input9.txt', 'r', encoding='utf-8') as file_input:
    n, m = map(int, file_input.readline().split())
    g = []
    for i in range(m):
        u, v, d = map(int, file_input.readline().split())
        g.append([u - 1, v - 1, d])
    with open('output9.txt', 'w', encoding='utf-8') as file_output:
        file_output.write(str(int(negative_cycles(g, n))))
