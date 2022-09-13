def factorial(num):
    """
    This is a recursive function to find the factorial of a given number
    """
    return 1 if num == 1 else (num*factorial(num - 1))

num = int(input("Enter a number:"))
print("factorial of {0} is {1}".format(num , factorial(num)))