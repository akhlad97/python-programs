# arr=[1,2,3,4,5]
input_str = input("Please enter elements of the list (space-separated): ")

# Convert the input string into a list of integers
arr = list(map(int, input_str.split()))
n=len(arr)
# find maximum element 
max=arr[0]
for i in range(1,n):
    if arr[i]>max:
        max=arr[i]

print(max)

# find minimum element 
min=arr[0]
for i in range(1,n):
    if arr[i]<min:
        min=arr[i]

print(min)