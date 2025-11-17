from functions_numbers import check, fibonacci, digit_sum, palindrome

if __name__ == "__main__":
    print(" Demonstration of imported functions ")
    
    print("----------------------------------------")

    numbers = [10, 18, 90, 100]

    try:
        for num in numbers:
            print(f"\nAnalyzing number: {num}")
            check(num)
            fibonacci(num)
            digit_sum(num)
            palindrome(num)
    except ValueError:
        print("⚠️ Invalid input. Please enter an integer.")
