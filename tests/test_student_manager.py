from src.student_manager import StudentManager


def test_add_student():
    manager = StudentManager()

    result = manager.add_student("Samet", "1245")

    assert result is True
    assert len(manager.students) == 1
    assert manager.students[0].name == "Samet"


def test_find_student():
    manager = StudentManager()

    manager.add_student("Samet", "1245")

    student = manager.find_student("1245")

    assert student is not None
    assert student.name == "Samet"


def test_find_student_not_found():
    manager = StudentManager()

    student = manager.find_student("9999")

    assert student is None


def test_duplicate_student_id():
    manager = StudentManager()

    first = manager.add_student("Samet", "1245")
    second = manager.add_student("Ali", "1245")

    assert first is True
    assert second is False
    assert len(manager.students) == 1

def test_delete_student():
    manager = StudentManager()

    manager.add_student("Samet", "1245")

    result = manager.delete_student("1245")

    assert result is True
    assert len(manager.students) == 0


def test_delete_student_not_found():
    manager = StudentManager()

    result = manager.delete_student("9999")

    assert result is False


def test_update_student():
    manager = StudentManager()

    manager.add_student("Samet", "1245")

    result = manager.update_student("1245", "Samet Can")

    assert result is True
    assert manager.students[0].name == "Samet Can"


def test_update_student_not_found():
    manager = StudentManager()

    result = manager.update_student("9999", "Ali")

    assert result is False


def test_statistics():
    manager = StudentManager()

    manager.add_student("Samet", "1245")
    manager.add_student("Ali", "1246")

    manager.students[0].add_grade(80)
    manager.students[1].add_grade(60)

    stats = manager.statistics()

    assert stats["total_students"] == 2
    assert stats["highest_average"] == 80
    assert stats["lowest_average"] == 60
    assert stats["overall_average"] == 70

def test_search_by_name():
    manager = StudentManager()

    manager.add_student("Samet", "1")
    manager.add_student("Ali","2")
    manager.add_student("Mehmet", "3")

    results = manager.search_by_name("Mehmet")

    assert len(results) == 1
    assert results[0].name == "Mehmet"
    
def test_show_students(capsys):
    manager = StudentManager()

    manager.add_student("Ayşen", "100")
    student = manager.find_student("100")
    student.add_grade(80)
    student.add_grade(90)

    manager.show_students()

    captured = capsys.readouterr()

    assert "ID: 100" in captured.out
    assert "Name: Ayşen" in captured.out
    assert "Average: 85.00" in captured.out