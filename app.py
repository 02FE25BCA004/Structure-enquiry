
# app.py

def calculate_grade(average):
    if 90 <= average <= 100:
        return "Grade S"
    elif average >= 80:
        return "Grade A"
    elif average >= 65:
        return "Grade B"
    elif average >= 50:
        return "Grade C"
    elif average >= 40:
        return "Grade D"
    else:
        return "Grade F"


def get_marks(subject_number):
    while True:
        try:
            marks = float(input(
                f"Enter marks for subject {subject_number} (0-100): "
            ))

            if 0 <= marks <= 100:
                return marks

            print("Invalid marks! Enter a value between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    print("=== Student Grade Evaluation System ===")

    name = input("Enter student name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter student name: ").strip()

    department = input("Enter department: ").strip()
    semester = input("Enter semester: ").strip()

    marks = []

    for i in range(1, 4):
        marks.append(get_marks(i))

    average = sum(marks) / len(marks)
    grade = calculate_grade(average)

    print("\n===== STUDENT RESULT =====")
    print(f"Student Name  : {name}")
    print(f"Department    : {department}")
    print(f"Semester      : {semester}")
    print(f"Subject Marks : {marks}")
    print(f"Average Score : {average:.2f}")
    print(f"Assigned Grade: {grade}")
    print("Student evaluation completed successfully!")


if __name__ == "__main__":
    main()
