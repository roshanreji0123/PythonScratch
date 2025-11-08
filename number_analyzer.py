number=int(input("Enter a number: "))
#Check whether prime,even or odd
count=0
for i in range(1,(number//2)+1):
    if(number%i==0):
        count+=1
    if(count>2):
        print(f"{number} is not prime")
        break
if(count==2):
   print(f"{number} is  prime")

if(number%2==0):
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")

#Actions based on number range

#number<10 [print factorial]
def fact(N):
        if(N==0):
            return 1
        else:
            return N*fact(N-1)
if(number<10):#factorial
    print(fact(number))
elif(number>10 and number<50):#divisors

    print(f"The divisors of {number}")
    for i in range (1,number+1):
        if(number % i==0):
            print(i)
else:#number of stars
    number_of_stars=number%10
    print(f"The last digit of {number} is {number_of_stars} ->")
    while(number_of_stars>0):
        print("*",sep="")
        number_of_stars-=1

     
   