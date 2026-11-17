class Course:
    def __init__(self, course_id, name, credit, department):
        self.course_id = course_id
        self.name = name
        self.credit = credit
        self.department = department
        department.course_list.append(self)
        self.status = "Pending"
        self.rejection_reason = None

        self.professor = None
        self.schedule = None
        self.enrollments = []

    def display_info(self):
        info = {
            "Course ID": self.course_id,
            "Name": self.name,
            "Credit": self.credit,
            "Professor": self.professor.name if self.professor else "Not Assigned",
            "Schedule": self.schedule,
            "Department": self.department.name,
            "Status": self.status,
        }

        for key, value in info.items():
            print(key, ":", value)

        if self.status == "Rejected":
            print("Rejection Reason:", self.rejection_reason)


    def view_enrolled_students(self):
        if not self.enrollments:
            print("No students have enrolled in this course.")
            return

        for enrollment in self.enrollments:
            print(enrollment.student.name)

    #No students have enrolled in this course.
