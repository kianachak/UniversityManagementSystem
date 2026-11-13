import enrollments

class Student:
    def __init__(self, student_id, name, email, department, semester, grade):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.department = department
        self.semester = semester
        self.grade = grade
        self.enrollments = []

    def display_info(self):
        info = {"Student ID" : self.student_id,
            "Name": self.name,
            "Email": self.email,
            "Department" : self.department.name, 
            "Semester" : self.semester,
            "GPA" : self.grade,
            }

        for key, value in info.items():
            print(key, ":", value)

    def enroll(self, course, semester):

        if course.status != "Approved":
            print("This course is not available for enrollment.")
            return
        
        for enrollment in self.enrollments:
            if (
                enrollment.course == course
                and enrollment.status == "Completed"
            ):
                print("You have already completed this course.")
                return

        for enrollment in self.enrollments:
            if (
                enrollment.course == course
                and enrollment.semester == semester
                and enrollment.status == "Enrolled"
            ):
                print("You are already enrolled in this course.")
                return

        enrollment = enrollments.Enrollment(
            self,
            course,
            semester
        )

        self.enrollments.append(enrollment)
        course.enrollments.append(enrollment)

        print("Enrollment successful.")

    
    def view_enrollments(self):
        if not self.enrollments:
            print("No enrollments found.")
            return

        for enrollment in self.enrollments:
            enrollment.display_info()

    def view_schedule(self):
        has_active_enrollment = False

        for enrollment in self.enrollments:
            if enrollment.status == "Enrolled":
                has_active_enrollment = True
                print(f'{enrollment.course.name}: {enrollment.course.schedule}')

        if not has_active_enrollment:
            print("No active enrollments found.")

    def view_available_courses(self):
        self.department.view_available_courses()
