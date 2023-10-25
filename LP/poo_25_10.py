class UndergraduateStudent(self):

    def __init__(self, name, student_id, year, major):
        self.name = name
        self.student_id = student_id
        self.year = year
        self.major = major

class MathStudent(UndergraduateStudent):
    
    def __init__(self, name, student_id, year, specialization):
        super().__init__(self, name, student_id, year, major = "Mathematics")

        self.specialization = specialization

    def solve_math_problem(self, problem):
        return f"{self.name} is solving a {self.specialization} math problem: {problem}"

