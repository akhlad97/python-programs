# approach1 
import bdb # importing bdb module
# python -m pdb your_script.py # to run the script with pdb debugger
mylist=[1,2,34,5,1,7,5]
ele=71
i=0
flag=0
while i < (len(mylist)):
    if mylist[i] == ele:
        flag = 1
        
        break
    i += 1
        
if flag==1:
    print("element is found ")

else:
    print("element is not found")
    
### approach2 using in operator

mylist=[1,2,34,5,1,7,5]
ele=71

if ele in mylist:
    print("element is founf ")

else:
    print("not found")
    