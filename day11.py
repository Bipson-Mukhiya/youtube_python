# {} // this means scope 
# all the things are scoreps
# in python there is no curly braces
# global scope and function scope


# from outside we can bring information in 
# from inside we cannot get out of information

username = "chai aur code"
def func():
    #username = "chai"
    print(username)
print(username)
func()

#if the information is not found inside it will go outside to check.

# LEGB

x = 99
def func2(y):
    z = x + y
    return z


