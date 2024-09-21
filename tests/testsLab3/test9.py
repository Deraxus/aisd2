from unittest import TestCase, main
from NewLabs.ex9 import read_graph_from_file, negative_cycles, write_result_to_file


class Test(TestCase):
    def test_example(self):
        n, graph = read_graph_from_file('input9.txt')
        result = negative_cycles(graph, n)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    main()