
# name = "Alice"
# age = 21
# def greet():
#     pass 
# 
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# 
#     def info(self):
#         print(f"Привет, меня зовут {self.name} мне {self.age} лет!")
# 
# person = Person("Bob", 20)
# person.info()
# 
# 
# class Employee(Person):
#     def __init__(self, name, age, position):
#         super().__init__(name, age)
#         self.position = position
# 
#     def info(self):
#         super().info()
#         print(f"Я работаю на позитций {self.position}")
# 
# e1 = Employee("Alice", 19, "Java Back-End")
# e1.info()
# 

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def drive(self):
        return f"Машина {self.brand}, {self.year} года!"

car = Car("BMW", 2025)
print(car.drive())