#exploring_dicts.py
student={"name":"Roshan","age":17,"Eligible_for_License":None} # key value pair

if student["age"]>=18:
    student["Eligible_for_License"]=True# modifying
    print(f"{student['name']} is eligible to drive.")
else:
    student["Eligible_for_License"]=False# modifying 
    print(f"{student['name']} is not eligible to drive.")
    
print(student)

