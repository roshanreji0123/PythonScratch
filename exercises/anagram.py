#anagram.py
print("Enter two words.\n")
word_one=input("1)")
word_two=input("2)")
visited=""
check=True
for one in word_one.strip():
    if one in visited:
        continue
    count=0
    for two in word_two.strip():
        if(one==two):
            count=count+1
    count2=0
    for one_char in word_one.strip():
        if(one_char==two):
            count2=count2+1
    if(count2==count):
        visited=visited+one
        
    else:
        
        check=False
        break
if check==False:
    print("Not anagram")
else:
    print("anagram")


    
            
    