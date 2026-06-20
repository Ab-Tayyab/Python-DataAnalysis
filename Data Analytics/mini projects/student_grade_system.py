from statistics import mean
import json
import os

# ================= FILE HANDLING =================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(BASE_DIR, "files", "student_grade_system.json")

os.makedirs(os.path.dirname(file_name), exist_ok=True)

def load_file():
    try:
        with open(file_name,'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {} 

def save_file():
    with open(file_name,'w') as file:
        json.dump(grades,file,indent=4)

grades = load_file()
if not grades:
    grades = {
        '01':[80,90,85,76,91],
        '02':[70,80,51,66,71]
    }


# ================= GENERAL DESIGN =================


def design_function(text):
    print("\n" + "-" * len(text))
    print(text)
    print("-" * len(text))

# ================= FIND STUDENT =================


def get_student():
    roll_no = input("Enter Roll No! ")
    if roll_no not in grades:
        print("❌ Student Not found")
        return None
    return roll_no

# ================= ADD NEW GRADE =================

def add_new_record():
    s_RollNo = input("Enter student Rool No! 01, 02 and so on: ")
    if s_RollNo in grades:
        design_function("Student Record Already Present")
        return
    try:
        grade = list(map(int,input("Enter grade in a single seperated by space: ").split()))
        if not grade:
            print("❌ At least one grade is required")
            return
        grades[s_RollNo] = grade
        print("✅ Record added successfully")
    except ValueError:
        print("❌ Grade must be numbers")


# ================= SHOW GRADE =================


def show_grade():
    try:
        choice = int(input("Press 1 for show whole data and 2 for specific student data: "))
    except ValueError:
        print("❌ Invalid input")
        return
    match choice:
        case 1:
            design_function("All Student Grades")
            for key,marks in grades.items():
                print(f"{key}: {marks}")
        case 2:
                roll_no = get_student()
                if roll_no:
                    design_function("Single Student Grade")
                    grade = grades[roll_no]
                    print(f"{roll_no}: {grade}")
        case _:
            print("❌ Invalid Choice")

# ================= CALCULATE AVERAGE GRADE =================


def calculate_avg():
    try:
        choice = int(input("Press 1 for show all students grade average and 2 for specific student grade: "))
    except ValueError:
        print("❌ Invalid input")
        return
    match choice:
        case 1:
            design_function("R_No: Average")
            for key,marks in grades.items():
                print(f"{key}  : {mean(marks):.2f} %")
        case 2:
                roll_no = get_student()
                if roll_no:
                    design_function("R_No: Average")
                    grade = grades[roll_no]
                    print(f"{roll_no}: {mean(grade):.2f} %")
        case _:
            print("❌ Invalid Choice")

# ================= FIND HIGHEST AND LOWEST GRADE =================


def calculate_highest_lowest():
    try:
        choice = int(input("Press 1 for show all students highest lowest grade and 2 for specific student highest lowest grade: "))
    except ValueError:
        print("❌ Invalid input")
        return
    match choice:
        case 1:
            design_function("R_No: Highest: Lowest")
            for key,value in grades.items():
                print(f"{key}  : {max(value)} %  : {min(value)} %")
        case 2:
                roll_no = get_student()
                if roll_no:
                    design_function("R_No: Highest: Lowest")
                    grade = grades[roll_no]
                    print(f"{roll_no}: {max(grade)} %  : {min(grade)} %")
        case _:
            print("❌ Invalid Choice")

# ================= MENU =================

def menu():
        print("""
==========================
   Student Grade System
==========================
1. Add Student Grade
2. Show Grade
3. Average Grade
4. Highest and Lowest Grade
0. Exit
==========================
""")


while True:
    menu()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
         print("❌ Please enter a valid number.")
         continue
    
    match choice:
        case 1:
            add_new_record()
        case 2:
            show_grade()
        case 3:
            calculate_avg()
        case 4:
            calculate_highest_lowest()
        case 0:
            save_file()
            print("👋 Good Bye!")
            break
        case _:
            print("❌ Invalid Choice")