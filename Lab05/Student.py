class Member:
    def __init__(self, name: str, address: str, email: str) -> None:

        self.name = name
        self.address = address
        self.email = email
    
    def __repr__(self):
        return "{0}({1},{2},{3})".format(self.__class__.__name__,self.name,self.address,self.email)

class Faculty(Member):
    def __init__(self, name: str, address: str, email: str,
                 faculty_num: str) -> None:
        super().__init__(name, address, email)
        self.faculty_number = faculty_num
        self.courses_teaching = []

    def __repr__(self):
        return "{0}({1},{2},{3},{4},{5})".format(self.__class__.__name__,self.name,self.address,self.email,self.faculty_number,self.courses_teaching)


class Student(Member):
    def __init__(self, name: str, address: str, email: str,
                 student_num: str) -> None:
        super().__init__(name, address, email)
        self.student_number = student_num
        self.courses_taken = []
        self.courses_taking = []
    
    def __str__(self):
        return "Name of the student : {0} \nAddress : {1} \nemail : {2} \nStudent number : {3} \nCourses_taken : {4} \nCourses_taking : {5} \n".format(self.name,self.address,self.email,self.student_number,self.courses_taken,self.courses_taking)

    def __repr__(self):
        return "{0}({1},{2},{3},{4},{5},{6})".format(self.__class__.__name__,self.name,self.address,self.email,self.student_number,self.courses_taken,self.courses_taking)
