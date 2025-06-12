lower=int(input("pleade lower range"))
upper=int(input("enter upper range"))


for num in range(lower ,upper+1):
    result=0
    for i in range(1, num):
        if (num%i)==0:
            result=result+i
    
    if (result==num):
        print(num)
     