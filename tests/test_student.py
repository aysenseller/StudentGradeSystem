from src.student import Student


def test_student_creation():
    student = Student("Samet", "1245")

    assert student.name == "Samet"
    assert student.student_id == "1245"
    assert student.grades == []


def test_add_grade():
    student = Student("Samet", "1245")

    student.add_grade(80)
    student.add_grade(90)

    assert student.grades == [80, 90]


def test_average():
    student = Student("Samet", "1245")

    student.add_grade(80)
    student.add_grade(90)

    assert student.average() == 85

def test_student_details():
    student = Student("Samet", "1245")

    student.add_grade(80)
    student.add_grade(90)

    details = student.details()

    assert "Samet" in details
    assert "1245" in details
    assert "80" in details
    assert "90" in details