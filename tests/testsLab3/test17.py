from unittest import TestCase, main
from lab3.ex17 import floyd_warshall, find_min_k_connected, is_weakly_k_connected, read_graph_from_file


class Test(TestCase):
    def test_example(self):
        graph, n = read_graph_from_file("input17.txt")
        result = find_min_k_connected(graph, n)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    main()