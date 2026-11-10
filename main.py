import students
import professors
import departments
import courses

def main():
    # 1. Create Department
    computer_department = departments.Department("Computer Engineering")
    electronic_department = departments.Department("Electronic Engineering")

    # 2. Create Professors
    head_professor_computer = professors.Professor(
        "c101",
        "Hasan Ebrahimi",
        "hasan@gmail.com",
        computer_department,
        "Computer Engineering"
    )

    head_professor_electronic = professors.Professor(
        "e101",
        "Ali Rajabi",
        "ali@gmail.com",
        electronic_department,
        "Electronic Engineering"
    )

    professor_computer_1 = professors.Professor(
        "c102",
        "Sara Ahmadi",
        "sara@gmail.com",
        computer_department,
        "Data Science"
    )

    professor_electronic_1 = professors.Professor(
        "e102",
        "David Sohrabi",
        "david@gmail.com",
        electronic_department,
        "Data Communications"
    )

    computer_department.add_professor(head_professor_computer)
    computer_department.add_professor(professor_computer_1)
    electronic_department.add_professor(head_professor_electronic)
    electronic_department.add_professor(professor_electronic_1)

    computer_department.set_head_professor(head_professor_computer)
    electronic_department.set_head_professor(head_professor_electronic)

    # 3. Create Students
    student1 = students.Student(
        "c2001",
        "Kiana Chak",
        "kiana@gmail.com",
        computer_department,
        7,
        15.67
    )

    student2 = students.Student(
        "c2002",
        "Saina Kouchak",
        "saina@gmail.com",
        computer_department,
        4,
        12.02
    )

    student3 = students.Student(
        "e2001",
        "Hojat Kochak",
        "hoji@gmail.com",
        electronic_department,
        5,
        19.24
    )

    computer_department.add_student(student1)
    computer_department.add_student(student2)
    electronic_department.add_student(student3)

    # 4. Create Courses
    computer_course_1 = courses.Course(
        "c10001",
        "Database",
        3,
        computer_department
    )
    computer_course_2 = courses.Course(
        "c10002",
        "Software Engineering",
        3,
        computer_department
    )
    computer_course_3 = courses.Course(
        "c10003",
        "Computer Architecture",
        3,
        computer_department
    )
    electronic_course_1 = courses.Course(
        "e10001",
        "Networking",
        2,
        electronic_department
    )
    electronic_course_2 = courses.Course(
        "e10002",
        "Digital Electronics",
        3,
        electronic_department
    )

    professor_computer_1.take_course(computer_course_1)
    professor_computer_1.take_course(computer_course_2)
    head_professor_computer.take_course(computer_course_3)

    professor_electronic_1.take_course(electronic_course_1)
    head_professor_electronic.take_course(electronic_course_2)


    professor_computer_1.set_availability("Monday 07:00-13:00")
    professor_computer_1.assign_schedule(computer_course_1, "Monday 09:00-11:00")
    head_professor_computer.approve_course(computer_course_1)

    professor_computer_1.assign_schedule(computer_course_2, "Monday 07:00-09:00")
    head_professor_computer.approve_course(computer_course_2)

    head_professor_computer.set_availability("Tuesday 07:00-13:00")
    head_professor_computer.assign_schedule(computer_course_3, "Tuesday 09:00-11:00")
    head_professor_computer.approve_course(computer_course_3)

    professor_electronic_1.set_availability("Wednesday 07:00-15:00")
    professor_electronic_1.assign_schedule(electronic_course_1, "Wednesday 12:00-14:00")
    head_professor_electronic.approve_course(electronic_course_1)

    head_professor_electronic.set_availability("Friday 07:00-13:00")
    head_professor_electronic.assign_schedule(electronic_course_2, "Friday 08:00-11:00")
    head_professor_electronic.approve_course(electronic_course_2)

    computer_department.display_info()
    electronic_department.display_info()

    student1.enroll(computer_course_1, 7)
    student2.enroll(computer_course_2, 4)
    student3.enroll(electronic_course_1, 5)

if __name__ == "__main__":
    main()