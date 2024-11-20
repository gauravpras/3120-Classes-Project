class Animal:
    def __init__(self, nickname, species, habitat):
        self.nickname = nickname
        self.species = species
        self.habitat = habitat
        self.energy = 100
        self.satiation = 50

    def feed(self, food):
        print(f"{self.nickname} the {self.species} is eating {food}.")
        self.energy = min(self.energy + 15, 100)
        self.satiation = min(self.satiation + 30, 100)

    def rest(self):
        print(f"{self.nickname} the {self.species} is resting.")
        self.energy = 100
        self.satiation = max(self.satiation - 10, 0)

    def roam(self, distance):
        print(f"{self.nickname} is roaming.")
        self.energy = max(self.energy - distance * 2, 0)
        self.satiation = max(self.satiation - distance, 0)
