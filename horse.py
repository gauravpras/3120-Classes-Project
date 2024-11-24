
from animal import Animal

class Horse(Animal):
    def __init__(self, nickname, habitat):
        super().__init__(nickname, "Horse", habitat)
        self.speed = 30  # Initial speed in km/h
        self.stamina = 70  # Stamina percentage

    def gallop(self, duration):
        print(f"{self.nickname} is galloping for {duration} minutes!")
        self.energy = max(self.energy - duration * 2, 0)
        self.satiation = max(self.satiation - duration * 1.5, 0)
        self.stamina = max(self.stamina - duration, 0)

    def rest_in_stable(self):
        print(f"{self.nickname} is resting in the stable.")
        self.energy = min(self.energy + 30, 100)
        self.stamina = min(self.stamina + 40, 100)

    def neigh(self):
        print(f"{self.nickname} says: Neigh!")

if __name__ == "__main__":
    myHorse = Horse("Spirit", "Open Plains")
    myHorse.neigh()
    myHorse.feed("hay")
    myHorse.gallop(20)
    myHorse.rest_in_stable()
    print(f"{myHorse.nickname}'s energy: {myHorse.energy}, satiation: {myHorse.satiation}, stamina: {myHorse.stamina}, speed: {myHorse.speed}")
