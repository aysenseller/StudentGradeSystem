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
    manager.add_student("Ali", "2")
    manager.add_student("Alihan", "3")
    manager.add_student("Mehmet", "4")

    results = manager.search_by_name("ali")

    assert len(results) == 2
    assert results[0].name == "Ali"
    assert results[1].name == "Alihan"

def test_search_by_name_case_insensitive():
    manager = StudentManager()

    manager.add_student("Ali", "1")
    manager.add_student("Mehmet", "2")

    results = manager.search_by_name("ALI")

    assert len(results) == 1
    assert results[0].name == "Ali"

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

def test_save_and_load_students(tmp_path):
    filename = tmp_path / "test_data.json"

    manager = StudentManager()

    manager.add_student("Ali", "100")
    student = manager.find_student("100")
    student.add_grade(85)
    student.add_grade(95)

    manager.save_students(filename)

    new_manager = StudentManager()
    new_manager.load_students(filename)

    loaded_student = new_manager.find_student("100")

    assert loaded_student is not None
    assert loaded_student.name == "Ali"
    assert loaded_student.student_id == "100"
    assert loaded_student.grades == [85, 95]
    assert loaded_student.average() == 90

def test_statistics_students_with_and_without_grades():
    manager = StudentManager()

    manager.add_student("Samet","1")
    manager.add_student("Ali","2")
    manager.add_student("Mehmet","3")

    manager.find_student("1").add_grade(80)
    manager.find_student("2").add_grade(60)

    stats= manager.statistics()

    assert stats["total_students"] == 3
    assert stats["students_with_grades"] == 2
    assert stats["students_without_grades"] == 1