# Function to determine grade based on average marks
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

#  Function to make sure entered marks are between 0 and 100
def is_valid_marks(marks):
    # Check that each mark is within the valid range
    return all(0 <= m <= 100 for m in marks)

# Function to calculate the average score from a list of marks
def calculate_average(marks):
    return sum(marks) / len(marks)

# Function to create a dictionary representing a student
def create_student(name, marks):
    #Calculate average and grade based on marks
    avg = calculate_average(marks)
    grade = get_grade(avg)
    # Return storing all student info
    return {
        "name": name,
        "marks": marks,
        "average": avg,
        "grade": grade
    }

# Function to find a student in the list by name 
def find_student(student_list, name):
    return next((s for s in student_list if s['name'].lower() == name.lower()), None)

# Function to display overall statistics for the class
def show_statistics(student_list):
      # If list is empty, exit 
    if not student_list:
        print("No student data to show.")
        return
    print("\nClass Stats")
    # Collect all average scores into a list
    all_averages = [s['average'] for s in student_list]
     # Calculate and print class average
    print(f"Class Average: {sum(all_averages) / len(all_averages):.2f}")
    # Print highest and lowest averages in the class
    print(f"Highest Average: {max(all_averages):.2f}")
    print(f"Lowest Average: {min(all_averages):.2f}")
    
# Count how many students received each grade
    grades = [s['grade'] for s in student_list]
    print("Grade Distribution:")
    for g in ['A', 'B', 'C', 'D', 'F']:
        count = grades.count(g)
        if count > 0:
            print(f"   {g}: {count} student(s)")

# Function to display all student records
def show_all_students(student_list):
    if not student_list:
        print("No student records yet.")
        return
    print("\nAll Student Records")
      # Loop through each student and display their info
    for idx, s in enumerate(student_list, start=1):
        print(f"{idx}. Name: {s['name']}")
        print(f"   Marks: {s['marks']}")
        print(f"   Average: {s['average']:.2f}")
        print(f"   Grade: {s['grade']}")
        print("    " + "-" * 25)

# Function to add a new student based on user input
def input_add_student(student_list):
    # Ask for student's name
    name = input("Enter student name: ").strip()
    if not name:
        print("Name can't be empty.")
        return
    try:
         # Ask for 3 space-separated marks and convert to integers
        marks_input = input("Enter 3 marks (space-separated): ").strip()
        marks = list(map(int, marks_input.split()))
        # Ensure exactly 3 numbers were entered
        if len(marks) != 3:
            print("Please enter exactly 3 marks.")
            return
        # Validate marks are in range 0–100
        if not is_valid_marks(marks):
            print("Marks must be between 0 and 100.")
            return
        # Create and add student record to the list
        student = create_student(name, marks)
        student_list.append(student)
        print(f"{name} was added successfully.")
    except ValueError:
        print("Invalid input. Please use only numbers for marks.")

# Function to search and display a student's record
def search_student(student_list):
    if not student_list:
        print("No student records yet.")
        return
     # Get name to search
    name = input("Enter name to search: ").strip()
    # Try to find student in the list
    found = find_student(student_list, name)
    # If student found, display info
    if found:
        print("\nStudent Found:")
        print(f"Name: {found['name']}")
        print(f"Marks: {found['marks']}")
        print(f"Average: {found['average']:.2f}")
        print(f"Grade: {found['grade']}")
    else:
        print("Student not found.")

# Function to load sample students testing
def load_sample_students(student_list):
     # Predefined sample students (name + 3 marks each) 
    sample_data = [
        ("Z", [88, 92, 81]),
        ("V", [95, 87, 91]),
        ("M", [67, 73, 70]),
        ("T", [85, 89, 90]),
        ("S", [45, 52, 49])
    ]
    print("Adding sample data...")
    # Add each sample student to the list
    for name, marks in sample_data:
        student = create_student(name, marks)
        student_list.append(student)
    print("Sample students added.\n")

# Main function to run the menu-driven Student Grade Management System
def main():
    print("Welcome to the Student Grade Management System!\n")
    
    # Initialize student list
    student_list = []

    # Ask if the user wants to preload sample data
    print("Do you want to load sample student data? (yes/no)")
    if input(">> ").strip().lower() in ['yes', 'y']:
        load_sample_students(student_list)

    # Menu loop- runs until user chooses to exit
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search for Student")
        print("4. View Statistics")
        print("5. Exit")

        # Get menu choice
        choice = input("Choose an option (1-5): ").strip()

        # Match input with actions
        if choice == "1":
            input_add_student(student_list)
        elif choice == "2":
            show_all_students(student_list)
        elif choice == "3":
            search_student(student_list)
        elif choice == "4":
            show_statistics(student_list)
        elif choice == "5":
            print("Thanks for using the Student Grade System.")
            break
        else:
            print("Invalid option. Please try again.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
