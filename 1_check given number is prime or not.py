num = int(input("Enter a number: "))  # convert string into integer
isDivisible = False;
i=2;
while i < num:
    if num % i == 0:
        isDivisible = True;
        print("{} is divisible by {}".format(num,i))
    i += 1;
if isDivisible:
    print("{} is not a Prime Number".format(num))
else:
    print(" {} is a Prime Number".format(num))

