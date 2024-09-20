class KMaxStructure:
    def __init__(self):
        self.elements = []
    
    def add_element(self, key):
        self.elements.append(key)
    
    def delete_element(self, key):
        self.elements.remove(key)
    
    def find_kth_max(self, k):
        sorted_elements = sorted(self.elements, reverse=True)
        return sorted_elements[k-1]

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

with open("output16.txt", "w") as file:
    file.write("\n".join(result))


