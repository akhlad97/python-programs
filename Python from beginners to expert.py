# %% [markdown]
# ## Function in python
# - why do we need function lets understan one scenario you might be workion on simple or complex project
# - when you work on complex project break down complex project to smaller task . 
# - when you talk about smaller task of course you need to write multiple statement.
# - e.g if you want to operate payment operation in that you need to multiple statement all that statement keep it together & re useable later. 
# - all the statment of the tasks are stay together thats why we are creation function 

# %% [markdown]
# 

# %% [markdown]
# # FUNCTION -->
# - Inbuild function  -- print(), type(), id(), sqrt() etc
# - User defined function 
# - function is collection of statement
# - 2 main property of the function is -- define the function & calling the function 
# - function always define with def & function always declares as ()
# difference between variable & function || a - variable || b() - function 

# %%
def greet():
    print("hello")
    print("good morning")

# it will not give any out put until unless we call the function
greet()


# %%
def greet():
    print("hello")
    print("good morning") 
greet()

def greet():
    print("hello")
    print("good morning") 
greet()

# %%
def greet():
    print("hello")
    print("good morning") 
# if you need call the function multiple time
greet()
greet()
greet()

# %%
# create a function and give the definition somthing add two numbers 
def add(x,y):
    c=x+y
    print(c)
# call the add function
add(2,4)

# %%
def add(x,y,z):
    c=x+y+z
    print(c)
# call the add function
add(3,2,6)

# %%
def greet():
    print("hello")
    print("good morning")

def add(x,y):
    c=x+y
    print(c)

greet()
add(2,9)

greet()
add(2,11)

# you can create multple functions and call them as many time as you want 


# %%
def add_sub(x,y):
    c=x+y
    d=x-y

    return c,d

sum,sub=add_sub(23,27)
result=add_sub(23,27) ## result will store in the form of tuple
print(sum,sub)
print(result)
    
type(result)

    

# %% [markdown]
# - function are always reuseable 
# - in one code you can write multiple function as well
# - FUNCTION ARGUMENT
# - How to pass parameter to a function & what happend to the variable when you pass to a function & if you modify the value then what happen
# - every code check with debug

# %%
def update(x): #update function take the value from the user
    x = 8
    print(x)
    
update(100)

# %%
def update(x): # user want to update the value from 8 to 10 
    x = 8
    print(x)
    
print(update(10))

# %%
def update(x):
    x=8
    print(x)

print(update(10))

# %%
def update(x):
    x=8
    print(x)
a=10
update(a)
print(a)

# %%
def change(a):
    a = a+ 10
    print('inside the fun a =',a)
    
x = 10
print('x before calling:', x)
change(x)
print('x after calling:', x)


# %%
def change(list):
    list[0]=list[0]+10
    print("inside the function",list)

list=[10]
print("print list before calling function",list)
change(list)
print("print list after calling function ", list)

# %% [markdown]
# 

# %%
# by default there is not pass by value and pass by refference
def update(x):   
    print(id(x))
    x = 8
    print(id(x))
    print('x', x)    

a = 10
print(id(a))
update(a)
print('a',a)

# %% [markdown]
# 
# - when you call a function by pass the value they will share the same memory location 
# - the variabel which you pass & the variable which you accessing heear a & x refer to same obejct 
# -  the above concept is neither pass by value or pass by reference
# - Interview( Normally in python we dont use pass by value or pass by reference but other programing       language it does & the reason is python is object oriented programing language 

# %% [markdown]
# ## TYPE OF ARGUMENTS --> formal argument & actual argument
# 

# %%
def add(x,y):# formal arguments
     c = x + y
     return c

sum=add(2,3) ## actual  arguments
print(sum)

def add(a,b,d): # a & b &d called formal argument
    c = a+b+d
    print(c)
    
sum=add(5,6,7) #5 and 6 &7 we called as actual argument
print(sum)
  

# %% [markdown]
# ## Actual arguments

# %% [markdown]
# ### Positional arguments

# %%
def person(name,age):
    print("Name:", name)
    print("Age:", age)

person("Alice", 30)  # positional arguments
# this is called postion argument becuase name we assigned to position name to Alice & age to 30
# how it know that name - Alice & age - 30 we need to take care of the position, we need to maintain the sequence but what if we dont know the sequence
# lets check we have 10 variable and we need to assign them with position but what if we forget the sequence

# %%
def person(name,age):
    print(name)
    print(age)
    
person(22,'nit')
# this is called positional argument, we need to take care of the sequence


# %%
def person(name,age):
    print(name)
    print(age-5)
    
