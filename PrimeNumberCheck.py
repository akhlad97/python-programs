# 1 natural number >1
# 2 having two factors 1 and itself
# 19 --> having two factors 1 and 19 
num=5
count=0

for i in range(1,num+1):
    if (num%i)==0:
        count+=1

if count==2:
    print(f"{num} is a prime number")

else:
    print(f"{num} is not a prime number")