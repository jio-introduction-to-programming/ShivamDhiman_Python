class Vehicle:
    def __init__(self, name, speed, mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage    

    def change_speed(self, new_speed):
        self.speed = new_speed

    def get_speed(self):
        return self.speed


class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def change_age(self, new_age):
        if new_age < 0:
            raise ValueError("Age cannot be negative.")
        self.age = new_age

    def get_age(self):
        return self.age


class Plant:
    def __init__(self, name, height, species):
        self.name = name
        self.height = height
        self.species = species

    def change_height(self, new_height):
        if new_height < 0:
            raise ValueError("Height cannot be negative.")
        self.height = new_height

    def get_height(self):
        return self.height


class Tree(Plant):
    def __init__(self, name, height, species, age):
        super().__init__(name, height, species)
        self.age = age

    def change_age(self, new_age):
        if new_age < 0:
            raise ValueError("Age cannot be negative.")
        self.age = new_age

    def get_age(self):
        return self.age
