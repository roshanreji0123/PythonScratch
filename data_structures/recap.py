# 🧾 Employee Performance Tracker
import math

def employee_entry(Employees):
    print("\nEnter Employee Details")
    print("-" * 25)
    try:
        # Auto-generate ID
        if not Employees:
            id = 1
        else:
            id = max(Employees.keys()) + 1

        aadharno = int(input("Enter Aadhar No: "))

        # Check if employee already exists
        for emp_id, info in Employees.items():
            if info[1] == aadharno:
                print("⚠️ Employee already exists!")
                return

        name = input("Enter employee name: ")
        age = int(input("Enter age: "))
        salary = float(input("Enter salary: "))
        score = float(input("Enter performance score (0-100): "))

        employee = [name, aadharno, age, salary, score]
        Employees[id] = employee
        print(f"✅ Record added for {name} (ID: {id})")

    except ValueError:
        print("⚠️ Enter valid numeric data!")


def employee_performance(Employees):
    if not Employees:
        print("⚠️ No employee records available.")
        return

    print("\n Employee Performance Report")
    print("-" * 50)
    for id, info in Employees.items():
        name, aadhar, age, salary, score = info
        grade = "A" if score >= 90 else "B" if score >= 75 else "C" if score >= 50 else "F"
        print(f"ID: {id} | {name} | Score: {score} | Grade: {grade}")


def main():
    Employees = {}
    while True:
        print("\n--- Employee Performance Tracker ---")
        print("1. Add a new employee record")
        print("2. View performance report")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            employee_entry(Employees)
        elif choice == "2":
            employee_performance(Employees)
        elif choice == "3":
            print("👋 Exiting tracker. Have a great day!")
            break
        else:
            print("❌ Invalid choice, please try again.")



 
if __name__ == "__main__":
    main()


