# multiple inheritance eg
print("\nMultiple Inheritance eg")

class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def to_emit_sound(self):
        pass


class Mammal(Animal):
    def to_breastfeed (self):
        return f"{self.name} is breastfeeding"
    
class Bird(Animal):
    def to_fly(self):
        return f"{self.name} is flying"

class Bat(Mammal, Bird):
    def to_emit_sound(self):
        return f"{self.name} is emiting ultrasonic sound"
    

bat = Bat(name="Batman")

print("Bat name: ", bat.name)
print(bat.to_emit_sound())
print(bat.to_breastfeed())
print(bat.to_fly())
