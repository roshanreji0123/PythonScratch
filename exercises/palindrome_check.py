string="Malayalam"
new_string=""
for st in string:
    new_string=st.lower()+new_string
if(new_string==string.lower()):
    print("Palindrome")
else:
    print("Not Palindrome")
