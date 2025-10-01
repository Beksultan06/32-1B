class Database:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []


    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher): 
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def enrool(self, course):
        self.courses.append(course)
        course.add_studnet(self)

    def __str__(self):
        return f"Student : {self.name} ({self.student_id} Age : {self.age})"

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject 


    def __str__(self):
        return f"Teacher : {self.name} Subject : {self.subject}"


class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.students = []

    def add_studnet(self, student):
        self.students.append(student)


    def __str__(self):
        return f"COurse {self.title} Teacher : {self.teacher.name}, Кол-ВО : {len(self.students)}"


db = Database()

t1 = Teacher("Bob", 35, "Python")
t2 = Teacher("Alice", 30, "Kotlin")

db.add_teacher(t1)
db.add_teacher(t2)

student1 = Student("Касым", 14, "1")
student2 = Student("Адалат", 23, "2")
student3 = Student("Ислам", 21, "3")

db.add_student(student1)
db.add_student(student2)
db.add_student(student3)

kotlin = Course("Kotlin", t2)
python_course = Course("Python", t1)

db.add_course(kotlin)
db.add_course(python_course)

student1.enrool(kotlin)
student2.enrool(kotlin)
student3.enrool(python_course)

for course in db.courses:
    print(course)

for student in db.students:
    print(student)

for teacher in db.teachers:
    print(teacher)  