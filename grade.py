# grade.py

class Grade:
    def __init__(self, student, course, grade):
        self.student = student
        self.course = course
        self.grade = grade

    def display_info(self):
        print(f"Student ID: {self.student.student_id}")
        print(f"Course ID: {self.course.course_id}")
        print(f"Grade: {self.grade}")
