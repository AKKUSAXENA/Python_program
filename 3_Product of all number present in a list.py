
#index 0  1  3  4  5
lst = [10,20,30,40,60]

product = 1
index = 0 

while index < len(lst):   # 0 < 5        || 1 < 5
    product *= lst[index] # product = 10 || product = 200
    index += 1            # index = 1    || index = 2

print("Product is: {}".format(product))