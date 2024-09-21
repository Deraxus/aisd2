from unittest import TestCase, main
from dopTasks.ex16 import KMaxStructure


class Test(TestCase):
    def test_example(self):
        with open("input16.txt", "r") as file:
            n = int(file.readline().strip())
            commands = [list(map(int, file.readline().strip().split())) for _ in range(n)]

        kmax_structure = KMaxStructure()
        result = []

        for command in commands:
            if command[0] == 1:
                kmax_structure.add_element(command[1])
            elif command[0] == 0:
                result.append(str(kmax_structure.find_kth_max(command[1])))
            elif command[0] == -1:
                kmax_structure.delete_element(command[1])
        expected_output = ['7', '5', '3', '10', '7', '3']


        self.assertEqual(result, expected_output)
