# prime number is natural number greater than that has no positive divisor other than 1 and itself
lower=int(input("please eneter the lower range number "))
upper=int(input("please enter the upper range number"))

for num in range(lower ,upper+1):
    if num>1:
        for i in range(2,num):
            if (num%i==0):
                break
        
        else:
            print(num)
                
                 