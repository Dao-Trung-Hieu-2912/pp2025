import math


# =======================
#        MODELS
# =======================

class Person:
    def __init__(self, sid, name, dob):
        self._id = sid
        self._name = name
        self._dob = dob

    def get_id(self):
        return self._id
import math
import numpy as np
import curses

class Person:
    def __init__(self, sid, name, dob):
        self._id = sid
        self._name = name
        self._dob = dob

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def info(self):
        return f"{self._id} | {self._name} | {self._dob}"


class Student(Person):
    def __init__(self, sid, name, dob):
        super().__init__(sid, name, dob)
        self.gpa = 0.0


class Course:
    def __init__(self, cid, name, credit):
        self._cid = cid
        self._name = name
        self._credit = credit

    def get_id(self):
        return self._cid

    def get_credit(self):
        return self._credit

    def info(self):
        return f"{self._cid} | {self._name} | Credit: {self._credit}"


class Mark:
    def __init__(self, student, course, value):
        self.student = student
        self.course = course
        self.value = value


class StudentMarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_students(self):
        n = int(input("Number of students: "))
        for _ in range(n):
            sid = input("ID: ")
            name = input("Name: ")
            dob = input("DOB: ")
            self.students.append(Student(sid, name, dob))

    def input_courses(self):
        n = int(input("Number of courses: "))
        for _ in range(n):
            cid = input("Course ID: ")
            name = input("Course name: ")
            credit = int(input("Credit: "))
            self.courses.append(Course(cid, name, credit))

    def input_marks(self):
        cid = input("Enter course ID: ")
        course = next((c for c in self.courses if c.get_id() == cid), None)

        if not course:
            print("Course not found!")
            return

        for s in self.students:
            raw = float(input(f"Mark for {s.get_name()}: "))
            value = math.floor(raw * 10) / 10
            self.marks.append(Mark(s, course, value))

    def calculate_gpa(self, student):
        values = []
        credits = []

        for m in self.marks:
            if m.student == student:
                values.append(m.value)
                credits.append(m.course.get_credit())

        if not values:
            return 0.0

        total_weighted = sum(v * c for v, c in zip(values, credits))
        total_credits = sum(credits)
        gpa = total_weighted / total_credits
        return round(gpa, 2)

    def update_all_gpa(self):
        for s in self.students:
            s.gpa = self.calculate_gpa(s)

    def sort_students_by_gpa(self):
        self.update_all_gpa()
        self.students.sort(key=lambda s: s.gpa, reverse=True)


def console_ui(manager):
    while True:
        print("\nSTUDENT MARK MANAGEMENT")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. Show GPA (sorted)")
        print("5. List students")
        print("6. List courses")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            manager.input_students()
        elif choice == '2':
            manager.input_courses()
        elif choice == '3':
            manager.input_marks()
        elif choice == '4':
            manager.sort_students_by_gpa()
            print("\nSTUDENTS SORTED BY GPA")
            for s in manager.students:
                print(f"{s.get_name()} | GPA: {s.gpa}")
            input("\nPress Enter to continue...")
        elif choice == '5':
            print("\n--- Students ---")
            for s in manager.students:
                print(s.info())
            input("\nPress Enter to continue...")
        elif choice == '6':
            print("\n--- Courses ---")
            for c in manager.courses:
                print(c.info())
            input("\nPress Enter to continue...")
        elif choice == '0':
            break
        else:
            print("Invalid choice. Try again.")


def main():
    manager = StudentMarkManager()
    console_ui(manager)


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