person(20,'nit')
# in this case we cant assign name - 20 & age to 'nit' then we can assign them as keyword 
# this code not give you error but output is in different format


# %%
def person(name,age):
    print(name)
    print(age-5)
    
person('nit',20) 

# in this case we cant assign name - 20 & age to 'nit' then we can assign them as keyword 
# this code not give you error but output is in different format

# %% [markdown]
# ### keyword argument

# %%
def person(name,age):
    print(name)
    print(age-5)
    
person(age = 20, name = 'nit') 


# this is called keyword argument, we can assign them in any order

# %%
def person(name, age,age2):
    print(name)
    print(age)
    print(age2)

person(name='nit', age=20, age2=30)  # keyword arguments

# %% [markdown]
# ## default argument
# - while you open meta account minumu age criterial is so. by default age is 18 

# %%
def person(name, age=18):
    print(name)
    print(age)

person('Alice', 25) # positional argument with default value
person('Bob')  # positional argument with default value

# %% [markdown]
# ### variable length argument

# %%
def sum(a, b, c):
    print(a + b + c)
    
sum(1, 2, 3)  # 
    

# %%
def add(a,b):
    print(a + b)
    
add(2, 3, 4, 5, 6, 7)  # this will give error because we are passing more than 2 arguments but function is defined with only 2 arguments

# %%
def add(a,*b):
    print(a)
    print(b)
    print(type(a))
    print(type(b))
add(2, 3, 4, 5, 6, 7)  # this will not give error because we are using *args which allows us to pass variable number of arguments

# %% [markdown]
# ### KWARGs key worded variable length arguments

# %%
def person(name, *data):
    print("Name:", name)
    print("Data:", data)

person("Alice", 30, "Engineer", "New York")  # variable-length arguments

# %%
def person(name, *data):
   print("Name:", name)
   print("Data:", data)
   
person("Alice", age=30, city="New York")  # variable-length arguments with keyword arguments  it will give error because we are passing keyword arguments with *args which is not allowed


# %%
def person(name, **data):
    print("Name:", name)
    print("Data:", data)

person("Alice", age=30, city="New York", country="USA")  # keyword arguments this will not give error because we are using **kwargs which allows us to pass variable number of keyword arguments

# %%
## gloabal variable vs local variable
## discuss about global variable and local variable
## sometime we need to use global variable and local variable 
## sometime we create a variable inside the function and some times we create a variable outside the function
## when we create a variable outside the function it is called global variable and when we create a variable inside the function it is called local variable
x = 10  # global variable
def my_function():
    a = 5  # local variable
    print("Inside function:", a)
    print("Global variable:", x)

# %%
## if i want to define a global variable inside the function then we need to use global keyword
def my_function():
    global x  # declare x as global
    x = 20  # modify the global variable
    print("Inside function:", x)
    print(id(x))  # 
my_function()
print("Global variable outside function:", x)
print(id(x))  # check the id of global variable

# %%
## globals built-in function that give you the dictionary of all global variables
x= 10  # global variable
def update_global():
    globals()['x'] = 20  # modify the global variable using globals() 


update_global()
print("Global variable outside function:", x)
    

# %% [markdown]
# # pass list to function 
# - Can we pass list of element in the function that function will return the count of even or odd number from the list 

# %%
def count(lst):
    even=0
    odd=0
    
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even, odd

lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count,odd_count=count(lst)
print("Even count:", even_count)
print("Odd count:", odd_count)
    

# %% [markdown]
# ### RECURSSION - CALLING FUNCTION FROM ITSELF IS CALLED RECURSSION

# %%
# i want to cal the hello multiple time
# it will execute maximum 1000 time & in below code wish is calling by itself
# bydefault we have 1000 limitation can we extend the recurssion limitation yes we can 

def wish(): #---------> 2-greeting function will executed
    print('hello') 
    
wish() # What if i call the function again #3---------> function calls itself is called recurssion

wish() #------------> 1-at this point we are calling wish() function 

# it will print infinity time cuz recursion its own function 

# %%
def wish():
    print("hello")
    wish()
wish()

# %%
import sys
sys.getrecursionlimit()

# %%
import sys
sys.setrecursionlimit(100)
print(sys.getrecursionlimit())

# %%
def wish():
    print("hello")
    wish()
wish()
## it will print 100 times

# %%
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
result=fact(4)
print(result)

# %% [markdown]
# ### Function without name is called - ANONYMOUS FUNCTION OR LAMBDA

# %%
def square(a):
    return a * a
    
result = square(5)
print(result)
# what if i dont want to call square() multiple times 

