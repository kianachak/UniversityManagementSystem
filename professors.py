class Professor:
    def __init__(self, professor_id, name, email, department, specialization):
        self.professor_id = professor_id
        self.name = name
        self.email = email
        self.department = department
        self.specialization = specialization
        self.availability = []
        self.courses = []

    def display_info(self):
        info = {"Professor ID" : self.professor_id,
            "Name": self.name,
            "Email": self.email,
            "Department" : self.department.name, 
            "Specialization" : self.specialization,
            }

        for key, value in info.items():
            print(key, ":", value)

    def view_courses(self):
        courses = self.department.course_list
        for course in courses:
            print(course.name)

    def take_course(self, course):
        if course.department != self.department:
            print("This course does not belong to this professor's department.")
            return

        if course not in self.courses:
            self.courses.append(course)

        course.professor = self

    def set_availability(self, time):
        self.availability.append(time)

    def is_schedule_available(self, schedule):
        schedule_day, schedule_time = schedule.split(" ")
        schedule_start, schedule_end = schedule_time.split("-")

        for availability in self.availability:
            availability_day, availability_time = availability.split(" ")
            availability_start, availability_end = availability_time.split("-")

            if schedule_day != availability_day:
                continue

            if (
                availability_start <= schedule_start
                and schedule_end <= availability_end
            ):
                return True

        return False

    def assign_schedule(self, course, schedule):
        if course not in self.courses:
            print("Professor is not assigned to this course.")
            return

        if not self.is_schedule_available(schedule):
            print("This schedule is not available for this professor.")
            return

        course.schedule = schedule
        print("Schedule assigned successfully.")

    def enter_grade(self, enrollment, grade):
        enrollment.set_grade(grade)

    def approve_course(self, course):
        if course.department != self.department:
            print("This course does not belong to this department.")
            return

        if self.department.is_head_professor(self):
            if course.professor is None:
                print("Course cannot be approved without a professor.")
                return

            if course.schedule is None:
                print("Course cannot be approved without a schedule.")
                return

            course.status = "Approved"
            print("Course approved.")
        else:
            print("Only head professor can approve courses.")

    def reject_course(self, course, reason):
        if course.department != self.department:
            print("This course does not belong to this department.")
            return

        if self.department.is_head_professor(self):
            course.status = "Rejected"
            course.rejection_reason = reason
            print("Course rejected.")
        else:
            print("Only head professor can reject courses.")
            