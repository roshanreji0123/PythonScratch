number = int(input("Enter a number: "))

# Prime Check
count = 0
for i in range(1, (number // 2) + 1):
    if number % i == 0:
        count += 1
if count == 1:
    print(f"{number} is Prime")
else:
    print(f"{number} is Not Prime")

# Even or Odd
if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")

# Function for factorial
def fact(N):
    if N == 0:
        return 1
    return N * fact(N - 1)

# Range actions
if number < 10:
    print(f"Factorial of {number} = {fact(number)}")
elif 10 < number < 50:
    print(f"The divisors of {number}:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
else:
    number_of_stars = number % 10
    print(f"The last digit of {number} is {number_of_stars} ->")
    print("*" * number_of_stars)
