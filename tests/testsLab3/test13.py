from unittest import TestCase, main
from lab3.ex13 import count_components, parse_input, write_output


class Test(TestCase):
    def test_example(self):
        n = 5
        m = 10
        grid = [
            list('##......#.'),
            list('.#..#...#.'),
            list('.###....#.'),
            list('..##....#.'),
            list('........#.')
        ]
        result = count_components(n, m, grid)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    main()