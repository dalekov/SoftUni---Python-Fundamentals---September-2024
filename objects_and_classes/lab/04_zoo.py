class Zoo:
    __animals = []

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "bird":
            self.birds.append(name)
        elif species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)

    def get_info(self, species):
        if species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {len(self.birds) + len(self.mammals) + len(self.fishes)}"
        elif species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {len(self.birds) + len(self.mammals) + len(self.fishes)}"
        elif species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {len(self.birds) + len(self.mammals) + len(self.fishes)}"


name = input()
zoo = Zoo(name)

n = int(input())
for i in range(n):
    line = input().split()

    species = line[0]
    name = line[1]
    zoo.add_animal(species, name)


species = input()
print(zoo.get_info(species))


