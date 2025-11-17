#character_frequency.py
word = input("Enter a word.\n")
visited = ""

for i in range(len(word)):
    character = word[i]

    # Skip characters  already counted
    if character in visited:
        continue

    count = 1
    for j in range(i+1, len(word)):
        if character == word[j]:
            count += 1

    print(f"{character} has a frequency of {count}")
    visited += character
