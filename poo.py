#class eg
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def greeting(self):
        return f"Hi, my name is {self.name} and I'm {self.age}."

# object

person1 = Person("Keeki", 17)
# print("Name: ", person1.name) 
# print("Age: ", person1.age)
message = person1.greeting()
print(message)

person2 = Person(name="Alice", age=25)
message = person2.greeting()
print(message)