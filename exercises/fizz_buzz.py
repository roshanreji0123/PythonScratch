#fizz_buzz.py
print("Enter a number")
choice = "y"

while choice.lower() == "y":
    try:
        num = int(input())

        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print("Not special")

        print("Do you want to continue? (Y/N)")
        choice = input().strip().lower()

        if choice == "y":
            continue
        elif choice == "n":
            print("Thank You")
            break
        else:
            print("Invalid choice, exiting.")
            break

    except ValueError:
        print("Enter a valid integer.")
