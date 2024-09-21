def read_graph_from_file(file_path):
    with open(file_path, "r") as file:
        n, m = map(int, file.readline().split())
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u, v = map(int, file.readline().split())
            graph[u - 1].append((v - 1, 0))
            graph[v - 1].append((u - 1, 1))
    return graph, n


def floyd_warshall(graph, n):
    dist = [[float("inf")] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u in range(n):
        for v, w in graph[u]:
            dist[u][v] = min(dist[u][v], w)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float("inf") and dist[k][j] != float("inf"):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def is_weakly_k_connected(dist, n, k):
    for u in range(n):
        for v in range(n):
            if u != v and dist[u][v] > k:
                return False
    return True


def find_min_k_connected(graph, n):
    dist = floyd_warshall(graph, n)

    low, high = 0, n
    while low < high:
        mid = (low + high) // 2
        if is_weakly_k_connected(dist, n, mid):
            high = mid
        else:
            low = mid + 1

    return low


def main(input_file='input17.txt', output_file='output17.txt'):
    graph, n = read_graph_from_file(input_file)
    result = find_min_k_connected(graph, n)
    with open(output_file, "w") as file:
        file.write(str(result))


if __name__ == "__main__":
    main()