#count_words.py
sentence = "hello i am Roshan"
words = []
i = 0
length = len(sentence)

while i < length:
    if sentence[i] == " ":
        i += 1
        continue
    else:
        temp = ""
        while i < length and sentence[i] != " ":
            temp += sentence[i]
            i += 1
        words.append(temp)

print("Number of words:", len(words))
