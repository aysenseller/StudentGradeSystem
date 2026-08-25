from src.student import Student
from src.student_manager import StudentManager


manager = StudentManager()

manager.load_students()


while True:
    print("\n================================")
    print("      STUDENT GRADE SYSTEM")
    print("================================")
    print("1 - Add student")
    print("2 - Show students")
    print("3 - Add grade")
    print("4 - Find student")
    print("5 - Delete student")
    print("6 - Edit student")
    print("7- Statistics")
    print("8 - Search by name")
    print("9 - Show student details")
    print("0 - Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Student name: ").strip()
        student_id = input("Student ID: ").strip()

        if not name:
            print("Student name cannot be empty.")
            continue
        if not student_id:
            print("Student ID cannot be empty.")
            continue
        if manager.add_student(name,student_id):
            manager.save_students()
            print("Student added successfully.")

        else:
            print("A student with this ID already exists.")


    elif choice == "2":
        manager.show_students()

    elif choice == "3":
        student_id = input("Student ID: ")
        student = manager.find_student(student_id)

        if student is None:
            print("Student not found.")
        else:
            try:
                grade = float(input("Grade: "))

                if grade < 0 or grade > 100:
                    print("Grade must be between 0 and 100.")
                    continue

                student.add_grade(grade)
                manager.save_students()

                print("Grade added successfully.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        student_id = input("Student ID: ")
        student = manager.find_student(student_id)

        if student is None:
            print("Student not found.")
        else:
            print(f"Name: {student.name}")
            print(f"ID: {student.student_id}")
            print(f"Grades: {student.grades}")
            print(f"Average: {student.average()}")

    elif choice == "5":
        student_id = input("Student ID: ").strip()

        if manager.delete_student(student_id):
            manager.save_students()
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    elif choice == "6":
        student_id = input("Student ID: ").strip()
        new_name = input("New name: ").strip()

        if not new_name:
            print("Student name cannot be empty.")
            continue

        if manager.update_student(student_id, new_name):
            manager.save_students()
            print("Student updated successfully.")
        else:
            print("Student not found.")

    elif choice == "7":
        stats = manager.statistics()

        if stats is None:
            print("No students found.")
        else:
            print("\n========== STATISTICS ==========")
            print(f"Total students: {stats['total_students']}")
            print(f"Highest average: {stats['highest_average']:.2f}")
            print(f"Lowest average: {stats['lowest_average']:.2f}")
            print(f"Overall average: {stats['overall_average']:.2f}")


    elif choice == "8":
        name = input("Student name: ").strip()

        results = manager.search_by_name(name)

        if not results:
            print("No students found.")
        else:
            for student in results:
                print(
                    f"ID: {student.student_id} | "
                    f"Name: {student.name} | "
                    f"Average: {student.average():.2f}"
                )

    elif choice == "9":
        student_id = input("Student ID: ").strip()

        student = manager.find_student(student_id)

        if student is None:
            print("Student not found.")
        else:
            print("\n====================")
            print(student.details())
            print("====================")


    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
