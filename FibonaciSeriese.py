# n1=0
# n2=1
#  each subsequent number is the sum of the two preceding ones (0, 1, 1, 2, 3, 5, ...
n1=int(input("entere lower value "))
n2=int(input("enter hiehger range"))
print(n1)
print(n2)


for i in range(2, 10):
    sum=n1+n2
    print(sum)
    n1=n2
    n2=sum