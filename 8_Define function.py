#program 1
def print_name(name):
    """
    This function prints the same
    """
    print("Hello " +str(name))

#program 2
print_name('ANUJ')

# programe 3 --- Return statement

def get_sum(lst):
    """
    This function returns the sum of all the elements in a list
    """
    #initializing sum
    sum_ = 0

    # iterating over the list
    for num in lst:
        sum_ += num
    return sum_

print()


s = get_sum ([1,2,3,4])
print(s)  
