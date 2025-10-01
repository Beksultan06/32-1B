# import sqlite3

# conn = sqlite3.connect("database.db")
# cursor = conn.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY,
#         name TEXT, 
#         age INTEGER         
#     )
# """)

# cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 45))
# conn.commit()

# cursor.execute("SELECT * FROM users")
# print(cursor.fetchall())

# conn.close()


import sqlite3

class Student:
    school_name = 'IT'

    def __init__(self, name, age, grade):
        self.name = name
        self._age = age
        self.grade = grade

    @classmethod
    def school(cls):
        return cls.school_name

    @staticmethod
    def is_adult(age):
        return age >= 18

    def __str__(self):
        return f"{self.name} {self.age} {self.grade}"

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age

class CollegeStudent(Student):
    def __init__(self, name, age, grade, major):
        super().__init__(name, age, grade)
        self.major = major

    def __str__(self):
        return f"{self.name} {self._age} age {self.grade} class, fcultati {self.major}"

    
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER, 
        grade TEXT, 
        major TEXT    
    )
""")
conn.commit()

def add_student(student):
    cursor.execute(
        "INSERT INTO students (name, age, grade, major) VALUES (?, ?, ?, ?)",
        (student.name, student.get_age(), student.grade, getattr(student, "major", None))
    )
    conn.commit()

def get_student():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

def update_student_age(student_id, new_age):
    cursor.execute("UPDATE students SET age = ? WHERE id = ?", (new_age, student_id))
    conn.commit()

def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()

s1 = Student("ALice", 17, "11")
s2 = CollegeStudent("Bob", 19, "1", "Java Back-End")

add_student(s1)
add_student(s2)

students = get_student()
for st in students:
    print(st)

update_student_age(1, 18)
for st in get_student():
    print(st)

delete_student(2)
for st in get_student():
    print(st)

conn.close()