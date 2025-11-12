# license_dictbased_fixed.py

def add_student(register):
    """Add one student to the register ."""
    print("\nEnter the student details:")

    try:
        # generate next id 
        new_id = max(register.keys(), default=0) + 1 # default id value will be 1 or be incremented during runtime

        name = input("Enter student name: ").strip()
        age_input = input("Enter student age: ").strip()
        age = int(age_input)  

        entry = {"name": name, "age": age, "eligible": age >= 18}# assigns eligible True or False based on age
        register[new_id] = entry  # Modify main dictionary
        print(f"✅ Student Record Added! (ID: {new_id})")

    except ValueError:
        print("⚠️ Invalid age. Please enter a numeric age.")


def view_student(register):
    """Print list of students."""
    if not register:
        print(" No student records found.")
        return

    print("\n📋 Students:")
    for id, info in register.items():
        print(f"ID No-{id}: {info['name']} aged {info['age']} years")


def status_students(register):
    """Print eligibility status for each student."""
    if not register:
        print(" No student records found.")
        return

    print("\n📋 Student License Records:")
    for id, info in register.items():
        status = "eligible" if info.get("eligible") else "not eligible" #assigns eligible if True ,not eligible is False
        print(f"(ID No-{id}) {info['name']} aged {info['age']} is {status} for license.")


def main():
    register = {}
    while True:
        print("\n--- Student License Register ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Show Eligibility Status")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()  # strip whitespace

        # Debug print (uncomment if you want visibility)
        # print(f"[DEBUG] Raw choice: {repr(choice)}")

        if choice == "1":
            add_student(register)
        elif choice == "2":
            view_student(register)
        elif choice == "3":
            status_students(register)
        elif choice == "4":
            print(" THANK YOU!!!")
            break
        else:
            print(" Invalid choice, please try again (enter 1,2,3 or 4).")


if __name__ == "__main__":
    main()
