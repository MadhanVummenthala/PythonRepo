# Simple welcome message
print("Welcome to the Student Grade Management System!\n")

#  creates an empty list where all student information will be saved (name, marks, grade,)
student_list = []

# Function to find the grade based on average marks
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

# Function to make sure entered marks are between 0 and 100
def is_valid_marks(marks):
    return all(0 <= m <= 100 for m in marks)

# Function to add a new student
def add_student(name, marks):
    if not is_valid_marks(marks):
        print("Marks must be between 0 and 100.")
        return False

    try:
        avg = sum(marks) / len(marks)
        grade = get_grade(avg)
        student = {
            "name": name,
            "marks": marks,
            "average": avg,
            "grade": grade
        }
        student_list.append(student)
        return True
    except Exception as e:
        print("Error while adding student:", e)
        return False

# Function to show stats about the whole class
def show_statistics():
    if not student_list:
        print("No student data to show.")
        return

    print("\n Class Stats")
    all_averages = [s['average'] for s in student_list]
    print(f"Class Average: {sum(all_averages) / len(all_averages):.2f}")
    print(f"Highest Average: {max(all_averages):.2f}")
    print(f"Lowest Average: {min(all_averages):.2f}")

    # Count how many students got each grade
    grades = [s['grade'] for s in student_list]
    print("Grade Distribution:")
    for g in ['A', 'B', 'C', 'D', 'F']:
        count = grades.count(g)
        if count > 0:
            print(f"  {g}: {count} student(s)")

# Function to search for a student by name
def find_student_by_name(name):
    for s in student_list:
        if s['name'].lower() == name.lower():
            return s
    return None

# Add student through input
def input_add_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("Name can't be empty.")
        return

    try:
        marks_input = input("Enter 3 marks (space-separated): ")
        marks = list(map(int, marks_input.split()))

        if len(marks) != 3:
            print("Please enter exactly 3 marks.")
            return

        if add_student(name, marks):
            print(f"{name} was added successfully.")
    except ValueError:
        print("Invalid input. Please use only numbers for marks.")

# Show all students
def show_all_students():
    if not student_list:
        print("No student records yet.")
        return

    print("\n All Student Records")
    for idx, s in enumerate(student_list, start=1):
        print(f"{idx}. Name: {s['name']}")
        print(f"   Marks: {s['marks']}")
        print(f"   Average: {s['average']:.2f}")
        print(f"   Grade: {s['grade']}")
        print("   " + "-" * 25)

# Search student by name
def search_student():
    if not student_list:
        print("No student records yet.")
        return

    name = input("Enter name to search: ").strip()
    found = find_student_by_name(name)

    if found:
        print("\n Student Found:")
        print(f"Name: {found['name']}")
        print(f"Marks: {found['marks']}")
        print(f"Average: {found['average']:.2f}")
        print(f"Grade: {found['grade']}")
    else:
        print("Student not found.")

# 
def load_sample_students():
    sample_data = [
        ("Z", [88, 92, 81]),
        ("V", [95, 87, 91]),
        ("M", [67, 73, 70]),
        ("T", [85, 89, 90]),
        ("S", [45, 52, 49])
    ]
    print("Adding sample data...")
    for name, marks in sample_data:
        add_student(name, marks)
    print("Sample students added.\n")

# Show example student outputs
def show_example_outputs():
    print("\nShowing example student data...")
    show_all_students()
    show_statistics()

# Main menu to navigate the system
def main():
    print("Do you want to load sample student data? (yes/no)")
    if input(">> ").lower() in ['yes', 'y']:
        load_sample_students()

    while True:
        print("\n===== MAIN MENU =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search for Student")
        print("4. View Statistics")
        print("5. Show Example Output")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            input_add_student()
        elif choice == "2":
            show_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            show_statistics()
        elif choice == "5":
            show_example_outputs()
        elif choice == "6":
            print("Thanks for using the Student Grade System.")
            break
        else:
            print("Invalid option. Please try again.")

# Run the app
if __name__ == "__main__":                                                              
    main()
