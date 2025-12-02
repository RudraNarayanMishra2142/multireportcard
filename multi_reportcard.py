def get_student_info():
    print("\n📝 Please enter student details:")
    name = input("Student Name: ")
    roll_no = input("Roll Number: ")
    email = input("Registered Email: ")
    reg_no = input("Registration Number: ")
    school_code = input("School Code: ")
    centre_code = input("Centre Code: ")
    
    return {
        "name": name,
        "roll_no": roll_no,
        "email": email,
        "reg_no": reg_no,
        "school_code": school_code,
        "centre_code": centre_code
    }

def get_student_marks():
    print("\n📚 Enter marks for the following subjects (out of 100):")
    subjects = ["Hindi", "English", "Physical Education", "Mathematics", "Science", "Social Science"]
    marks = {}
    
    for subject in subjects:
        while True:
            try:
                score = int(input(f"{subject}: "))
                if 0 <= score <= 100:
                    marks[subject] = score
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
    return marks

def calculate_results(student):
    marks = student["marks"]
    total = sum(marks.values())
    percentage = total / len(marks)
    
    if percentage >= 60:
        grade = "E"
        division = "First Division"
    elif percentage >= 33.33:
        grade = "G"
        division = "Second Division"
    else:
        grade = "F"
        division = "Third Division"

    top_subject = max(marks, key=marks.get)
    
    student.update({
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "division": division,
        "top_subject": top_subject
    })

def print_individual_report(student):
    print("\n🎉 Congratulations! 🎉")
    print(f"🎓 {student['info']['name']} - Roll No: {student['info']['roll_no']}")
    print("-" * 50)
    for subject, score in student["marks"].items():
        print(f"{subject}: {score}")
    print("-" * 50)
    print(f"📊 Total Marks: {student['total']}/600")
    print(f"📈 Percentage: {student['percentage']:.2f}%")
    print(f"🏅 Grade: {student['grade']} ({student['division']})")
    print(f"🏆 Highest Scoring Subject: {student['top_subject']}")
    
    if student["marks"]["Hindi"] >= 90:
        print("💰 Eligible for Hindi Scholarship!")

    # Improvement exam advice based on grade
    print("-" * 50)
    if student["grade"] == "F":
        print("⚠️ You are advised to contact your school and fill out the improvement exam form immediately.")
    elif student["grade"] == "G":
        print("ℹ️ You may apply for the improvement exam by contacting your school.")
    elif student["grade"] == "E":
        print("✅ You passed with First Division. Improvement exam is optional if you're aiming for higher scores.")

    print("=" * 50)

def print_summary(students):
    print("\n📋 Final Summary:")
    print("=" * 50)
    
    sorted_students = sorted(students, key=lambda s: s["percentage"], reverse=True)
    topper = sorted_students[0]

    print(f"🥇 Topper: {topper['info']['name']} - {topper['percentage']:.2f}%")
    
    print("\n💸 Scholarship Eligibility (Hindi ≥ 90):")
    found = False
    for student in students:
        if student["marks"]["Hindi"] >= 90:
            print(f" - {student['info']['name']} ({student['marks']['Hindi']} in Hindi)")
            found = True
    if not found:
        print("No students eligible for Hindi scholarship.")

    print("=" * 50)
    print("✨ Thank you ! ✨")
    print(" A big ❤️ for you and blessings from Board for your future.")
    print("=" * 50)

def main():
    students = []

    while True:
        info = get_student_info()
        marks = get_student_marks()

        student = {
            "info": info,
            "marks": marks
        }

        calculate_results(student)
        print_individual_report(student)
        students.append(student)

        choice = input("\n➕ Do you want to add another student? (y/n): ").strip().lower()
        if choice != 'y':
            break

    print_summary(students)

# Run the program
main()
