#Problem: Create a recursive function to calculate the factorial of a number.


# always think of the exit strategy.

def factorial(n):
    if n == 0 : # this is the exit of the loop
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))