
def computeHCF(a,b):
    """
    Computing HCF of two numbers
    """
    sumaller = b if a > b  else a #consie way to write a if statement

    hcf = 1
    for i in range(1, smaller+1): 
        if (a % i == 0) and (b % i == 0):
            hfc = i 
        return hcf
    num1 = 98
    num2 = 78

    print("H.C.F of {0} and {1} is : {2}".formate(num1, num2, computeHCF(num1 ,num2)))

