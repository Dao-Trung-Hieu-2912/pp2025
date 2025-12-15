import math
import numpy as np
import curses

# =======================
#        DOMAINS
# =======================

class Person:
    def __init__(self, sid, name, dob):
        self._id = sid
        self._name = name
        self._dob = dob

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name


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


class Mark:
    def __init__(self, student, course, value):
        self.student = student
        self.course = course
        self.value = value


# =======================
#       MANAGER
# =======================

class StudentMarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def calculate_gpa(self, student):
        values = []
        credits = []

        for m in self.marks:
            if m.student == student:
                values.append(m.value)
                credits.append(m.course.get_credit())

        if not values:
            return 0.0

        values = np.array(values)
        credits = np.array(credits)

        return round(np.sum(values * credits) / np.sum(credits), 2)

    def sort_students_by_gpa(self):
        for s in self.students:
            s.gpa = self.calculate_gpa(s)
        self.students.sort(key=lambda x: x.gpa, reverse=True)


# =======================
#        INPUT
# =======================

def input_students(manager):
    n = int(input("Number of students: "))
    for _ in range(n):
        sid = input("ID: ")
        name = input("Name: ")
        dob = input("DOB: ")
        manager.students.append(Student(sid, name, dob))


def input_courses(manager):
    n = int(input("Number of courses: "))
    for _ in range(n):
        cid = input("Course ID: ")
        name = input("Course name: ")
        credit = int(input("Credit: "))
        manager.courses.append(Course(cid, name, credit))


def input_marks(manager):
    cid = input("Course ID: ")
    course = next((c for c in manager.courses if c.get_id() == cid), None)

    if not course:
        print("Course not found!")
        return

    for s in manager.students:
        raw = float(input(f"Mark for {s.get_name()}: "))
        value = math.floor(raw * 10) / 10   # round down 1 digit
        manager.marks.append(Mark(s, course, value))


# =======================
#        OUTPUT (CURSES)
# =======================

def run_ui(stdscr, manager):
    curses.curs_set(0)

    while True:
        stdscr.clear()
        stdscr.addstr(1, 2, "STUDENT MARK MANAGEMENT", curses.A_BOLD)
        stdscr.addstr(3, 4, "1. Input students")
        stdscr.addstr(4, 4, "2. Input courses")
        stdscr.addstr(5, 4, "3. Input marks")
        stdscr.addstr(6, 4, "4. Show GPA (sorted)")
        stdscr.addstr(7, 4, "0. Exit")
        stdscr.refresh()

        key = stdscr.getch()

        if key == ord('1'):
            curses.endwin()
            input_students(manager)
            stdscr = curses.initscr()

        elif key == ord('2'):
            curses.endwin()
            input_courses(manager)
            stdscr = curses.initscr()

        elif key == ord('3'):
            curses.endwin()
            input_marks(manager)
            stdscr = curses.initscr()

        elif key == ord('4'):
            manager.sort_students_by_gpa()
            stdscr.clear()
            stdscr.addstr(1, 2, "GPA RESULT", curses.A_BOLD)
            row = 3
            for s in manager.students:
                stdscr.addstr(row, 4, f"{s.get_name()} | GPA: {s.gpa}")
                row += 1
            stdscr.getch()

        elif key == ord('0'):
            break


# =======================
#          MAIN
# =======================

def main():
    manager = StudentMarkManager()
    curses.wrapper(run_ui, manager)


if __name__ == "__main__":
    main()
