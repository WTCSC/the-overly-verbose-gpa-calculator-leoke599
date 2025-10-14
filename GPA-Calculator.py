print("Welcome to GPA Calculator\n")
classes = int(input("How many classes are you in? (Both first and second semester) "))
grades = []
for i in range(classes):
    try:
        grade = float(input(f"\nEnter grade {i + 1} (0.0-4.0): "))
        if grade < 0.0 or grade > 4.0:
            raise ValueError("Grade must be between 0.0 and 4.0. This input won't be counted.")
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid grade.")
    else:
        grades.append(grade)
        gpa = sum(grades) / len(grades)
print(f"\nYour GPA is: {gpa:.2f}")

semester = input("\nWhich semester do you want to analyze?\n 1. First Semester (first half of classes)\n 2. Second Semester (second half of classes)\nEnter 1 or 2: ")
if semester == '1':
    semester_grades = grades[:len(grades)//2]
    semester_gpa = sum(semester_grades) / len(semester_grades) if semester_grades else 0
    print("First Semester GPA:", f"{semester_gpa:.2f}")
    if semester_gpa > gpa:
        print("Your first semester GPA is above your overall GPA.")
    elif semester_gpa < gpa:
        print("Your first semester GPA is below your overall GPA.")
    else:
        print("Your first semester GPA is equal to your overall GPA.")

elif semester == '2':
    semester_grades = grades[len(grades)//2:]
    semester_gpa = sum(semester_grades) / len(semester_grades) if semester_grades else 0
    print("Second Semester GPA:", f"{semester_gpa:.2f}")
    if semester_gpa > gpa:
        print("Your second semester GPA is above your overall GPA.")
    elif semester_gpa < gpa:
        print("Your second semester GPA is below your overall GPA.")
    else:
        print("Your second semester GPA is equal to your overall GPA.")

else:
    print("Invalid choice. Exiting.")
    exit()

while True:
    try:
        target_gpa = float(input("\nEnter your target GPA (0.0-4.0): "))
        if target_gpa < 0.0 or target_gpa > 4.0:
            raise ValueError("Target GPA must be between 0.0 and 4.0.")
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid target GPA.")
    else:
        break

if target_gpa > gpa:
    required_gpa = (target_gpa * (len(grades) + 1)) - sum(grades)
    if required_gpa > 4.0:
        print("Achieving this target GPA is not possible with one additional class.")
    else:
        print(f"To reach a target GPA of {target_gpa:.2f}, you need to score at least {required_gpa:.2f} in your next class.")
elif target_gpa < gpa:
    print("Your current GPA is already above your target GPA.")
else:
    print("Your current GPA is equal to your target GPA.")