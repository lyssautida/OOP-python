# @classmethod
# @staticmethod

class MyClass:
    value = 10 #class attr

    def __init__(self, name) -> None:
        self.name = name #instance attr

    def instance_method(self):
        return f"Instance method has been called {self.name}"
    
    @classmethod
    def class_method(cls):
        return f"Instance method has been called {cls.value}"

    @staticmethod
    def static_method():
        return "Static method has been called"
    

obj = MyClass(name = "Eg Class")
print(obj.instance_method())
print(MyClass.value)
print(MyClass.class_method())
print(MyClass.static_method())



class Car:
    def __init__(self, brand, model, year ) -> None:
        self.brand = brand 
        self.model = model 
        self.year = year 

    @classmethod
    def create_car(cls, config):
        brand, model, year = config.split(",")
        return cls(brand, model, int(year))
    
config1 = "Toyota, Corolla, 2022"
car1 = Car.create_car(config1)
print(f"Brand: {car1.brand} \nModel: {car1.model}\nAno: {car1.year}")


class Math:
    @staticmethod
    def sum(a,b):
        return a + b
    
print(Math.sum(a=10, b=15))