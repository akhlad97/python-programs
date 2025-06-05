string=input("enter the input string ")

for row in range(len(string)):
    for col in range(row+1):
        print(string[col],end=" ")
    
    print()