
def add(a,b):
    """
    This function adds two numbers
    """
    return a+b

def multiply(a,b):
    """
    This function adds two numbers
    """
    return a*b

def subtract(a,b):
    """
    This function adds two numbers
    """
    return a-b
def divide (a,b):
    """
    This function adds two numbers
    """
    return a / b

print("select option")
print("1.addition")
print("2.Substraction")
print("3.Multiplication")
print("4. Division")

# take input from user

choice = int(input("Enter choice 1/2/3/4 "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter Second number: "))

if choice  == 1:
    print("Addition of {0} and {1} is {2}".format(num1, num2, add(num1,num2)))

elif choice == 2:
    print("Subtraction of {0} and {1} is {2}".format(num1, num2, subtract(num1,num2)))

elif choice == 3:
    print("Multiplication of {0} and {1} is {2}".format(num1, num2, multiply(num1,num2)))
elif choice == 4:
    print("division of {0} and {1} is {2}".format(num1, num2, divide(num1,num2)))
else:
    print("invalid number")