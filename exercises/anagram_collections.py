from collections import Counter

s1 = input("Enter first word: ").replace(" ", "").lower()
s2 = input("Enter second word: ").replace(" ", "").lower()

if Counter(s1) == Counter(s2):
    print("It is an anagram")
else:
    print("Not an anagram")
