# student_management_system.py

from student import Student
from course import Course
from grade import Grade

# Create students
student1 = Student(1, "Alice", "alice@example.com")
student2 = Student(2, "Bob", "bob@example.com")

# Create courses
course1 = Course(101, "Python Programming")
course2 = Course(102, "Data Structures")

# Create grades
grade1 = Grade(student1, course1, "A")
grade2 = Grade(student2, course1, "B")
grade3 = Grade(student1, course2, "C")

# Display information
print("Student Information:")
student1.display_info()
print()
student2.display_info()

print("\nCourse Information:")
course1.display_info()
print()
course2.display_info()

print("\nGrade Information:")
grade1.display_info()
print()
grade2.display_info()
print()
grade3.display_info()
