# OOP in Python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 to 100

    def get_grade(self):
        return self.grade

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        # self.is_active = False

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


student1 = Student("Sam", 34, 79)
student2 = Student("Tim", 32, 45)
student3 = Student("Jill", 45, 43)

course = Course("Software Engineering", 2)
# add student
course.add_student(student1)
course.add_student(student2)
# course.add_student(student3)
print(course.students[0].name)  # Sam

print(course.get_average_grade())


