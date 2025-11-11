# studentdata_listbased.py
# Menu-driven student data (list-based)

def add_student(students): # STUDENT DATA ENTRY
    print("Enter student details")
    try:
        mark_list = []
        roll_no = int(input("Enter student roll no: "))
        student_name = input("Enter student name: ")

        print("Enter marks of student in five subjects:")
        for i in range(1, 6):
            mark = float(input(f"Subject {i}: "))
            mark_list.append(mark)

        total = sum(mark_list)
        average = total / 5

        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 50:
            grade = "C"
        else:
            grade = "F"

        # Store data in list
        studentdata = [roll_no, student_name, mark_list, total, average, grade]
        students.append(studentdata)

        print(f" Record added for {student_name} (Roll no: {roll_no})")

    except ValueError:
        print(" Enter valid numeric data for roll number and subject marks!")


def view_all(students): # STUDENT RECORD VIEW
    print("\n--- All Student Records ---")
    for s in students:
        print(f"Roll No: {s[0]} | Student Name: {s[1]} | Total: {s[3]} | Avg: {s[4]:.2f} | Grade: {s[5]}")

def show_topper(students): #STUDENT TOPPERS 
    if not students:
     print("⚠️ No student records found.")
     return
    
    highest_total = 0
    topper = None

    """for s in students:
        if s[3] > highest_total:
            highest_total = s[3]"""
    
    highest_total = max(s[3] for s in students) #inbuilt python function " max " which is versatile for any iterable
            
    for s in students:
        if s[3]==highest_total:
         topper=s
         print(f"🏆 Topper: {topper[1]} (Roll {topper[0]}) - Total: {highest_total} | Grade: {topper[5]}")

             
    

def main():# main program
    students = []
    while True:
        print("\n--- Student Marks Evaluator ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Show Class Topper")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_all(students)
        elif choice == '3':
            show_topper(students)
        elif choice == '4':
            print("Thankyou and Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, try again.")

if __name__ == "__main__": #main program execution
    main()
