from src.student import Student
import json

class StudentManager:

    def __init__(self):
        self.students = []

    def add_student(self, name,student_id):
        if self.find_student(student_id) is not None:
            return False

        student = Student(name,student_id)
        self.students.append(student)

        return True
    
    def show_students(self):
        if not self.students :
            print("No students found.")
            return

        for student in self.students:
            print(f"ID: {student.student_id} |"
                  f"Name: {student.name} |"
                  f"Average: {student.average():.2f}"
                  )

    def find_student(self,student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        
        return None

    def save_students(self, filename="data.json"):
        data = []

        for student in self.students:
            data.append(student.to_dict())

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_students(self,filename="data.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)

            self.students = []

            for student_data in data:
                student = Student.from_dict(student_data)
                self.students.append(student)

        except (FileNotFoundError, json.JSONDecodeError):
            self.students = []

    def delete_student(self, student_id):
        student = self.find_student(student_id)

        if student is None:
            return False

        self.students.remove(student)
        return True

    def update_student(self,student_id,new_name):
        student = self.find_student(student_id)

        if student is None:
            return False

        student.name = new_name
        return True

    def statistics(self):
        if not self.students:
            return None

        averages = [student.average() for student in self.students]

        return {
            "total_students": len(self.students),
            "highest_average": max(averages),
            "lowest_average": min(averages),
            "overall_average": sum(averages) / len(averages)
         }

    def search_by_name(self, name):
        results = []

        for student in self.students:
            if name.lower() in student.name.lower():
                results.append(student)

        return results