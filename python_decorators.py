# %%
## function copy 
def welcome():
    print("Welcome to the Python script!")

# %%
wel=welcome
print(wel())
del welcome
print(wel())

# %%
# closures 
def main_welcome():
    msg = "Welcome to the Python script!"
    def sub_welcome():
        print("welcome to advanced python course")
        print("please learn this concept properly")
        
    return sub_welcome()
main_welcome()

# %%
def main_welcome():
    msg = "Welcome to the Python script!"
    def sub_welcome():
        print("welcome to advanced python course")
        print(msg)
        print("please learn this concept properly")
    
    return sub_welcome()

main_welcome()

# %%
def main_welcome():
    msg = "Welcome to the Python script!"
    def sub_welcome():
        print("welcome to advanced python course")
        print(msg)
        print("please learn this concept properly")
    
    return sub_welcome

main_welcome()()

# %%
def main_welcome(func):
    msg = "Welcome to the Python script!"
    def sub_welcome():
        print("welcome to advanced python course")
        func(msg)
        print("please learn this concept properly")
        
        
    return sub_welcome()
    
main_welcome(print) # passing built function as argument

# %%
def main_welconme(func):
    msg = "Welcome to the Python script!"
    def sub_welcome():
        print("welcome to advanced python course")
        print(func(msg))
        print("please learn this concept properly")
        
    return sub_welcome

main_welconme(len)() # passing built function as argument

# %%
def main_welcome(func):
    msg = "Welcome to the Python script!"
    def sub_welcome():
        print("welcome to advanced python course")
        func()
        print("please learn this concept properly")
        
    return sub_welcome()
    


# %%
def course_introduction():
    print("This is an advanced Python course.")
    print("We will cover closures, decorators, and more.")

main_welcome(course_introduction) # 

# %%
@main_welcome
def course_intrpduction():
    print("This is an advanced Python course.")
    print("We will cover closures, decorators, and more.")


