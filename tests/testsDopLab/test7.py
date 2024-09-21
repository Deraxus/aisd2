from unittest import TestCase, main
from DopLabs.ex7 import max_boots


class Test(TestCase):
    def test_example(self):
        with open("input7.txt", "r") as file:
            K, n = map(int, file.readline().split())
            repair_times = list(map(int, file.readline().split()))
        result = max_boots(K, n, repair_times)
        self.assertEqual(result, 2)
