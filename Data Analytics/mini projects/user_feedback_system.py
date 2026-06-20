import json
import os

# ================= FILE HANDLING =================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(BASE_DIR, "files", "user_feedback_system.json")

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
        json.dump(user_feedback,file,indent=4)

user_feedback = load_file()
if not user_feedback:
    user_feedback = {
        "tayyab@gmail.com":[{
            "name":"tayyab",
            "feedback":"good product, i love it."
        }],
        "abdullah@gmail.com":[{
            "name":"abdullah",
            "feedback":"excellent product, i love it."
        },
        {
            "name":"abdullah",
            "feedback":"bad product, i hate it."
        }],
    }


# ================= FHOW FEEDBACK =================


def show_feedback():
    if user_feedback:
        isFound = False
        choice =  input("1 for all feedback, 2 for search by G-mail: ")
        if choice == "1":
            for emails, feedbacks in user_feedback.items():
                print("------------------------------------")
                for index,feedback in enumerate(feedbacks,start=1):
                    print(f"{index}- {feedback["name"]}: \n   {feedback["feedback"]} ")
        elif choice == "2":
            email = input("Enter E-mail: ")
            if email in user_feedback:
                for index,feedback in enumerate(user_feedback[email],start=1):
                    print(f"{index}- {feedback['name']}: \n   {feedback['feedback']}")
                isFound = True
            if not isFound:
                print("Invalid E-mail or user not found!")
        else:
            print("Invalid choice!")
    else:
        print("No Feedback available!")


# ================= ADD FEEDBACK =================


def add_feedback():
    email = input("Enter Email: ").strip()
    name = input("Enter Name: ").strip()
    feedback = input("Enter Feedback: ").strip()

    new_feedback = {
        "name" : name,
        "feedback" : feedback
    }

    if email in user_feedback:
        user_feedback[email].append(new_feedback)
        print("Feedback submitted successfully!")
    else:
        user_feedback[email] = [new_feedback]
        print("Feedback submitted successfully!")

# ================= DELETE FEDBACK =================

def delete_feedback():
    email = input("Enter Email: ").strip()
    if email in user_feedback:
        count = len(user_feedback[email])
        print(f"Your have {count} feedback")
        for index, feedback in enumerate(user_feedback[email],start=0):
            print(f"{index}- {feedback["name"]}: {feedback["feedback"]}")

        if count>1:
            num = int(input("Enter index number which you want to delete: "))
            confirmation = input("Are you sure: y/n: ").strip().lower()

            if confirmation == "y":
                del user_feedback[email][num]
                print("Feedback deleted successfully!")
            elif confirmation == "n":
                print("Thanks for your confirmation!")
            else:
                print("Invalid choice!")
        else:
            confirmation = input("Are you sure: y/n: ").strip().lower()

            if confirmation == "y":
                del user_feedback[email]
                print("Feedback deleted successfully!")
            elif confirmation == "n":
                print("Thanks for your confirmation!")
            else:
                print("Invalid choice!")


# ================= EDIT FEEDBACK =================

def edit_feedback():
    email = input("Enter your email: ")
    if email in user_feedback:
        for index,feedback in enumerate(user_feedback[email],start=0):
            print(f"{index}- {feedback["name"]} \n   {feedback["feedback"]}")
        
        index = int(input("Enter index number: start 0 to so on which is mention above: "))
        get_feedback = user_feedback[email][index]
        print(f"Selected feedback is=> {get_feedback["name"]} : {get_feedback["feedback"]}")

        feedback = input("Enter feedback: ")
        get_feedback["feedback"] = feedback
        print(f"Selected feedback is=. {get_feedback["name"]} : {get_feedback["feedback"]}")

        
    else:
        print("Invalid email or feedback not found!")


# ================= COUNT TOTAL, POSITIVE AND NEGATIVE FEEDBACK =================


def count_feedback():
    count= 0
    isFound = False

    choice = input("Enter your choice: 1 for specific word containing feedback, 2 for total number of feeback: ")
    if choice == "1":
        keyword = input("Enter single for search positive or negative feedback: like => good,excellent,bad etc: ")
        for emails,feedbacks in user_feedback.items():
            for index,feedback in enumerate(feedbacks,start=1):
                if keyword in feedback["feedback"]:
                    print(f"{index}- {feedback["name"]}: \n   {feedback["feedback"]}")
                    isFound = True
        if not isFound:
            print(f"No Feedback Found that contain {keyword} word!")
    elif choice == "2":
        for emails,feedbacks in user_feedback.items():
            for index,feedback in enumerate(feedbacks,start=1):
                count +=1
    
        print(f"Total numbers of feedback is {count}")


# ================= MENU =================

def menu():
        print("""
==========================
   User Feedback System
==========================
1. Show Feedbacks
2. Add Feedback
3. Delete Feedback
4. Edit Feedback
5. Count Feedback
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
            show_feedback()
        case 2:
            add_feedback()
        case 3:
            delete_feedback()
        case 4:
            edit_feedback()
        case 5:
            count_feedback
        case 0:
            save_file()
            print("👋 Good Bye!")
            break
        case _:
            print("❌ Invalid Choice")