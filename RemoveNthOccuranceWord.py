mylist=["geek","for","geek","geek"]
word="geek"
count=0
i=0
while i <len(mylist):
    if mylist[i]==word:
        count+=1
        if count>1 :
            del mylist[i]
            i-=1 # adjust index after deletion
    i+=1
print(mylist)
    
    
