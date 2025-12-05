students = []     
courses = []     
marks = []        


# ---------------- INPUT FUNCTIONS ----------------

def input_number_of_students():
    return int(input("Enter number of students: "))


def input_student_information():
    sid = input("Student ID: ")
    name = input("Name: ")
    dob = input("Date of Birth: ")
    students.append({"id": sid, "name": name, "dob": dob})


def input_number_of_courses():
    return int(input("Enter number of courses: "))


def input_course_information():
    cid = input("Course ID: ")
    cname = input("Course Name: ")
    courses.append({"id": cid, "name": cname})


def input_marks_for_course():
    print("\nCourses:")
    for c in courses:
        print(f"{c['id']} - {c['name']}")

    cid = input("\nEnter ID of course to input marks: ")

    exists = any(c["id"] == cid for c in courses)
    if not exists:
        print("Course not found!\n")
        return

    print("\nEnter marks for each student:")
    for s in students:
        print(f"{s['id']} - {s['name']}")
        m = float(input("  Mark: "))
        marks.append({"student_id": s["id"], "course_id": cid, "mark": m})


# ---------------- LISTING FUNCTIONS ----------------

def list_students():
    print("\n--- Student List ---")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")
    print()


def list_courses():
    print("\n--- Course List ---")
    for c in courses:
        print(f"ID: {c['id']} | Name: {c['name']}")
    print()


def show_student_marks():
    cid = input("Enter course ID to show marks: ")

    print(f"\n--- Marks for Course {cid} ---")
    for m in marks:
        if m["course_id"] == cid:
            name = ""
            for s in students:
                if s["id"] == m["student_id"]:
                    name = s["name"]
                    break
            print(f"{m['student_id']} - {name}: {m['mark']}")
    print()


# ---------------- PROGRAM EXECUTION ----------------

# 1. Input students
n_students = input_number_of_students()
for _ in range(n_students):
    input_student_information()

# 2. Input courses
n_courses = input_number_of_courses()
for _ in range(n_courses):
    input_course_information()

# 3. Input marks for one selected course
input_marks_for_course()

# 4. Listing output
list_students()
list_courses()
show_student_marks()
