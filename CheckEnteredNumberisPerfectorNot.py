# Perfect number : Perfect number is a positive integre number that is equal to sum of its divisor exclusind its number
# eg  6 =1*2*3=6 is perfect number

num=int(input("enter positive integre number to check perfect number or not "))

result=0
for i in range(1,num):
    if (num%i)==0:
        result=result+i
    
if result==num:
    print(f"{num } is perfect number ")

else:
    print(f"{num } is not per6fect number")
