

username = "black forest"

def test():
    username = "chai" # if we comment this this will print black forest this will print global. 
    print(username)
    pass

print(username)
test()


# function is like a home. a new namespace. in memory we are making a new home. 
# there are different homes at different places. 
# outside information inside
# in python everything is thought as username.



x = 99

def func2(y):
    z = x + y # this takes the value form the x.
    return z

result = func2(1)
print(result)


def func3():
    global x 
    x = 145 

func3() # after calling the function it will call from the global space.
print(x)

# we should not manipulate the global mechanism. because while multiple developers are working at the same code so we dont' expect the changes.


def f1():
    x = 88
    def f2 ():
        print(x)
    return f2
myResult= f1()
myResult()
# we can make multiple rooms and make the print. 
# we are packing up the backup. 

def chaicoder(Num):
    def actual(x):
        return x ** Num
    return actual

# they are known as factory function and closure.


f = chaicoder(2)
g = chaicoder(3)
print(f)# <function chaicoder.<locals>.actual at 0x000001CA7CDF3010>   

print(f(3))
print(g(3))