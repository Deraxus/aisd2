with open('input13.txt', 'r', encoding='utf-8') as file_input:
    with open('output13.txt', 'w', encoding='utf-8') as file_output:
        n, m = map(int, file_input.readline().split())
        g = [[j for j in file_input.readline().strip()] for i in range(n)]
        k=0
        for i in range(n):
            for j in range(m):
                if g[i][j] == '#':
                    k += 1
                    s = [(i, j)]
                    while len(s) > 0:
                        x, y = s.pop()
                        if g[x][y] == '#':
                            g[x][y] = '.'
                            if x > 0:
                                s.append((x - 1, y))
                            if x < n - 1:
                                s.append((x + 1, y))
                            if y > 0:
                                s.append((x, y - 1))
                            if y < m - 1:
                                s.append((x, y + 1))
        file_output.write(str(k))
                            