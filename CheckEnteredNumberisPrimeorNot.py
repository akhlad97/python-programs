n=int(input("please enter the posivtive integer number to check number is prime or not"))
if n>1:
    for i in range (2,n):
        if (n%i)==0:
            print(f"{n} is not a prme number")
            break
    else :
        print(f"{n} is a prime number ")