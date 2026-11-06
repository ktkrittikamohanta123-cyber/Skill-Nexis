"""JSON File Reader: load JSON data and print formatted output.
Topics: JSON, dict, list, tuple, set, exception handling.
"""
import json
import sys


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def print_students(data):
    """Pretty table for the sample student data."""
    students = data.get("students", [])
    print(f"\nClass: {data.get('class', 'N/A')}  |  Students: {len(students)}")
    print(f"{'Name':<10}{'Age':<5}{'Marks':<18}{'Avg':>6}")
    print("-" * 40)
    all_subjects = set()                       # set of subjects
    for s in students:
        marks = s.get("marks", [])             # list of marks
        avg = sum(marks) / len(marks) if marks else 0
        all_subjects.update(s.get("subjects", []))
        print(f"{s['name']:<10}{s['age']:<5}{str(marks):<18}{avg:>6.1f}")
    print("\nSubjects offered:", ", ".join(sorted(all_subjects)))


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.json"
    try:
        data = load_json(path)
    except FileNotFoundError:
        print(f"Error: '{path}' not found.")
        return
    except json.JSONDecodeError as e:
        print(f"Error: invalid JSON at line {e.lineno}, column {e.colno}: {e.msg}")
        return

    print("=== Formatted JSON ===")
    print(json.dumps(data, indent=4, sort_keys=True))

    if isinstance(data, dict) and "students" in data:
        try:
            print_students(data)
        except (KeyError, TypeError) as e:
            print(f"Error: unexpected data structure ({e!r}).")


if __name__ == "__main__":
    main()
