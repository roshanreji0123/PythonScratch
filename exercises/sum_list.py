#sum  of a list

def list_sum(nums):
    total = 0
    for n in nums:
        total += n
    return total

def main():
    numbers = [10, 20, 30, 40]
    print(list_sum(numbers))
    print(count(numbers))
def count(numbers):
    count1=0
    for i in numbers:
        count1=count1+1
    return count1

if __name__ == "__main__":
    main()

