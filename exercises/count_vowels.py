#count_vowels.py

string = "hello"
count = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for ch in string:
    if ch.lower() in vowels:
        count += 1

print("Vowel count: " + str(count))
