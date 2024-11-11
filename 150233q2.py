

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade

    def display_grades(self):
        print(f"Grades for {self.name}:")
        for assignment, grade in self.assignments.items():
            print(f"{assignment}: {grade}")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def assign_grade(self, student, assignment_name, grade):
        student.add_assignment(assignment_name, grade)

    def display_all_students(self):
        print(f"Students in {self.course_name} taught by {self.name}:")
        for student in self.students:
            print(f"{student.name} ({student.student_id}) - Grades:")
            student.display_grades()


# Interactive code for adding students and assigning grades
def interactive_course_management():
    instructor = Instructor("Dr. Smith", "Python Programming")

    while True:
        print("\nCourse Management System")
        print("1. Add student")
        print("2. Assign grade to student")
        print("3. Display all students and grades")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_name = input("Enter student's name: ")
            student_id = input("Enter student's ID: ")
            student = Student(student_name, student_id)
            instructor.add_student(student)
            print(f"Student {student_name} added.")

        elif choice == '2':
            student_name = input("Enter student's name: ")
            assignment_name = input("Enter assignment name: ")
            grade = float(input("Enter grade: "))
            student = next((s for s in instructor.students if s.name == student_name), None)
            if student:
                instructor.assign_grade(student, assignment_name, grade)
                print(f"Grade assigned to {student_name}.")
            else:
                print(f"Student {student_name} not found.")

        elif choice == '3':
            instructor.display_all_students()

        elif choice == '4':
            print("Exiting system.")
            break

        else:
            print("Invalid choice.")

()
