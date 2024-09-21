from unittest import TestCase, main
from lab3.ex16 import detect_cycles, parse_input, write_output



def evaluate_commands(commands):
    results = []
    stack = []

    for command in commands:
        if command.startswith('p'):
            stack.append(command)
        elif command.startswith(' '):
            value = command.strip()
            if stack:
                top = stack.pop()
                if int(value) == 2 and top == 'p1':
                    results.append('YES')
                elif int(value) == 1 and top in ['p2', 'p3']:
                    results.append('YES')
                else:
                    results.append('NO')
        elif command == '*****':
            results.append('*****')

    return results

class Test(TestCase):
    def test_example(self):
        edges_list = parse_input('input16.txt')  # Путь к вашему входному файлу
        results = []

        for n, edges in edges_list:
            result = detect_cycles(n, edges)
            results.append(result)
        clearResults = []
        for i in results:
            clearResults.append(i[0])
        clearResults.reverse()
        expected_output = ['YES', 'YES', 'NO']
        self.assertEqual(clearResults, expected_output)


if __name__ == '__main__':
    main()