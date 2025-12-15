

class Person:
    def __init__(self, sid, name, dob):
        self.__id = sid
        self.__name = name
        self.__dob = dob

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def info(self):
        return f"ID: {self.__id} | Name: {self.__name} | DoB: {self.__dob}"


class Student(Person):
    def __init__(self, sid, name, dob):
        super().__init__(sid, name, dob)


class Course:
    def __init__(self, cid, name):
        self.__cid = cid
        self.__name = name

    def get_id(self):
        return self.__cid

    def get_name(self):
        return self.__name

    def info(self):
        return f"ID: {self.__cid} | Name: {self.__name}"


class Mark:
    def __init__(self, student, course, value):
        self.__student = student
        self.__course = course
        self.__value = value

    def get_course_id(self):
        return self.__course.get_id()

    def show(self):
        return f"{self.__student.get_id()} - {self.__student.get_name()}: {self.__value}"




class StudentMarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    

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
