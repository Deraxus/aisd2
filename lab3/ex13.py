def count_components(n, m, grid):
    k = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                k += 1
                s = [(i, j)]
                while s:
                    x, y = s.pop()
                    if grid[x][y] == '#':
                        grid[x][y] = '.'
                        if x > 0:
                            s.append((x - 1, y))
                        if x < n - 1:
                            s.append((x + 1, y))
                        if y > 0:
                            s.append((x, y - 1))
                        if y < m - 1:
                            s.append((x, y + 1))
    return k


def parse_input(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file_input:
        n, m = map(int, file_input.readline().split())
        grid = [list(file_input.readline().strip()) for _ in range(n)]
    return n, m, grid


def write_output(file_path: str, output: str):
    with open(file_path, 'w', encoding='utf-8') as file_output:
        file_output.write(output)


if __name__ == '__main__':
    n, m, grid = parse_input('input13.txt')
    result = count_components(n, m, grid)
    write_output('output13.txt', str(result))