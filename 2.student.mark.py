# ---------------------------------------------------------
# 2.student.mark.oop.py
# Student Mark Management System (OOP version)
# ---------------------------------------------------------

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
        return f"ID: {self._id} | Name: {self._name} | DoB: {self._dob}"


class Student(Person):
    # inherits Person
    pass


class Course:
    def __init__(self, cid, name):
        self._cid = cid
        self._name = name

    def get_id(self):
        return self._cid

    def get_name(self):
        return self._name

    def info(self):
        return f"ID: {self._cid} | Name: {self._name}"


class Mark:
    def __init__(self, student, course, value):
        self._student = student
        self._course = course
        self._value = value

    def get_course_id(self):
        return self._course.get_id()

    def show(self):
        return f"{self._student.get_id()} - {self._student.get_name()}: {self._value}"


# ---------------------------------------------------------
# Manager class to handle all operations
# ---------------------------------------------------------

class StudentMarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    # ------------ Input methods (polymorphic: all use .input()) ------------

    def input_students(self):
        n = int(input("Enter number of students: "))
        for _ in range(n):
            sid = input("Student ID: ")
            name = input("Name: ")
            dob = input("Date of Birth: ")
            self.students.append(Student(sid, name, dob))

    def input_courses(self):
        n = int(input("Enter number of courses: "))
        for _ in range(n):
            cid = input("Course ID: ")
            name = input("Course name: ")
            self.courses.append(Course(cid, name))

    def input_marks(self):
        print("\nCourses:")
        for c in self.courses:
            print(c.info())

        cid = input("\nEnter course ID to input marks: ")

        # find course object
        course = None
        for c in self.courses:
            if c.get_id() == cid:
                course = c
                break

        if course is None:
            print("Course not found!\n")
            return

        print("\nEnter marks:")
        for s in self.students:
            print(f"{s.get_id()} - {s.get_name()}")
            value = float(input("  Mark: "))
            self.marks.append(Mark(s, course, value))

    # ------------ Listing methods (also polymorphic: all use .list()) ------------

    def list_students(self):
        print("\n--- Student List ---")
        for s in self.students:
            print(s.info())

    def list_courses(self):
        print("\n--- Course List ---")
        for c in self.courses:
            print(c.info())

    def list_marks_for_course(self):
        cid = input("Enter course ID: ")

        print(f"\n--- Marks for Course {cid} ---")
        for m in self.marks:
            if m.get_course_id() == cid:
                print(m.show())


# ---------------------------------------------------------
# Program Execution (same steps, no while-true)
# ---------------------------------------------------------

def main():
    manager = StudentMarkManager()

    manager.input_students()
    manager.input_courses()
    manager.input_marks()

    manager.list_students()
    manager.list_courses()
    manager.list_marks_for_course()


if __name__ == "__main__":
    main()
