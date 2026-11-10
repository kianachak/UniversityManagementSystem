import enrollments
import students
import professors
import departments
import courses

# ==================================================
# 1. Setup: Department and Head Professor and Professor
# ==================================================
mechanical_department = departments.Department("Mechanical Engineering")

head_professor_mechanical = professors.Professor(
    "m101",
    "Naghi Mamuli",
    "naghi@gmail.com",
    mechanical_department,
    "Mechanical Design"
)

mechanical_department.add_professor(head_professor_mechanical)
mechanical_department.set_head_professor(head_professor_mechanical)

professor_mechanical_1 = professors.Professor(
    "m102",
    "Ali Zand",
    "aliz@gmail.com",
    mechanical_department,
    "Thermodynamics"
)

mechanical_department.add_professor(professor_mechanical_1)

# ==================================================
# 2. Setup: Students
# ==================================================
student4 = students.Student(
    "m2001",
    "Sayeh Moradi",
    "sayeh@gmail.com",
    mechanical_department,
    1,
    16.53
)

student5 = students.Student(
    "m2003",
    "Tara Rezaii",
    "tara@gmail.com",
    mechanical_department,
    3,
    14.97
)

mechanical_department.add_student(student4)
mechanical_department.add_student(student5)

# ==================================================
# 3. Setup: Courses
# ==================================================
mechanical_course_1 = courses.Course(
    "m10001",
    "Engineering Mechanics",
    3,
    mechanical_department
)

mechanical_course_2 = courses.Course(
    "m10002",
    "Thermodynamics",
    3,
    mechanical_department
)

mechanical_course_3 = courses.Course(
    "m10003",
    "Machine Design",
    2,
    mechanical_department
)

# ==================================================
# TEST 1: Approve Course Without a Professor
# ==================================================

print("\n" + "=" * 50)
print("TEST 1: Approve Course Without a Professor")
print("=" * 50)

print("Before approval:")
print("Status:", mechanical_course_1.status)
print("Professor:", mechanical_course_1.professor)

head_professor_mechanical.approve_course(mechanical_course_1)

print("\nAfter approval attempt:")
print("Status:", mechanical_course_1.status)
print("Professor:", mechanical_course_1.professor)

assert mechanical_course_1.status == "Pending"
assert mechanical_course_1.professor is None

# ==================================================
# TEST 2: Approve Course With Professor and Schedule
# ==================================================

print("\n" + "=" * 50)
print("TEST 2: Approve Course With Professor and Schedule")
print("=" * 50)

professor_mechanical_1.take_course(mechanical_course_1)

professor_mechanical_1.set_availability("Monday 09:00-12:00")
professor_mechanical_1.assign_schedule(
    mechanical_course_1,
    "Monday 09:00-11:00"
)

head_professor_mechanical.approve_course(mechanical_course_1)

print("Course status:", mechanical_course_1.status)
print("Course professor:", mechanical_course_1.professor.name)
print("Course schedule:", mechanical_course_1.schedule)

assert mechanical_course_1.status == "Approved"
assert mechanical_course_1.professor is professor_mechanical_1
assert mechanical_course_1.schedule == "Monday 09:00-11:00"

# ==================================================
# TEST 3: Reject a Course
# ==================================================

print("\n" + "=" * 50)
print("TEST 3: Reject a Course")
print("=" * 50)

professor_mechanical_1.take_course(mechanical_course_2)

reason = "Course schedule needs revision."

head_professor_mechanical.reject_course(
    mechanical_course_2,
    reason
)

print("Course status:", mechanical_course_2.status)
print("Rejection reason:", mechanical_course_2.rejection_reason)

assert mechanical_course_2.status == "Rejected"
assert mechanical_course_2.rejection_reason == reason

# ==================================================
# TEST 4: Unauthorized Course Rejection
# ==================================================

print("\n" + "=" * 50)
print("TEST 4: Unauthorized Course Rejection")
print("=" * 50)

regular_reason = "Testing unauthorized rejection."

professor_mechanical_1.reject_course(
    mechanical_course_3,
    regular_reason
)

