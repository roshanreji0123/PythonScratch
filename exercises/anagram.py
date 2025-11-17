#anagram.py
# anagram.py
print("Enter two words.\n")
word_one = input("1) ").strip()
word_two = input("2) ").strip()

# Quick length check
if len(word_one) != len(word_two):
    print("Not anagram")
    exit()

visited = ""
check = True

for one in word_one:
    # Skip if  already counted this character
    if one in visited:
        continue

    # Count occurrences of 'one' in word_two
    count = 0
    for two in word_two:
        if one == two:
            count += 1

    # Count occurrences of 'one' in word_one
    count2 = 0
    for one_char in word_one:
        if one_char == one:      
            count2 += 1

    # Compare frequencies
    if count2 == count:
        visited += one
    else:
        check = False
        break

# Final result
if check == False:
    print("Not anagram")
else:
    print("Anagram")


    
            
    
