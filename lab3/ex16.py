def detect_cycles(n, edges):
    d = {}
    g = [[] for _ in range(n)]

    for i in range(n):
        key, connections = edges[i]
        d[key] = i
        for value in connections:
            if value in d:  # Проверяем, есть ли узел в словаре
                g[i].append(d[value])

    def dfs(v: int, used: list, stack: set) -> bool:
        if v in stack:  # Если узел уже в стеке, найден цикл
            return True
        if used[v]:  # Если узел уже обработан, возвращаем False
            return False

        used[v] = True
        stack.add(v)

        for to in g[v]:
            if dfs(to, used, stack):
                return True

        stack.remove(v)  # Убираем узел из стека
        return False

    res = []
    used = [False] * n
    for cur in range(n):
        if dfs(cur, used, set()):
            res.append('NO')  # Найден цикл
        else:
            res.append('YES')

    return res


def parse_input(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file_input:
        content = file_input.read().strip().splitlines()

    edges_list = []
    current_block = []
    n = 0

    for line in content:
        line = line.strip()
        if line == '*****':
            if current_block:  # Если есть текущий блок, обрабатываем его
                edges_list.append(parse_block(current_block))
                current_block = []
        elif n == 0:
            n = int(line)  # Считываем количество узлов
        else:
            current_block.append(line)

    # Обрабатываем последний блок, если он есть
    if current_block:
        edges_list.append(parse_block(current_block))

    return edges_list


def parse_block(block: list):
    edges = []
    index = 0

    while index < len(block):
        key = block[index].strip()
        index += 1
        m = int(block[index].strip())
        index += 1
        connections = [block[index + i].strip() for i in range(m)]
        edges.append((key, connections))
        index += m

    return len(edges), edges


def write_output(file_path: str, output: list):
    with open(file_path, 'w', encoding='utf-8') as file_output:
        for result in output:
            file_output.write('\n'.join(result) + '\n')


if __name__ == '__main__':
    edges_list = parse_input('input16.txt')  # Путь к вашему входному файлу
    results = []

    for n, edges in edges_list:
        result = detect_cycles(n, edges)
        results.append(result)

    write_output('output16.txt', results)  # Путь к вашему выходному файлу
