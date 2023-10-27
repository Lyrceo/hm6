class University:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def enroll_student(self, student):
        self.students.append(student)
        print(f"{student.name} прийнятий до {self.name}")

    def hire_teacher(self, teacher):
        self.teachers.append(teacher)
        print(f"{teacher.name} призначений вчителем у {self.name}")

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)
        print(f"{self.name} зареєструвався на курс {course.title}")

class Teacher:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
        self.courses_taught = []

    def assign_course(self, course):
        self.courses_taught.append(course)
        print(f"{self.name} веде курс {course.title}")

class Course:
    def __init__(self, title, code):
        self.title = title
        self.code = code

university = University("Університет XYZ")
student1 = Student("Іван", "S12345")
student2 = Student("Марія", "S67890")
teacher1 = Teacher("Професор Сміт", "T98765")
teacher2 = Teacher("Доцент Джонсон", "T54321")
course1 = Course("Математика", "MATH101")
course2 = Course("Історія", "HIST202")

university.enroll_student(student1)
university.enroll_student(student2)
university.hire_teacher(teacher1)
university.hire_teacher(teacher2)

student1.enroll_course(course1)
student2.enroll_course(course2)
teacher1.assign_course(course1)
teacher2.assign_course(course2)
