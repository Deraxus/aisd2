
with open('input5.txt', 'r', encoding='utf-8') as file_input:
    with open('output5.txt', 'w', encoding='utf-8') as file_output:
        n, m = map(int, file_input.readline().split())
        order = []
        visited = [False for i in range(n)]
        g, g_reverse = [[] for i in range(n)], [[] for i in range(n)]
        for i in range(m):
            a, b = map(int, file_input.readline().split())
            g[a - 1].append(b - 1)
            g_reverse[b - 1].append(a - 1)
        def dfs1(u: int) -> None:
            visited[u] = True
            for i in range(len(g[u])):
                if not visited[g[u][i]]:
                    dfs1(g[u][i])
            order.append(u)
        def dfs2(v: int) -> None:
            visited[v] = True
            for i in range(len(g_reverse[v])):
                if not visited[g_reverse[v][i]]:
                    dfs2(g_reverse[v][i])
        for i in range(n):
            if not visited[i]:
                dfs1(i)
        visited = [False for i in range(n)]
        k=0
        for i in range(n):
            v = order[n - 1 - i]
            if not visited[v]:
                k += 1
                dfs2(v)
        file_output.write(str(k))   