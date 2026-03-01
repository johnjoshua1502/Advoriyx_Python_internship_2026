import csv
import os

# determine the path of this script so CSV is always located alongside it
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "students.csv")

# Load students from CSV
def load_students():
    students = []
    try:
        with open(CSV_FILE, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        # no file yet, return empty list
        pass
    return students

# Save students to CSV
def save_students(students):
    with open(CSV_FILE, mode="w", newline="") as file:
        fieldnames = ["RollNo", "Name", "Class"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)
# ----------------------------------------------------------------------
# ADD STUDENT RECORD
# ----------------------------------------------------------------------

def add_student(students):
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    cls = input("Enter Class: ")
    student = {"RollNo": roll, "Name": name, "Class": cls}
    students.append(student)
    save_students(students)
    print(f"Student {name} added successfully!\n")

# ----------------------------------------------------------------------
#  VIEW A STUDENT RECORD
# ----------------------------------------------------------------------


def view_students(students):
    if not students:
        print("No records found.\n")
        return

    print("\n--- Student Records ---")
    for s in students:
        print(f"RollNo: {s['RollNo']} | Name: {s['Name']} | Class: {s['Class']}")
    print("")


# ----------------------------------------------------------------------
# UPDATE A STUDENT RECORD
# ----------------------------------------------------------------------
def update_student(students):
    roll = input("Enter Roll No to update: ").strip()

    found = False
    for s in students:
        if s["RollNo"] == roll:
            new_name = input("Enter new name: ").strip()
            new_class = input("Enter new class: ").strip()

            s["Name"] = new_name
            s["Class"] = new_class
            found = True
            break

    if found:
        save_students(students)
        print("Record updated successfully!\n")
    else:
        print("Roll No not found.\n")


# ----------------------------------------------------------------------
# DELETE A STUDENT
# ----------------------------------------------------------------------
def delete_student(students):
    roll = input("Enter Roll No to delete: ").strip()
    new_list = [s for s in students if s["RollNo"] != roll]

    if len(new_list) == len(students):
        print("Roll No not found.\n")
    else:
        save_students(new_list)
        print("Record deleted successfully!\n")

    return new_list


def main():
    students = load_students()
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            students = delete_student(students)
        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()