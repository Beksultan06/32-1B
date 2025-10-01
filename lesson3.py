

# class Point:
#     def __init__(self, x, y):
#         self.x = x 
#         self.y = y

#     def __str__(self):
#         return f"Point({self.x} {self.y})"

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y +other.y)

# p1 = Point(2, 3)
# p2 = Point(5, 7)
# print(p1)
# p3 = p1 + p2 
# print(p3)


# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b

# print(Math.add(5, 10))


# class Person:
#     species =  "Homo speiens"
# 
#     def __init__(self, name):
#         self.name = name
# 
#     @classmethod
#     def create_anonymous(cls):
#         return cls("Anonymous")
# 
# print(Person.species)
# 
# p = Person.create_anonymous()
# print(p.name)


# class A:
#     def method_a(self):
#         print("Method A")
# 
# class B:
#     def method_b(self):
#         print("Method B")
# 
# class C(A, B):
#     def mehtod_c(self):
#         print("Method C")
# 
# c = C()
# c.method_a()
# c.method_b()
# c.mehtod_c()
# 
# print(C.__mro__)

# class A:
#     def greet(self):
#         print("A")

# class B(A):
#     def greet(self):
#         print("B")
#         super().greet()

# class C(A):
#     def greet(self):
#         print("C")
#         super().greet()

# class D(B,C):
#     def greet(self):
#         print("D")
#         # super().greet()
        
# d = D()
# d.greet()

# print(D.__mro__)

class Employee:
    def __init__(self, name, salary):
        self._name = name
        self.salary = salary

    def work(self):
        print(f"{self._name} выполняет свои обязанности")

    def __str__(self):
        return f"Сотрудник: {self._name}, salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def work(self):
        print(f"{self._name} управляет командой из {self.team_size} человек")


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def work(self):
        print(f"{self._name} пишет код на {self.language}")


class TechManage(Manager, Developer):
    def __init__(self, name, salary, team_size, language):
        Manager.__init__(self, name, salary, team_size)
        Developer.__init__(self, name, salary, language)

    def work(self):
        print(f"{self._name} управляет командой и пишет код")
        Manager.work(self)
        Developer.work(self)


class Utils:
    @staticmethod
    def bonus(salary, percent):
        return salary * percent / 100

    @classmethod
    def description(cls):
        print(f"{cls.__name__} — класс для расчета бонусов сотрудников")


mrg = Manager("Alice", 5000, 5)
dev = Developer("Bob", 5000, "Java")
# tech_mgr = TechManage("Mark", 6000, 6, "Python")

mrg.work()
dev.work()
# tech_mgr.work()

employees = [mrg, dev]
for e in employees:
    e.work()

print(mrg)
print(dev)
# print(tech_mgr)