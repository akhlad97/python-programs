n=int (input("enter the number of rows "))

for row in range(1,n+1):
    for col in range(1,n*2):
        if row==n or col+row==n+1 or col-row==n-1:
            print("*",end="")
        
        else:
            print(end=" ")
    
    print()