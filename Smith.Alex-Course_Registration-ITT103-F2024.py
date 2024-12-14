
class Course:# represents a course
    def __init__(self,course_id,course_name,fee):
        self.course_id=course_id
        self.course_name=course_name
        self.fee=fee

class Student:#Represents a student in the system.
    def __init__(self,student_id,student_name,student_email):
        self.student_id=student_id
        self.student_name=student_name
        self.student_email=student_email
        self.enrolled_courses=[]
        self.balance=0.0

    def enroll(self,course):#Adds a course to the student's list and updates the balance. Prevents duplicate enrollments.
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            self.balance+=course.fee
            print(f"Student has successfully enrolled in Course: {course.course_name}. Student has a balance of: $ {self.balance} ")
        else:
            print(f"Student already enrolled in course {course.course_name}.")

    def get_total_balance(self):#Calculates and returns the total fees for all enrolled courses.
        return self.balance

class Registration: #Manages courses, students, enrollments, and payments.
    def __init__(self):
        self.available_courses={}
        self.registered_students={}

    def add_course(self,course_id,course_name,fee):#Adds a new course to the system, ensuring unique course IDs.
        if course_id in self.available_courses:
            print(f"Course with ID: {course_id} already exists.")
        else:
            new_course= Course(course_id,course_name,fee)
            self.available_courses[course_id]=new_course
            print(f"Course: {course_name}  ID Num:{course_id} added successfully.")

    def registered_student(self,student_id,student_name,student_email):#Registers a new student, ensuring unique student IDs.
        if student_id in self.registered_students:
            print(f"Student with ID:{student_id} already registered.")
        else:
            new_student=Student(student_id,student_name,student_email)
            self.registered_students[student_id]=new_student
            print(f"Student: {student_name}  ID:{student_id} Email:{student_email} registered successfully.")

    def enroll_in_course(self,student_id,course_id):#Enrolls a student in a course, checking for validity and duplicates.
        if student_id not in self.registered_students:
            print("student not registered")
            return
        if course_id not in self.available_courses:
            print("Course not found in the registration system")

            return

        student= self.registered_students[student_id]
        course=self.available_courses[course_id]
        student.enroll(course)

    def calculate_payment(self,student_id):#Accepts a partial payment (minimum 40% of balance) and updates the remaining balance.
        if student_id not in self.registered_students:
            print("student not registered.")
            return
        student=self.registered_students[student_id]
        balance=student.get_total_balance()
        if balance==0:
            print("Student has no outstanding balance.")
            return

        min_payment=0.4*balance#calculate 40% payment
        try:
            payment=float(input("enter amount paid:"))
            if payment< min_payment:
                print(f"Payment must be 40% of the total balance of ${balance} which is ${min_payment}")
            else:
                student.balance-= payment
                print(f"Payment accepted. remaining balance is ${student.balance}")
        except ValueError:
            print("Invalid Input/Payment Amount")

    def check_student_balance(self,student_id):#Displays a student's current outstanding balance.
        if student_id not in self.registered_students:
            print("Student not Registered")
            return
        student= self.registered_students[student_id]
        print(f"Student {student.student_name} has a balance of ${student.balance}")

    def show_courses(self):# Lists all courses currently available in the system.
        if not self.available_courses:
            print("no course has been added")
            return
        for course in self.available_courses.values():
            print(f"Course_id: {course.course_id} Course Name: {course.course_name} Fee: {course.fee}")

    def show_registered_students(self):#Lists all registered students with details.
        if not self.registered_students:
            print("no student has been registered.")
            return
        print("Registered Students")
        for student in self.registered_students.values():
            print(f"ID: {student.student_id}, Name: {student.student_name}, Email: {student.student_email}")

    def show_students_in_course(self, course_id):# Lists all students enrolled in a specific course.
        if course_id not in self.available_courses:
            print("Course not found in the registration system.")
            return
        course = self.available_courses[course_id]
        enrolled_students = [student.student_name for student in self.registered_students.values() if course in student.enrolled_courses]
        if not enrolled_students:
            print(f"No students enrolled in {course.course_name}.")
        else:
            print(f"Students enrolled in {course.course_name}:")
            for student_name in enrolled_students:
                print(student_name)








def menu():
    system = Registration()
    print("____Welcome to UCC Student Registration System.____")

    while True:
        print(" Please select a option from the menu (1-9)")
        print("\n1. Add Course")
        print("2. Register Student")
        print("3. Enroll in Course")
        print("4. Calculate Payment")
        print("5. Check Student Balance")
        print("6. Show All Courses")
        print("7. Show Registered Students")
        print("8. Show Students in a Course")
        print("9. Exit")

        try:
            choice = int(input("\nSelect Menu Option: "))

            if choice == 1:#Prompts the administrator to enter a course's details and adds it to the system.
                course_id = input("\nEnter course ID: ")
                course_name = input("Enter course name: ")
                fee = float(input("Enter course fee: "))
                system.add_course(course_id, course_name, fee)

            elif choice == 2:#Prompts the administrator to add student details and registers the student in the system.
                student_id = input("\nEnter student ID: ")
                student_name = input("Enter student name: ")
                student_email = input("Enter student email: ")
                system.registered_student(student_id,student_name,student_email)

            elif choice == 3:#Enrolls a registered student in a specified course.
                student_id = input("\nEnter student ID: ")
                course_id = input("Enter course ID: ")
                system.enroll_in_course(student_id, course_id)

            elif choice == 4:# Accepts a payment from a student and updates their balance.
                student_id = input("\nEnter student ID: ")
                system.calculate_payment(student_id)

            elif choice == 5:#Displays the outstanding balance for a specific student.
                student_id = input("\nEnter student ID: ")
                system.check_student_balance(student_id)

            elif choice == 6:#Lists all courses currently available in the system.
                system.show_courses()

            elif choice == 7:#Displays all registered students with their details.
                system.show_registered_students()

            elif choice == 8:#Lists all students enrolled in a specified course.
                course_id = input("\nEnter course ID: ")
                system.show_students_in_course(course_id)

            elif choice == 9:#end/exit system
                print("Exiting Registration System, Goodbye.")
                break
            else:
                 print("Invalid choice. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a valid option.")


if __name__ == "__main__":
    menu()



