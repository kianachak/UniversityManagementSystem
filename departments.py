class Department:
    def __init__(self, name):
        self.name = name
        self.head_professor = None
        self.professors_list = []
        self.student_list = []
        self.course_list = []
        


    def display_info(self):
        print(f'Name: {self.name}')

        if self.head_professor is None:
            print('Head Professor: Not assigned')
        else:
            print(f'Head Professor: {self.head_professor.name}')

        self.view_professors()
        self.view_students()
        self.view_courses()

    def add_professor(self, professor):
        if professor in self.professors_list:
            print("This professor is already in the list.")
        else:
            self.professors_list.append(professor)
    
    def remove_professor(self, professor):
        if professor in self.professors_list:
            self.professors_list.remove(professor)

            if self.head_professor == professor:
                self.head_professor = None
        else:
            print("This professor is not in the department.")

    def set_head_professor(self, professor):
        if professor in self.professors_list:
            self.head_professor = professor
            print("Head professor assigned successfully.")
        else:
            print("Professor is not part of this department.")
    
    def is_head_professor(self, professor):
        return self.head_professor == professor

    def view_professors(self):
        if self.professors_list == []:
            print("There is no professor in this department.")
        else:
            print("Professors:")
            for professor in self.professors_list:
                print(professor.name)

    def add_student(self, student):
        self.student_list.append(student)

    def view_students(self):
        if self.student_list == []:
            print("There is no student in this department.")
        else:
            print("Students:")
            for student in self.student_list:
                print(student.name)

    def add_course(self,course):
        self.course_list.append(course)

    def view_courses(self):
        if self.course_list == []:
            print("There is no course in this department.")
        else:
            print("Courses:")
            for course in self.course_list:
                print(course.name)

    def view_available_courses(self):
        available_courses = []

        for course in self.course_list:
            if (
                course.professor is not None
                and course.schedule is not None
                and course.status == "Approved"
            ):
                available_courses.append(course)

        if not available_courses:
            print("No available courses.")

        else:
            print("Available Courses:")

            for course in available_courses:
                print(course.name)
                #print(course.name, course.professor is not None, course.schedule is not None, course.status == "Approved")