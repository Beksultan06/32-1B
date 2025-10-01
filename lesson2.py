


# class User:
#     def __init__(self, name):
#         self.name = name

# user = User("Bob")
# print(user.name)


# class User:
#     def __init__(self, name):
#         self._name = name

#     def get(self):
#         return self._name

# user = User("Bob")
# print(user.get())


# class User:
#     def __init__(self, name):
#         self.__name = name
# 
# user = User("Bob")
# # print(user.__name)
# # print(user._User__name)
# 
# 
# class Car:
#     def __init__(self, brand, engine_power, secret_code):
#         self.brand = brand
#         self._engine_power = engine_power
#         self.__secret_code = secret_code
# 
#     @property
#     def secret_code(self):
#         return self.__secret_code
# 
#     @secret_code.setter
#     def secret_code(self, code):
#         if len(code) < 4:
#             raise ValueError("Код должен быть минимум из 4 символов!")
#         self.__secret_code = code
# 
#     def info(self):
#         return f"Марка : {self.brand} Мощность {self._engine_power}"
# 
# car = Car("BWM", 250, "1234")
# 
# print(car.brand)
# print(car._engine_power)
# print(car.secret_code)
# 
# car.secret_code = "5678"
# print(car.secret_code)

#
#class Animal:
#    def speak(self):
#        print("Животное издает звук")
#
#class Dog(Animal):
#    def speak(self):
#        print("Гав-ГАв")
#
#class Cat(Animal):
#    def speak(self):
#        print("Мяу")    
#
#animals = [Dog(), Cat(), Animal()]
#
#for animal in animals:
#    animal.speak()
#


class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self._max_speed = max_speed
        self.__vin_code = '123456789'

    @property
    def vin_code(self):
        return self.__vin_code

    @vin_code.setter
    def vin_code(self, code):
        if len(code) < 8:
            raise ValueError("Vin код слишком короткий")
        self.__vin_code = code

    def info(self):
        return f"Brand {self.brand} Max Speed {self._max_speed}"

    def start_engine(self):
        print("Запуск матора")


class Car(Vehicle):
    def __init__(self, brand, max_speed, doors):
        super().__init__(brand, max_speed)
        self.doors = doors

    def start_engine(self):
        print(f"{self.brand} Started Engine")

    def info(self):
        return f"{super().info()}. Кол- во дверей {self.doors}"

class Motorcycle(Vehicle):
    def __init__(self, brand, max_speed, has_sidecar):
        super().__init__(brand, max_speed)
        self.has_sidecar = has_sidecar

    def start_engine(self):
        print(f"{self.brand} Started Engine")

    def info(self):
        sidecar = "есть" if self.has_sidecar  else None
        return f"{super().info()}. Сиденье с коляской {self.has_sidecar}"

viheciles = [
    Car("BWM", 250, 4),
    Motorcycle("HArley", 180, False),
    Vehicle('Beheric', 100)
]

for v in viheciles:
    print(v.info())
    v.start_engine()
    
car = Car("Audi", 380, 4)
print("VIN code updated", car.vin_code)
car.vin_code = 'AUDI1234'
print("VIN code updated", car.vin_code)
