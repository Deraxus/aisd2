from unittest import TestCase, main
from lab3.ex5 import unitFunc


class Test(TestCase):
    def test_example(self):
        result = unitFunc("input5.txt", "output5.txt")
        self.assertEqual(result, 2)


if __name__ == '__main__':
    main()