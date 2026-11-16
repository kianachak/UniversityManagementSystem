class Enrollment:
    def __init__(self, student, course, semester):
        self.student = student
        self.course = course
        self.semester = semester
        self.grade = None
        self.status = "Enrolled"

    def display_info(self):
        info = {"Student" : self.student.name,
            "Course": self.course.name,
            "Semester": self.semester,
            "Grade" : self.grade,
            "Status" : self.status,
            }

        for key, value in info.items():
            print(key, ":", value)

    def change_status(self, status):
        valid_statuses = ["Enrolled", "Completed", "Dropped", "Failed"]
        if status in valid_statuses:
            self.status = status
        else:
            print("Your status is wrong")

    def set_grade(self, grade):
        if not 0 <= grade <= 20:
            print("Your grade is incorrect.")
            return

        if grade < 10:
            self.change_status("Failed")
        else:
            self.change_status("Completed")

        self.grade = grade
