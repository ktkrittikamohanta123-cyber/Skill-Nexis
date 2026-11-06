"""Mini Project (W2): Student Management System
Stores student data (roll number, name, marks) in a CSV file.
Features: add, delete, search, update, list. Changes are saved permanently.
Topics: lists, tuples, sets, dictionaries, CSV files, exception handling.
"""
import csv
import os

FILE_NAME = "students.csv"
FIELDS = ("roll", "name", "marks")  # tuple: fixed column order


def load_students():
    """Read the CSV into a dict {roll: {"name": ..., "marks": ...}}."""
    students = {}
    if not os.path.exists(FILE_NAME):
        return students
    try:
        with open(FILE_NAME, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    students[row["roll"]] = {
                        "name": row["name"],
                        "marks": float(row["marks"]),
                    }
                except (KeyError, ValueError, TypeError):
                    print(f"Skipping bad row: {row}")
    except OSError as e:
        print(f"Could not read {FILE_NAME}: {e}")
    return students


def save_students(students):
    """Write all students back to the CSV (called after every change)."""
    try:
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(FIELDS)
            for roll in sorted(students, key=lambda r: (len(r), r)):
                s = students[roll]
                writer.writerow([roll, s["name"], s["marks"]])
    except OSError as e:
        print(f"Could not save to {FILE_NAME}: {e}")


def read_marks(prompt):
    value = float(input(prompt).strip())
    if not 0 <= value <= 100:
        raise ValueError("Marks must be between 0 and 100.")
    return value


def add_student(students):
    roll = input("Roll number: ").strip()
    if not roll:
        print("Roll number cannot be empty.")
        return
    if roll in set(students):  # set for fast duplicate check
        print(f"Roll number {roll} already exists.")
        return
    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    marks = read_marks("Marks (0-100): ")
    students[roll] = {"name": name, "marks": marks}
    save_students(students)
    print(f"Added {name} (Roll {roll}).")


def delete_student(students):
    roll = input("Roll number to delete: ").strip()
    if roll not in students:
        print("Student not found.")
        return
    removed = students.pop(roll)
    save_students(students)
    print(f"Deleted {removed['name']} (Roll {roll}).")


def search_student(students):
    query = input("Search by roll number or name: ").strip().lower()
    matches = [
        (roll, s["name"], s["marks"])  # list of tuples
        for roll, s in students.items()
        if query == roll.lower() or query in s["name"].lower()
    ]
    if not matches:
        print("No matching student found.")
        return
    print_table(matches)


def update_student(students):
    roll = input("Roll number to update: ").strip()
    if roll not in students:
        print("Student not found.")
        return
    s = students[roll]
    name = input(f"New name [{s['name']}]: ").strip()
    marks_text = input(f"New marks [{s['marks']}]: ").strip()
    if name:
        s["name"] = name
    if marks_text:
        marks = float(marks_text)
        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100.")
        s["marks"] = marks
    save_students(students)
    print("Record updated.")


def print_table(rows):
    print(f"\n{'Roll':<8}{'Name':<20}{'Marks':>7}")
    print("-" * 35)
    for roll, name, marks in rows:
        print(f"{roll:<8}{name:<20}{marks:>7.1f}")


def list_students(students):
    if not students:
        print("No students on record.")
        return
    rows = [(r, s["name"], s["marks"]) for r, s in students.items()]
    rows.sort(key=lambda t: (len(t[0]), t[0]))
    print_table(rows)
    marks = [m for _, _, m in rows]
    print(f"\nTotal: {len(marks)} | Average: {sum(marks)/len(marks):.1f} "
          f"| Highest: {max(marks)} | Lowest: {min(marks)}")


def main():
    students = load_students()
    menu = {
        "1": ("Add student", add_student),
        "2": ("Delete student", delete_student),
        "3": ("Search student", search_student),
        "4": ("Update student", update_student),
        "5": ("List all students", list_students),
    }
    while True:
        print("\n=== Student Management System ===")
        for key, (label, _) in menu.items():
            print(f"{key}. {label}")
        print("6. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "6":
            print("Goodbye! All changes are saved in", FILE_NAME)
            break
        if choice not in menu:
            print("Invalid choice. Try again.")
            continue
        try:
            menu[choice][1](students)
        except ValueError as e:
            print(f"Invalid input: {e}")
        except (KeyboardInterrupt, EOFError):
            print("\nCancelled.")


if __name__ == "__main__":
    main()
