def maximum(nums):
   highest=nums[0]
   for i in nums:
      if i>highest:
         highest=i
   return highest

def main():
 nums=[]
 print("Enter numbers you want to check")
 while True:
    try:
        num=float(input())
        nums.append(num)
        print("Do you want to add more numbers?")
        choice=input("YES/NO")
        if(choice.lower()=="yes"):
         continue
        elif(choice.lower()=="no"):
           print(f"Highest number is {maximum(nums)}")
           print("Thank You.")

           break
        else:
           print("Invalid Input.Please provide a suitable input.")
    except ValueError:
       print("Enter valid numeric numbers")

if __name__=="__main__":
   main()