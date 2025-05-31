lst=[12,34,23,60,27] # indx start from zero
print("before swap",lst)

# approach1
# pos1,pos2=1,3
# lst[pos1],lst[pos2]=lst[pos2],lst[pos1]
# print("aftre swapping ",lst)


# approach2 using pop function

# pos1,pos2=1,2
# pos1_element=lst.pop(pos1)
# pos2_element=lst.pop(pos2-1)

# lst.insert(pos2,pos1_element)
# lst.insert(pos1,pos2_element)
# print("aftre swapping ",lst)

# approach3 using tuple
get=()
pos1,pos2=1,3
get=lst[pos1],lst[pos2]
lst[pos2],lst[pos1]=get
print("aftre swapping ",lst)
