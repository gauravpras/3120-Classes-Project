from Animal import Animal

class Lion(Animal):
    def __init__(self, nickname, habitat):
        super().__init__(nickname, "Lion", habitat)
        self.pride_name = None  
    def roar(self):
        print(f"{self.nickname} the Lion roars loudly!")
    def hunt(self):
        print(f"{self.nickname} is hunting for food.")
        self.energy = max(self.energy - 20, 0)
        self.satiation = min(self.satiation + 40, 100)
