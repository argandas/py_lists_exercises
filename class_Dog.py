class Dog:
    species = "Dog"
    __my_private_var = 100

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__my_private_var = age * 10

    def get_private_value(self):
        return self.__my_private_var


class BullDog(Dog):
    species = "BullDog"

    def __init__(self, name, age):
        super().__init__(name, age + 5)


class Poodle(Dog):
    species = "Poodle"

    def __init__(self, name, age):
        Dog.__init__(self, name, age + 5)


dog1 = BullDog("Fido", 3)
dog2 = Poodle("Fido", 5)
print(f"This is {dog1.name}, he is {dog1.age} yo, species = {dog1.species}")
print(f"This is {dog2.name}, he is {dog2.age} yo, species = {dog2.species}")
