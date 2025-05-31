
lst=[12,34,23,56,90]
print ("before swapping the list",lst)

# approach1 using temporary variable 

# sizeoflist=len(lst)
# temp=lst[0]
# lst[0]=lst[sizeoflist-1]
# lst[sizeoflist-1]=temp
# print("List after swapping first and last elements:", lst)

# approach2 
# lst[0],lst[-1]=lst[-1],lst[0]
# print("List after swapping first and last elements:", lst)

# approach3 using tuple variable

# get=()
# get=[lst[-1],lst[-0]]  #90 12 this concept called packing
# lst[0],lst[-1]=get    # unpacking 
# print("ist after swapping first and last elements:", lst)

# approach4  * operand
# start,*middle,end=lst
# lst=[end,middle,start]
# print("lst after swapping first and last element ",lst)

# approach5 using pop function

first=lst.pop(0)
last=lst.pop(-1)

lst.insert(0,last)
lst.append(first)

print("lst after swapping first and last element ",lst)


