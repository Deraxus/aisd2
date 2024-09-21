from unittest import TestCase, main
from lab3.ex12 import labyrinth, parse_input, write_output


class Test(TestCase):
    def test_example(self):
        n = 3
        m = 2
        edges = [(1, 2, 10), (1, 3, 5)]
        colors = [10, 10, 10, 10, 5]

        result = labyrinth(n, m, edges, colors)

        self.assertEqual(result, '3')


if __name__ == '__main__':
    main()