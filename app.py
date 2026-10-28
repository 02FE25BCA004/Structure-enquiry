# app.py

def calculate_grade(average):
    if 90 <= average <= 100:
        return "Grade S"
    elif 80 <= average <= 89:
        return "Grade A"
    elif 65 <= average <= 79:
        return "Grade B"
    elif 50 <= average <= 64:
        return "Grade C"
    elif 40 <= average <= 49:
        return "Grade D"
    else:
        return "Grade F"

def main():
    print("=== Student Grade Evaluation System ===")
    
    # Mock input data (can be modified to input() for interactive use)
    name = "Alice Smith"
    department = "Computer Science"
    semester = 4
    marks = [85, 90, 78]
    
    avg_score = sum(marks) / len(marks)
    grade = calculate_grade(avg_score)
    
    print(f"Student Name : {name}")
    print(f"Department   : {department}")
    print(f"Semester     : {semester}")
    print(f"Marks        : {marks}")
    print(f"Average Score: {avg_score:.2f}")
    print(f"Assigned Grade: {grade}")
    print("Student evaluation executed successfully!")

if __name__ == "__main__":
    main()