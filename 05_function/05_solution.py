# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.


# default parameter value. 

def greet(name = "user"): # (name) this is required. "user is give"
    return "Hello, " + name + "!"


print(greet())