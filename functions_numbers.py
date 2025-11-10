def check(n):
    """Check if the number is prime and whether it is even or odd."""
    count = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            count += 1
    if count == 1:
        print(f"{n} is Prime.")
    else:
        print(f"{n} is Not Prime.")

    if n % 2 == 0:
        print(f"{n} is Even.")
    else:
        print(f"{n} is Odd.")


def fibonacci(n):
    """Check if the number is part of the Fibonacci sequence."""
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n or n == 0:
        print(f"{n} is part of the Fibonacci series.")
    else:
        print(f"{n} is not part of the Fibonacci series.")


def digit_sum(n):
    """Calculate and print the sum of digits of the number."""
    total = 0
    while n > 0:
        r = n % 10
        n = n // 10
        total += r
    print(f"Sum of digits is {total}")


def palindrome(n):
    """Check if the number is a palindrome."""
    original = n
    reversed_num = 0
    while n > 0:
        r = n % 10
        reversed_num = reversed_num * 10 + r
        n = n // 10
    if reversed_num == original:
        print(f"The number {original} is a palindrome.")
    else:
        print(f"The number {original} is not a palindrome.")


# -----------------------------
# Main Program Execution
# -----------------------------
if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        print("\nAnalyzing...\n")
        check(number)
        fibonacci(number)
        digit_sum(number)
        palindrome(number)
    except ValueError:
        print("⚠️ Invalid input. Please enter an integer.")

