# Character: mother class
# Hero: controlled by user
# Enemy: user opponent

class Character:
    def __init__(self, name, health_point, level) -> None:
        self.__name = name
        self.__health_point = health_point
        self.__level = level

    def get_name(self):
        return self.__name

    def get_health_point(self):
        return self.__health_point
    
    def get_level(self):
        return self.__level

    def show_details(self):
        return f"Name: {self.get_name()}\nHealth Points: {self.get_health_point()}\nLevel: {self.get_level()}"

class Hero(Character):
    def __init__(self, name, health_point, level, special_skill):
        super().__init__(name, health_point,level)
        self.__special_skill = special_skill

    def get_special_skill(self):
        return self.__special_skill

    def show_details(self):
        return f"{super().show_details()}\nSpecial skill: {self.get_special_skill()}\n"

class Enemy(Character):
    def __init__(self, name, health_point, level, type):
        super().__init__(name, health_point,level)
        self.__type = type

    def get_type(self):
        return self.__type

    def show_details(self):
        return f"{super().show_details()}\nType: {self.get_type()}\n"

hero = Hero(name="Hero W", health_point=100, level=5, special_skill="Super Strength")
print(hero.show_details())

enemy = Enemy(name="Bat L", health_point=50, level=3, type="Flying")
print(enemy.show_details())
    
