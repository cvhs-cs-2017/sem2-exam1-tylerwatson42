"""Define a function that will take a parameter, n, and triple it and return
the result"""
n = 3
def TripFunc(n):
    a = n**3
    return a

print(TripFunc(n))


"""Write a program that will prompt the user for an input value (n) and print
the result of 3n by calling the function defined above.  Make sure you include
the necessary print statements and address any issues with whitespace. """

n = int(input("Type in a number:"))

print(TripFunc(n))
