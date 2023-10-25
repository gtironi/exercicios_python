class UndergraduateStudent:

    def __init__(self, name, student_id, year, major):
        self.name = name
        self.student_id = student_id
        self.year = year
        self.major = major
        UndergraduateStudent.total_students += 1
    
    @staticmethod #não precisa ter objeto para chamar
    def total_students_count(): #sem self
        return UndergraduateStudent.total_students


class MathStudent(UndergraduateStudent):
    
    def __init__(self, name, student_id, year, specialization):
        super().__init__(self, name, student_id, year, major = "Mathematics")

        self.specialization = specialization

    def solve_math_problem(self, problem):
        return f"{self.name} is solving a {self.specialization} math problem: {problem}"

print(f'Total Students: {UndergraduateStudent.total_students_count()}')
