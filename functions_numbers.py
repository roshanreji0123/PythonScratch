def check(n):
    count =0
    for i in range (1,n//2):
        if(n%i==0):
            count+=1
        else:
            continue
    if count == 1:
        print(f"{n} is Prime.")
    else:
        print(f"{n} is Not Prime.")
    if(n%2==0):
        print(f"{n} is Even.")
    else:
        print(f"{n} is Odd.")

def fibonacci(n):
    a=0
    b=1
    if(n==0 or n==1):
        print(f"{n} is part of fibonacci series.")
    else:
        while(b<=n):
            next=a+b
            a=b
            b=next
            if(b==n):
                break
        if(b==n):
            print(f"{n} is part of fibonacci series")     
        else:
              print(f"{n} is not part of fibonacci series")     

def sum(n):
    sum=0
    while n>0:
        r=n%10
        n=n//10
        sum=sum+r
    print(f"Sum of digits is {sum}")
def palindrome(n):
    num=n
    sum=0
    while  n>0:
        r=n%10
        sum=sum*10+r
        n=n//10
    if(sum==num):
     print(f"The number {sum} is palindrome")
    else:
         print(f"The number {sum} is not palindrome")

number=int(input("Enter a number:"))
check(number)
fibonacci(number)
sum(number)
palindrome(number)
    