# %%
# lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.
f= lambda a: a * a  # lambda function to calculate square
result = f(5)  # calling lambda function
print(result)

# %%
# lambda with more than one argument
f= lambda a, b: a + b  # lambda function to calculate sum
result = f(5, 6)  # calling lambda function
print(result)

# %%
# find the qube using lambda function 
f= lambda a: a * a * a  # lambda function to calculate cube
result = f(5)  # calling lambda function
print(result)

# %%
# find the addtion of 4 numbers using lambda function
f=lambda a, b, c, d: a + b + c + d  # lambda function to calculate sum of 4 numbers
result = f(1, 2, 3, 4)  # calling lambda function
print(result)

# %% [markdown]
# 

# %% [markdown]
# ### how can use lambda function with map, filter and reduce

# %%
def envens(n):
    if n % 2 == 0:
        return True
    
nums= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(envens, nums))  # filter even numbers using lambda function
print(evens)  # print even numbers



# %%
# usin lambda function to filter even numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda n: n % 2 == 0, nums))  # filter even numbers using lambda function
print(evens)  # print even numbers

# %%
# usinf lambda function to filter the odd number 
nums=[1,2,3,4,5,6,7,8,9.10]
odds=list(filter(lambda n : n%2!=0,nums))
print(odds)

# %% [markdown]
# - What ever even number I have from the assigned list
# - I want to increase  that even number by 2 for example  2 become 4  || 4 become 6 || 6 become 8
# - that we will do using map function 
# - this largly we are using in google map reduce programme
# - we can build using user define & lambda

# %%
def is_even(n):
    if n%2==0:
        return True
def update(n):
    return n+2

nums=[1,2,3,4,5,6,7,8,9,10]
evens=list(filter(is_even,nums))
print(evens)
evensincreasedByTwo=list(map(update,evens))
print(evensincreasedByTwo)

# %%
# to do above task using lamda function 
nums=[1,2,3,4,5,6,7,8,9,10]
evens=list(filter(lambda n:n%2==0,nums))
print(evens)
evensincreasedByTwo=list(map(lambda n:n+2,evens))
print(evensincreasedByTwo)


# %% [markdown]
# - i want to perform reduce now 
# - i want reduce all the values 
# - reduce you can add only 2 values
# - [4, 12, 16, 8, 12, 4] if you sum everything then you will get 56

# %%
from functools import reduce
nums=[1,2,3,4,5,6,7,8,9,10]

evens=list(filter(lambda n:n%2==0,nums))
evensincreasedByTwo=list(map(lambda n:n+2,nums))
sum=reduce(lambda a,b:a+b,nums)

print(evens)
print(evensincreasedByTwo)
print(sum)

# %% [markdown]
# ### modules
# - In Python, modules are files containing Python code that define functions, classes, and variables that can be imported and used in other Python scripts. They help organize code into logical units and facilitate code reusability. Here are some key points about modules in Python:
# - Modules are fundamental to Python's modular design philosophy, promoting code reuse, maintainability, and scalability in Python projects

# %% [markdown]
# ### Standard Library Modules:
# - Python comes with a standard library of modules that provide functionalities ranging from mathematical operations (math), file I/O (os, sys), to internet protocols (urllib, http).

# %%
import math

# %% [markdown]
# ### Custom Modules: 
# - You can create your own modules by writing Python code in a .py file and then import them in other scripts.

# %% [markdown]
# ### Module Aliasing:
# - Modules can be imported with an alias to simplify usage, especially for modules with long names or to avoid name conflicts:

# %% [markdown]
# ### Module Search Path:
# - Python searches for modules in directories listed in sys.path. You can modify sys.path to include additional directories where your modules are located.

# %% [markdown]
# ### Packages:
# - Packages are a way of organizing modules hierarchically. A package is a directory containing Python modules and a special __init__.py file.

# %% [markdown]
# ## Special Variable __name__ 

# %%
__name__

# %%
__name__ = "math_module"
__name__

# %% [markdown]
# 

# %% [markdown]
# - The moment when we print __name__ then i will get output as main
# - in your project if you have 5 modules or 10 modules there will some modules which will be run first 
# - so the first module name is always __main__. thats why the code start 
# - to understand indetaild review we will work with PYCHARM
# - from the main function we can call all other function 
# - please work 4 file in pycharm (hi.py, bye.py, hi1-specialvariable, bye1-specialvariable)
# - refer more about chatgpt

# %%
import module1
# using the function from module1 
print(module1.greet('akhlad'))  # calling the greet function from module1
print(module1.add(2, 3))  # calling the add function from module1
print(module1.factorial(8))  # calling the add_sub function from module1


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%



