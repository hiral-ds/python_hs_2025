class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = {}  # course_name: {'grade': grade, 'credits': credits}

    def enroll(self, course_name):
        self.courses[course_name] = {'grade': None, 'credits': 0}

    def update_grade(self, course_name, grade):
        if course_name in self.courses:
            self.courses[course_name]['grade'] = grade

    def add_credits(self, course_name, credits):
        if course_name in self.courses:
            self.courses[course_name]['credits'] = credits

    def calculate_gpa(self):
        grades = [data['grade'] for data in self.courses.values() if data['grade'] is not None]
        return sum(grades) / len(grades) if grades else 0.0

    def calculate_weighted_gpa(self):
        total_points = 0
        total_credits = 0
        for course, data in self.courses.items():
            if data['grade'] is not None and data['credits'] > 0:
                total_points += data['grade'] * data['credits']
                total_credits += data['credits']
        return total_points / total_credits if total_credits else 0.0

    def get_highest_grade(self):
        valid_courses = {k: v['grade'] for k, v in self.courses.items() if v['grade'] is not None}
        if not valid_courses:
            return None, None
        highest_course = max(valid_courses, key=valid_courses.get)
        return highest_course, valid_courses[highest_course]

    def __str__(self):
        return f"Student(Name: {self.name}, ID: {self.student_id}, GPA: {self.calculate_gpa():.2f})"

# Demo
student = Student("Hiral", "S101")
student.enroll("Math")
student.enroll("Science")
student.update_grade("Math", 90)
student.update_grade("Science", 80)
student.add_credits("Math", 3)
student.add_credits("Science", 4)

print(student)
print("Weighted GPA:", student.calculate_weighted_gpa())
print("Highest Grade:", student.get_highest_grade())