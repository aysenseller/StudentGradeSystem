class Student:
    def __init__(self,name,student_id, grades=None):
        self.name =name
        self.student_id=student_id
        self.grades = grades if grades is not None else []

    def add_grade(self,grade):
        self.grades.append(grade)

    def average(self):
        if not self.grades:
            return 0

        return sum(self.grades) / len(self.grades)

    def to_dict(self):
            return{
                "name" : self.name,
                "student_id" : self.student_id,
                "grades" : self.grades
            }

    @classmethod
    def from_dict(cls, data):
         return cls(
              data["name"],
              data["student_id"],
              data["grades"]
         )

    def details(self):
        return (
            f"Name: {self.name}\n"
            f"ID: {self.student_id}\n"
            f"Grades: {self.grades}\n"
            f"Average: {self.average():.2f}"
        )
    