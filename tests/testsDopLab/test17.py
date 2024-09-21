from unittest import TestCase, main
from DopLabs.ex17 import count_phone_numbers


class Test(TestCase):
    def test_example(self):
        with open('input17.txt', 'r') as file:
            N = int(file.readline())

        result = count_phone_numbers(N)


        self.assertEqual(result, 16)
