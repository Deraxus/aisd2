from unittest import TestCase, main
from NewLabs.ex10 import ford_bellman, parse_input, write_output


class Test(TestCase):
    def test_example(self):
        g = parse_input("input10.txt")
        expected = ['0', '10', '-', '-', '-', '*']

        result = ford_bellman(g[0], g[1], g[2])

        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()