from animal import Animal

class Cat(Animal):
    def __init__(self, nickname, habitat):
        super().__init__(nickname, "Cat", habitat)
        self.affection_level = 70

    def meow(self):
        print(f"{self.nickname} says: Meow!")

    def cuddle(self, minutes):
        print(f"Cuddling with {self.nickname} for {minutes} minutes.")
        self.affection_level = min(self.affection_level + minutes * 2, 100)
        self.energy = max(self.energy - minutes * 1.5, 0)

if __name__ == "__main__":
    myCat = Cat("Whiskers", "Apartment")
    myCat.meow()
    myCat.feed("salmon")
    myCat.cuddle(10)
    myCat.rest()
    print(f"{myCat.nickname}'s energy: {myCat.energy}, satiation: {myCat.satiation}, affection level: {myCat.affection_level}")

