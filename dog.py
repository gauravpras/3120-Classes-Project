from animal import Animal

class Dog(Animal):
    def __init__(self, nickname, habitat, breed, gender):
        super().__init__(nickname, "Dog", habitat)
        self.breed = breed
        self.gender = gender

    def bark(self):
        print(f"{self.nickname} the {self.breed} says: Woof!")

    def fetch(self, item):
        print(f"{self.nickname} the {self.breed} is fetching a {item}.")
        self.energy = max(self.energy - 10, 0)
        self.satiation = max(self.satiation - 5, 0)

if __name__ == "__main__":
    myDog = Dog("Buddy", "Yard", "Golden Retriever", "Male")
    myDog.bark()
    myDog.feed("dog food")
    myDog.fetch("ball")
    myDog.rest()
    print(f"{myDog.nickname}'s energy: {myDog.energy}, satiation: {myDog.satiation}, breed: {myDog.breed}, gender: {myDog.gender}")
