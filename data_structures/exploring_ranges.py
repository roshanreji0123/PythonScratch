# exploring_ranges.py

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    # print leading spaces (3 spaces per missing row for symmetry)
    print("   " * (n - i), end="")

    # ascending part
    for j in range(i, 2 * i):
        print(f"{j:2}", end=" ")

    # descending part
    for j in range(2 * i - 2, i - 1, -1):
        print(f"{j:2}", end=" ")
        

    print()