assert mechanical_course_3.status == "Pending"
assert mechanical_course_3.rejection_reason is None

# ==================================================
# TEST 5: Student Enrollment
# ==================================================

print("\n" + "=" * 50)
print("TEST 5: Student Enrollment")
print("=" * 50)

student4.enroll(mechanical_course_1, 1)

print("Student enrollments:", len(student4.enrollments))
print("Course enrollments:", len(mechanical_course_1.enrollments))

assert len(student4.enrollments) == 1
assert len(mechanical_course_1.enrollments) == 1

# ==================================================
# TEST 6: Duplicate Enrollment
# ==================================================

print("\n" + "=" * 50)
print("TEST 6: Duplicate Enrollment")
print("=" * 50)

student_before = len(student4.enrollments)
course_before = len(mechanical_course_1.enrollments)

student4.enroll(mechanical_course_1, 1)

student_after = len(student4.enrollments)
course_after = len(mechanical_course_1.enrollments)

print("Student enrollments before:", student_before)
print("Student enrollments after:", student_after)
print("Course enrollments before:", course_before)
print("Course enrollments after:", course_after)

assert student_before == student_after
assert course_before == course_after

# ==================================================
# TEST 7: Re-enrollment After Dropping
# ==================================================

print("\n" + "=" * 50)
print("TEST 7: Re-enrollment After Dropping")
print("=" * 50)

student4.enrollments[0].change_status("Dropped")

before = len(student4.enrollments)
student4.enroll(mechanical_course_1, 1)
after = len(student4.enrollments)

print("Enrollments before:", before)
print("Enrollments after:", after)

assert after == before + 1
assert student4.enrollments[0].status == "Dropped"
assert student4.enrollments[1].status == "Enrolled"

# ==================================================
# TEST 8: Enrollment in a Different Semester
# ==================================================

print("\n" + "=" * 50)
print("TEST 8: Enrollment in a Different Semester")
print("=" * 50)

before = len(student4.enrollments)

student4.enroll(mechanical_course_1, 2)

after = len(student4.enrollments)

print("Enrollments before:", before)
print("Enrollments after:", after)

assert after == before + 1
assert student4.enrollments[2].semester == 2
assert student4.enrollments[2].status == "Enrolled"

# ==================================================
# TEST 9: Prevent Re-enrollment After Completion
# ==================================================

print("\n" + "=" * 50)
print("TEST 9: Prevent Re-enrollment After Completion")
print("=" * 50)

student4.enrollments[2].change_status("Completed")

before = len(student4.enrollments)

student4.enroll(mechanical_course_1, 3)

after = len(student4.enrollments)

print("Enrollments before:", before)
print("Enrollments after:", after)

assert after == before
assert student4.enrollments[2].status == "Completed"

# ==================================================
# TEST 10: Enrollment Status and Grade
# ==================================================

print("\n" + "=" * 50)
print("TEST 10: Enrollment Status and Grade")
print("=" * 50)

grade_test = enrollments.Enrollment(
    student5,
    mechanical_course_1,
    1
)

assert grade_test.status == "Enrolled"
print("Initial status:", grade_test.status)

grade_test.set_grade(7)

assert grade_test.grade == 7
assert grade_test.status == "Failed"
print("After grade 7:", grade_test.grade, grade_test.status)

grade_test.set_grade(18)

assert grade_test.grade == 18
assert grade_test.status == "Completed"
print("After grade 18:", grade_test.grade, grade_test.status)

# ==================================================
# TEST 11: Invalid Grade
# ==================================================

print("\n" + "=" * 50)
print("TEST 11: Invalid Grade")
print("=" * 50)

previous_grade = grade_test.grade
previous_status = grade_test.status

grade_test.set_grade(25)

print("Grade:", grade_test.grade)
print("Status:", grade_test.status)

assert grade_test.grade == previous_grade
assert grade_test.status == previous_status

# ==================================================
# TEST 12: Student Views Schedule
# ==================================================

print("\n" + "=" * 50)
print("TEST 12: Student Views Schedule")
print("=" * 50)

student4.view_schedule()