#remove_vowels.py
word=input("Enter a word.\n")
vowels = "aeiou"
new_word = ""

for w in word:
    if w.lower() not in vowels:
        new_word += w

print(new_word)
