# 1 fatorial of 5 is =1*2*3*4*5=120
# approach1
factorial=1
# num=1
num=int(input("enter a to find out factorial "))
if num<0:
    print("factorial does not exist")
    
elif num==0:
    print(f"factorial of {num} is 1")
    
else:
    for i in range(1,num+1):
        factorial*=i
    
    print(f"factorial of {num} is {factorial}")
    