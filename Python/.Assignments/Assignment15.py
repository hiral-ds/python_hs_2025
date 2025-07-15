class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = {}

    def enroll(self, course_name):
        self.courses[course_name] = None

    def update_grade(self, course_name, grade):
        if course_name in self.courses:
            self.courses[course_name] = grade
        else:
            print(f"{course_name} not found. Please enroll first.")

    def calculate_gpa(self):
        grades = [grade for grade in self.courses.values() if grade is not None]
        if grades:
            return sum(grades) / len(grades)
        return 0.0

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print("Courses and Grades:")
        for course, grade in self.courses.items():
            print(f"  {course}: {grade}")
        print(f"GPA: {self.calculate_gpa():.2f}")

# Demonstration
student1 = Student("Hiral", "S101")
student2 = Student("Riya", "S102")

student1.enroll("Math")
student1.enroll("Science")
student1.update_grade("Math", 85)
student1.update_grade("Science", 90)

student2.enroll("English")
student2.update_grade("English", 78)

student1.display_info()
print()
student2.display_info()