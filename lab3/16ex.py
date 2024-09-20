with open('input16.txt', 'r', encoding='utf-8') as file_input:
    with open('output16.txt', 'w', encoding='utf-8') as file_output:
        n = int(file_input.readline().strip())
        d = {}
        g = [[] for _ in range(n)]

        for i in range(n):
            key = file_input.readline().strip()
            d[key] = i
            try:
                m = int(file_input.readline().strip())
            except ValueError:
                continue
            for _ in range(m):
                value = file_input.readline().strip()
                if value in d:
                    g[i].append(d[value])
        
        def dfs(v: int, used: list, f: list) -> None:
            used[v] = True
            for to in g[v]:
                if to == cur:
                    f[0] = True
                if not used[to]:
                    dfs(to, used, f)

        res = []
        for cur in range(n):
            used = [False] * n
            f = [False]
            dfs(cur, used, f)
            if f[0]:
                pass
            else:
                res.append('YES')

        res.append('NO')
        file_output.write('\n'.join(res))
