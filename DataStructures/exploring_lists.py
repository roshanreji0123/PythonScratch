# exploring_lists.py
# Exploring Python List Operations

if __name__ == "__main__":
    numbers = [20, 30, 40, 50, 60, 70]
    print("Original List:", numbers)
    print("Length:", len(numbers))# length of list

    numbers.insert(1, 3) #inserting 3 at index 1
    print("After insert:", numbers)

    numbers.append("EOF")#appends EOF to the end of the list
    print("After append:", numbers)

    if 3 in numbers: #checks for 3 in list using keyword in
        numbers.remove(3)
        print("After remove:", numbers)
    else:
        print("Value 3 not found")

    numbers.clear()#clearing the values in the list
    print("After clear:", numbers)
