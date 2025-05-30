def factorial(n):
    # if (n==0 or n==1):
    #     return 1
    # else:
    #     return n*factorial(n-1) # 5*$*3*2*1==120
    
    # Ternary approach 
    return 1 if (n==1 or n==0) else n*factorial(n-1)

num=int(input("enter a number to find the factorial"))
print(f"the factorial of {num} is {factorial(num)}")